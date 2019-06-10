'use strict'

var rat = require('../index')
var cmp = require('../cmp')
var sgn = require('signum')
var tape = require('tape')

tape('comparison - tiny integer', function(t) {
  for(var i=-10; i<=10; ++i) {
    for(var j=-10; j<=10; ++j) {
      var x = rat(i)
      var y = rat(j)
      t.equals(cmp(x,y), sgn(i-j))
      t.equals(x[0].toString(), ''+i)
      t.equals(y[0].toString(), ''+j)
    }
  }
  t.end()
})


tape('comparison - random floats', function(t) {
  for(var i=0; i<100; ++i) {
    var x = Math.random()
    var y = Math.random()
    var a = rat(x)
    var b = rat(y)
    t.equals(cmp(a,b), sgn(x-y), 'compare:' + x + ' to ' + y)
  }
  t.end()
})
