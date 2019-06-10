"use strict"

var robustSum = require("../robust-sum.js")
var validate = require("validate-robust-sequence")

require("tape")(function(t) {
	t.same(robustSum([1, 64], [-1e-64, 1e64]),  [-1e-64, 65, 1e64])
	t.same(robustSum([0], [0]), [0])
	t.same(robustSum([0], [1]), [1])
	t.same(robustSum([1, 1e64], [1e-64, 2]), [1e-64, 3, 1e64])
  
  t.same(robustSum([1], [1e-64, 1e-16]), [1e-64, 1e-16, 1])

  t.same(robustSum([0], [1]), [1])
  
  for(var i=-10; i<=10; ++i)
  for(var j=-10; j<=10; ++j) {
    t.same(robustSum([i], [j]), [i+j])
  }

  t.ok(validate(robustSum([ 5.711861227349496e-133, 1e-116 ], [ 5.711861227349496e-133, 1e-116 ])))

  var nois = new Array(10)
  var expect = new Array(10)
  for(var i=0; i<10; ++i) {
    nois[i] = Math.pow(2, -1000+53*i)
    expect[i] = Math.pow(2, -999+53*i)
  }
  var x = robustSum(nois, nois)
  t.same(x, expect)
  t.ok(validate(x))

  t.same(robustSum([0], [1, 1e64]), [1, 1e64])

  var s = [0]
  for(var i=0; i<1000; ++i) {
    s = robustSum(s, [Math.random() * Math.pow(2, Math.random()*1800-900)])
    t.ok(validate(s))
  }

	t.end()
})