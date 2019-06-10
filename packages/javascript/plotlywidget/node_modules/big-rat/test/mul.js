'use strict'

var rat = require('../index')
var mul = require('../mul')
var equals = require('../equals')
var tape = require('tape')

tape('multiply - small integers', function(t) {

  for(var i=-10; i<=10; ++i) {
    for(var j=-10; j<=10; ++j) {
      var x = rat(i)
      var y = rat(j)
      t.ok(equals(mul(x,y), rat(i*j)), i + '*' + j)
    }
  }

  t.end()
})
