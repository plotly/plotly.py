# array-rearrange  [![experimental](https://img.shields.io/badge/stability-unstable-yellow.svg)](http://github.com/badges/stability-badges) [![Build Status](https://img.shields.io/travis/dfcreative/array-rearrange.svg)](https://travis-ci.org/dfcreative/array-rearrange)

Reorder elements within array by index.

[![npm install array-rearrange](https://nodei.co/npm/array-rearrange.png?mini=true)](https://npmjs.org/package/array-rearrange/)

```js
const reorder = require('array-rearrange')

let arr = reorder([9,8,7,6], [3,2,1,0]) // [6,7,8,9]

let arr2 = reorder([3,3, 2,2, 1,1], [2,1,0]) // [1,1, 2,2, 3,3]
```

## API

### array = reorder(array, index, stride=1)

Shuffle elements in `array` according to the `index` array passed. Permutes original array. `index` array should contain unique indexes. Pass `stride` to indicate groups of elements to shuffle.

Originally based on the [reference solution](https://www.geeksforgeeks.org/reorder-a-array-according-to-given-indexes/), which turns out to be wrong, so algorithm is fully rewritten.

## See also

* [array-normalize](https://github.com/dfcreative/array-normalize)
* [array-bounds](https://github.com/dfcreative/array-bounds)
* [array-same](https://github.com/dfcreative/array-same)
* [array-polar](https://github.com/dfcreative/array-polar)
* [negative-index](https://github.com/dfcreative/negative-index)
* [deinterleave](https://github.com/dfcreative/deinterleave)
