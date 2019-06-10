var test = require('tape');
var equal = require('../equals')
var rv = require('../index');

test('(1/5) == 1/5', function(t) {
  var a = rv([1/5]);
  var b = rv([1/5]);

  t.deepEqual(equal(a, b), true, '[0]');
  t.end();
});

test('(1/5) != 1/2', function(t) {
  var a = rv([1/5]);
  var b = rv([1/2]);

  t.deepEqual(equal(a, b), false, '[0]');
  t.end();
});
