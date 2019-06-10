ndarray-fill
============
Initialize an [ndarray](https://github.com/mikolalysenko/ndarray) with a function.

[![Build Status](https://travis-ci.org/scijs/ndarray-fill.svg?branch=master)](https://travis-ci.org/scijs/ndarray-fill)

## Example

```javascript
var zeros = require("zeros")
var fill = require("ndarray-fill")

var x = zeros([5, 5])

fill(x, function(i,j) {
  return 10*i + j
})

//Now x = 
//
//   0  1  2  3  4
//  10 11 12 13 14
//  20 21 22 23 24
//  30 31 32 33 34
//
```

## Install

```
npm install ndarray-fill
```

### `require("ndarray-fill")(array, func)`
Fills an ndarray with a pattern

* `array` is an ndarray which will be initialized
* `func` is a function that will be used to initialize the array

**Returns** An initialized ndarray

## Credits
(c) 2013 Mikola Lysenko. MIT License
