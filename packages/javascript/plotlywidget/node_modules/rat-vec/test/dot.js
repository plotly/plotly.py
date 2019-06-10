var test = require('tape')
var cmp = require('big-rat/cmp')
var dot = require('../dot')
var rv = require('../index')
var rat = require('big-rat')

test('(0, 1) dot (1, 1)', function(t) {
  var a = rv([0, 1])
  var b = rv([1, 1])

  t.equals(cmp(dot(a, b), rat(1)), 0, 'equals rat(1)')
  t.end()
});

test('(.5, 0, 0) dot (100.125, 0, 50.2)', function(t) {
  var a = rv([0.5, 0, 0])
  var b = rv([100.125, 0, 50.2])

  t.equals(cmp(dot(a, b), rat(801, 16)), 0, 'equals rat(801/16)')
  t.end()
});
