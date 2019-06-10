'use strict'

var rat = require('../index')
var toFloat = require('../to-float')
var tape = require('tape')

function verify(t, x) {
  t.equals(toFloat(rat(x)), x, 'to-float: ' + x)
}

tape('to-float: small integers', function(t) {
  for(var i=-1000; i<1000; ++i) {
    verify(t, i)
  }
  t.end()
})


tape('to-float: selected cases', function(t) {
  verify(t, 0)
  verify(t, 0.1)
  verify(t, 0.2)
  verify(t, 0.3)
  verify(t, 1/3)
  verify(t, 0.5)
  verify(t, 0.25)
  verify(t, 0.9)
  verify(t, 11111.11111)
  verify(t, -155.87571739999998)

  t.end()
})

tape('to-float: powers of 2', function(t) {
  for(var i=-1075; i<1024; ++i) {
    verify(t, Math.pow(2, i))
  }

  t.end()
})

tape('to-float: fuzz', function(t) {
  for(var i=-1075; i<1023; ++i) {
    for(var j=0; j<50; ++j) {
      verify(t, Math.random() * Math.pow(2, i))
    }
  }

  t.end()
})
