# mat4-interpolate

[![stable](http://badges.github.io/stability-badges/dist/stable.svg)](http://github.com/badges/stability-badges)

Interpolates between two 4x4 matrices, using algorithms from W3C Spec to produce consistent results with CSS animations. Like [mat4-interpolator](https://www.npmjs.org/package/mat4-interpolator) but does the decomposition in place. 

Translation, scale, skew and perspective are interpolated linearly, and rotation is interpolated with spherical interpolation.

```js
var mat4 = require('gl-mat4')
var start = mat4.create()
var end = mat4.fromRotationTranslation([], [0,1,0,0], [20, 50, -10])
var out = mat4.create()

//the matrix interpolator
var interpolate = require('mat4-interpolate')


//.. in your render loop
function render() {
    //interpolate based on alpha, storing results in 'out' matrix
    var vlid = interpolate(out, start, end, alpha)
    
    if (!valid) {
        //could not interpolate, you need to animate yourself somehow   
    }
}
```

## Usage

[![NPM](https://nodei.co/npm/mat4-interpolate.png)](https://nodei.co/npm/mat4-interpolate/)

#### `valid = interpolate(out, start, end, alpha)`

Interpolates between `start` and `end` matrices (16 floats in an array) and stores the result in `out`, using `alpha` for interpolation. This will decompose the two matrices into components, lerp/slerp, and then recompose.

Returns `true` is the interpolation succeeded, or `false` if either matrix is non-invertible (i.e. scale or perspective W of zero). W3C suggests falling back to discrete animations in this case.

## License

MIT, see [LICENSE.md](http://github.com/mattdesl/mat4-interpolate/blob/master/LICENSE.md) for details.
