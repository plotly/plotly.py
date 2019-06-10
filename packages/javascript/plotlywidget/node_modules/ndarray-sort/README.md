ndarray-sort
============
Sorts [ndarrays](https://github.com/mikolalysenko/ndarray) in place using a dual pivot quick sort.

## Example

```javascript
var ndarray = require("ndarray")
var ndsort = require("ndarray-sort")
var unpack = require("ndarray-unpack")

//Create an array
var x = ndarray(new Float32Array(60), [20, 3])

for(var i=0; i<20; ++i) {
  for(var j=0; j<3; ++j) {
    x.set(i,j, Math.random())
  }
}

//Print out x:
console.log("Unsorted:", unpack(x))

//Sort x
ndsort(x)

//Print out sorted x:
console.log("Sorted:", unpack(x))
```

## Install

    npm install ndarray-sort

## API

### `require("ndarray-sort")(array)`
Sorts the given array along the first axis in lexicographic order.  The sorting is done in place.

* `array` is an ndarray

**Returns** `array`

## Credits
Based on Google Dart's dual pivot quick sort implementation by Ola Martin Bini and Michael Haubenwallner.  For more information see lib/dart/AUTHORS and lib/dart/LICENSE

JavaScript implementation (c) 2013 Mikola Lysenko.  MIT License