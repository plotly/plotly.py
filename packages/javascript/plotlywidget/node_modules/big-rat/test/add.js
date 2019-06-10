'use strict'

var rat = require('../index')
var add = require('../add')
var equals = require('../equals')
var tape = require('tape')

tape('addition - small integers', function(t) {
  for(var i=-10; i<=10; ++i) {
    for(var j=-10; j<=10; ++j) {
      var x = rat(i)
      var y = rat(j)
      t.ok(equals(add(x,y), rat(i+j)), i + '+' + j + '=' + add(x,y))
      t.ok(equals(x, rat(i)), 'x unchanged')
      t.ok(equals(y, rat(j)), 'y unchanged')
    }
  }

  t.end()
})
