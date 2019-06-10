'use strict'

var tape = require('tape')
var almostEqual = require('array-almost-equal')
var filterVec = require('../fvec')

tape('filter-vec', function(t) {
  var v = filterVec([0,0,0,0])


  t.ok(almostEqual(v.curve(0), [0,0,0,0]))

  t.ok(almostEqual(v.curve(-1e6), [0,0,0,0]))


  v.push(1,1,2,3,4)
  t.ok(almostEqual(v.curve(0), [0,0,0,0]))
  t.ok(almostEqual(v.curve(1), [1,2,3,4]))
  t.ok(almostEqual(v.dcurve(1), [1,2,3,4]))

  v.push(3, 2,3,4,5)
  t.ok(almostEqual(v.curve(1), [1,2,3,4]))
  t.ok(almostEqual(v.dcurve(1), [1,2,3,4]))
  t.ok(almostEqual(v.curve(3), [2,3,4,5]))
  t.ok(almostEqual(v.dcurve(3), [0.5,0.5,0.5,0.5]))

  v.idle(4)
  t.ok(almostEqual(v.curve(4), [2,3,4,5]))
  t.ok(almostEqual(v.dcurve(4), [0,0,0,0]))
  t.ok(v.stable(5))

  v.move(6, 1,-1,1,-1)
  t.ok(almostEqual(v.curve(6), [3,2,5,4]), v.curve(6))
  t.ok(almostEqual(v.dcurve(6), [0.5,-0.5,0.5,-0.5]))
  t.ok(!v.stable(7))


  t.end()
})
