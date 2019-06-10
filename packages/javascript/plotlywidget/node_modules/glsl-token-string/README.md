# glsl-token-string

[![experimental](http://badges.github.io/stability-badges/dist/experimental.svg)](http://github.com/badges/stability-badges)

Simple helper package that converts an array of GLSL tokens to a plain GLSL
source string.

## Usage

[![NPM](https://nodei.co/npm/glsl-token-string.png)](https://nodei.co/npm/glsl-token-string/)

### `src = stringify(tokens)`

``` javascript
var tokenize  = require('glsl-tokenizer/string')
var stringify = require('glsl-token-string')
var assert    = require('assert')

var src    = 'vec3 light = vec3(1.0);'
var tokens = tokenize(src)

assert(stringify(tokens) === src)
```

## See Also

* [glsl-tokenizer](http://github.com/stackgl/glsl-tokenizer)
* [glsl-token-scope](http://github.com/stackgl/glsl-token-scope)
* [glsl-token-depth](http://github.com/stackgl/glsl-token-depth)
* [glsl-token-properties](http://github.com/stackgl/glsl-token-properties)
* [glsl-token-assignments](http://github.com/stackgl/glsl-token-assignments)

## License

MIT. See [LICENSE.md](http://github.com/stackgl/glsl-token-string/blob/master/LICENSE.md) for details.
