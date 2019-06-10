'use strict'

var rat = require('../index')
var sub = require('../sub')
var equals = require('../equals')
var tape = require('tape')

tape('subtract - small integers', function(t) {
  for(var i=-10; i<=10; ++i) {
    for(var j=-10; j<=10; ++j) {
      var x = rat(i)
      var y = rat(j)
      var z = sub(x, y)
      t.ok(equals(z, rat(i-j)), i + '+' + j)
      t.ok(x, rat(i))
      t.ok(y, rat(j))
    }
  }
  t.end()
})
