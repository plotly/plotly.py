"use strict"

var tape = require("tape")
var orderSegments = require("../lib/order-segments")

function sgn(x) {
  if(x < 0) { 
    return -1
  }
  if(x > 0) {
    return 1
  }
  return 0
}

function compareSegments(t, a, b, s) {
  var label = " (" + a.join(")-(") + ") / (" + b.join(")-(") + ")"
  for(var flip=0; flip<2; ++flip) {
    for(var i=0; i<2; ++i) {
      for(var j=0; j<2; ++j) {
        t.equals(sgn(orderSegments(
          [a[i], a[i^1]],
          [b[j], b[j^1]])), s, "check order flip:" + flip + ",aperm:" + i + ",bperm:" + j + label)
      }
    }
    var tmp = a
    a = b
    b = tmp
    s *= -1
  }
}

tape("order-segments", function(t) {

  //Harder cases
  compareSegments(t,
    [[0,0], [0.5,0.5]],
    [[0,2], [2,0]],
    1)

  compareSegments(t,
    [[0,0], [0.5,0.5]],
    [[-2,0], [1,-3]],
    -1)

  //Check some easy examples
  compareSegments(t, 
    [[0, 0], [1, 0]],
    [[0, 1], [1, 1]],
    1)
  compareSegments(t,
    [[0, 0], [1, 0]],
    [[1, 0], [2, 0]],
    1)
  //Create a fan of segments
  var fan = [[[0,0], [0,-1]]]
  for(var x=1; x<30; ++x) {
    var theta = (x / 30) * Math.PI
    fan.push(
      [[0,0],
        [Math.sin(theta), -Math.cos(theta)]])
  }
  fan.push([[0,0], [0, 1]])
  for(var i=0; i<fan.length; ++i) {
    compareSegments(t, fan[i], fan[i], 0)
    for(var j=i+1; j<fan.length; ++j) {
      compareSegments(t, fan[i], fan[j], 1)
    }
  }
  //Create negative fan
  var negFan = fan.map(function(seg) {
    return [seg[0], [-seg[1][0], seg[1][1]]]
  })
  for(var i=0; i<fan.length; ++i) {
    compareSegments(t, negFan[i], negFan[i], 0)
    for(var j=i+1; j<fan.length; ++j) {
      compareSegments(t, fan[i], fan[j], 1)
    }
  }

  t.end()
})