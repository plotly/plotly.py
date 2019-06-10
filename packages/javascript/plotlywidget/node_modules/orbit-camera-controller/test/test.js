'use strict'

var tape = require('tape')
var createOrbit = require('../orbit')
var lookAt = require('gl-mat4/lookAt')

function arrayApproxEquals(a, b) {
  for(var i=0; i<a.length; ++i) {
    if(!(Math.abs(a[i] - b[i]) < 1e-4)) {
      return false
    }
  }
  return true
}

function matrixApproxEquals(a, b) {
  var x = a[15]
  var y = b[15]
  for(var i=0; i<15; ++i) {
    if(!(Math.abs(a[i] * y - b[i] * x) < 1e-4)) {
      return false
    }
  }
  return true
}

tape('orbit camera', function(t) {

  for(var i=0; i<100; ++i) {
    var center = [Math.random()-0.5, Math.random()-0.5, Math.random()-0.5]
    var eye = [Math.random()-0.5, Math.random()-0.5, Math.random()-0.5]
    var up = [Math.random()-0.5, Math.random()-0.5, Math.random()-0.5]

    var mat = lookAt([], eye, center, up)
    var smat = mat[15]

    var controller = createOrbit()
    controller.lookAt(10, eye, center, up)

    var orbitMat = controller.getMatrix(10, [])
    t.ok(matrixApproxEquals(mat, orbitMat), 'compare mat: ' + mat + '   :    ' + orbitMat)

    var ocenter = controller.computedCenter
    var oeye = controller.computedEye
    t.ok(arrayApproxEquals(center, ocenter), 'compare center: ' + center + ':' + ocenter)
    t.ok(arrayApproxEquals(eye, oeye), 'compare eye: '  + eye + ':' + oeye)

    var dist = 0.0
    for(var j=0; j<3; ++j) {
      dist += Math.pow(eye[j] - center[j], 2)
    }
    dist = Math.sqrt(dist)
    t.ok(Math.abs(dist - Math.exp(controller.computedRadius[0])) < 1e-4, 'distance:' + controller.computedRadius + " expect " + dist)
  }

  for(var i=0; i<100; ++i) {
    var center = [Math.random()-0.5, Math.random()-0.5, Math.random()-0.5]
    var eye = [Math.random()-0.5, Math.random()-0.5, Math.random()-0.5]
    var up = [Math.random()-0.5, Math.random()-0.5, Math.random()-0.5]

    var mat = lookAt([], eye, center, up)

    var controller = createOrbit()
    controller.setMatrix(10, mat)

    var orbitMat = controller.getMatrix(10, [])
    t.ok(matrixApproxEquals(mat, orbitMat), 'compare mat: ' + mat + '   :    ' + orbitMat)

    var oeye = controller.computedEye
    t.ok(arrayApproxEquals(eye, oeye), 'compare eye: '  + eye + ':' + oeye)
  }

  t.end()
})