'use strict'

module.exports = createAxes

var createText        = require('./lib/text.js')
var createLines       = require('./lib/lines.js')
var createBackground  = require('./lib/background.js')
var getCubeProperties = require('./lib/cube.js')
var Ticks             = require('./lib/ticks.js')

var identity = new Float32Array([
  1, 0, 0, 0,
  0, 1, 0, 0,
  0, 0, 1, 0,
  0, 0, 0, 1])

function copyVec3(a, b) {
  a[0] = b[0]
  a[1] = b[1]
  a[2] = b[2]
  return a
}

function Axes(gl) {
  this.gl             = gl

  this.pixelRatio     = 1

  this.bounds         = [ [-10, -10, -10],
                          [ 10,  10,  10] ]
  this.ticks          = [ [], [], [] ]
  this.autoTicks      = true
  this.tickSpacing    = [ 1, 1, 1 ]

  this.tickEnable     = [ true, true, true ]
  this.tickFont       = [ 'sans-serif', 'sans-serif', 'sans-serif' ]
  this.tickSize       = [ 12, 12, 12 ]
  this.tickAngle      = [ 0, 0, 0 ]
  this.tickAlign      = [ 'auto', 'auto', 'auto' ]
  this.tickColor      = [ [0,0,0,1], [0,0,0,1], [0,0,0,1] ]
  this.tickPad        = [ 10, 10, 10 ]

  this.lastCubeProps  = {
    cubeEdges: [0,0,0],
    axis:      [0,0,0]
  }

  this.labels         = [ 'x', 'y', 'z' ]
  this.labelEnable    = [ true, true, true ]
  this.labelFont      = 'sans-serif'
  this.labelSize      = [ 20, 20, 20 ]
  this.labelAngle     = [ 0, 0, 0 ]
  this.labelAlign     = [ 'auto', 'auto', 'auto' ]
  this.labelColor     = [ [0,0,0,1], [0,0,0,1], [0,0,0,1] ]
  this.labelPad       = [ 10, 10, 10 ]

  this.lineEnable     = [ true, true, true ]
  this.lineMirror     = [ false, false, false ]
  this.lineWidth      = [ 1, 1, 1 ]
  this.lineColor      = [ [0,0,0,1], [0,0,0,1], [0,0,0,1] ]

  this.lineTickEnable = [ true, true, true ]
  this.lineTickMirror = [ false, false, false ]
  this.lineTickLength = [ 0, 0, 0 ]
  this.lineTickWidth  = [ 1, 1, 1 ]
  this.lineTickColor  = [ [0,0,0,1], [0,0,0,1], [0,0,0,1] ]

  this.gridEnable     = [ true, true, true ]
  this.gridWidth      = [ 1, 1, 1 ]
  this.gridColor      = [ [0,0,0,1], [0,0,0,1], [0,0,0,1] ]

  this.zeroEnable     = [ true, true, true ]
  this.zeroLineColor  = [ [0,0,0,1], [0,0,0,1], [0,0,0,1] ]
  this.zeroLineWidth  = [ 2, 2, 2 ]

  this.backgroundEnable = [ false, false, false ]
  this.backgroundColor  = [ [0.8, 0.8, 0.8, 0.5],
                            [0.8, 0.8, 0.8, 0.5],
                            [0.8, 0.8, 0.8, 0.5] ]

  this._firstInit = true
  this._text  = null
  this._lines = null
  this._background = createBackground(gl)
}

var proto = Axes.prototype

