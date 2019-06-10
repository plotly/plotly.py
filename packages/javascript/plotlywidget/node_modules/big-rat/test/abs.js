'use strict'

var rat = require('../index')
var abs = require('../abs')
var equals = require('../equals')
var tape = require('tape')

tape('absolute - small integers', function(t) {

  for(var i=-10; i<=10; ++i) {
    var x = rat(i)
    t.ok(equals(abs(x), rat(Math.abs(i))), 'abs ok')
  }

  t.end()
})
