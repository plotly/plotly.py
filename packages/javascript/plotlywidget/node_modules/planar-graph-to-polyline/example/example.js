var graphToPolygons = require("../pg2pl")

var edges = []
var positions = []

for(var i=1; i<=3; ++i) {
  var v0 = positions.length
  for(var j=0; j<10; ++j) {
    var theta = 2.0 * Math.PI * j / 10
    positions.push([ i * Math.cos(theta), i * Math.sin(theta) ])
    edges.push([ v0+j, v0+((j+1)%10) ])
  }
}

console.log(graphToPolygons(edges, positions))