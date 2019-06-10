# μMath [![Build Status](https://travis-ci.org/dfcreative/mumath.svg?branch=master)](https://travis-ci.org/dfcreative/mumath) [![Code Climate](https://codeclimate.com/github/dfcreative/mumath/badges/gpa.svg)](https://codeclimate.com/github/dfcreative/mumath) <a href="UNLICENSE"><img src="http://upload.wikimedia.org/wikipedia/commons/6/62/PD-icon.svg" width="20"/></a>

Set of practical math utils to shorten code.

[`$ npm install mumath`](https://npmjs.org/package/mumath)

```js
var round = require('mumath/round');
round(123.32, .5); //123.5

//require any function as
//var <fn> = require('mumath/<fn>');
```

## API

### `round(value, step?)`

Rounds value to optional `step`.

`round(0.3, .5)` → `.5`


### `len(a, b)`

Return length of a vector.


### `precision(value)`

Get precision from float:

`1.1 → 1, 1234 → 0, .1234 → 4`


### `clamp(value, left, right)`

Return value clamped by left/right limits (or vice-versa).


### `lerp(x, y, ratio)`

Return value interpolated between x and y.


### `within(value, left, right)`

Whether element is between left & right, including.


### `mod(value, min?, max)`

An enhanced [mod-loop](http://npmjs.org/package/mod-loop) — loops value within a frame.


### `closest(value, list)`

Get closest value out of a set.


### `scale(value, list)`

Get first scale out of a list of basic scales, aligned to the power. E. g.

`step(.37, [1, 2, 5])` → `.5`
`step(456, [1, 2])` → `1000`

Similar to closest, but takes all possible powers of scales.

### `order(value)`

Get order of magnitude for a number.

`order(123) → 100; order(-0.0003) → 0.0001;`


### `isMultiple(a, b, eps?)`

Same as `a % b === 0`, but with precision check.


## Related

* [bit-twiddle](https://www.npmjs.com/package/bit-twiddle) — utils for power-of-two numbers.
* [pretty-number](https://www.npmjs.com/package/pretty-number) — format number to pretty view.
