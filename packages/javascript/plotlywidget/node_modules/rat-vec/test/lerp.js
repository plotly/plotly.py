var test = require('tape');

var rat = require('big-rat')
var lerp = require('../lerp')
var rv = require('../index')
var toFloat = require('../to-float')
var equal = require('../equals')


test('lerp to 0', function(t) {
  var start = rv([-2.5, -2.5])
  var end = rv([2.5, 2.5])

  var r = lerp(start, end, rat(0))

  t.ok(equal(start, r), 'at t=0 the result is same as start [-2.5, -2.5]')
  t.end();
})

test('lerp to 1/2', function(t) {
  var start = rv([-2.5, -2.5])
  var end = rv([2.5, 2.5])
  var exp = rv([0, 0])

  var r = lerp(start, end, rat(1, 2))

  t.ok(equal(r, exp), 'at t=0.5 the result is [0, 0]')
  t.end()
})

test('lerp to 1', function(t) {
  var start = rv([-2.5, -2.5])
  var end = rv([2.5, 2.5])

  var r = lerp(start, end, rat(1))
  t.ok(equal(r, end), 'at t=1 the result is end [2.5, 2.5]')
  t.end()
})

test('lerp down a 2d line', function(t) {
  var start = rv([0, 0]);
  var end = rv([100, 0]);
  for (var i=0; i<=10; i++) {
    var r = lerp(start, end, rat(i, 10))
    var expected = rv([i*10, 0])
    t.ok(equal(r, expected), 'at t=' + (i/10))
  }
  t.end()
})
