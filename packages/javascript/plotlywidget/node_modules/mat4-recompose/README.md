# mat4-recompose

[![stable](http://badges.github.io/stability-badges/dist/stable.svg)](http://github.com/badges/stability-badges)

Recompose a 4x4 matrix from translation, scale, skew, perspective, and rotation. This is commonly used in matrix animations (i.e. after [decompose](https://github.com/mattdesl/mat4-decompose) and interpolation). Code ported from [W3 CSS Spec](http://www.w3.org/TR/css3-transforms/#decomposing-a-3d-matrix). PRs for more tests/robustness/optimizations welcome. 

You may also be interested in [mat4-interpolate](https://www.npmjs.com/package/mat4-interpolate), [mat4-decompose](https://www.npmjs.com/package/mat4-decompose), and [css-mat4](https://www.npmjs.com/package/css-mat4).

## Usage

[![NPM](https://nodei.co/npm/mat4-recompose.png)](https://nodei.co/npm/mat4-recompose/)

#### `recompose(matrix, translation, scale, skew, perspective, quaternion)`

Recomposes a matrix with the given vectors, storing the result into `matrix` (a 16 float array). 

- `translation` [x, y, z]
- `scale` [x, y, z]
- `skew` [xy, xz, yz] skew factors
- `perspective` [x, y, z, w]
- `quaternion` [x, y, z, w]

Returns the `matrix` being recomposed.

Builds a translation matrix, then applies the quaternion rotation and perspective. The matrix is then multiplied by YZ shear, then XZ shear, then XY shear (if they are non-zero). Finally multiplied by scale to get the resulting recomposed matrix.

## License

MIT, see [LICENSE.md](http://github.com/mattdesl/mat4-recompose/blob/master/LICENSE.md) for details.
