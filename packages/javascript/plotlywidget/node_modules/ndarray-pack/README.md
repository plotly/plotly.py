ndarray-pack
============
Converts an array-of-arrays (ie [numeric.js array](http://www.numericjs.com/)) into  a packed [ndarray](https://github.com/mikolalysenko/ndarray).

Example
=======
```javascript
//First create a numeric.js style array:
var x = [[1, 0, 1],
         [0, 1, 1],
         [0, 0, 1],
         [1, 0, 0]]

var y = require("ndarray-pack")(x)
```

Install
=======

    npm install ndarray-pack

### `require("ndarray-pack")(nested_array[,out])`
Converts the nested array into a packed ndarray.

* `nested_array` is an array-of-arrays (ie a numeric.js array)
* `out` is an optional ndarray that gets the result of unpacking `array`

**Returns** A packed ndarray representation of the nested arrays.

# Credits
(c) 2013 Mikola Lysenko. MIT License
