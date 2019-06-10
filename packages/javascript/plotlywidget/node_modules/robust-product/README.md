robust-product
==============
Computes the product of two non-overlapping increasing sequences exactly.

## Install

    npm install robust-product

## Example

```javascript
var robustProduct = require("robust-product")

var a = [ Math.pow(2, -50), Math.pow(2, 50) ]

var b = robustProduct(a,a)

//Now:
//
//    b == [ Math.pow(2, -100), 2.0, Math.pow(2, 100) ]
//
```

## API

### `require("robust-product")(a, b)`
Multiplies `a` and `b` together exactly.

* `a`, `b` are both non-overlapping increasing sequences

**Returns** A non-overlapping increasing sequence representing the product of `a` and `b`

## Credits
(c) 2013 Mikola Lysenko. MIT License