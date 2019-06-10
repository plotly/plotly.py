ndarray
=======
Modular multidimensional arrays for JavaScript. 

[![browser support](https://ci.testling.com/mikolalysenko/ndarray.png)
](https://ci.testling.com/mikolalysenko/ndarray)

[![build status](https://secure.travis-ci.org/mikolalysenko/ndarray.png)](http://travis-ci.org/mikolalysenko/ndarray)

[![stable](https://rawgithub.com/hughsk/stability-badges/master/dist/frozen.svg)](http://github.com/hughsk/stability-badges)

#### [Big list of ndarray modules](https://github.com/mikolalysenko/ndarray/wiki/ndarray-module-list#core-module)


Introduction
============
`ndarrays` provide higher dimensional views of 1D arrays.  For example, here is how you can turn a length 4 typed array into an nd-array:

```javascript
var mat = ndarray(new Float64Array([1, 0, 0, 1]), [2,2])

//Now:
//
// mat = 1 0
//       0 1
//
```

Once you have an nd-array you can access elements using `.set` and `.get`.  For example, here is an implementation of [Conway's game of life](http://en.wikipedia.org/wiki/Conway's_Game_of_Life) using ndarrays:

```javascript
function stepLife(next_state, cur_state) {

  //Get array shape
  var nx = cur_state.shape[0], 
      ny = cur_state.shape[1]

  //Loop over all cells
  for(var i=1; i<nx-1; ++i) {
    for(var j=1; j<ny-1; ++j) {

      //Count neighbors
      var n = 0
      for(var dx=-1; dx<=1; ++dx) {
        for(var dy=-1; dy<=1; ++dy) {
          if(dx === 0 && dy === 0) {
            continue
          }
          n += cur_state.get(i+dx, j+dy)
        }
      }
      
      //Update state according to rule
      if(n === 3 || n === 3 + cur_state.get(i,j)) {
        next_state.set(i,j,1)
      } else {
        next_state.set(i,j,0)
      }
    }
  }
}
```

You can also pull out views of ndarrays without copying the underlying elements.  Here is an example showing how to update part of a subarray:

```javascript
var x = ndarray(new Float32Array(25), [5, 5])
var y = x.hi(4,4).lo(1,1)

for(var i=0; i<y.shape[0]; ++i) {
  for(var j=0; j<y.shape[1]; ++j) {
    y.set(i,j,1)
  }
}

//Now:
//    x = 0 0 0 0 0
//        0 1 1 1 0
//        0 1 1 1 0
//        0 1 1 1 0
//        0 0 0 0 0
```

ndarrays can be transposed, flipped, sheared and sliced in constant time per operation. They are useful for representing images, audio, volume graphics, matrices, strings and much more. They work both in node.js and with [browserify](http://browserify.org/).

Install
=======
Install the library using [npm](http://npmjs.org):

```sh
npm install ndarray
```

You can also use ndarrays in a browser with any tool that follows the CommonJS/node module conventions.  The most direct way to do this is to use [browserify](https://github.com/substack/node-browserify).  If you want live-reloading for faster debugging, check out [beefy](https://github.com/chrisdickinson/beefy).

API
===
Once you have ndarray installed, you can use it in your project as follows:

```javascript
var ndarray = require("ndarray")
```

## Constructor

### `ndarray(data[, shape, stride, offset])`
The default `module.exports` method is the constructor for ndarrays.  It creates an n-dimensional array view wrapping an underlying storage type

* `data` is a 1D array storage.  It is either an instance of `Array`, a typed array, or an object that implements `get(), set(), .length`
* `shape` is the shape of the view (Default: `data.length`)
* `stride` is the resulting stride of the new array.  (Default: row major)
* `offset` is the offset to start the view (Default: `0`)

**Returns** an n-dimensional array view of the buffer

## Members

The central concept in `ndarray` is the idea of a view.  The way these work is very similar to [SciPy's array slices](http://docs.scipy.org/doc/numpy/reference/arrays.indexing.html).  Views are affine projections to 1D storage types.  To better understand what this means, let's first look at the properties of the view object.  It has exactly 4 variables:

* `array.data` - The underlying 1D storage for the multidimensional array
* `array.shape` - The shape of the typed array
* `array.stride` - The layout of the typed array in memory
* `array.offset` - The starting offset of the array in memory

Keeping a separate stride means that we can use the same data structure to support both [row major and column major storage](http://en.wikipedia.org/wiki/Row-major_order)

## Element Access
To access elements of the array, you can use the `set/get` methods:

### `array.get(i,j,...)`
Retrieves element `i,j,...` from the array.  In psuedocode, this is implemented as follows:

```javascript
function get(i,j,...) {
  return this.data[this.offset + this.stride[0] * i + this.stride[1] * j + ... ]
}
```

### `array.set(i,j,...,v)`
Sets element `i,j,...` to `v`. Again, in psuedocode this works like this:

```javascript
function set(i,j,...,v) {
  return this.data[this.offset + this.stride[0] * i + this.stride[1] * j + ... ] = v
}
```

### `array.index(i,j, ...)`
Retrieves the index of the cell in the underlying ndarray.  In JS,

```javascript
function index(i,j, ...) {
  return this.offset + this.stride[0] * i + this.stride[1] * j + ...
}
```

## Properties
The following properties are created using Object.defineProperty and do not take up any physical memory.  They can be useful in calculations involving ndarrays

### `array.dtype`
Returns a string representing the undelying data type of the ndarray.  Excluding generic data stores these types are compatible with [`typedarray-pool`](https://github.com/mikolalysenko/typedarray-pool).  This is mapped according to the following rules:

Data type | String
--------: | :-----
`Int8Array` | "int8"
`Int16Array` | "int16"
`Int32Array` | "int32"
`Uint8Array` | "uint8"
`Uint16Array` | "uint16"
`Uint32Array` | "uint32"
`Float32Array` | "float32"
`Float64Array` | "float64"
`Array` | "array"
`Uint8ArrayClamped` | "uint8_clamped"
`Buffer` | "buffer"
Other | "generic"

Generic arrays access elements of the underlying 1D store using get()/set() instead of array accessors.

### `array.size`
Returns the size of the array in logical elements.

### `array.order`
Returns the order of the stride of the array, sorted in ascending length. The first element is the first index of the shortest stride and the last is the index the longest stride.

### `array.dimension`
Returns the dimension of the array.

## Slicing
Given a view, we can change the indexing by shifting, truncating or permuting the strides.  This lets us perform operations like array reversals or matrix transpose in **constant time** (well, technically `O(shape.length)`, but since shape.length is typically less than 4, it might as well be).  To make life simpler, the following interfaces are exposed:

### `array.lo(i,j,k,...)`
This creates a shifted view of the array.  Think of it as taking the upper left corner of the image and dragging it inward by an amount equal to `(i,j,k...)`.

### `array.hi(i,j,k,...)`
This does the dual of `array.lo()`.  Instead of shifting from the top-left, it truncates from the bottom-right of the array, returning a smaller array object.   Using `hi` and `lo` in combination lets you select ranges in the middle of an array.

**Note:**  `hi` and `lo` do not commute.   In general:

```javascript
a.hi(3,3).lo(3,3)  !=  a.lo(3,3).hi(3,3)
```

### `array.step(i,j,k...)`
Changes the stride length by rescaling.  Negative indices flip axes.  For example, here is how you create a reversed view of a 1D array:

```javascript
var reversed = a.step(-1)
```

You can also change the step size to be greater than 1 if you like, letting you skip entries of a list.  For example, here is how to split an array into even and odd components:

```javascript
var evens = a.step(2)
var odds = a.lo(1).step(2)
```

### `array.transpose(p0, p1, ...)`
Finally, for higher dimensional arrays you can transpose the indices in place.  This has the effect of permuting the shape and stride values.  For example, in a 2D array you can calculate the matrix transpose by:

```javascript
M.transpose(1, 0)
```

Or if you have a 3D volume image, you can shift the axes using more generic transformations:

```javascript
volume.transpose(2, 0, 1)
```

### `array.pick(p0, p1, ...)`
You can also pull out a subarray from an ndarray by fixing a particular axis.  The way this works is you specify the direction you are picking by giving a list of values.  For example, if you have an image stored as an nxmx3 array you can pull out the channel as follows:

```javascript
var red   = image.pick(null, null, 0)
var green = image.pick(null, null, 1)
var blue  = image.pick(null, null, 2)
```

As the above example illustrates, passing a negative or non-numeric value to a coordinate in pick skips that index.

# More information

For more discussion about ndarrays, here are some talks, tutorials and articles about them:

* [ndarray presentation](http://mikolalysenko.github.io/ndarray-presentation/)
* [Implementing multidimensional arrays in JavaScript](http://0fps.wordpress.com/2013/05/22/implementing-multidimensional-arrays-in-javascript/)
* [Cache oblivious array operations](http://0fps.wordpress.com/2013/05/28/cache-oblivious-array-operations/)
* [Some experiments](https://github.com/mikolalysenko/ndarray-experiments)

Credits
=======
(c) 2013 Mikola Lysenko. MIT License
