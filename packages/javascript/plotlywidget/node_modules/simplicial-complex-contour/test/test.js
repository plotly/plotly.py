'use strict'

var tape = require('tape')
var msc = require('../contour')

tape('marching simplex contour', function(t) {

  var vals = [
    -1,
    -1,
    1,
    -1,
    -1
  ]

  var cells = [
    [0,1,4],
    [1,2,4],
    [2,3,4],
    [3,0,4]
  ]

  console.log(msc(cells, vals))

  t.end()
})