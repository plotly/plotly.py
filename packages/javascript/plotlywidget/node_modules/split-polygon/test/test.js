var splitPolygon = require("../clip-poly.js")
var tape = require("tape")

tape(function(t) {

  var p = splitPolygon([[0,0], [1, 0], [1, 1], [0,1]], [0, 1, -0.5])
  console.log(p)

  var p = splitPolygon([[0,0], [1, 0], [1, 1], [0,1]], [0, 1, 1e-16 -1.0])
  console.log(p)



  t.end()
})