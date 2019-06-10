compare-oriented-cell
=====================
This module defines an ordering on oriented cells.  It is similar to `compare-cell`, except that it considers cells which are oriented clockwise/counter clockwise to be distinct.

# Example

```javascript
var compare = require('compare-oriented-cell')

//Create 3 triangles
var a = [0, 1, 2]
var b = [1, 2, 0]
var c = [1, 0, 2]

//Triangle a and b are equivalent up to an even permutation
console.log(compare(a, b) === 0)

//Triangle a and c are different as they not oriented the same
console.log(compare(a, c) === 0)
```

# Install

```
npm i compare-oriented-cell
```

# API

#### `require('compare-oriented-cell')(a, b)`
Compares two oriented cells.

* `a, b` are lists of integers

**Returns** `+/-1` if `a` and `b` are different, `0` otherwise

# License
(c) 2015 Mikola Lysenko. MIT License
