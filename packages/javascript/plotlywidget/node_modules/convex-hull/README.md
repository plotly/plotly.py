convex-hull
===========
This module is a wrapper over various convex hull modules which exposes a simple interface for computing convex hulls of point sets in any dimension.

# Example

```javascript
var ch = require('convex-hull')

var points = [
  [0,0],
  [1,0],
  [0,1],
  [0.15,0.15],
  [0.5, 0.5]
]


//Picture:
//
// [0,1] *
//       |\
//       | \
//       |  \
//       |   \
//       |    \
//       |     \
//       |      \
//       |       * [0.5,0.5]
//       |        \
//       |         \
//       |          \
//       |           \
//       |            \
//       |    *        \
//       | [0.15,0.15]  \
// [0,0] *---------------* [1,0]
//

console.log(ch(points))
```

Output:

```javascript
[[0, 1], [1, 2], [2, 0]]
```

# Install

```
npm install convex-hull
```

If you want to use it in a webpage, use [browserify](http://browserify.org).

# API

#### `require('convex-hull')(points)`
Computes the convex hull of `points`

* `points` is an array of points encoded as `d` length arrays

**Returns** A polytope encoding the convex hull of the point set.

**Time complexity** The procedure takes O(n^floor(d/2) + n log(n)) time.

**Note** This module is a wrapper over incremental-convex-hull and monotone-convex-hull for convenience.  It will select an optimal algorithm for whichever dimension is appropriate.


# Credits
(c) 2014 Mikola Lysenko. MIT License