two-sum
=======
Computes the sum of two floating point numbers as a non-overlapping sequence using Knuth's method.

* D.E. Knuth.  "The Art of Computer Programming: Seminumerical Algorithms".  Volume 2.  1981

## Install
Using npm:

		npm install two-sum


## Example

```javascript
var twoSum = require("two-sum")

//Add two wildly different sized floats
var result = twoSum(1e64, 1e-64)
console.log(result)

//Prints:
//  [1e-64, 1e64]
```

## API

### `require("two-sum")(a, b[, result])`
Computes a non-overlapping sequence representing the sum of a and b.

* `a` is a number
* `b` is a number
* `result` is an optional length 2 array encoding the result of the sum of `a` and `b`

**Returns** A length 2 array representing the non-overlapping sequence encoding the sum of a and b.  The first term has smaller magnitude than the second.

## Credits
Based on an idea from JRS robust geometric predicates paper.

Implementation (c) 2013 Mikola Lysenko.  MIT License