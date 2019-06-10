# quat-slerp

[![stable](http://badges.github.io/stability-badges/dist/stable.svg)](http://github.com/badges/stability-badges)

Standalone spherical interpolation for quaternions, from [gl-matrix](https://github.com/toji/gl-matrix/blob/master/src/gl-matrix/quat.js).

```js
var slerp = require('quat-slerp')

var out = []
slerp(out, [0, 0, 0, 1], [0, 1, 0, 0], 0.5)

// out is now [0, 0.707106, 0, 0.707106]
```

## Usage

[![NPM](https://nodei.co/npm/quat-slerp.png)](https://nodei.co/npm/quat-slerp/)

#### `slerp(out, a, b, t)`

Interpolates from quaternion `a` to `b` with the given `t` alpha, storing the result in `out`. Returns the `out` quaternion.

`out`, `a` and `b` are all 4-component arrays in the form `[x, y, z, w]`. 

## License

MIT, see [LICENSE.md](http://github.com/mattdesl/quat-slerp/blob/master/LICENSE.md) for details.
