var test = require('tape');
var equal = require('../equals')
var muls = require('../muls')
var frac = require('big-rat')
var rv = require('../index')

test('muls: 1/5 * 0.5', function(t) {
  var a = rv([1/5])
  var e = rv([1/10])
  var r = muls(a, 0.5)

  t.ok(equal(r, e), 'is rat(1/10)')
  t.end()
});

test('muls 1/2 * 0.5', function(t) {
  var a = rv([1/2]);
  var e = rv([1/4]);
  var r = muls(a, 0.5);

  t.ok(equal(r, e), '1/2 * .5 === rat(1/4)')
  t.end()
});

test('muls 1/2 * 1/2', function(t) {
  var a = rv([1/2])
  var e = rv([1/4])
  var r = muls(a, frac(1, 2))

  t.ok(equal(r, e), '1/2 * 1/2 === rat(1/4)')
  t.end()
});

test('muls accepts a rat', function(t) {
  var a = rv([1/2])
  var e = rv([1/4])
  var r = muls(a, frac(1, 2))

  t.ok(equal(r, e), '1/2 * 1/2 == rat(1/4)')
  t.end()
});
