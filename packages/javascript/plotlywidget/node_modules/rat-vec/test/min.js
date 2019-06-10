'use strict'

var tape = require('tape')
var rv = require('../index')
var equal = require('../equals')
var min = require('../min')

tape('2d min (positive)', function(t) {
  var a = rv([10, 100]);
  var b = rv([50, 5]);

  var r = min(a, b);
  var e = rv([10, 5]);

  t.ok(equal(r, e), 'min is (10, 5)')

  t.end()
})

tape('2d min (negative)', function(t) {
  var a = rv([-10, -100]);
  var b = rv([-50, -5]);

  var r = min(a, b);
  var e = rv([-50, -100]);

  t.ok(equal(r, e), 'min is (-50, -100)')

  t.end()
});

tape('2d min (zero)', function(t) {
  var a = rv([10, 100]);
  var b = rv([0, 0]);

  var r = min(a, b);
  var e = rv([0, 0]);

  t.ok(equal(r, e), 'min is (0, 0)')

  t.end()
});
