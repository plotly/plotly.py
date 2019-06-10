"use strict"

var dotProduct = require("../dot-prod.js")

require("tape")(function(t) {

  var p = dotProduct([10, 3], [4, 5])
  t.same(p, [55])

  t.end()
})