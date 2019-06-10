//First we need to reqire the module
var cdt2d = require('../cdt2d')

//Then we define a list of points, represented as pairs of x,y coordinates
var points = [
  [-2,-2],
  [-2, 2],
  [ 2, 2],
  [ 2,-2],
  [ 1, 0],
  [ 0, 1],
  [-1, 0],
  [ 0,-1]
]

//Next we can optionally define some edge constraints
// This set of edges determines a pair of loops
var edges = [
 //Outer loop
 [0, 1],
 [1, 2],
 [2, 3],
 [3, 0],

 //Inner loop
 [4, 5],
 [5, 6],
 [6, 7],
 [7, 4]
]

//Finally we call cdt2d with the points and edges
// The flag {exterior: false} tells  it to remove exterior faces
console.log(cdt2d(points, edges, {exterior: false}))
