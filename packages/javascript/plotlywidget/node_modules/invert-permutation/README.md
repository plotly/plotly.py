invert-permutation
==================
Computes the [inverse of a permutation](http://en.wikipedia.org/wiki/Permutation#Product_and_inverse)

Example
========

```javascript
console.log( require("invert-permutation")([1,3,0,2]) )

//Prints:
//          [ 2, 1, 3, 0 ]
```

# Install

    npm install invert-permutation

# API

## `require("invert-permutation")(perm[, result])
Inverts a permutation

* `perm` is the permutation to invert
* `result` is an optional array that gets the result of inverting the permutation

**Returns** `result` or a newly allocated array if nothing is specified

Credits
=======
(c) 2013 Mikola Lysenko. MIT License