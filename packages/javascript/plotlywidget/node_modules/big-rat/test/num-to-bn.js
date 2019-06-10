var test = require('tape')
var bn = require('bn.js')
var toBN = require('../lib/num-to-bn')

test('simple cases', function(t) {
  t.equals(toBN(0).toString(), '0', 'zero')
  t.equals(toBN(-1234567).toString(), (new bn(-1234567)).toString(), 'negative')
  t.equals(toBN(1234567).toString(), (new bn(1234567)).toString(), 'positive')
  t.end()
})

test('powers of 2', function(t) {
  for(var i=0; i<1024; ++i) {
    var x = Math.pow(2, i)
    var y = (new bn(1)).ushln(i)
    t.equals(toBN(x).toString(), y.toString())
    t.equals(toBN(-x).toString(), y.neg().toString())
  }
  t.end()
})

test('powers of 2 with 2 bits set', function(t) {
  for(var i=52; i<1024; ++i) {
    for(var j=1; j<53; ++j) {
      var x = Math.pow(2, i) + Math.pow(2, i-j)
      var y = (new bn(1)).ushln(i).add((new bn(1)).ushln(i-j))
      t.equals(toBN(x).toString(), y.toString(), y.toString())
      t.equals(toBN(-x).toString(), y.neg().toString(), y.neg().toString())
    }
  }
  t.end()
})
