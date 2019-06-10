"use strict"

var det = require("../robust-determinant.js")

require("tape")(function(t) {
  t.same(det([[1,2,3],[3,4,5],[6,7,8]]), [0])
  t.same(det([[1,2], [3,4]]), [-2])

  t.same(det[3]([[1,2,3],[3,4,5],[6,7,8]]), [0])
  t.same(det[2]([[1,2], [3,4]]), [-2])

  t.end()
})