'use strict'

var rat = require('../index')
var recip = require('../recip')
var equals = require('../equals')
var tape = require('tape')

tape('reciprocal - small rationals', function(t) {

  for(var i=1; i<=10; ++i) {
    for(var j=1; j<=10; ++j) {
      var x = rat(i, j)
      t.ok(equals(recip(x), rat(j, i)))
    }
  }

  t.end()
})
