ndarray-linear-interpolate
==========================
Multilinear (ie [bilinear](http://en.wikipedia.org/wiki/Bilinear_interpolation)/[trilinear](http://en.wikipedia.org/wiki/Trilinear_interpolation)) interpolation for ndarrays.

Example
=======

```javascript
var ndarray = require("ndarray")
var interp = require("ndarray-linear-interpolate")

var x = ndarray(new Float32Array(9), [3, 3])
x.set(1, 1, 1.0)

for(var u=0.0, u<=3.0; u+=0.25) {
  var row = []
  for(var v=0.0; v<=3.0; v+=0.25) {
    row.push(interp(x, u, v))
  }
  console.log(row.join(" "))
}

//Prints out:
//
//    0 0 0 0 0 0 0 0 0 0 0 0 0
//    0 0.0625 0.125 0.1875 0.25 0.1875 0.125 0.0625 0 0 0 0 0
//    0 0.125 0.25 0.375 0.5 0.375 0.25 0.125 0 0 0 0 0
//    0 0.1875 0.375 0.5625 0.75 0.5625 0.375 0.1875 0 0 0 0 0
//    0 0.25 0.5 0.75 1 0.75 0.5 0.25 0 0 0 0 0
//    0 0.1875 0.375 0.5625 0.75 0.5625 0.375 0.1875 0 0 0 0 0
//    0 0.125 0.25 0.375 0.5 0.375 0.25 0.125 0 0 0 0 0
//    0 0.0625 0.125 0.1875 0.25 0.1875 0.125 0.0625 0 0 0 0 0
//    0 0 0 0 0 0 0 0 0 0 0 0 0
//    0 0 0 0 0 0 0 0 0 0 0 0 0
//    0 0 0 0 0 0 0 0 0 0 0 0 0
//    0 0 0 0 0 0 0 0 0 0 0 0 0
//    0 0 0 0 0 0 0 0 0 0 0 0 0
//
```

# Install

    npm install ndarray-linear-interpolate
    
### `require("ndarray-linear-interpolate")(array, x, y, z, ...)`
Interpolates values on an ndarray.

* `array` the array to interpolate from
* `x, y, z...` the coordinate to evaluate the interpolated grid at

**Returns** The multilinearly interpolated value

**Note** To avoid the overhead of variable arguments, special interfaces are available for 1, 2 and 3 dimensions.  You can access these using:

* `require("ndarray-linear-interpolate").d1`
* `require("ndarray-linear-interpolate").d2`
* `require("ndarray-linear-interpolate").d3`


# Credits
(c) 2013 Mikola Lysenko. MIT License

