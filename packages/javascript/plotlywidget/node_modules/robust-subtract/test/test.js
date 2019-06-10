"use strict"

var robustDiff = require("../robust-diff")
var validate = require("validate-robust-sequence")

require("tape")(function(t) {
  t.same(robustDiff([1],[1]), [0])

  var s = [0]
  for(var i=0; i<100; ++i) {
    s = robustDiff(s, [Math.random() * Math.pow(2, Math.random()*1000)])
    t.ok(validate(s))
  }

  t.end()
})