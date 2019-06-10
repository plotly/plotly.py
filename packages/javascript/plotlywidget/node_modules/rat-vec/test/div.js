var test = require('tape');
var cmp = require('../cmp')
var div = require('../div')
var rv = require('../index');

test('(1/5) / (1/2) == 2/5', function(t) {
  var a = rv([1/5]);
  var b = rv([1/2]);
  var c = rv([2/5]);

  t.deepEqual(cmp(div(a, b), c), [0], '[0, 0]');
  t.end();
});

test('(1/2) / (1/2) == 1', function(t) {
  var a = rv([1/2]);
  var b = rv([1/2]);
  var c = rv([1]);

  t.deepEqual(cmp(div(a, b), c), [0], '[0, 0]');
  t.end();
});
