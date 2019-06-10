edges-to-adjacency-list
=======================
Converts a collection of edges in a graph to an [adjacency list](http://en.wikipedia.org/wiki/Adjacency_list) representation. For the more general operation on simplicial complexes, use the [`stars`](https://github.com/mikolalysenko/stars) module.

Example
=======

```javascript
var e2a = require("edges-to-adjacency-list")

console.log(e2a([
  [0, 1],
  [1, 2],
  [2, 3]
]))
```

Output:

```javascript
[ [1],
  [0, 2],
  [1, 3],
  [2]
]
```

Install
=======

```
npm install edges-to-adjacency-list
```

API
===

#### `require("edges-to-adjacency-list")(edges[, numVertices])`
Converts a collection of edges to an adjacency list representation.

* `edges` are the edges of the graph
* `numVertices` is an optional parameter giving the number of vertices in the graph

**Returns** An array encoding the adjacency list of the graph

**Note** Repeated edges will be combined.

# Credits
(c) 2014 Mikola Lysenko. MIT License