nextafter
=========
Returns the next floating point number after any given number in the direction of some other floating point number. (Like the [C standard library function](http://en.cppreference.com/w/cpp/numeric/math/nextafter)).

[![testling badge](https://ci.testling.com/mikolalysenko/nextafter.png)](https://ci.testling.com/mikolalysenko/nextafter)

[![build status](https://secure.travis-ci.org/mikolalysenko/nextafter.png)](http://travis-ci.org/mikolalysenko/nextafter)

## Example

```javascript
var nextafter = require("nextafter")

var x = 0.1
console.log("The number", x, "is between", nextafter(x, -Infinity), "and", nextafter(x, Infinity))
```

Output:

```
The number 0.1 is between 0.09999999999999999 and 0.10000000000000002
```

## Install

```
npm install nextafter
```

## API

#### `require("nextafter")(from, to)`
Returns the floating point number closest to `from` in the direction on of `to`

* If `from === to`, then returns `from`
* If `from < to`, then returns next representable float after `from`
* If `from > to`, then returns the floating point nubmer immediately before `from`

## Credits
(c) 2014 Mikola Lysenko. MIT License