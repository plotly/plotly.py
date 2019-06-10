typedarray-pool
===============
A global pool for typed arrays.

[![testling badge](https://ci.testling.com/mikolalysenko/typedarray-pool.png)](https://ci.testling.com/mikolalysenko/typedarray-pool)

[![build status](https://secure.travis-ci.org/mikolalysenko/typedarray-pool.png)](http://travis-ci.org/mikolalysenko/typedarray-pool)

# Example

```javascript
var pool = require("typedarray-pool")

//Allocate a buffer with at least 128 floats
var f = pool.malloc(128, "float")

// ... do stuff ...

//When done, release buffer
pool.free(f)
```

# Install

    npm install typedarray-pool

# API

```javascript
var pool = require("typedarray-pool")
```

### `pool.malloc(n[, dtype])`
Allocates a typed array (or ArrayBuffer) with at least n elements.

* `n` is the number of elements in the array
* `dtype` is the data type of the array to allocate.  Must be one of:

  + `"uint8"`
  + `"uint16"`
  + `"uint32"`
  + `"int8"`
  + `"int16"`
  + `"int32"`
  + `"float"`
  + `"float32"`
  + `"double"`
  + `"float64"`
  + `"arraybuffer"`
  + `"data"`
  + `"uint8_clamped"`
  + `"buffer"`

**Returns** A typed array with at least `n` elements in it.  If `dtype` is undefined, an ArrayBuffer is returned.

**Note**  You can avoid the dispatch by directly calling one of the following methods:

* `pool.mallocUint8`
* `pool.mallocUint16`
* `pool.mallocUint32`
* `pool.mallocInt8`
* `pool.mallocInt16`
* `pool.mallocInt32`
* `pool.mallocFloat`
* `pool.mallocDouble`
* `pool.mallocArrayBuffer`
* `pool.mallocDataView`
* `pool.mallocUint8Clamped`
* `pool.mallocBuffer`

### `pool.free(array)`
Returns the array back to the pool.

* `array` The array object to return to the pool.

**Note** You can speed up the method if you know the type of array before hand by calling one of the following:

* `pool.freeUint8`
* `pool.freeUint16`
* `pool.freeUint32`
* `pool.freeInt8`
* `pool.freeInt16`
* `pool.freeInt32`
* `pool.freeFloat`
* `pool.freeDouble`
* `pool.freeArrayBuffer`
* `pool.freeDataView`
* `pool.freeUint8Clamped`
* `pool.freeBuffer`

### `pool.clearCache()`
Removes all references to cached arrays.  Use this when you are done with the pool to return all the cached memory to the garbage collector.

# Credits
(c) 2014 Mikola Lysenko. MIT License