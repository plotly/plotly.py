cell-orientation
================
Computes the orientation of a cell, given by a list of integer indices.

# Example

```javascript
var orientation = require('cell-orientation')

console.log(orientation([0, 1, 2]))
console.log(orientation([1, 0, 2]))
console.log(orientation([1, 1, 2]))
```

# API

#### `require('cell-orienation')(s)`
Computes the orientation of the cell

* `s` is a list of integers

**Returns** `0` if `s` has any duplicates (ie is degenerate), otherwise `+/-` depending on the ordering of `s`

# License
(c) 2015 Mikola Lysenko. MIT License
