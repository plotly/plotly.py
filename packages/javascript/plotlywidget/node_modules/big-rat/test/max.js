'use strict'

var max = require('../max')
var rat = require('../index')
var equals = require('../equals')
var tape = require('tape')

tape('min - small integers', function(t) {
  for(var i=-10; i<=10; ++i) {
    for(var j=-10; j<=10; ++j) {
      var x = rat(i)
      var y = rat(j)
      var z = max(x, y)
      t.ok(equals(max(x, y), rat(Math.max(i,j))))
    }
  }

  t.end()
})
