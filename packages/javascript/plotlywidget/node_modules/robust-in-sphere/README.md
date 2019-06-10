robust-in-sphere
================
Exact arithmetic test to check if (n+2) points are cospherical.

(Very) loosely inspired by [Jonathan Shewchuk's work on robust predicates](http://www.cs.cmu.edu/~quake/robust.html).  Currently not as fast, but pull requests are welcome.

[![testling badge](https://ci.testling.com/mikolalysenko/robust-in-sphere.png)](https://ci.testling.com/mikolalysenko/robust-in-sphere)

[![build status](https://secure.travis-ci.org/mikolalysenko/robust-in-sphere.png)](http://travis-ci.org/mikolalysenko/robust-in-sphere)

# Example

```javascript
var inSphere = require("robust-in-sphere")

console.log(inSphere(
  [0, 1],
  [1, 0],
  [-1, 0],
  [0, -1]))
```

# Install

```
npm install robust-in-sphere
```

# API

```javascript
var inSphere = require("robust-in-sphere")
```

### `inSphere(a,b,c,...)`
Tests if a collection of `n+2` points in `n`-dimensional space are cospherical or if the last point is contained in the sphere or not.

* `a,b,c,...` is a list of points

**Returns** A signed integer that gives the orientation of the points
* `<0` if the last point is contained in the oriented sphere defined by the previous two points
* `>0` if the last point is outside the sphere
* `0` is the points are cospherical

**Notes** Up to 6 points it is possible to get a specialized version of `inSphere` that avoids an extra dispatch using the syntax:

```javascript
inSphere[4](a,b,c,d) === inSphere(a,b,c,d)
```

## Credits
(c) 2014 Mikola Lysenko. MIT License