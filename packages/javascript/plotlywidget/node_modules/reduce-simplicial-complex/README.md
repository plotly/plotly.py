reduce-simplicial-complex
=========================
Given an oriented simplicial complex, this module computes a minimal basis for the complex in the integer homology sense.  That is, it cancels out all pairs of equivalent cells which have opposite orientation.

# Example

```javascript
var reduceCells = require('reduce-simplicial-complex')

var cells = [
  [1, 2, 3],
  [2, 1, 3],
  [3, 2, 1],
  [4, 5, 6],
  [7, 8]
]

console.log(reduceCells(cells))
```

# Install

```
npm i reduce-simplicial-complex
```

# API

#### `require('reduce-simplicial-complex')(cells)`
Cancels all pairs of oppositely oriented cells

* `cells` is an array of cells

**Returns** A collapsed list of cells

**Note** This is done in place.  If you need a copy, you should make a copy first, for example using `cells.slice()`.

# License
(c) 2015 Mikola Lysenko. MIT License
