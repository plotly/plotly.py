var cleanupPSLG = require('../clean-pslg')

//Create a planar straight line graph with many degenerate crossings
var points      = [
  [ 0.25, 0.5  ],
  [ 0.75, 0.5  ],
  [ 0.5,  0.25 ],
  [ 0.5,  0.75 ],
  [ 0.25, 0.25 ],
  [ 0.75, 0.75 ],
  [ 0.25, 0.75 ],
  [ 0.75, 0.25 ]
]

//These are the edges of the graph
var edges       = [
  [0, 1],
  [2, 3],
  [4, 5],
  [6, 7]
]

//Run clean up on the graph
if(cleanupPSLG(points, edges)) {
  console.log('removed degeneracies from graph')
}

console.log('points = \n', points)
console.log('edges = \n', edges)
