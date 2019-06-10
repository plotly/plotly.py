bit-twiddle
===========

This is a collection of miscellaneous bit twiddling hacks ported to JavaScript, mostly taken from here:

* [Stanford Bit Twiddling Hacks](http://graphics.stanford.edu/~seander/bithacks.html)

[![testling badge](https://ci.testling.com/mikolalysenko/bit-twiddle.png)](https://ci.testling.com/mikolalysenko/bit-twiddle)

[![build status](https://secure.travis-ci.org/mikolalysenko/bit-twiddle.png)](http://travis-ci.org/mikolalysenko/bit-twiddle)

Install
=======
Via npm:

    npm install bit-twiddle

# API

### `sign(v)`
Computes the sign of the integer v.  Returns:
* -1 if v < 0
*  0 if v === 0
* +1 if v > 0

### `abs(v)`
Returns the absolute value of the integer v

### `min(x,y)`
Computes the minimum of integers x and y

### `max(x,y)`
Computes the maximum of integers x and y

### `isPow2(v)`
Returns `true` if v is a power of 2, otherwise false.

### `log2(v)`
Returns an integer approximation of the log-base 2 of v

### `log10(v)`
Returns log base 10 of v.

### `popCount(v)`
Counts the number of bits set in v

###  `countTrailingZeros(v)`
Counts the number of trailing zeros.

### `nextPow2(v)`
Rounds v up to the next power of 2.

### `prevPow2(v)`
Rounds v down to the previous power of 2.

### `parity(v)`
Computes the parity of the bits in v.

### `reverse(v)`
Reverses the bits of v.

### `interleave2(x,y)`
Interleaves a pair of 16 bit integers.  Useful for fast quadtree style indexing.  (See wiki: http://en.wikipedia.org/wiki/Z-order_curve )

### `deinterleave2(v, n)`
Deinterleaves the bits of v, returns the nth part.  If both x and y are 16 bit, then it is true that:

```javascript
deinterleave2(interleave2(x,y), 0) === x
deinterleave2(interleave2(x,y), 1) === y
```
    
### `interleave3(x,y,z)`
Interleaves a triple of 10 bit integers.  Useful for fast octree indexing.

### `deinterleave3(v, n)`
Same deal as `deinterleave2`, only for triples instead of pairs

### `nextCombination(x)`
Returns next combination ordered colexicographically.

Acknowledgements
================
Code is ported from Sean Eron Anderson's public domain bit twiddling hacks page.  http://graphics.stanford.edu/~seander/bithacks.html
JavaScript implementation (c) 2013 Mikola Lysenko.  MIT License
