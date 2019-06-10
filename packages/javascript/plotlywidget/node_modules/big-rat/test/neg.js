'use strict'

var rat = require('../index')
var neg = require('../neg')
var equals = require('../equals')
var tape = require('tape')

tape('negate - small integers', function(t) {

  for(var i=-10; i<=10; ++i) {
    var x = rat(i)
    t.ok(equals(neg(x), rat(-i)), 'negate ok')
  }

  t.end()
})
