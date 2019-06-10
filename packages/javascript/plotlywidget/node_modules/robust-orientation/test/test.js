"use strict"

var tape = require("tape")
var orientation = require("../orientation.js")

tape("2d orientation", function(t) {

  t.equals(orientation(
    [0.1, 0.1],
    [0.1, 0.1],
    [0.3, 0.7]
    ), 0)

  t.ok(orientation(
      [0,0],
      [-1e-64,0],
      [0,1]
    )>0)

  t.equals(orientation(
      [0,0],
      [1e-64,1e-64],
      [1,1]
    ), 0)

  t.ok(orientation(
      [0,0],
      [1e-64,0],
      [0,1]
    )<0)

  var x = 1e-64
  for(var i=0; i<200; ++i) {
    t.ok(orientation(
        [-x, 0],
        [0, 1],
        [x, 0]
      )>0)
   t.equals(orientation(
        [-x, 0],
        [0, 0],
        [x, 0]
      ), 0)
   t.ok(orientation(
        [-x, 0],
        [0, -1],
        [x, 0]
      )<0, "x=" + x)
   t.ok(orientation(
      [0, 1],
      [0, 0],
      [x, x]
    )<0, "x=" + x)
    x *= 10
  }
  t.end()
})

tape("3d orientation", function(t) {

  t.ok(orientation(
      [0, 0, 0],
      [1, 0, 0],
      [0, 1, 0],
      [0, 0, 1]
    ) < 0)

  t.ok(orientation(
      [0, 0, 0],
      [1, 0, 0],
      [0, 0, 1],
      [0, 1, 0]
    ) > 0)


  t.ok(orientation(
      [0, 0, 0],
      [1e-64, 0, 0],
      [0, 0, 1],
      [0, 1e64, 0]
    ) > 0)

  t.end()
})

tape("4d orientation", function(t) {

  t.ok(orientation(
    [0,0,0,0],
    [1,0,0,0],
    [0,1,0,0],
    [0,0,1,0],
    [0,0,0,1]
  ) > 0)

  t.end()
})

tape("5d orientation", function(t) {

  t.ok(orientation(
    [0,0,0,0,0],
    [1,0,0,0,0],
    [0,1,0,0,0],
    [0,0,1,0,0],
    [0,0,0,1,0],
    [0,0,0,0,1]
  ) > 0)

  t.end()
})