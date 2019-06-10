var test = require('tape');
var recip = require('../recip')
var cmp = require('../cmp')
var rv = require('../index');

test('recip of 1/2 is 2', function(t) {
  var a = rv([1/2])
  var b = rv([2]);
  t.deepEqual(cmp(recip(a), b), [0], 'same');
  t.end();
});

test('recip of 2 is 1/2', function(t) {
  var a = rv([2])
  var b = rv([1/2]);
  t.deepEqual(cmp(recip(a), b), [0], 'same');
  t.end();
});

test('recip of [1/2, 2] is [2, 1/2]', function(t) {
  var a = rv([1/2, 2])
  var b = rv([2, 1/2]);
  t.deepEqual(cmp(recip(a), b), [0, 0], 'same');
  t.end();
});
