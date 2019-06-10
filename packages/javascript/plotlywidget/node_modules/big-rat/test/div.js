'use strict'

var rat = require('../index')
var div = require('../div')
var equals = require('../equals')
var tape = require('tape')

tape('multiply - small integers', function(t) {

  for(var i=1; i<=10; ++i) {
    for(var j=1; j<=10; ++j) {
      var x = rat(i)
      var y = rat(j)
      t.ok(equals(div(x,y), rat(i, j)), i + '/' + j)
    }
  }

  t.end()
})