proto.update = function(options) {
  options = options || {}

  //Option parsing helper functions
  function parseOption(nest, cons, name) {
    if(name in options) {
      var opt = options[name]
      var prev = this[name]
      var next
      if(nest ? (Array.isArray(opt) && Array.isArray(opt[0])) :
                 Array.isArray(opt) ) {
        this[name] = next = [ cons(opt[0]), cons(opt[1]), cons(opt[2]) ]
      } else {
        this[name] = next = [ cons(opt), cons(opt), cons(opt) ]
      }
      for(var i=0; i<3; ++i) {
        if(next[i] !== prev[i]) {
          return true
        }
      }
    }
    return false
  }

  var NUMBER  = parseOption.bind(this, false, Number)
  var BOOLEAN = parseOption.bind(this, false, Boolean)
  var STRING  = parseOption.bind(this, false, String)
  var COLOR   = parseOption.bind(this, true, function(v) {
    if(Array.isArray(v)) {
      if(v.length === 3) {
        return [ +v[0], +v[1], +v[2], 1.0 ]
      } else if(v.length === 4) {
        return [ +v[0], +v[1], +v[2], +v[3] ]
      }
    }
    return [ 0, 0, 0, 1 ]
  })

  //Tick marks and bounds
  var nextTicks
  var ticksUpdate   = false
  var boundsChanged = false
  if('bounds' in options) {
    var bounds = options.bounds
i_loop:
    for(var i=0; i<2; ++i) {
      for(var j=0; j<3; ++j) {
        if(bounds[i][j] !== this.bounds[i][j]) {
          boundsChanged = true
        }
        this.bounds[i][j] = bounds[i][j]
      }
    }
  }
  if('ticks' in options) {
    nextTicks      = options.ticks
    ticksUpdate    = true
    this.autoTicks = false
    for(var i=0; i<3; ++i) {
      this.tickSpacing[i] = 0.0
    }
  } else if(NUMBER('tickSpacing')) {
    this.autoTicks  = true
    boundsChanged   = true
  }

  if(this._firstInit) {
    if(!('ticks' in options || 'tickSpacing' in options)) {
      this.autoTicks = true
    }

    //Force tick recomputation on first update
    boundsChanged   = true
    ticksUpdate     = true
    this._firstInit = false
  }

  if(boundsChanged && this.autoTicks) {
    nextTicks = Ticks.create(this.bounds, this.tickSpacing)
    ticksUpdate = true
  }

  //Compare next ticks to previous ticks, only update if needed
  if(ticksUpdate) {
    for(var i=0; i<3; ++i) {
      nextTicks[i].sort(function(a,b) {
        return a.x-b.x
      })
    }
    if(Ticks.equal(nextTicks, this.ticks)) {
      ticksUpdate = false
    } else {
      this.ticks = nextTicks
    }
  }

  //Parse tick properties
  BOOLEAN('tickEnable')
  if(STRING('tickFont')) {
    ticksUpdate = true  //If font changes, must rebuild vbo
  }
  NUMBER('tickSize')
  NUMBER('tickAngle')
  NUMBER('tickPad')
  COLOR('tickColor')

  //Axis labels
  var labelUpdate = STRING('labels')
  if(STRING('labelFont')) {
    labelUpdate = true
  }
  BOOLEAN('labelEnable')
  NUMBER('labelSize')
  NUMBER('labelPad')
  COLOR('labelColor')

  //Axis lines
  BOOLEAN('lineEnable')
  BOOLEAN('lineMirror')
  NUMBER('lineWidth')
  COLOR('lineColor')

  //Axis line ticks
  BOOLEAN('lineTickEnable')
  BOOLEAN('lineTickMirror')
  NUMBER('lineTickLength')
  NUMBER('lineTickWidth')
  COLOR('lineTickColor')

  //Grid lines
  BOOLEAN('gridEnable')
  NUMBER('gridWidth')
  COLOR('gridColor')

  //Zero line
  BOOLEAN('zeroEnable')
  COLOR('zeroLineColor')
  NUMBER('zeroLineWidth')

  //Background
  BOOLEAN('backgroundEnable')
  COLOR('backgroundColor')

  //Update text if necessary
  if(!this._text) {
    this._text = createText(
      this.gl,
      this.bounds,
      this.labels,
      this.labelFont,
      this.ticks,
      this.tickFont)
  } else if(this._text && (labelUpdate || ticksUpdate)) {
    this._text.update(
      this.bounds,
      this.labels,
      this.labelFont,
      this.ticks,
      this.tickFont)
  }

  //Update lines if necessary
  if(this._lines && ticksUpdate) {
    this._lines.dispose()
    this._lines = null
  }
  if(!this._lines) {
    this._lines = createLines(this.gl, this.bounds, this.ticks)
  }
}

function OffsetInfo() {
  this.primalOffset = [0,0,0]
  this.primalMinor  = [0,0,0]
  this.mirrorOffset = [0,0,0]
  this.mirrorMinor  = [0,0,0]
}

var LINE_OFFSET = [ new OffsetInfo(), new OffsetInfo(), new OffsetInfo() ]

function computeLineOffset(result, i, bounds, cubeEdges, cubeAxis) {
  var primalOffset = result.primalOffset
  var primalMinor  = result.primalMinor
  var dualOffset   = result.mirrorOffset
  var dualMinor    = result.mirrorMinor
  var e = cubeEdges[i]

  //Calculate offsets
  for(var j=0; j<3; ++j) {
    if(i === j) {
      continue
    }
    var a = primalOffset,
        b = dualOffset,
        c = primalMinor,
        d = dualMinor
    if(e & (1<<j)) {
      a = dualOffset
      b = primalOffset
      c = dualMinor
      d = primalMinor
    }
    a[j] = bounds[0][j]
    b[j] = bounds[1][j]
    if(cubeAxis[j] > 0) {
      c[j] = -1
      d[j] = 0
    } else {
      c[j] = 0
      d[j] = +1
    }
  }
}

var CUBE_ENABLE = [0,0,0]
var DEFAULT_PARAMS = {
  model:      identity,
  view:       identity,
  projection: identity,
  _ortho:      false
}

