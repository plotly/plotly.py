'use strict'

var tape = require('tape')
var rv = require('../index')
var round = require('../to-float')

tape('exact rational', function(t) {

  function verify(v) {
    t.equals(round(rv(v)).toString(), v.toString(), 'verify: ' + v.toString())
  }

  verify([5e-324, 1.4210854715202004e-14])
  verify([0, 3.2159095049723066e-24])
  verify([5e-324, 4.04007015999455e-25])
  verify([5e-324,4.830474736584587e-26])

  verify([Math.pow(2,1023)])
  verify([Math.pow(2,-1074)])
  verify([Math.pow(2,-1074), Math.pow(2,1023)])

  verify([0.1])
  verify([1.5])
  verify([Math.pow(2, 500)])
  verify([1])
  verify([0.5])
  verify([2])
  verify([2, 4])
  verify([1, 1.5])
  verify([0.1])
  verify([0.3])
  verify([0.7])
  verify([0.3, 0.9])
  verify([1/3])

  //across multiple scales
  for(var i=-1074; i<1024; ++i) {
    var x = Math.pow(2, i)
    verify([x])
    verify([x + Math.pow(2,i-52)])
    verify([x*Math.random()])
    for(var j=-1070; j<1024; j+=32) {
      var y = Math.pow(2, j)
      verify([x, y])
      verify([x + Math.pow(2,i-52), y])
      verify([x, y + Math.pow(2,j-52)])
      verify([x + Math.pow(2,i-52), y + Math.pow(2,j-52)])
      verify([x*Math.random(), y*Math.random()])
    }
  }

  t.end()
})
