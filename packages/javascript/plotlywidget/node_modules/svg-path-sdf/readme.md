# svg-path-sdf [![experimental](https://img.shields.io/badge/stability-unstable-green.svg)](http://github.com/badges/stability-badges)

Create signed distance field for an svg path data.

![svg-path-sdf](https://github.com/dy/svg-path-sdf/blob/master/preview.png?raw=true)

## Usage

[![npm install svg-path-sdf](https://nodei.co/npm/svg-path-sdf.png?mini=true)](https://npmjs.org/package/svg-path-sdf/)

```js
let pathSdf = require('svg-path-sdf')

let arr = pathSdf('M40,0A40,40 0 1,1 0,-40A40,40 0 0,1 40,0Z', {
	width: 200,
	height: 200
})
```

`arr` has `200×200` elements with value from `0..1` range, corresponding to distance. The path is drawn at the center of the sdf fitting to the minimum side.

## distances = pathSdf(path, options|shape?)

Option | Meaning
---|---
`width`,`w`, `height`,`h` or `shape` | Output sdf size in px, defaults to `200×200`.
`cutoff`, `radius` | SDF parameters for [bitmap-sdf](https://github.com/dy/bitmap-sdf), by default detected from shape to fit min side.
`viewBox` | View box for the path data. If not defined, it is detected as path bounds via [svg-path-bounds](https://github.com/dy/svg-path-bounds).
`stroke` | Whether to stroke shape. Positive number will stroke outside the amount of pixels, negative number will stroke inside, `0`-ish will disable stroke.

## License

(c) 2017 Dima Yv. MIT License

Development supported by plot.ly.
