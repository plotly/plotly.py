gl-matrix-invert
================
Dimension independent matrix inverse

# Example

```javascript
var invert = require('gl-matrix-invert')


console.log(invert(new Array(9), [1, 0, 0,
                                  0, 1, 0,
                                  -1, 10, 1]))
```

# API

### `require('gl-matrix-invert')(dest, src)`
Computes the inverse of an array matrix in column-major order (as is the convention in WebGL/gl-matrix).

* `src` is the input matrix
* `dest` is an array which receives the result of the matrix inverse

**Returns** dst

**Notes** Currently only works with matrices up to 4x4

# Credits
(c) 2014 Mikola Lysenko. MIT License