'use strict'

var min = require('../min')
var rat = require('../index')
var equals = require('../equals')
var tape = require('tape')

tape('min - small integers', function(t) {
  for(var i=-10; i<=10; ++i) {
    for(var j=-10; j<=10; ++j) {
      var x = rat(i)
      var y = rat(j)
      var z = min(x, y)
      t.ok(equals(min(x, y), rat(Math.min(i,j))))
    }
  }

  t.end()
})
