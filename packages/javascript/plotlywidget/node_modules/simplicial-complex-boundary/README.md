simplicial-complex-boundary
===========================
Extracts the boundary of a simplicial complex.

# Example

```javascript
var boundary = require('simplicial-complex-boundary')

var cells = [
  [0,1,2],
  [1,2,3]
]

console.log(boundary(cells))
```

Output:

```
[ [ 0, 1 ], [ 0, 2 ], [ 1, 3 ], [ 2, 3 ] ]
```

# Install

```
npm i simplicial-complex-boundary
```

# API

#### `var bnd = require('simplicial-complex-boundary')(cells)`
Computes the boundary of a simplicial complex

* `cells` are the cells of a simplicial complex

**Returns** The boundary of the simplicial complex (in the Z/2 homology sense)

# License

(c) 2015 Mikola Lysenko. MIT License