proto.isOpaque = function() {
  return true
}

proto.isTransparent = function() {
  return false
}

proto.drawTransparent = function(params) {}

var ALIGN_OPTION_AUTO = 0 // i.e. as defined in the shader the text would rotate to stay upwards range: [-90,90]

var PRIMAL_MINOR  = [0,0,0]
var MIRROR_MINOR  = [0,0,0]
var PRIMAL_OFFSET = [0,0,0]

proto.draw = function(params) {
  params = params || DEFAULT_PARAMS

  var gl = this.gl

  //Geometry for camera and axes
  var model       = params.model || identity
  var view        = params.view || identity
  var projection  = params.projection || identity
  var bounds      = this.bounds
  var isOrtho     = params._ortho || false

  //Unpack axis info
  var cubeParams  = getCubeProperties(model, view, projection, bounds, isOrtho)
  var cubeEdges   = cubeParams.cubeEdges
  var cubeAxis    = cubeParams.axis

  var cx = view[12]
  var cy = view[13]
  var cz = view[14]
  var cw = view[15]

  var orthoFix = (isOrtho) ? 2 : 1 // double up padding for orthographic ticks & labels
  var pixelScaleF = orthoFix * this.pixelRatio * (projection[3]*cx + projection[7]*cy + projection[11]*cz + projection[15]*cw) / gl.drawingBufferHeight

  for(var i=0; i<3; ++i) {
    this.lastCubeProps.cubeEdges[i] = cubeEdges[i]
    this.lastCubeProps.axis[i] = cubeAxis[i]
  }

  //Compute axis info
  var lineOffset  = LINE_OFFSET
  for(var i=0; i<3; ++i) {
    computeLineOffset(
      LINE_OFFSET[i],
      i,
      this.bounds,
      cubeEdges,
      cubeAxis)
  }

  //Set up state parameters
  var gl = this.gl

  //Draw background first
  var cubeEnable = CUBE_ENABLE
  for(var i=0; i<3; ++i) {
    if(this.backgroundEnable[i]) {
      cubeEnable[i] = cubeAxis[i]
    } else {
      cubeEnable[i] = 0
    }
  }

  this._background.draw(
    model,
    view,
    projection,
    bounds,
    cubeEnable,
    this.backgroundColor)

  //Draw lines
  this._lines.bind(
    model,
    view,
    projection,
    this)

  //First draw grid lines and zero lines
  for(var i=0; i<3; ++i) {
    var x = [0,0,0]
    if(cubeAxis[i] > 0) {
      x[i] = bounds[1][i]
    } else {
      x[i] = bounds[0][i]
    }

    //Draw grid lines
    for(var j=0; j<2; ++j) {
      var u = (i + 1 + j) % 3
      var v = (i + 1 + (j^1)) % 3
      if(this.gridEnable[u]) {
        this._lines.drawGrid(u, v, this.bounds, x, this.gridColor[u], this.gridWidth[u]*this.pixelRatio)
      }
    }

    //Draw zero lines (need to do this AFTER all grid lines are drawn)
    for(var j=0; j<2; ++j) {
      var u = (i + 1 + j) % 3
      var v = (i + 1 + (j^1)) % 3
      if(this.zeroEnable[v]) {
        //Check if zero line in bounds
        if(Math.min(bounds[0][v], bounds[1][v]) <= 0 && Math.max(bounds[0][v], bounds[1][v]) >= 0) {
          this._lines.drawZero(u, v, this.bounds, x, this.zeroLineColor[v], this.zeroLineWidth[v]*this.pixelRatio)
        }
      }
    }
  }

  //Then draw axis lines and tick marks
  for(var i=0; i<3; ++i) {

    //Draw axis lines
    if(this.lineEnable[i]) {
      this._lines.drawAxisLine(i, this.bounds, lineOffset[i].primalOffset, this.lineColor[i], this.lineWidth[i]*this.pixelRatio)
    }
    if(this.lineMirror[i]) {
      this._lines.drawAxisLine(i, this.bounds, lineOffset[i].mirrorOffset, this.lineColor[i], this.lineWidth[i]*this.pixelRatio)
    }

    //Compute minor axes
    var primalMinor = copyVec3(PRIMAL_MINOR, lineOffset[i].primalMinor)
    var mirrorMinor = copyVec3(MIRROR_MINOR, lineOffset[i].mirrorMinor)
    var tickLength  = this.lineTickLength
    for(var j=0; j<3; ++j) {
      var scaleFactor = pixelScaleF / model[5*j]
      primalMinor[j] *= tickLength[j] * scaleFactor
      mirrorMinor[j] *= tickLength[j] * scaleFactor
    }



    //Draw axis line ticks
    if(this.lineTickEnable[i]) {
      this._lines.drawAxisTicks(i, lineOffset[i].primalOffset, primalMinor, this.lineTickColor[i], this.lineTickWidth[i]*this.pixelRatio)
    }
    if(this.lineTickMirror[i]) {
      this._lines.drawAxisTicks(i, lineOffset[i].mirrorOffset, mirrorMinor, this.lineTickColor[i], this.lineTickWidth[i]*this.pixelRatio)
    }
  }
  this._lines.unbind()

  //Draw text sprites
  this._text.bind(
    model,
    view,
    projection,
    this.pixelRatio)

  var alignOpt // options in shader are from this list {-1, 0, 1, 2, 3, ..., n}
  // -1: backward compatible
  //  0: raw data
  //  1: auto align, free angles
  //  2: auto align, horizontal or vertical
  //3-n: auto align, round to n directions e.g. 12 -> round to angles with 30-degree steps

  var hv_ratio = 0.5 // can have an effect on the ratio between horizontals and verticals when using option 2

  var enableAlign
  var alignDir

  function alignTo(i) {
    alignDir = [0,0,0]
    alignDir[i] = 1
  }

  function solveTickAlignments(i, minor, major) {

    var i1 = (i + 1) % 3
    var i2 = (i + 2) % 3

    var A = minor[i1]
    var B = minor[i2]
    var C = major[i1]
    var D = major[i2]

         if ((A > 0) && (D > 0)) { alignTo(i1); return; }
    else if ((A > 0) && (D < 0)) { alignTo(i1); return; }
    else if ((A < 0) && (D > 0)) { alignTo(i1); return; }
    else if ((A < 0) && (D < 0)) { alignTo(i1); return; }
    else if ((B > 0) && (C > 0)) { alignTo(i2); return; }
    else if ((B > 0) && (C < 0)) { alignTo(i2); return; }
    else if ((B < 0) && (C > 0)) { alignTo(i2); return; }
    else if ((B < 0) && (C < 0)) { alignTo(i2); return; }
  }

  for(var i=0; i<3; ++i) {

    var minor      = lineOffset[i].primalMinor
    var major      = lineOffset[i].mirrorMinor

    var offset     = copyVec3(PRIMAL_OFFSET, lineOffset[i].primalOffset)

    for(var j=0; j<3; ++j) {
      if(this.lineTickEnable[i]) {
        offset[j] += pixelScaleF * minor[j] * Math.max(this.lineTickLength[j], 0)  / model[5*j]
      }
    }

    var axis = [0,0,0]
    axis[i] = 1

    //Draw tick text
    if(this.tickEnable[i]) {

      if(this.tickAngle[i] === -3600) {
        this.tickAngle[i] = 0
        this.tickAlign[i] = 'auto'
      } else {
        this.tickAlign[i] = -1
      }

      enableAlign = 1;

      alignOpt = [this.tickAlign[i], hv_ratio, enableAlign]
      if(alignOpt[0] === 'auto') alignOpt[0] = ALIGN_OPTION_AUTO
      else alignOpt[0] = parseInt('' + alignOpt[0])

      alignDir = [0,0,0]
      solveTickAlignments(i, minor, major)

      //Add tick padding
      for(var j=0; j<3; ++j) {
        offset[j] += pixelScaleF * minor[j] * this.tickPad[j] / model[5*j]
      }

      //Draw axis
      this._text.drawTicks(
        i,
        this.tickSize[i],
        this.tickAngle[i],
        offset,
        this.tickColor[i],
        axis,
        alignDir,
        alignOpt)
    }

    //Draw labels
    if(this.labelEnable[i]) {

      enableAlign = 0
      alignDir = [0,0,0]
      if(this.labels[i].length > 4) { // for large label axis enable alignDir to axis
        alignTo(i)
        enableAlign = 1
      }

      alignOpt = [this.labelAlign[i], hv_ratio, enableAlign]
      if(alignOpt[0] === 'auto') alignOpt[0] = ALIGN_OPTION_AUTO
      else alignOpt[0] = parseInt('' + alignOpt[0])

      //Add label padding
      for(var j=0; j<3; ++j) {
        offset[j] += pixelScaleF * minor[j] * this.labelPad[j] / model[5*j]
      }
      offset[i] += 0.5 * (bounds[0][i] + bounds[1][i])

      //Draw axis
      this._text.drawLabel(
        i,
        this.labelSize[i],
        this.labelAngle[i],
        offset,
        this.labelColor[i],
        [0,0,0],
        alignDir,
        alignOpt)
    }
  }

  this._text.unbind()
}

proto.dispose = function() {
  this._text.dispose()
  this._lines.dispose()
  this._background.dispose()
  this._lines = null
  this._text = null
  this._background = null
  this.gl = null
}

function createAxes(gl, options) {
  var axes = new Axes(gl)
  axes.update(options)
  return axes
}
