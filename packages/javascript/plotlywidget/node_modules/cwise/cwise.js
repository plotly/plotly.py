"use strict"

var transform = require("./lib/cwise-transform.js")
var base = require("./lib/cwise-esprima.js")

module.exports = function(a, b) {
  if(typeof a === "string") {
    return transform(a, b)
  } else if(typeof a === "object") {
    return base(a)
  } else {
    throw new Error("cwise: Invalid arguments")
  }
}