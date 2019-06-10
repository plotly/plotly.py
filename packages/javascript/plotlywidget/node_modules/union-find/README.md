union-find
==========

A basic union-find data structure for node.js.  For more information, see wikipdia:

[Disjoint Set Datastructures](http://en.wikipedia.org/wiki/Disjoint-set_data_structure)

Union find data structures solve the incremental connectivity problem. (That is maintaining a spanning forest under incremental insertions of edges.)  To handle fully dynamic connectivity, you can use a [dynamic forest](https://www.npmjs.org/package/dynamic-forest) data structure.

Usage
=====
Here is an example showing how to do connected component labelling.  Assume we are given a graph with `VERTEX_COUNT` vertices and a list of edges stored in array represented by pairs of vertex indices:

```javascript
//Import data structure
var UnionFind = require('union-find')

var VERTEX_COUNT = 8
var edges = [
    [0,1],
    [1,2],
    [2,3],
    [5,6],
    [7,1]
]

//Link all the nodes together
var forest = new UnionFind(VERTEX_COUNT)
for(var i=0; i<edges.length; ++i) {
  forest.link(edges[i][0], edges[i][1])
}

//Label components
var labels = new Array(VERTEX_COUNT)
for(var i=0; i<VERTEX_COUNT; ++i) {
  labels[i] = forest.find(i)
}
```

Installation
============

```
npm install union-find
```

# API

```javascript
var UnionFind = require('union-find')
```

## Constructor

### `var forest = new UnionFind(numVertices)`
Creates a new union-find data structure.

* `numVertices` is the number of vertices in the graph

**Returns** A new union-find data structure

## Methods

### `forest.length`
Returns the number of vertices in the forest

### `forest.makeSet()`
Creates a new vertex

**Returns** An integer id for the new vertex

### `forest.find(v)`
Returns an identifier representing the connected component of any given vertex

**Returns** An integer id representing the connected component of `v`

### `forest.link(s, t)`
Links a pair of connected components together

* `s` and `t` are both vertices
    
Credits
=======
(c) 2013-2014 Mikola Lysenko.  MIT License