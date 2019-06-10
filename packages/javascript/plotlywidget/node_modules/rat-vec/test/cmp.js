var test = require('tape');
var cmp = require('../cmp')
var rv = require('../index');

test('ensure equal is 0', function(t) {
  var a = rv([0, 1])
  var b = rv([0, 1]);

  t.deepEqual(cmp(a, b), [0, 0], '[0, 0]');
  t.end();
});

test('ensure less is -1', function(t) {
  var a = rv([-5.5, -2.5])
  var b = rv([5.5, 2.5]);

  t.deepEqual(cmp(a, b), [-1, -1], '[-1, -1]');
  t.end();
});

test('ensure greater is 1', function(t) {
  var a = rv([5.5, 2.5])
  var b = rv([-5.5, -2.5]);

  t.deepEqual(cmp(a, b), [1, 1], '[1, 1]');
  t.end();
});

test('cmp mixed [0, -1]', function(t) {
  var a = rv([1, -2.5])
  var b = rv([1, 2.5]);

  t.deepEqual(cmp(a, b), [0, -1], '[0, -1]');
  t.end();
});

test('cmp mixed [-1, 1]', function(t) {
  var a = rv([-1, 2.5])
  var b = rv([1, -2.5]);

  t.deepEqual(cmp(a, b), [-1, 1], '[-1, 1]');
  t.end();
});

test('cmp mixed [1, -1]', function(t) {
  var a = rv([1,-2.5])
  var b = rv([-1, 2.5]);

  t.deepEqual(cmp(a, b), [1, -1], '[1, -1]');
  t.end();
});
