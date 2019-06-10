"use strict"

var twoProduct = require("../two-product.js")
var testOverlap = require("test-float-overlap")
var BN = require("bn.js")
var db = require("double-bits")

require("tape")(function(t) {
  var testValues = [
    0, 
    1,
    Math.pow(2, -52), 
    Math.pow(2, -53), 
    1.0-Math.pow(2, -53), 
    1.0+Math.pow(2, -52), 
    Math.pow(2,-500), 
    Math.pow(2, 500),
    2,
    0.5,
    3,
    1.5,
    0.1,
    0.3,
    0.7 ]
  for(var i=0; i<20; ++i) {
    testValues.push(Math.random())
    testValues.push(Math.random() * Math.pow(2, 1000 * Math.random() - 500))
  }
  for(var i=testValues.length-1; i>0; --i) {
    testValues.push(-testValues[i])
  }

  function floatToBigNum(a) {
    var fa = db.fraction(a)
    var ea = db.exponent(a)
    var na = BN(fa[0]&((1<<24)-1))
    na = na.add(BN(fa[0]>>>24).ishln(24))
    na = na.add(BN(fa[1]).ishln(32))
    na.ishln(ea+2000)
    if(a < 0) {
      return na.neg()
    }
    return na
  }

  function testTwoProduct(a, b, s) {
    var nr = floatToBigNum(a).mul(floatToBigNum(b))
    if(nr.bitLength()>0) {
      nr = nr.ishrn(2000+52)
    }
    var ns = floatToBigNum(s[0]).add(floatToBigNum(s[1]))
    t.equals(ns.toString(16), nr.toString(16), "test vs exact")
    if(ns.toString(16) !== nr.toString(16)) {
      console.log(a, b, s)
      throw new Error("DIE")
    }
  }  

  for(var j=0; j<testValues.length; ++j) {
    var a = testValues[j]
    t.ok(a*a < Infinity, "check finite: " + a)
    t.same(twoProduct(0, a), [0,0], "multiply by 0")
    t.same(twoProduct(1, a), [0,a], "multiply by 1")
    t.same(twoProduct(-1, a), [0,-a], "multiply by -1")

    for(var k=0; k<testValues.length; ++k) {
      var b = testValues[k]

      var s = twoProduct(a, b)

      t.ok(!testOverlap(s[0], s[1]), "overlapping")
      t.ok(Math.abs(s[0]) <= Math.abs(s[1]), "increasing")
      t.equals(s[1], a*b, "approximation")

      var r = twoProduct(b, a)
      t.same(s, r, "commutativity")

      testTwoProduct(a, b, s)
    }
  }

  //Test expansion
  t.same(twoProduct(
    1.0 + Math.pow(2, -52), 
    1.0 + Math.pow(2, -52)),
    [Math.pow(2, -104), 1.0 + Math.pow(2, -51)], "test expansion") 

  t.end()
})