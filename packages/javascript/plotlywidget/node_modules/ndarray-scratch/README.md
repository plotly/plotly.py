ndarray-scratch
===============
A simple wrapper for typedarray-pool.  I got tired of manually constructing ndarrays from typedarrays, and so this module saves some keystrokes/sanity.

[![testling badge](https://ci.testling.com/scijs/ndarray-scratch.png)](https://ci.testling.com/scijs/ndarray-scratch)

[![build status](https://secure.travis-ci.org/scijs/ndarray-scratch.png)](http://travis-ci.org/scijs/ndarray-scratch)

# Example

```javascript
var pool = require("ndarray-scratch")

//Create a temporary typed array
var x = pool.malloc([100,100])

//Do stuff with x

//Release x
pool.free(x)
```

# Install

    npm install ndarray-scratch

# API

```javascript
var pool = require("ndarray-pool")
```

### `pool.malloc(shape[, dtype])`
Allocates a temporary ndarray

* `shape` is the shape of the array to allocate
* `dtype` is the dtype of the array to allocate (default `"double"`)

**Returns** a temporary ndarray

### `pool.zeros(shape[,dtype])`
Creates a scratch ndarray initialized to `0`

* `shape` is the shape of the resulting array
* `dtype` is the datatype of the array (default `"double"`)

**Returns** A temporary ndarray initialized to 0

### `pool.ones(shape[,dtype])`
Creates a scratch ndarray initialized to `1`

* `shape` is the shape of the resulting array
* `dtype` is the datatype of the array (default `"double"`)

**Returns** A temporary ndarray initialized to 1

### `pool.eye(shape[,dtype])`
Creates a scratch ndarray initialized to `1` if all indices equal, `0` otherwise.

* `shape` is the shape of the resulting array
* `dtype` is the datatype of the array (default `"double"`)

**Returns** A temporary ndarray initialized to the identity matrix

### `pool.free(array)`
Releases a temporary ndarray

* `array` is the ndarray to release.

### `pool.clone(array)`
Creates a copy of an ndarray with row-major order.

* `array` is an ndarray

**Returns** A temporary copy of `array`

# Credits
(c) 2013-2014 Mikola Lysenko. MIT License
