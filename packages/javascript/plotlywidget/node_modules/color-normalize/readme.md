# color-normalize [![Build Status](https://travis-ci.org/colorjs/color-normalize.png)](https://travis-ci.org/colorjs/color-normalize) [![Greenkeeper badge](https://badges.greenkeeper.io/colorjs/color-normalize.svg)](https://greenkeeper.io/)

Convert any color argument (string, color, number, object etc.) to an array with channels data of desired output format.


## Usage

[![npm install color-normalize](https://nodei.co/npm/color-normalize.png?mini=true)](https://npmjs.org/package/color-normalize/)

```js
const rgba = require('color-normalize')

rgba('red') // [1, 0, 0, 1]
rgba('rgb(80, 120, 160)', 'uint8') // Uint8Array<[80, 120, 160, 255]>
rgba('rgba(255, 255, 255, .5)', 'float64') // Float64Array<[1, 1, 1, .5]>
rgba('hsla(109, 50%, 50%, .75)', 'uint8') // Uint8Array<[87, 191, 64, 191]>
rgba(new Float32Array([0, 0.25, 0, 1]), 'uint8_clamped') // Uint8ClampedArray<[0, 64, 0, 255]>
rgba(new Uint8Array([0, 72, 0, 255]), 'array') // [0, 0.2823529411764706, 0, 1]

// ambivalent input
rgba([0,0,0]) // [0,0,0]
rgba([.5,.5,.5]) // [.5,.5,.5]
rgba([1,1,1]) // [1,1,1]
rgba([127,127,127]) // [.5,.5,.5]
rgba([255,255,255]) // [1,1,1]
```

Output format can be any [dtype](https://npmjs.org/package/dtype): `uint8`, `uint8_clamped`, `array`, `float32`, `float64` etc. By default it converts to `array` with `0..1` range values.


## Related

* [color-alpha](https://github.com/colorjs/color-alpha) − change alpha of a color string.
* [color-interpolate](https://github.com/colorjs/color-interpolate) − interpolate by color palette.
* [color-parse](https://github.com/colorjs/color-parse) − comprehensive color string parser.
* [color-rgba](https://github.com/colorjs/color-rgba) − get rgba channel values from a string.
* [flatten-vertex-data](https://npmjs.org/package/flatten-vertex-data) − ensure sequence of point coordinates is flat.

## License

(c) 2017 Dima Yv. MIT License
