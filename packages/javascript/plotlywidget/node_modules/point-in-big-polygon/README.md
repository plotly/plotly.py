point-in-big-polygon
====================
Industrial scale point-in-polygon test. Given a polygon, this module preprocesses it in O(n log(n)) time such that any point can be classified against the polygon in O(log(n)) operations. All computations are performed in exact arithmetic.

If you want to use multiple polygons/regions, you should use [point-in-region](https://github.com/mikolalysenko/point-in-region) instead.

# Example

```javascript
var preprocessPolygon = require("point-in-big-polygon")

//Define the polygon loops
var loops = [
  [ [-10, -10], [-10, 10], [10, 10], [10, -10] ],
  [ [-1, -1], [1, -1], [1, 1], [-1, 1] ]
]

//Preprocess it
var classifyPoint = preprocessPolygon(loops)

//Render polygon test in ASCII to console
var img = []
for(var y=-12; y<=12; y+=1) {
  var row = []
  for(var x=-12; x<=12; x+=0.5) {
    var v = classifyPoint([x, y])
    if(v < 0) {
      row.push('-')
    } else if(v === 0) {
      row.push('o')
    } else {
      row.push('+')
    }
  }
  img.push(row.join(''))
}
console.log(img.join('\n'))
```

Example output:

```
+++++++++++++++++++++++++++++++++++++++++++++++++
+++++++++++++++++++++++++++++++++++++++++++++++++
++++ooooooooooooooooooooooooooooooooooooooooo++++
++++o---------------------------------------o++++
++++o---------------------------------------o++++
++++o---------------------------------------o++++
++++o---------------------------------------o++++
++++o---------------------------------------o++++
++++o---------------------------------------o++++
++++o---------------------------------------o++++
++++o---------------------------------------o++++
++++o-----------------ooooo-----------------o++++
++++o-----------------o+++o-----------------o++++
++++o-----------------ooooo-----------------o++++
++++o---------------------------------------o++++
++++o---------------------------------------o++++
++++o---------------------------------------o++++
++++o---------------------------------------o++++
++++o---------------------------------------o++++
++++o---------------------------------------o++++
++++o---------------------------------------o++++
++++o---------------------------------------o++++
++++ooooooooooooooooooooooooooooooooooooooooo++++
+++++++++++++++++++++++++++++++++++++++++++++++++
+++++++++++++++++++++++++++++++++++++++++++++++++
```

# Install

This module works in any reasonable CommonJS environment including browserify, iojs and node.js.

```
npm install point-in-big-polygon
```

# API

## Constructor

#### `var classifyPoint = require("point-in-big-polygon")(loops)`
Preprocess a polygon given by a collection of clockwise oriented loops to handle point membership queries.

* `loops` are a collection of oriented loops representing the boundary of the polygon. These loops must be manifold (ie no self intersections or dangling edges).

**Returns** A point membership function that can be used to classify points relative to the function

## Method

#### `classifyPoint(p)`
This function is the result of running the preprocessing operation on a polygon. It takes a single point as input and tests it against the boundary.

* `p` is a point encoded as a length 2 array

**Returns** A number which classifies `p` relative to the boundary

* `-1` means that `p` is inside
* `0` means that `p` is on the boundary
* `+1` means that `p` is outside

# Credits
(c) 2014 Mikola Lysenko. MIT License