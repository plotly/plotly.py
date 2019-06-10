zero-crossings
==============
Finds all zero crossings in a 1D ndarray assuming piecewise-linear interpolation.

# Example

```javascript
var ndarray = require("ndarray")
var zc = require("zero-crossings")

var array = ndarray([1, -1, 0, 10, 3, -1])

console.log(zc(array))
```

Output:

```
[ 0.5, 2, 4.75 ]
```

# Install

```
npm install zero-crossings
```

# API

#### `require("zero-crossings")(array[,level])`
Finds all zero crossings in the 1D ndarray `array`

* `array` is a 1D ndarray
* `level` is an optional parameter which indicates the crossings

**Returns** A list of all zero crossings in `array`

# Credits
(c) 2014 Mikola Lysenko. MIT License