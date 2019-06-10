var simplify = require("../simplify")

//Create a circle
var positions = []
var edges = []
for(var i=0; i<100; ++i) {
  var theta = i / 100 * Math.PI * 2.0
  positions.push([Math.cos(theta), Math.sin(theta)])
  edges.push([i, (i+1)%100])
}

//Simplify it
console.log(simplify(edges, positions, 0.1))