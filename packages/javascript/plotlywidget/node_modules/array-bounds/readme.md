# array-bounds  [![experimental](https://img.shields.io/badge/stability-unstable-yellow.svg)](http://github.com/badges/stability-badges) [![Build Status](https://img.shields.io/travis/dfcreative/array-bounds.svg)](https://travis-ci.org/dfcreative/array-bounds)

Find min and max values of a sequence of values/coordinates.

[![npm install array-bounds](https://nodei.co/npm/array-bounds.png?mini=true)](https://npmjs.org/package/array-bounds/)

```js
const getBounds = require('array-bounds')

let bounds = getBounds([0, 25, 50, 75, 100]) // [0, 100]
```

## API

### box = bounds(array, dim=1)

Figures out bounds of sequence of points using dimensions `dim` as stride, ie. for 1d values expected data layout is `[x, x, x, ...]` for 2d is `[x, y, x, y, ...]`, etc. Returned array contains bounds for every dimension as `[minX, minY, ..., maxX, maxY]`, eg.

```js
//get bounding box
let [minX, minY, maxX, maxY] = bounds([x1, y1, x2, y2, x3, y3, ...], 2)

//get bounding cube
let [minX, minY, minZ, maxX, maxY, maxZ] = bounds([x1, y1, z1, x2, y2, z2, ...], 3)
```
