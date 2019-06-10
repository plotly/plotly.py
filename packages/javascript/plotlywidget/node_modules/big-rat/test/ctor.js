'use strict'

var bn = require('bn.js')
var rat = require('../index')
var tape = require('tape')

tape('bignum ctor', function(t) {
  var a = new bn(10000)
  var b = new bn(3)

  var f = rat(a, b)

  t.equals(f[0].toString(), a.toString())
  t.equals(f[1].toString(), b.toString())

  t.end()
})

tape('string ctor', function(t) {
  var f = rat('20', '80')

  t.equals(f[0].toString(), '1')
  t.equals(f[1].toString(), '4')

  t.end()
})

tape('rational ctor', function(t) {
  var x = rat('5', '6')
  var y = rat(x)
  var z = rat(y, y)

  t.equals(x[0].toString(), y[0].toString())
  t.equals(x[1].toString(), y[1].toString())

  t.equals(z[0].toString(), '1')
  t.equals(z[1].toString(), '1')

  t.end()
})

tape('integer ctor', function(t) {
  for(var i=-10; i<10; ++i) {
    var x = rat(i)
    t.equals(x[0].toString(), ''+i)
    t.equals(x[1].toString(), '1')
  }

  t.end()
})

tape('float ctor', function(t) {
  var x = rat(1.5)

  t.equals(x[0].toString(), '3')
  t.equals(x[1].toString(), '2')

  t.end()
})
