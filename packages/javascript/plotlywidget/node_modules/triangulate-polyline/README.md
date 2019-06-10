triangulate-polyline
====================
Triangulates a polygon with holes encoded as a list of loops.

# Example

```javascript
var triangulate = require("triangulate-polyline")

var positions = [
  [-2, -2],
  [ 2, -2],
  [ 2,  2],
  [-2,  2],
  [-1, -1],
  [ 1, -1],
  [ 1,  1],
  [-1,  1]
]

var loops = [
  [0, 1, 2, 3],
  [4, 5, 6, 7]
]

console.log(triangulate(loops, positions))
```

Example output:

```javascript
[ [ 3, 7, 2 ],
  [ 3, 0, 7 ],
  [ 0, 4, 7 ],
  [ 4, 0, 1 ],
  [ 5, 4, 1 ],
  [ 6, 5, 1 ],
  [ 6, 1, 2 ],
  [ 7, 6, 2 ] ]
```

# Install

```
npm install triangulate-polyline
```

# API

#### `require("triangulate-polyline")(loops, positions)`
Triangulates a complex polygon

* `loops` is a list of vertices of the polygon, where each vertex is represented as an index into `positions`
* `positions` is a list of vertex positions encoded, each represented by a length 2 array

**Returns** A list of triangles represented by triples of indices of position indices.

**Note** This library is built on top of poly2tri, which is not robust.  Points which are close together or near the boundary of other loops may be incorrectly classified and could result in broken triangulations.

# Credits
(c) 2014 Mikola Lysenko. MIT License