'use strict'

var test = require('tape')
var compareCells = require('../compare')

test("compareCells", function(t) {
  t.ok(!!compareCells([], [1]))
  t.ok(!!compareCells([1,3,5], [1,3,5,7]))

  t.ok(!!compareCells([2], [3]) )
  t.ok( !compareCells([0], [0]) )

  t.ok(!!compareCells([4,3],[7,0]))
  t.ok( !compareCells([10,11], [11,10]))

  t.ok(!!compareCells([2,0,5], [3,0,4]))
  t.ok( !compareCells([0,1,2], [2,0,1]))
  t.ok( !compareCells([0,1,2], [1,2,0]))
  t.ok( !compareCells([0,1,2], [1,0,2]))

  t.ok(!!compareCells([2,4,5,6], [6,7,8,9]))
  t.ok(!!compareCells([1,2,3,6], [1,2,3,7]))
  t.ok( !compareCells([0,1,2,3], [3,1,2,0]))

  t.end()
})
