var test = require('tape');
var cmp = require('../cmp')
var divs = require('../divs')
var rv = require('../index');
var rat = require('big-rat')

test('divs: (1/5) / (1/2)', function(t) {
  var a = rv([1/5]);
  var b = rv([2/5]);

  t.deepEqual(cmp(divs(a, 0.5), b), [0], 'is rat(2/5)');
  t.end();
});

test('divs 0.5 / 0.5', function(t) {
  var a = rv([1/2]);
  var b = rv([1]);

  t.deepEqual(cmp(divs(a, 0.5), b), [0], '1/2 / .5 === rat(1)');
  t.end();
});

test('divs accepts a rat', function(t) {
  var a = rv([1/2]);
  var b = rv([1]);

  t.deepEqual(cmp(divs(a, rat(0.5)), b), [0], '1/2 / rat(.5) == rat(1)');
  t.end();
});
