# flatten-vertex-data

[![stable](http://badges.github.io/stability-badges/dist/stable.svg)](http://github.com/badges/stability-badges)

Copies flat or nested array data into the specified typed array, or a new typed array. Intended to be used for WebGL buffers. If the input is nested array data, this guesses the dimensionality based on the length of the first sub-array.

## Install

```sh
npm install flatten-vertex-data --save
```

## Example

Accepts a [dtype string](https://www.npmjs.com/package/dtype) (creating a new array) or an output typed array to re-use. Defaults to creating a new Float32Array.

```js
var flatten = require('flatten-vertex-data')

var positions = [ [x1, y1], [x2, y2], [x3, y3] ]

flatten(positions)
//=> new Float32Array([ x1, y1, x2, y2, x3, y3 ])

flatten(positions, 'uint16')
//=> new Uint16Array([ x1, y1, x2, y2, x3, y3 ])

// flatten & copy positions into output
var output = new Uint16Array(positions.length * 2)
flatten(positions, output)
```

## Usage

[![NPM](https://nodei.co/npm/flatten-vertex-data.png)](https://www.npmjs.com/package/flatten-vertex-data)

#### `output = flatten(data, [output|type], [offset])`

Copies flat or nested arrays into a typed array, where `data` can be:

- a nested array like `[ [ x, y ], [ x, y ] ]`
- a flat array like `[ x, y, z, x, y, z ]`
- a typed array like `new Float32Array([ x, y ])`

The second parameter can be a `type` string for [dtype](https://www.npmjs.com/package/dtype), which creates a new array. Or, it can be an existing typed array to re-use as the `output` destination. It defaults to `'float32'` (a new Float32Array).

Returns the `output` typed array.

The third parameter, `offset`, can be a number (default 0), the index in the destination array at which to start copying the `data`. If a new array is being created, its capacity will be expanded to fit `dataLength + offset` (i.e. it will have leading zeros).

## License

MIT, see [LICENSE.md](http://github.com/glo-js/flatten-vertex-data/blob/master/LICENSE.md) for details.
