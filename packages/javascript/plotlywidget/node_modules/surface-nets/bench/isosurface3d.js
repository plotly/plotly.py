"use strict"

var isosurface = require("isosurface")

function sphere(i,j,k) {
  return Math.pow(i-16,2) + Math.pow(j-16,2) + Math.pow(k-16,2) - 100
}

var complex

console.time("isosurface.surfaceNets")
for(var i=0; i<1000; ++i) {
  complex = isosurface.surfaceNets([32,32,32], sphere)
}
console.timeEnd("isosurface.surfaceNets")