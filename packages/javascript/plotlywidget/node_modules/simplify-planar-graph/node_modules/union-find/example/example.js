var VERTEX_COUNT = 8;
var edges = [
    [0,1],
    [1,2],
    [2,3],
    [5,6],
    [7,1]
];

console.log(edges);

//Import data structure
var UnionFind = require('../index.js');

//Link all the nodes together
var forest = new UnionFind(VERTEX_COUNT);
for(var i=0; i<edges.length; ++i) {
  forest.link(edges[i][0], edges[i][1]);
}

//Label components
var labels = new Array(VERTEX_COUNT);
for(var i=0; i<VERTEX_COUNT; ++i) {
  labels[i] = forest.find(i);
}

console.log(labels);