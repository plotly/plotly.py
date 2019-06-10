"use strict"

//Load modules
var surfaceNets = require("../surfacenets.js")
var ndarray = require("ndarray")
var fill = require("ndarray-fill")

//Initialize array
var array = ndarray(new Float32Array(32*32*32), [32,32,32])
fill(array, function(i,j,k) {
  return Math.pow(i-16,2) + Math.pow(j-16,2) + Math.pow(k-16,2)
})

//Generate surface!
var complex = surfaceNets(array, 100)
for(var i=0; i<10; ++i) {
  complex = surfaceNets(array, 100)
}

console.time("surface-nets 3d")
for(var i=0; i<1000; ++i) {
  complex = surfaceNets(array, 100)
}
console.timeEnd("surface-nets 3d")