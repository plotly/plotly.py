var test = require('tape')
var bn = require('bn.js')
var toFloat = require('../lib/bn-to-num')

test('single word', function (t) {
  t.equal(toFloat(new bn(-1234567)), -1234567, 'negative')
  t.equal(toFloat(new bn(1234567)), 1234567, 'positive')
  t.end()
})

test('two words', function (t) {
  var v = 12345671234567
  t.equal(toFloat(new bn(v)), v, 'positive')
  t.equal(toFloat(new bn(-v)), -v, 'negative')
  t.end()
})

test('more words (positive)', function (t) {
  var n = new bn('1234567123456712345671234567', 10)
  var v = toFloat(n)
  t.equal(v, +n.toString(), 'positive')
  t.end()
})

test('more words (negative)', function (t) {
  var n = new bn('-1234567123456712345671234567', 10)
  var v = toFloat(n)
  t.equal(v, +n.toString(), 'negative')
  t.end()
})

test('powers of 2', function (t) {
  for (var i = 0; i < 1024; ++i) {
    var x = Math.pow(2, i)
    var y = (new bn(1)).ushln(i)
    t.same(toFloat(y), x, x)
    t.same(toFloat(y.neg()), -x, -x)
  }
  t.end()
})
