var alphaComplex = require('../alpha')

var points = []
for(var i=0; i<100; ++i) {
  points.push([Math.random(), Math.random()])
}

console.log(alphaComplex(0.1, points))