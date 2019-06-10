planar-dual
===========
Given a planar embedding of a graph, find all faces.

# Example

```javascript
var getFaces = require("planar-dual")

//Create a triforce
var positions = [
  [0, 0],
  [-1, -1],
  [0, 1],
  [1, -1]
]
var edges = [
  [1, 2],
  [2, 3],
  [3, 1],
  [0, 1],
  [0, 2],
  [0, 3]
]

//Compute dual graph
console.log(getFaces(edges, positions))
```

Output:

```javascript
[ [ 0, 1, 2 ], [ 0, 2, 3 ], [ 0, 3, 1 ], [ 1, 3, 2 ] ]
```

# Install

```
npm install planar-dual
```

# API

#### `require("planar-dual")(edges, positions)`
Splits an embedded planar graph into a collection of faces

* `edges` are the edges of the graph
* `positions` are the locations of the vertices of the graph

**Returns** A list of faces of the graph represented as ordered lists of vertices

# Credits
(c) 2014 Mikola Lysenko. MIT License