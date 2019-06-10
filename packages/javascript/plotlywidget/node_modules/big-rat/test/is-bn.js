'use strict'

var tape = require('tape')
var bn   = require('bn.js')
var isBN = require('../lib/is-bn')

tape('is-bn', function(t) {

  t.ok(!isBN([]))
  t.ok(!isBN())
  t.ok(!isBN(null))
  t.ok(!isBN(0))
  t.ok(!isBN(1000))
  t.ok(isBN(new bn(10)))
  t.ok(isBN(new bn(0)))

  t.end()
})
