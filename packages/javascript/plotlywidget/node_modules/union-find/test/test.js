"use strict"

var tape = require("tape")
var UnionFind = require("../index.js")

tape("union-find", function(t) {

  var VERTEX_COUNT = 8;
  var edges = [
      [0,1],
      [1,2],
      [2,3],
      [5,6],
      [7,1]
  ];

  //Link all the nodes together
  var forest = new UnionFind(VERTEX_COUNT);
  for(var i=0; i<edges.length; ++i) {
    forest.link(edges[i][0], edges[i][1]);
  }

  t.equals(forest.find(0), forest.find(1))
  t.equals(forest.find(0), forest.find(2))
  t.equals(forest.find(0), forest.find(3))
  t.notEquals(forest.find(0), forest.find(4))
  t.notEquals(forest.find(0), forest.find(5))
  t.notEquals(forest.find(4), forest.find(5))
  t.equals(forest.find(5), forest.find(6))
  t.equals(forest.find(7), forest.find(0))

  t.end()
})