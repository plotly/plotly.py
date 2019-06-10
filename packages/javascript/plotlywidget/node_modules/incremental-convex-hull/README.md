# incremental-convex-hull
Computes the convex hull of a collection of points in general position by incremental insertion.  No attempt is made to handle degeneracies. 

This module is meant to be used internally by other modules for calculating convex hulls and Delaunay triangulations.  You probably shouldn't call it directly unless you know what you are doing.  Instead, there will (eventually) be a wrapper over this module that handles all the special cases and correctly generates a convex hull.

[![testling badge](https://ci.testling.com/mikolalysenko/incremental-convex-hull.png)](https://ci.testling.com/mikolalysenko/incremental-convex-hull)

[![build status](https://secure.travis-ci.org/mikolalysenko/incremental-convex-hull.png)](http://travis-ci.org/mikolalysenko/incremental-convex-hull)

# Example

```javascript
var ch = require("incremental-convex-hull")
var points = [
  [0, 0, 0],
  [0, 0, 1],
  [0, 1, 0],
  [1, 0, 0],
  [1, 1, 1]
]
console.log(ch(points))
```

Output:

```javascript
[ [ 0, 2, 3 ],
  [ 1, 0, 3 ],
  [ 0, 1, 2 ],
  [ 2, 4, 3 ],
  [ 4, 1, 3 ],
  [ 1, 4, 2 ] ]
```

# Install

```
npm install incremental-convex-hull
```

# API

#### `require("incremental-convex-hull")(points[, randomInsert])`
Constructs a triangulation of the convex hull of `points` by incremental insertion.

* `points` is a list of points
* `randomInsert` is a flag, which if set uses a randomized jump and walk instead of walking from the last inserted facet.

**Returns** A list of the boundary cells of the convex hull of the point cloud.

**Notes** This module works in any dimension greater than 2, though becomes pretty slow after 5d.

# License

(c) 2014 Mikola Lysenko. MIT License