two-product
===========
Computes the product of two floating point numbers as a 2-term nonoverlapping increasing sequence.

## Install

```
npm install two-product
```
		
## Example

```javascript
var twoProduct = require("two-product")

console.log(twoProduct(1 + Math.pow(2, -52), Math.pow(2, 52) + 1))
```

Output:

```javascript
[ 2.220446049250313e-16, 4503599627370498 ]
```

## API

### `require("two-product")(a, b[, result])`
Multiplies `a` and `b` and returns the product as a non-overlapping sequence.  `result` is an optional length 2 array that stores the result.

* `a` is a number
* `b` is a number
* `result` is an optional length 2 array that gets the result of multiplying `a` and `b`

**Returns** A length 2 array representing the product of `a` and `b` as an expansion.  The first entry is the lower order bits, and the second entry is the upper order bits.

**Note** This algorithm does not work correctly with denormalized numbers.

## Credits
JavaScript implementation (c) 2013-2014 Mikola Lysenko.  Based on ideas from Jonathan Shewchuk's [robust adaptive geometric predicates](http://www.cs.cmu.edu/~quake/robust.html).