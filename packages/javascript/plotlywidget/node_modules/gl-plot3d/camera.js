'use strict'

module.exports = createCamera

var now         = require('right-now')
var createView  = require('3d-view')
var mouseChange = require('mouse-change')
var mouseWheel  = require('mouse-wheel')
var mouseOffset = require('mouse-event-offset')
var hasPassive  = require('has-passive-events')

function createCamera(element, options) {
  element = element || document.body
  options = options || {}

  var limits  = [ 0.01, Infinity ]
  if('distanceLimits' in options) {
    limits[0] = options.distanceLimits[0]
    limits[1] = options.distanceLimits[1]
  }
  if('zoomMin' in options) {
    limits[0] = options.zoomMin
  }
  if('zoomMax' in options) {
    limits[1] = options.zoomMax
  }

  var view = createView({
    center: options.center || [0,0,0],
    up:     options.up     || [0,1,0],
    eye:    options.eye    || [0,0,10],
    mode:   options.mode   || 'orbit',
    distanceLimits: limits
  })

  var pmatrix = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
  var distance = 0.0
  var width   = element.clientWidth
  var height  = element.clientHeight

  var camera = {
    keyBindingMode: 'rotate',
    enableWheel: true,
    view:               view,
    element:            element,
    delay:              options.delay          || 16,
    rotateSpeed:        options.rotateSpeed    || 1,
    zoomSpeed:          options.zoomSpeed      || 1,
    translateSpeed:     options.translateSpeed || 1,
    flipX:              !!options.flipX,
    flipY:              !!options.flipY,
    modes:              view.modes,
    _ortho: options._ortho || (options.projection && options.projection.type === 'orthographic') || false,
    tick: function() {
      var t = now()
      var delay = this.delay
      var ctime = t - 2 * delay
      view.idle(t-delay)
      view.recalcMatrix(ctime)
      view.flush(t-(100+delay*2))
      var allEqual = true
      var matrix = view.computedMatrix
      for(var i=0; i<16; ++i) {
        allEqual = allEqual && (pmatrix[i] === matrix[i])
        pmatrix[i] = matrix[i]
      }
      var sizeChanged =
          element.clientWidth === width &&
          element.clientHeight === height
      width  = element.clientWidth
      height = element.clientHeight
      if(allEqual) {
        return !sizeChanged
      }
      distance = Math.exp(view.computedRadius[0])
      return true
    },
    lookAt: function(eye, center, up) {
      view.lookAt(view.lastT(), eye, center, up)
    },
    rotate: function(pitch, yaw, roll) {
      view.rotate(view.lastT(), pitch, yaw, roll)
    },
    pan: function(dx, dy, dz) {
      view.pan(view.lastT(), dx, dy, dz)
    },
    translate: function(dx, dy, dz) {
      view.translate(view.lastT(), dx, dy, dz)
    }
  }

  Object.defineProperties(camera, {
    matrix: {
      get: function() {
        return view.computedMatrix
      },
      set: function(mat) {
        view.setMatrix(view.lastT(), mat)
        return view.computedMatrix
      },
      enumerable: true
    },
    mode: {
      get: function() {
        return view.getMode()
      },
      set: function(mode) {
        var curUp = view.computedUp.slice()
        var curEye = view.computedEye.slice()
        var curCenter = view.computedCenter.slice()
        view.setMode(mode)
        if(mode === 'turntable') {
          // Hacky time warping stuff to generate smooth animation
          var t0 = now()
          view._active.lookAt(t0, curEye, curCenter, curUp)
          view._active.lookAt(t0 + 500, curEye, curCenter, [0, 0, 1])
          view._active.flush(t0)
        }
        return view.getMode()
      },
      enumerable: true
    },
    center: {
      get: function() {
        return view.computedCenter
      },
      set: function(ncenter) {
        view.lookAt(view.lastT(), null, ncenter)
        return view.computedCenter
      },
      enumerable: true
    },
    eye: {
      get: function() {
        return view.computedEye
      },
      set: function(neye) {
        view.lookAt(view.lastT(), neye)
        return view.computedEye
      },
      enumerable: true
    },
    up: {
      get: function() {
        return view.computedUp
      },
      set: function(nup) {
        view.lookAt(view.lastT(), null, null, nup)
        return view.computedUp
      },
      enumerable: true
    },
    distance: {
      get: function() {
        return distance
      },
      set: function(d) {
        view.setDistance(view.lastT(), d)
        return d
      },
      enumerable: true
    },
    distanceLimits: {
      get: function() {
        return view.getDistanceLimits(limits)
      },
      set: function(v) {
        view.setDistanceLimits(v)
        return v
      },
      enumerable: true
    }
  })

  element.addEventListener('contextmenu', function(ev) {
    ev.preventDefault()
    return false
  })

  camera._lastX = -1
  camera._lastY = -1
  camera._lastMods = {shift: false, control: false, alt: false, meta: false}

  camera.enableMouseListeners = function() {

    camera.mouseListener = mouseChange(element, handleInteraction)

    //enable simple touch interactions
    element.addEventListener('touchstart', function (ev) {
      var xy = mouseOffset(ev.changedTouches[0], element)
      handleInteraction(0, xy[0], xy[1], camera._lastMods)
      handleInteraction(1, xy[0], xy[1], camera._lastMods)

      ev.preventDefault()
    }, hasPassive ? {passive: false} : false)

    element.addEventListener('touchmove', function (ev) {
      var xy = mouseOffset(ev.changedTouches[0], element)
      handleInteraction(1, xy[0], xy[1], camera._lastMods)

      ev.preventDefault()
    }, hasPassive ? {passive: false} : false)

    element.addEventListener('touchend', function (ev) {

      handleInteraction(0, camera._lastX, camera._lastY, camera._lastMods)

      ev.preventDefault()
    }, hasPassive ? {passive: false} : false)

    function handleInteraction (buttons, x, y, mods) {
      var keyBindingMode = camera.keyBindingMode

      if(keyBindingMode === false) return

      var rotate = keyBindingMode === 'rotate'
      var pan = keyBindingMode === 'pan'
      var zoom = keyBindingMode === 'zoom'

      var ctrl = !!mods.control
      var alt = !!mods.alt
      var shift = !!mods.shift
      var left = !!(buttons & 1)
      var right = !!(buttons & 2)
      var middle = !!(buttons & 4)

      var scale = 1.0 / element.clientHeight
      var dx    = scale * (x - camera._lastX)
      var dy    = scale * (y - camera._lastY)

      var flipX = camera.flipX ? 1 : -1
      var flipY = camera.flipY ? 1 : -1

      var drot  = Math.PI * camera.rotateSpeed

      var t = now()

      if(camera._lastX !== -1 && camera._lastY !== -1) {
        if((rotate && left && !ctrl && !alt && !shift) || (left && !ctrl && !alt && shift)) {
          // Rotate
          view.rotate(t, flipX * drot * dx, -flipY * drot * dy, 0)
        }

        if((pan && left && !ctrl && !alt && !shift) || right || (left && ctrl && !alt && !shift)) {
          // Pan
          view.pan(t, -camera.translateSpeed * dx * distance, camera.translateSpeed * dy * distance, 0)
        }

        if((zoom && left && !ctrl && !alt && !shift) || middle || (left && !ctrl && alt && !shift)) {
          // Zoom
          var kzoom = -camera.zoomSpeed * dy / window.innerHeight * (t - view.lastT()) * 100
          view.pan(t, 0, 0, distance * (Math.exp(kzoom) - 1))
        }
      }

      camera._lastX = x
      camera._lastY = y
      camera._lastMods = mods

      return true
    }

    camera.wheelListener = mouseWheel(element, function(dx, dy) {
      // TODO remove now that we can disable scroll via scrollZoom?
      if(camera.keyBindingMode === false) return
      if(!camera.enableWheel) return

      var flipX = camera.flipX ? 1 : -1
      var flipY = camera.flipY ? 1 : -1
      var t = now()
      if(Math.abs(dx) > Math.abs(dy)) {
        view.rotate(t, 0, 0, -dx * flipX * Math.PI * camera.rotateSpeed / window.innerWidth)
      } else {
        if(!camera._ortho) {
          var kzoom = -camera.zoomSpeed * flipY * dy / window.innerHeight * (t - view.lastT()) / 20.0
          view.pan(t, 0, 0, distance * (Math.exp(kzoom) - 1))
        }
      }
    }, true)
  }

  camera.enableMouseListeners()

  return camera
}
