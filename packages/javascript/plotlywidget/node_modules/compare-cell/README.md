compare-cell
============
Compares two unordered integer sequences to test if they contain the same elements. This can be used to implement various algorithms for unoriented simplicial complexes.

For more information, see the following blog post:

[Comparing sequences without sorting](http://0fps.net/2013/01/24/comparing-sequences-without-sorting/)

# Example

```javascript
var compareCells = require('compare-cell')
var bsearch = require('binary-search-bounds')

//Create a list of triangles defined by indexed faces
var triangles = [
  [1, 0, 2],
  [2, 1, 3],
  [3, 4, 5],
  [5, 6, 7]
]

//Sort triangles
triangles.sort(compareCells)

//Now we can test if various cells are contained in the list in O(log n)
console.log(bsearch.eq(triangles, [2, 1, 0], compareCells) >= 0)
console.log(bsearch.eq(triangles, [3, 5, 7], compareCells) >= 0)
```

# API

#### `var d = require('compare-cells')(a, b)`
Tests if two unordered lists contain the same elements.

* `a, b` are arrays of integers

**Returns** An order function which tests if `a` comes before or after `b`.  The value is `0` if they are equal.

# License
(c) 2015 Mikola Lysenko. MIT License
