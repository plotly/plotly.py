"use strict"

var tape = require("tape")
var toFixed = require("robust-sequence-to-fixed-point")
var compress = require("../compress.js")
var robustScale = require("robust-scale")

tape("robust-compress", function(t) {

  t.same(compress([0]), [0], "test 0")
  t.same(compress([1]), [1], "test 1")

  for(var i=0; i<10; ++i) {
    var h = Math.random()
    t.same(compress([h]), [h], "test " + h)
    h = -h
    t.same(compress([h]), [h], "test " + h)
  }

  t.same(compress([1, 2]), [3], "test 1+2")
  t.same(compress([Math.pow(2,-52), 1]), [1 + Math.pow(2,-52)], "1+eps")

  function verify(seq) {
    var rseq = compress(seq.slice())
    t.ok(rseq.length <= seq.length, "must compress: " + rseq.length + " <= " + seq.length)
    t.same(toFixed(rseq).toString(16), toFixed(seq).toString(16), "verifying sequence")
  }

  //Bigger sequences
  for(var i=0; i<10; ++i) {
    var seq = []
    for(var j=0; j<18; ++j) {
      seq.push(Math.pow(2, -900+100*j) * (Math.random()-0.5))
    }
    verify(seq)
  }

  //Multiply a bunch of random numbers
  for(var i=0; i<10; ++i) {
    var seq = [1]
    for(var j=0; j<20; ++j) {
      seq = robustScale(seq, [2*Math.random()-1.0])
    }
    verify(seq)
  }

  t.end()
})