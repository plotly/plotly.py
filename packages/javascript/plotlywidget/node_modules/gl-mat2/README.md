# gl-mat2 [![stable](http://badges.github.io/stability-badges/dist/stable.svg)](http://github.com/badges/stability-badges)

Part of a fork of [@toji](http://github.com/toji)'s
[gl-matrix](http://github.com/toji/gl-matrix) split into smaller pieces: this
package contains `glMatrix.mat2`.

## Usage

[![NPM](https://nodei.co/npm/gl-mat2.png)](https://nodei.co/npm/gl-mat2/)

### `mat2 = require('gl-mat2')`

Will load all of the module's functionality and expose it on a single
object. Note that any of the methods may also be required directly
from their files.

For example, the following are equivalent:

``` javascript
var scale = require('gl-mat2').scale
var scale = require('gl-mat2/scale')
```

## API

  - [mat2.adjoint()](#mat2adjointoutmat2amat2)
  - [mat2.copy()](#mat2copyoutmat2amat2)
  - [mat2.create()](#mat2create)
  - [mat2.determinant()](#mat2determinantamat2)
  - [mat2.frob()](#mat2frobamat2)
  - [mat2.identity()](#mat2identityoutmat2)
  - [mat2.invert()](#mat2invertoutmat2amat2)
  - [mat2.ldu()](#mat2ldulmat2dmat2umat2amat2)
  - [mat2.multiply()](#mat2multiplyoutmat2amat2bmat2)
  - [mat2.rotate()](#mat2rotateoutmat2amat2radnumber)
  - [mat2.scale()](#mat2scaleoutmat2amat2vvec2)
  - [mat2.transpose()](#mat2transposeoutmat2amat2)

### `mat2.adjoint(out:mat2, a:mat2)`

  Calculates the adjugate of a mat2

### `mat2.copy(out:mat2, a:mat2)`

  Copy the values from one mat2 to another

### `mat2.create()`

  Creates a new identity mat2

### `mat2.determinant(a:mat2)`

  Calculates the determinant of a mat2

### `mat2.frob(a:mat2)`

  Returns Frobenius norm of a mat2

### `mat2.identity(out:mat2)`

  Set a mat2 to the identity matrix

### `mat2.invert(out:mat2, a:mat2)`

  Inverts a mat2

### `mat2.ldu(L:mat2, D:mat2, U:mat2, a:mat2)`

  Returns L, D and U matrices (Lower triangular, Diagonal and Upper triangular) by factorizing the input matrix

### `mat2.multiply(out:mat2, a:mat2, b:mat2)`

  Multiplies two mat2's

### `mat2.rotate(out:mat2, a:mat2, rad:Number)`

  Rotates a mat2 by the given angle

### `mat2.scale(out:mat2, a:mat2, v:vec2)`

  Scales the mat2 by the dimensions in the given vec2

### `mat2.transpose(out:mat2, a:mat2)`

  Transpose the values of a mat2

## License

[zlib](http://en.wikipedia.org/wiki/Zlib_License). See [LICENSE.md](https://github.com/stackgl/gl-mat2/blob/master/LICENSE.md) for details.
