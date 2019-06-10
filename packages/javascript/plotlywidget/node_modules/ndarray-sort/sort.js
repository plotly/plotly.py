"use strict"

var compile = require("./lib/compile_sort.js")
var CACHE = {}

function sort(array) {
  var order = array.order
  var dtype = array.dtype
  var typeSig = [order, dtype ]
  var typeName = typeSig.join(":")
  var compiled = CACHE[typeName]
  if(!compiled) {
    CACHE[typeName] = compiled = compile(order, dtype)
  }
  compiled(array)
  return array
}

module.exports = sort