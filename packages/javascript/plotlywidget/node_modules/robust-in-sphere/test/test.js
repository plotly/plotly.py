"use strict"

var inSphere = require("../in-sphere.js")
var twoProduct = require("two-product")

function sgn(x) {
  if(x < 0) {
    return -1
  }
  if(x > 0) {
    return 1
  }
  return 0
}

require("tape")(function(t) {

  t.equals(sgn(inSphere([0], [1], [0.5])), -1)
  t.equals(sgn(inSphere([0], [1], [1.5])), 1)

  t.equals(sgn(inSphere(
      [0,-1],
      [1,0],
      [0,1],
      [-0.5,0])), 1)

  t.equals(sgn(inSphere(
      [0,-1],
      [1,0],
      [0,1],
      [-1,0])), 0)

  t.equals(sgn(inSphere(
      [0,-1],
      [1,0],
      [0,1],
      [-1.5,0])), -1 )

  var x = 1e-64
  for(var i=0; i<128; ++i) {
    t.equals(sgn(inSphere(
        [0,x],
        [-x,-x],
        [x,-x],
        [0,0])), 1, "sphere test:" + x)
    t.equals(sgn(inSphere(
        [0,x],
        [-x,-x],
        [x,-x],
        [0,2*x])), -1, "sphere test:" + x)
    
    t.equals(sgn(inSphere(
        [0,x],
        [-x,-x],
        [x,-x],
        [0,x])), 0, "sphere test:" + x)
    
    x *= 10
  }

  t.end()
})