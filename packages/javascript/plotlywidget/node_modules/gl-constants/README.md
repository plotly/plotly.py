# gl-constants

[![stable](http://badges.github.io/stability-badges/dist/stable.svg)](http://github.com/badges/stability-badges)

All the WebGL 1.0 constants as a module. Useful for testing.

```js
var constants = require('gl-constants')

texture.minFilter = constants.LINEAR
texture.magFilter = constants.NEAREST
```

You can also 'lookup' a constant by number:

```js
var lookup = require('gl-constants/lookup')

console.log(lookup(1282)) // INVALID_OPERATION
```

Note that some fields share the same number, like `NONE`, `ZERO` `POINTS` and `NO_ERROR` all use 0.

## Usage

[![NPM](https://nodei.co/npm/gl-constants.png)](https://www.npmjs.com/package/gl-constants)

#### `require('gl-constants')`

An object where each key corresponds to the WebGL constant integer value.

#### `require('gl-constants/lookup')(number)`

Returns the key name associated with the given WebGL constant integer value.

## License

MIT, see [LICENSE.md](http://github.com/mattdesl/gl-constants/blob/master/LICENSE.md) for details.
