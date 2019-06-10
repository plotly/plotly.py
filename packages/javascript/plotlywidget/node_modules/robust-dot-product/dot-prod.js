"use strict"

var twoProduct = require("two-product")
var robustSum = require("robust-sum")

module.exports = robustDotProduct

function robustDotProduct(a, b) {
  var r = twoProduct(a[0], b[0])
  for(var i=1; i<a.length; ++i) {
    r = robustSum(r, twoProduct(a[i], b[i]))
  }
  return r
}