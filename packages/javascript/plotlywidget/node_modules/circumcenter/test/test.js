"use strict"

var circumcenter = require("../circumcenter.js")

require("tap").test("circumcenter", function(t) {

  t.equals(circumcenter([[1], [2]]).join(","), [1.5].join(","))
  t.equals(circumcenter([[0,0], [0,1], [1,0]]).join(","), [0.5,0.5].join(","))

  t.end()
})
