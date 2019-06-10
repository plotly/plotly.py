simplicial-complex-contour
==========================
Finds a piecewise-linear isocontour on a simplicial complex using the marching simplex method.

# Example

```javascript
var extractContour = require('simplicial-complex-contour')
var bunny = require('bunny')

//Solve for the curve z=0 on the surface of the bunny
var zvalues = bunny.positions.map(function(p) {
  return p[2]
})
var curve = extractContour(bunny.cells, zvalues, 0.0)

//Unpack edges and positions of curve
var curveEdges = curve.cells
var curvePositions = curve.vertexWeights.map(function(w,i) {
  var a = bunny.positions[curve.vertexIds[i][0]]
  var b = bunny.positions[curve.vertexIds[i][1]]

  return [
    w * a[0] + (1 - w) * b[0],
    w * a[1] + (1 - w) * b[1],
    w * a[2] + (1 - w) * b[2]
  ]
})

//Render the curve
console.log({
  cells: curveEdges,
  positions: curvePositions
})
```

# Install

```
npm install simplicial-complex-contour
```

# API

#### `require('simplicial-complex-contour')(cells, values[, level])`
Computes a piecewise linear solution to the solution `values=levels`

* `cells` is an array of simplices represented by tuples of vertex indices
* `values` is an array of values defined at each vertex of the cell complex
* `level` is the level at which the surface is extracted (Default 0)

**Returns** An object with 3 properties

* `cells` which are the cells of the extracted isosurface
* `vertexIds` which is an array of pairs of vertex ids encoding the crossing edges
* `vertexWeights` which are linear weights applied to each vertex

# Credits
(c) 2014 Mikola Lysenko. MIT License