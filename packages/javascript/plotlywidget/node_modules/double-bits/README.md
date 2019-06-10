double-bits
===========
Routines for manipulating binary representations of a IEEE 754 double precision numbers.

[![testling badge](https://ci.testling.com/mikolalysenko/double-bits.png)](https://ci.testling.com/mikolalysenko/double-bits)

[![build status](https://secure.travis-ci.org/mikolalysenko/double-bits.png)](http://travis-ci.org/mikolalysenko/double-bits)

## Example

```javascript
var db = require("double-bits")

//Get higher order word
console.log(db.hi(1.0).toString(16))    //Prints out: 3ff00000

//Get lower order word
console.log(db.lo(1.0).toString(16))    //Prints out: 0

//Combine two words into a double
console.log(db.pack(0, 0x3ff00000))     //Prints out: 1.0

//More sophisticated example:  Print out base 2 representation
var pad = require("pad")
function base2Str(n) {
  var f = db.fraction(n)
  return (db.sign(n) ? "-" : "") +
    "2^" + (db.exponent(n)+1) +
    " * 0." + pad(f[1].toString(2), 20, "0") + 
              pad(f[0].toString(2), 32, "0")
}
console.log(base2Str(1.0))
//Prints out:
//
//   2^1 * 0.10000000000000000000000000000000000000000000000000000
//
```

## Install

```
npm install double-bits
```

## API

```javascript
var db = require("double-bits")
```

### `db(n)`
Returns a pair of 32-bit unsigned ints encoding the lower/higher order words respectively representing `n`

* `n` is an IEEE754 double number

**Returns** An array, `[lo,hi]` encoding `n`

### `db.lo(n)`
Returns the lower order word of `n`

* `n` is an IEEE754 number

**Returns** The lower order word of `n`

### `db.hi(n)`
Returns the higher order word of `n`

* `n` is an IEEE754 number

**Returns** The higher order word of `n`

### `db.pack(lo, hi)`
Given a pair of lower/higher order words, concatenate them into a 64 bit double precision number

* `lo` is the lower order word
* `hi` is the higher order word

**Returns** An IEEE754 double precision number formed by concatenating the bits of `lo` and `hi`

### `db.sign(n)`
Returns the state of the sign bit of `n`

* `n` is an IEEE754 double precision number

**Returns** The sign bit of `n`

### `db.exponent(n)`
Returns the exponent of `n`

* `n` is an IEEE754 double precision number

**Returns** The exponent of `n`

### `db.fraction(n)`
Returns the fractional part of `n`

* `n` is an IEEE754 double precision number

**Returns** The fractional part of `n` encoded as a pair of numbers, `[lo,hi]` where `lo` is a 32 bit integer and `hi` is a 21 bit integer.

### `db.denormalized(n)`
Test if a double is [denormalized](http://en.wikipedia.org/wiki/Denormal_number).

* `n` is a number

**Returns** `true` if `n` is denormal, `false` otherwise

## Credits
(c) 2014 Mikola Lysenko. BSD License