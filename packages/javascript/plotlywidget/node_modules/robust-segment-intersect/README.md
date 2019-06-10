robust-segment-intersect
========================
Exact arithmetic predicate to determine if two closed linesegments intersect.

[![testling badge](https://ci.testling.com/mikolalysenko/robust-segment-intersect.png)](https://ci.testling.com/mikolalysenko/robust-segment-intersect)

[![build status](https://secure.travis-ci.org/mikolalysenko/robust-segment-intersect.png)](http://travis-ci.org/mikolalysenko/robust-segment-intersect)

# Example

```javascript

var crosses = require("robust-segment-intersect")

var a0 = [-1, 0]
var a1 = [ 1, 0]
var b0 = [ 0,-1]
var b1 = [ 0, 1]

//Check if line segment a0, a1  crosses segment b0, b1
console.log(crosses(a0, a1, b0, b1))
```

# Install

```
npm install robust-segment-intersect
```

# API

#### `require("robust-segment-intersect")(a0, a1, b0, b1)`
Tests if the closed line segment `[a0,a1]` intersects the closed line segment `[b0,b1]`.

* `a0, a1` are the end points of the first line segment encoded as length 2 arrays
* `b0, b1` are the end points of the second line segment encoded again as length 2 arrays

**Returns** `true` if the linesegments intersect, false otherwise

# Credits
(c) 2014 Mikola Lysenko. MIT License