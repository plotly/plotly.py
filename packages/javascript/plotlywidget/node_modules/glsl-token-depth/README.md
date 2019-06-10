# glsl-token-depth

[![experimental](http://badges.github.io/stability-badges/dist/experimental.svg)](http://github.com/badges/stability-badges)

Determine the scope depth of an array of GLSL tokens.

Useful for inferring the scope of variables in a GLSL shader without having
to fully parse the source.

## Usage

[![NPM](https://nodei.co/npm/glsl-token-depth.png)](https://nodei.co/npm/glsl-token-depth/)

### `depth(tokens)`

Where `tokens` is an array of tokens returned from
[`glsl-tokenizer`](http://github.com/stackgl/glsl-tokenizer). Each token will
be modified in-place, and given a `depth` property.

``` javascript
var tokenize = require('glsl-tokenizer/string')
var depth    = require('glsl-token-depth')
var fs       = require('fs')

var src = fs.readFileSync('shader.frag', 'utf8')
var tokens = tokenize(src)

depth(tokens)

tokens[0].depth // 0
tokens[1].depth // 0
tokens[2].depth // 0
tokens[3].depth // 0
tokens[4].depth // 1
// ...
```

## See Also

* [stackgl/glsl-tokenizer](http://github.com/stackgl/glsl-tokenizer)

## License

MIT. See [LICENSE.md](http://github.com/stackgl/glsl-token-depth/blob/master/LICENSE.md) for details.
