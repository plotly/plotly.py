ndarray-gradient
================
Computes the gradient of an ndarray using a 2-point central finite difference template.

# Example

```javascript
var pack = require('ndarray-pack')
var pool = require('ndarray-scratch')
var grad = require('ndarray-gradient')
var show = require('ndarray-show')

var X = pack([[0, 0, 0],
              [0, 1, 0],
              [0, 0, 0]])

//Compute gradient of X
var dX = grad(pool.zero([3,3,2]), X)

console.log('grad(X) = \n', show(dX))
```

Output:

```
grad(X) =
   0.000    0.000    0.000
  -0.500    0.000    0.500
   0.000    0.000    0.000

   0.000   -0.500    0.000
   0.000    0.000    0.000
   0.000    0.500    0.000
```

# Install

```
npm install ndarray-gradient
```

# API

### `require('ndarray-gradient')(dst, src[, bc])`
Computes the gradient of `src` storing the result into `dst`.

* `dst` is an array of gradient values.  The shape of `dst` must be the shape of `src` with one additional dimension for the components of the gradient
* `src` is the array to differentiate
* `bc` is an array of boundary conditions.  The boundary conditions are encoded as string values and must be one of the following values:

    + `'clamp'` (Default) clamp boundary edges to boundary
    + `'mirror'` mirror values across the boundary
    + `'wrap'` wrap values across boundary

**Returns** `dst`

# Credits
(c) 2014 Mikola Lysenko. MIT License