# color-parse [![Build Status](https://travis-ci.org/colorjs/color-parse.svg?branch=master)](https://travis-ci.org/colorjs/color-parse)

Fast and tiny color string parser.


`$ npm install color-parse`

```js
var parse = require('color-parse')

parse('hsla(12, 10%, 50%, .3)')
// { space: 'hsl', values: [12, 10, 50], alpha: 0.3 }
```

## Parsed strings

* [x] `red`, `green` etc., see [color-name](https://ghub.io/color-name)
* [x] `rgb(10, 20, 30)`, `rgba(10, 20, 30, .3)`
* [x] `hsl()`, `hsla()` inc. [named hues](http://dev.w3.org/csswg/css-color/#simple-hues)
* [x] `hwb()`
* [x] `cmyk()`
* [x] `xyz()`
* [x] `lab()`
* [x] `lch()`
* [x] `luv()`
* [x] `#RGB`
* [x] `#RGBA`
* [x] `#RRGGBB`
* [x] `#RRGGBBAA`
* [x] `R:10 G:20 B:30`
* [x] `(R10 / G20 / B30)`
* [x] `C100/M80/Y0/K35`

## Parsed not strings

* [x] `[10, 20, 20]` as RGB color space
* [x] `{r: 10, g: 20, b: 30}`
* [x] `{red: 10, green: 20, blue: 30}`
* [x] `{h: 10, s: 20, l: 30}`
* [x] `0x00ff00`, `0x0000ff` numbers

## Not parsed strings

* [x] `'yellowblue'` returns `null`

## Related

* [color-space](https://npmjs.org/package/color-space) — collection of color space conversions.
* [color-rgba](https://npmjs.org/package/color-rgba) — convert any color string to rgba array.
* [color-alpha](https://npmjs.org/package/color-alpha) — change alpha component of any color.

## Analogs

* [parse-color](http://npmjs.org/package/parse-color) — parser by James Halliday. Initially inspired by that awesome parser. It performs calculations to every possible space which results in bloated size of lib.
* [color-parser](http://npmjs.org/package/color-parser) — parser by TJ. Supports limited set of spaces.
* [color-string](http://npmjs.org/package/color-string) — color parsing/serializing module by Heather Arthur. Has extensive API for parsing and serializing from any to any space.


[![NPM](https://nodei.co/npm/color-parse.png?downloads=true&downloadRank=true&stars=true)](https://nodei.co/npm/color-parse/)
