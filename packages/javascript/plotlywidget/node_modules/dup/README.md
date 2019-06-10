# dup
Initializes an n-dimensional array to a constant value.

## Install

    npm install dup
    
## Example

```javascript
var dup = require("dup")

console.log(dup(5))

//Prints:
//
//    [0, 0, 0, 0, 0]
//


console.log(dup([3,2], 1))

//Prints:
//
//    [[1, 1],
//     [1, 1],
//     [1, 1]]
//
```

## `require("dup")(shape[, value])`
Initializes an array to a constant value

* `shape` Either an array of dimensions or a scalar, representing the shape of the array to create.
* `value` The value to initialize the array with.  Default is 0

**Returns** An n-dimensional array with the given shape and value

## Rationale
I often find myself using [numeric.js'](http://www.numericjs.com/) `rep` method in my projects.  However, for many things pulling in all of numeric.js is total overkill, especially for code that ultimately needs to run on the browser.  So I decided to make this library which just implements the `rep` and nothing else in the spirit of promoting modularity by smaller and more numerous packages.

# Credits
(c) 2013 Mikola Lysenko. MIT License