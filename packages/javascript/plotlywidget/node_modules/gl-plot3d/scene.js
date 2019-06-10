'use strict'

var createCamera = require('./camera.js')
var createAxes   = require('gl-axes3d')
var axesRanges   = require('gl-axes3d/properties')
var createSpikes = require('gl-spikes3d')
var createSelect = require('gl-select-static')
var createFBO    = require('gl-fbo')
var drawTriangle = require('a-big-triangle')
var mouseChange  = require('mouse-change')
var mouseWheel   = require('mouse-wheel')
var perspective  = require('gl-mat4/perspective')
var ortho        = require('gl-mat4/ortho')
var createShader = require('./lib/shader')
var isMobile = require('is-mobile')({ tablet: true })

module.exports = {
  createScene: createScene,
  createCamera: createCamera
}

function MouseSelect() {
  this.mouse          = [-1,-1]
  this.screen         = null
  this.distance       = Infinity
  this.index          = null
  this.dataCoordinate = null
  this.dataPosition   = null
  this.object         = null
  this.data           = null
}

function getContext(canvas, options) {
  var gl = null
  try {
    gl = canvas.getContext('webgl', options)
    if(!gl) {
      gl = canvas.getContext('experimental-webgl', options)
    }
  } catch(e) {
    return null
  }
  return gl
}

function roundUpPow10(x) {
  var y = Math.round(Math.log(Math.abs(x)) / Math.log(10))
  if(y < 0) {
    var base = Math.round(Math.pow(10, -y))
    return Math.ceil(x*base) / base
  } else if(y > 0) {
    var base = Math.round(Math.pow(10, y))
    return Math.ceil(x/base) * base
  }
  return Math.ceil(x)
}

function defaultBool(x) {
  if(typeof x === 'boolean') {
    return x
  }
  return true
}

