'use strict'

var tape = require('tape')
var shuffle = require('shuffle-array')
var compareCells = require('../compare')

function testStability(t, array) {
  var expected = array.slice().sort(compareCells).map(function(c) {
    return c.slice().sort()
  }).join(':')
  for(var i=0; i<10; ++i) {
    var actual = shuffle(array).sort(compareCells).map(function(c) {
      return c.slice().sort()
    }).join(':')
    t.equals(actual, expected)
  }
}

tape('stability test - homog dimension', function(t) {
  for(var d=1; d<=5; ++d) {
    for(var n=0; n<10; ++n) {
      var cells = new Array(100)
      for(var j=0; j<100; ++j) {
        var c = cells[j] = new Array(d)
        for(var k=0; k<d; ++k) {
          c[k] = (Math.random() * 20)|0
        }
      }
      testStability(t, cells)
    }
  }
  t.end()
})

tape('stability test - mixed dimension', function(t) {
  for(var n=0; n<10; ++n) {
    var cells = []
    for(var d=1; d<=5; ++d) {
      for(var j=0; j<10; ++j) {
        var c = new Array(d)
        for(var k=0; k<d; ++k) {
          c[k] = (Math.random() * 20)|0
        }
        cells.push(c)
      }
    }
    testStability(t, cells)
  }
  t.end()
})
