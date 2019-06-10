"use strict"

var robustScale = require("../robust-scale.js")
var validate = require("validate-robust-sequence")
var robustSum = require("robust-sum")
var toFixed = require("robust-sequence-to-fixed-point")
var tape = require("tape")
var shuffle = require("shuffle-array")

tape("sample cases", function(t) {

  t.same(robustScale([4], 2), [8])
  t.same(robustScale([1, 1e64], 2), [2, 2e64])
  t.same(robustScale([1], 1), [1])

  var s = robustScale([ -2.4707339790384e-144, -1.6401064715739963e-142, 2e-126 ], -10e-64)
  t.ok(validate(s))
  t.ok(s[s.length-1]<0)

  t.end()
})

tape("scalar", function(t) {
  for(var i=-50; i<50; ++i) {
    for(var j=-50; j<50; ++j) {
      t.same(robustScale([i], j), [i*j])
    }
  }
  t.end()
})

tape("sequences", function(t) {
  var sequences = [
    [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9],
    [Math.random(), Math.random(), Math.random(), Math.random()],
    [1, 2, 1+Math.pow(2,-52), Math.pow(2, 100)]
  ]

  var nseq = []
  for(var i=0; i<10; ++i) {
    nseq.push(2* Math.random() - 1)
  }
  sequences.push(nseq)

  function fpMult(a, b) {
    var p = a.mul(b)
    return p.ishrn(toFixed.DECIMAL_POINT)
  }

  function verifySequence(seq) {
    var s = toFixed(1)
    var r = [1]
    for(var i=0; i<seq.length; ++i) {
      var h = seq[i]
      r = robustScale(r, h)
      s = fpMult(s, toFixed(h))
      t.ok(validate(r), "check increasing and non-overlapping")
      t.equals(toFixed(r).toString(16), s.toString(16), "check result correct")
    }
  }

  for(var j=0; j<sequences.length; ++j) {
    var seq = sequences[j]
    verifySequence(seq)

    for(var j=0; j<10; ++j) {
      verifySequence(shuffle(seq))
    }
  }

  t.end()
})