function createScene(options) {
  options = options || {}
  options.camera = options.camera || {}

  var canvas = options.canvas
  if(!canvas) {
    canvas = document.createElement('canvas')
    if(options.container) {
      var container = options.container
      container.appendChild(canvas)
    } else {
      document.body.appendChild(canvas)
    }
  }

  var gl = options.gl
  if(!gl) {
    gl = getContext(canvas,
      options.glOptions || {
        premultipliedAlpha: true,
        antialias: true,
        preserveDrawingBuffer: isMobile
      })
  }
  if(!gl) {
    throw new Error('webgl not supported')
  }

  //Initial bounds
  var bounds = options.bounds || [[-10,-10,-10], [10,10,10]]

  //Create selection
  var selection = new MouseSelect()

  //Accumulation buffer
  var accumBuffer = createFBO(gl,
    [gl.drawingBufferWidth, gl.drawingBufferHeight], {
      preferFloat: !isMobile
    })

  var accumShader = createShader(gl)

  var isOrtho =
    (options.cameraObject && options.cameraObject._ortho === true) ||
    (options.camera.projection && options.camera.projection.type === 'orthographic') ||
    false

  //Create a camera
  var cameraOptions = {
    eye:     options.camera.eye     || [2,0,0],
    center:  options.camera.center  || [0,0,0],
    up:      options.camera.up      || [0,1,0],
    zoomMin: options.camera.zoomMax || 0.1,
    zoomMax: options.camera.zoomMin || 100,
    mode:    options.camera.mode    || 'turntable',
    _ortho:  isOrtho
  }

  //Create axes
  var axesOptions = options.axes || {}
  var axes = createAxes(gl, axesOptions)
  axes.enable = !axesOptions.disable

  //Create spikes
  var spikeOptions = options.spikes || {}
  var spikes = createSpikes(gl, spikeOptions)

  //Object list is empty initially
  var objects         = []
  var pickBufferIds   = []
  var pickBufferCount = []
  var pickBuffers     = []

  //Dirty flag, skip redraw if scene static
  var dirty       = true
  var pickDirty   = true

  var projection     = new Array(16)
  var model          = new Array(16)

  var cameraParams = {
    view:         null,
    projection:   projection,
    model:        model,
    _ortho:        false
  }

  var pickDirty = true

  var viewShape = [ gl.drawingBufferWidth, gl.drawingBufferHeight ]

  var camera = options.cameraObject || createCamera(canvas, cameraOptions)

  //Create scene object
  var scene = {
    gl:           gl,
    contextLost:  false,
    pixelRatio:   options.pixelRatio || 1,
    canvas:       canvas,
    selection:    selection,
    camera:       camera,
    axes:         axes,
    axesPixels:   null,
    spikes:       spikes,
    bounds:       bounds,
    objects:      objects,
    shape:        viewShape,
    aspect:       options.aspectRatio || [1,1,1],
    pickRadius:   options.pickRadius || 10,
    zNear:        options.zNear || 0.01,
    zFar:         options.zFar  || 1000,
    fovy:         options.fovy  || Math.PI/4,
    clearColor:   options.clearColor || [0,0,0,0],
    autoResize:   defaultBool(options.autoResize),
    autoBounds:   defaultBool(options.autoBounds),
    autoScale:    !!options.autoScale,
    autoCenter:   defaultBool(options.autoCenter),
    clipToBounds: defaultBool(options.clipToBounds),
    snapToData:   !!options.snapToData,
    onselect:     options.onselect || null,
    onrender:     options.onrender || null,
    onclick:      options.onclick  || null,
    cameraParams: cameraParams,
    oncontextloss: null,
    mouseListener: null,
    _stopped: false
  }

  var pickShape = [ (gl.drawingBufferWidth/scene.pixelRatio)|0, (gl.drawingBufferHeight/scene.pixelRatio)|0 ]

  function resizeListener() {
    if(scene._stopped) {
      return
    }
    if(!scene.autoResize) {
      return
    }
    var parent = canvas.parentNode
    var width  = 1
    var height = 1
    if(parent && parent !== document.body) {
      width  = parent.clientWidth
      height = parent.clientHeight
    } else {
      width  = window.innerWidth
      height = window.innerHeight
    }
    var nextWidth  = Math.ceil(width  * scene.pixelRatio)|0
    var nextHeight = Math.ceil(height * scene.pixelRatio)|0
    if(nextWidth !== canvas.width || nextHeight !== canvas.height) {
      canvas.width   = nextWidth
      canvas.height  = nextHeight
      var style = canvas.style
      style.position = style.position || 'absolute'
      style.left     = '0px'
      style.top      = '0px'
      style.width    = width  + 'px'
      style.height   = height + 'px'
      dirty = true
    }
  }
  if(scene.autoResize) {
    resizeListener()
  }
  window.addEventListener('resize', resizeListener)

  function reallocPickIds() {
    var numObjs = objects.length
    var numPick = pickBuffers.length
    for(var i=0; i<numPick; ++i) {
      pickBufferCount[i] = 0
    }
    obj_loop:
    for(var i=0; i<numObjs; ++i) {
      var obj = objects[i]
      var pickCount = obj.pickSlots
      if(!pickCount) {
        pickBufferIds[i] = -1
        continue
      }
      for(var j=0; j<numPick; ++j) {
        if(pickBufferCount[j] + pickCount < 255) {
          pickBufferIds[i] = j
          obj.setPickBase(pickBufferCount[j]+1)
          pickBufferCount[j] += pickCount
          continue obj_loop
        }
      }
      //Create new pick buffer
      var nbuffer = createSelect(gl, viewShape)
      pickBufferIds[i] = numPick
      pickBuffers.push(nbuffer)
      pickBufferCount.push(pickCount)
      obj.setPickBase(1)
      numPick += 1
    }
    while(numPick > 0 && pickBufferCount[numPick-1] === 0) {
      pickBufferCount.pop()
      pickBuffers.pop().dispose()
    }
  }

  scene.update = function(options) {

    if(scene._stopped) {
      return
    }
    options = options || {}
    dirty = true
    pickDirty = true
  }

  scene.add = function(obj) {
    if(scene._stopped) {
      return
    }
    obj.axes = axes
    objects.push(obj)
    pickBufferIds.push(-1)
    dirty = true
    pickDirty = true
    reallocPickIds()
  }

  scene.remove = function(obj) {
    if(scene._stopped) {
      return
    }
    var idx = objects.indexOf(obj)
    if(idx < 0) {
      return
    }
    objects.splice(idx, 1)
    pickBufferIds.pop()
    dirty = true
    pickDirty = true
    reallocPickIds()
  }

  scene.dispose = function() {
    if(scene._stopped) {
      return
    }

    scene._stopped = true

    window.removeEventListener('resize', resizeListener)
    canvas.removeEventListener('webglcontextlost', checkContextLoss)
    scene.mouseListener.enabled = false

    if(scene.contextLost) {
      return
    }

    //Destroy objects
    axes.dispose()
    spikes.dispose()
    for(var i=0; i<objects.length; ++i) {
      objects[i].dispose()
    }

    //Clean up buffers
    accumBuffer.dispose()
    for(var i=0; i<pickBuffers.length; ++i) {
      pickBuffers[i].dispose()
    }

    //Clean up shaders
    accumShader.dispose()

    //Release all references
    gl = null
    axes = null
    spikes = null
    objects = []
  }

  scene.wheelListener = mouseWheel(canvas, function(dx, dy) {
    // TODO remove now that we can disable scroll via scrollZoom?
    if(camera.keyBindingMode === false) return
    if(!camera.enableWheel) return

    if(camera._ortho) {
      var s = (dx > dy) ? 1.1 : 1.0 / 1.1

      scene.aspect[0] *= s
      scene.aspect[1] *= s
      scene.aspect[2] *= s
      scene.redraw()
    }
  }, true)

  //Update mouse position
  scene._mouseRotating = false
  scene._prevButtons = 0

  scene.enableMouseListeners = function() {

    scene.mouseListener = mouseChange(canvas, function(buttons, x, y) {
      if(scene._stopped) {
        return
      }

      var numPick = pickBuffers.length
      var numObjs = objects.length
      var prevObj = selection.object

      selection.distance = Infinity
      selection.mouse[0] = x
      selection.mouse[1] = y
      selection.object = null
      selection.screen = null
      selection.dataCoordinate = selection.dataPosition = null

      var change = false

      if(buttons && scene._prevButtons) {
        scene._mouseRotating = true
      } else {
        if(scene._mouseRotating) {
          pickDirty = true
        }
        scene._mouseRotating = false

        for(var i=0; i<numPick; ++i) {
          var result = pickBuffers[i].query(x, pickShape[1] - y - 1, scene.pickRadius)
          if(result) {
            if(result.distance > selection.distance) {
              continue
            }
            for(var j=0; j<numObjs; ++j) {
              var obj = objects[j]
              if(pickBufferIds[j] !== i) {
                continue
              }
              var objPick = obj.pick(result)
              if(objPick) {
                selection.buttons        = buttons
                selection.screen         = result.coord
                selection.distance       = result.distance
                selection.object         = obj
                selection.index          = objPick.distance
                selection.dataPosition   = objPick.position
                selection.dataCoordinate = objPick.dataCoordinate
                selection.data           = objPick
                change = true
              }
            }
          }
        }
      }

      if(prevObj && prevObj !== selection.object) {
        if(prevObj.highlight) {
          prevObj.highlight(null)
        }
        dirty = true
      }
      if(selection.object) {
        if(selection.object.highlight) {
          selection.object.highlight(selection.data)
        }
        dirty = true
      }

      change = change || (selection.object !== prevObj)
      if(change && scene.onselect) {
        scene.onselect(selection)
      }

      if((buttons & 1) && !(scene._prevButtons & 1) && scene.onclick) {
        scene.onclick(selection)
      }
      scene._prevButtons = buttons
    })
  }

  function checkContextLoss() {
    if(scene.contextLost) {
      return true
    }
    if(gl.isContextLost()) {
      scene.contextLost = true
      scene.mouseListener.enabled = false
      scene.selection.object = null
      if(scene.oncontextloss) {
        scene.oncontextloss()
      }
    }
  }

  canvas.addEventListener('webglcontextlost', checkContextLoss)

  //Render the scene for mouse picking
  function renderPick() {
    if(checkContextLoss()) {
      return
    }

    gl.colorMask(true, true, true, true)
    gl.depthMask(true)
    gl.disable(gl.BLEND)
    gl.enable(gl.DEPTH_TEST)

    var numObjs = objects.length
    var numPick = pickBuffers.length
    for(var j=0; j<numPick; ++j) {
      var buf = pickBuffers[j]
      buf.shape = pickShape
      buf.begin()
      for(var i=0; i<numObjs; ++i) {
        if(pickBufferIds[i] !== j) {
          continue
        }
        var obj = objects[i]
        if(obj.drawPick) {
          obj.pixelRatio = 1
          obj.drawPick(cameraParams)
        }
      }
      buf.end()
    }
  }

  var nBounds = [
    [ Infinity, Infinity, Infinity],
    [-Infinity,-Infinity,-Infinity]]

  var prevBounds = [nBounds[0].slice(), nBounds[1].slice()]

  function redraw() {
    if(checkContextLoss()) {
      return
    }

    resizeListener()

    //Tick camera
    var cameraMoved = scene.camera.tick()
    cameraParams.view = scene.camera.matrix
    dirty     = dirty || cameraMoved
    pickDirty = pickDirty || cameraMoved

      //Set pixel ratio
    axes.pixelRatio   = scene.pixelRatio
    spikes.pixelRatio = scene.pixelRatio

    //Check if any objects changed, recalculate bounds
    var numObjs = objects.length
    var lo = nBounds[0]
    var hi = nBounds[1]
    lo[0] = lo[1] = lo[2] =  Infinity
    hi[0] = hi[1] = hi[2] = -Infinity
    for(var i=0; i<numObjs; ++i) {
      var obj = objects[i]

      //Set the axes properties for each object
      obj.pixelRatio = scene.pixelRatio
      obj.axes = scene.axes

      dirty = dirty || !!obj.dirty
      pickDirty = pickDirty || !!obj.dirty
      var obb = obj.bounds
      if(obb) {
        var olo = obb[0]
        var ohi = obb[1]
        for(var j=0; j<3; ++j) {
          lo[j] = Math.min(lo[j], olo[j])
          hi[j] = Math.max(hi[j], ohi[j])
        }
      }
    }

    //Recalculate bounds
    var bounds = scene.bounds
    if(scene.autoBounds) {
      for(var j=0; j<3; ++j) {
        if(hi[j] < lo[j]) {
          lo[j] = -1
          hi[j] = 1
        } else {
          if(lo[j] === hi[j]) {
            lo[j] -= 1
            hi[j] += 1
          }
          var padding = 0.05 * (hi[j] - lo[j])
          lo[j] = lo[j] - padding
          hi[j] = hi[j] + padding
        }
        bounds[0][j] = lo[j]
        bounds[1][j] = hi[j]
      }
    }

    var boundsChanged = false
    for(var j=0; j<3; ++j) {
        boundsChanged = boundsChanged ||
            (prevBounds[0][j] !== bounds[0][j])  ||
            (prevBounds[1][j] !== bounds[1][j])
        prevBounds[0][j] = bounds[0][j]
        prevBounds[1][j] = bounds[1][j]
    }

    //Recalculate bounds
    pickDirty = pickDirty || boundsChanged
    dirty = dirty || boundsChanged

    if(!dirty) {
      return
    }

    if(boundsChanged) {
      var tickSpacing = [0,0,0]
      for(var i=0; i<3; ++i) {
        tickSpacing[i] = roundUpPow10((bounds[1][i]-bounds[0][i]) / 10.0)
      }
      if(axes.autoTicks) {
        axes.update({
          bounds: bounds,
          tickSpacing: tickSpacing
        })
      } else {
        axes.update({
          bounds: bounds
        })
      }
    }

    //Get scene
    var width  = gl.drawingBufferWidth
    var height = gl.drawingBufferHeight
    viewShape[0] = width
    viewShape[1] = height
    pickShape[0] = Math.max(width/scene.pixelRatio, 1)|0
    pickShape[1] = Math.max(height/scene.pixelRatio, 1)|0

    //Compute camera parameters

    if(isOrtho) {
      ortho(projection,
        -width/height,
        width/height,
        -1,
        1,
        scene.zNear,
        scene.zFar
      )
      cameraParams._ortho = true
    } else {
      perspective(projection,
        scene.fovy,
        width/height,
        scene.zNear,
        scene.zFar
      )
      cameraParams._ortho = false
    }

    //Compute model matrix
    for(var i=0; i<16; ++i) {
      model[i] = 0
    }
    model[15] = 1

    var maxS = 0
    for(var i=0; i<3; ++i) {
      maxS = Math.max(maxS, bounds[1][i] - bounds[0][i])
    }

    for(var i=0; i<3; ++i) {
      if(scene.autoScale) {
        model[5*i] = scene.aspect[i] / (bounds[1][i] - bounds[0][i])
      } else {
        model[5*i] = 1  / maxS
      }
      if(scene.autoCenter) {
        model[12+i] = -model[5*i] * 0.5 * (bounds[0][i] + bounds[1][i])
      }
    }

    //Apply axes/clip bounds
    for(var i=0; i<numObjs; ++i) {
      var obj = objects[i]

      //Set axes bounds
      obj.axesBounds = bounds

      //Set clip bounds
      if(scene.clipToBounds) {
        obj.clipBounds = bounds
      }
    }
    //Set spike parameters
    if(selection.object) {
      if(scene.snapToData) {
        spikes.position = selection.dataCoordinate
      } else {
        spikes.position = selection.dataPosition
      }
      spikes.bounds = bounds
    }

    //If state changed, then redraw pick buffers
    if(pickDirty) {
      pickDirty = false
      renderPick()
    }

    //Recalculate pixel data
    scene.axesPixels = axesRanges(scene.axes, cameraParams, width, height)

    //Call render callback
    if(scene.onrender) {
      scene.onrender()
    }

    //Read value
    gl.bindFramebuffer(gl.FRAMEBUFFER, null)
    gl.viewport(0, 0, width, height)

    //General strategy: 3 steps
    //  1. render non-transparent objects
    //  2. accumulate transparent objects into separate fbo
    //  3. composite final scene

    //Clear FBO
    var clearColor = scene.clearColor
    gl.clearColor(clearColor[0], clearColor[1], clearColor[2], clearColor[3])
    gl.clear(gl.COLOR_BUFFER_BIT | gl.DEPTH_BUFFER_BIT)
    gl.depthMask(true)
    gl.colorMask(true, true, true, true)
    gl.enable(gl.DEPTH_TEST)
    gl.depthFunc(gl.LEQUAL)
    gl.disable(gl.BLEND)
    gl.disable(gl.CULL_FACE)  //most visualization surfaces are 2 sided

    //Render opaque pass
    var hasTransparent = false
    if(axes.enable) {
      hasTransparent = hasTransparent || axes.isTransparent()
      axes.draw(cameraParams)
    }
    spikes.axes = axes
    if(selection.object) {
      spikes.draw(cameraParams)
    }

    gl.disable(gl.CULL_FACE)  //most visualization surfaces are 2 sided

    for(var i=0; i<numObjs; ++i) {
      var obj = objects[i]
      obj.axes = axes
      obj.pixelRatio = scene.pixelRatio
      if(obj.isOpaque && obj.isOpaque()) {
        obj.draw(cameraParams)
      }
      if(obj.isTransparent && obj.isTransparent()) {
        hasTransparent = true
      }
    }

    if(hasTransparent) {
      //Render transparent pass
      accumBuffer.shape = viewShape
      accumBuffer.bind()
      gl.clear(gl.DEPTH_BUFFER_BIT)
      gl.colorMask(false, false, false, false)
      gl.depthMask(true)
      gl.depthFunc(gl.LESS)

      //Render forward facing objects
      if(axes.enable && axes.isTransparent()) {
        axes.drawTransparent(cameraParams)
      }
      for(var i=0; i<numObjs; ++i) {
        var obj = objects[i]
        if(obj.isOpaque && obj.isOpaque()) {
          obj.draw(cameraParams)
        }
      }

      //Render transparent pass
      gl.enable(gl.BLEND)
      gl.blendEquation(gl.FUNC_ADD)
      gl.blendFunc(gl.ONE, gl.ONE_MINUS_SRC_ALPHA)
      gl.colorMask(true, true, true, true)
      gl.depthMask(false)
      gl.clearColor(0,0,0,0)
      gl.clear(gl.COLOR_BUFFER_BIT)

      if(axes.isTransparent()) {
        axes.drawTransparent(cameraParams)
      }

      for(var i=0; i<numObjs; ++i) {
        var obj = objects[i]
        if(obj.isTransparent && obj.isTransparent()) {
          obj.drawTransparent(cameraParams)
        }
      }

      //Unbind framebuffer
      gl.bindFramebuffer(gl.FRAMEBUFFER, null)

      //Draw composite pass
      gl.blendFunc(gl.ONE, gl.ONE_MINUS_SRC_ALPHA)
      gl.disable(gl.DEPTH_TEST)
      accumShader.bind()
      accumBuffer.color[0].bind(0)
      accumShader.uniforms.accumBuffer = 0
      drawTriangle(gl)

      //Turn off blending
      gl.disable(gl.BLEND)
    }

    //Clear dirty flags
    dirty = false
    for(var i=0; i<numObjs; ++i) {
      objects[i].dirty = false
    }
  }

  //Draw the whole scene
  function render() {
    if(scene._stopped || scene.contextLost) {
      return
    }
    // this order is important: ios safari sometimes has sync raf
    redraw()
    requestAnimationFrame(render)
  }

  scene.enableMouseListeners()
  render()

  //Force redraw of whole scene
  scene.redraw = function() {
    if(scene._stopped) {
      return
    }
    dirty = true
    redraw()
  }

  return scene
}
