'use strict'

var rat = require('../index')
var sgn = require('../sign')
var tape = require('tape')

tape('signum - small integers', function(t) {

  t.equals(sgn(rat(0)), 0)

  for(var i=1; i<=10; ++i) {
    t.equals(sgn(rat(i)), 1)
    t.equals(sgn(rat(-i)), -1)
    t.equals(sgn(rat(1,i)), 1)
    t.equals(sgn(rat(1,-i)), -1)
    t.equals(sgn(rat(-1,-i)), 1)
  }

  t.end()
})
