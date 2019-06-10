split-polygon
=============
Splits a *convex* polygon by a plane into two parts (or optionally clips the polygon against a single plane) using the Sutherland-Hodgman algorithm.  Works in arbitrary dimensions, both in the server and the browser

## Install

    npm install split-polygon

## Example

```javascript
var splitPolygon = require("split-polygon")

var poly = [[1,2], [3,4], [0,0]]

var parts = splitPolygon(poly, [0, 1, 3])

console.log(parts.positive)
console.log(parts.negative)
```

## API

```javascript
var splitPolygon = require("split-polygon")
```

### `splitPolygon(poly, plane)`
Splits the *convex* polygon `poly` against plane into two parts, one above the plane and the other below it.  The equation for the plane is determined by:

```javascript
function planeDistance(x) {
  return plane[0] * x[0] + plane[1] * x[1] + ... + plane[n-1] * x[n-1] + plane[n]
}
```

Points above the plane are those where `planeDistance(x) >= 0` and below are those with `planeDistance(x) <= 0`

* `poly` is a *convex* polygon
* `plane` is the plane

**Returns** An object with two properties:

* `positive` is the portion of the polygon above the plane
* `negative` is the portion of the polygon below the plane

### `splitPolygon.positive(poly, plane)`
Same result as splitPolygon, except only returns the positive part.  This saves a bit of memory if you only need one side.

### `splitPolygon.negative(poly, plane)`
Ditto, except returns only the negative part.

## Credits
(c) 2013 Mikola Lysenko. MIT License