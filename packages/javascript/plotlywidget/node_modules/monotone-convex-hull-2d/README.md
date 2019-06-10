monotone-convex-hull-2d
=======================
Computes the convex hull of a set of points in the plane in O(n log(n)) time using the Monotone chain algorithm.

* [Demo Link](https://mikolalysenko.github.io/monotone-convex-hull-2d/visualizer/index.html)

# Example

```javascript
var convexHull = require('monotone-convex-hull-2d')

var points = [
  [0, 0],
  [1, 0],
  [0, 1],
  [1, 1],
  [0.5, 0.5]
]

console.log(convexHull(points))
```

Output:

```
[ 0, 2, 3, 1 ]
```

# Install

```
npm install monotone-convex-hull-2d
```

# API

### `require('monotone-convex-hull-2d')(points)`
Construct the convex hull of a set of points.

* `points` is an array of points represented as an array of length 2 arrays

**Returns** The convex hull of the point set represented by a clockwise oriented list of indices.

# Credits
(c) 2014 Mikola Lysenko. MIT License

Visualizer (c) 2013 Dan Melanz