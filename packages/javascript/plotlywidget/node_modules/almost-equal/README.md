almost-equal
============
Checks when two floats are almost equal.

Use
===
First install using npm:

    npm install almost-equal
    
Then use as follows:

```javascript
var almostEqual = require("almost-equal")

var a = 100
  , b = 100 + 1e-12

//Check if a == b up to float precision
console.log(almostEqual(a, b, almostEqual.FLT_EPSILON, almostEqual.FLT_EPSILON))

//Check if a == b up to double precision
console.log(almostEqual(a, b, almostEqual.DBL_EPSILON, almostEqual.DBL_EPSILON))
```

### `almostEqual(a, b[, absoluteTolerance [, relativeTolerance]])`
Checks if two floats are within the given tolerances of one another using the formula:

    |a - b| < max(absoluteTolerance, min(|a|, |b|) * relativeTolerance)

* `a` and `b` are the two numbers to comapre
* `absoluteTolerance` is a fixed minimal tolerance (set to 0 to ignore)
* `relativeTolerance` is a tolerance that scales with a/b (set to 0 to ignore)

**Returns** `true` if `a` and `b` are approximately equal.

If tolerance argument is omitted, `almostEqual.DBL_EPSILON` value is used by default.

### `almostEqual.FLT_EPSILON`
Floating point (32-bit) epsilon

### `almostEqual.DBL_EPSILON`
Double precision (64-bit) epsilon

Credits
=======
(c) 2013 Mikola Lysenko. MIT License
