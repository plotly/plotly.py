triangulate-hypercube
=====================
Triangulates an n-dimensional hypercube into a collection of simplices.

**Note:** In high dimensions, this triangulation is not very efficient. Pull requests welcome.

# Example

```javascript
var triangulateCube = require("triangulate-hypercube")

console.log(triangulateCube(2))
```

Output:

```javascript
[ [ 3, 2, 0 ], [ 0, 1, 3 ] ]
```

# Install

```
npm install triangulate-hypercube
```

# API

#### `require("triangulate-hypercube")(dimension)`
Computes a decomposition of an n-dimensional hypercube into simplices using a naive permutation based algorithm.

* `dimension` is an integer representing the dimension of the hypercube to triangulate

**Returns** A list of `n` dimensional simplices which subdivide the cube.

# Credits
(c) 2014 Mikola Lysenko. MIT License