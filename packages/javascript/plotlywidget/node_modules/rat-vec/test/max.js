'use strict'

var tape = require('tape')
var rv = require('../index')
var equal = require('../equals')
var max = require('../max')

tape('2d max (positive)', function(t) {
  var a = rv([10, 100]);
  var b = rv([50, 5]);

  var r = max(a, b);
  var e = rv([50, 100]);

  t.ok(equal(r, e), 'max is (50, 100)')

  t.end()
})

tape('2d max (negative)', function(t) {
  var a = rv([-10, -100]);
  var b = rv([-50, -5]);

  var r = max(a, b);
  var e = rv([-10, -5]);

  t.ok(equal(r, e), 'max is (-10, -5)')

  t.end()
});

tape('2d max (zero)', function(t) {
  var a = rv([-10, -100]);
  var b = rv([0, 0]);

  var r = max(a, b);
  var e = rv([0, 0]);

  t.ok(equal(r, e), 'max is (0, 0)')

  t.end()
});
