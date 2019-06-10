to-px
=====
Get the scale factor to convert any CSS unit to `px` (logical pixel units).

[![testling badge](https://ci.testling.com/mikolalysenko/to-px.png)](https://ci.testling.com/mikolalysenko/to-px)

# Example

```javascript
var toPX = require('to-px')

console.log(toPX('1em'))
console.log(toPX('.23vh'))
console.log(toPX('in'))
```

# Install

Note that this module only works within the DOM.

```
npm i to-px
```

# API

#### `var scaleFactor = require('to-px')(unit[, element])`

Computes the number of pixels in the `unit` string.

* `unit` is a CSS unit type or a number followed by CSS unit, eg `vh` or `2in`
* `element` is an optional element in which the unit is computed (default is `document.body`)

**Returns** The number of pixels in the `unit`

**Note** Conversions for `%` are not supported since they are context dependent.

# License
(c) 2015 Mikola Lysenko. MIT License
