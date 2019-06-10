# glsl-token-scope

[![experimental](http://badges.github.io/stability-badges/dist/experimental.svg)](http://github.com/badges/stability-badges)

Infer the scope of each token in an array of GLSL tokens.

## Usage

[![NPM](https://nodei.co/npm/glsl-token-scope.png)](https://nodei.co/npm/glsl-token-scope/)

### `scope(tokens)`

Where `tokens` is an array of tokens returned from
[`glsl-tokenizer`](http://github.com/stackgl/glsl-tokenizer). Each token will
be modified in-place, and given `scope` and `stack` properties.

`token.scope` is a unique number for the token's current scope.

`token.stack` is an array containing the scopes available to the current token.

Note that you must first determine the scope depth of each token using
[`glsl-token-depth`](http://github.com/stackgl/glsl-token-depth)

``` javascript
var tokenize = require('glsl-tokenizer/string')
var depth    = require('glsl-token-depth')
var scope    = require('glsl-token-scope')
var fs       = require('fs')

var src = fs.readFileSync('shader.frag', 'utf8')
var tokens = tokenize(src)

depth(tokens)
scope(tokens)

tokens[0].scope // 0
tokens[1].scope // 0
tokens[2].scope // 1
tokens[3].scope // 1
tokens[4].scope // 0
tokens[5].scope // 2
// ...

tokens[0].stack // [0]
tokens[1].stack // [0]
tokens[2].stack // [0, 1]
tokens[3].stack // [0, 1]
tokens[4].stack // [0]
tokens[5].stack // [0, 2]
// ...
```

## See Also

* [stackgl/glsl-tokenizer](http://github.com/stackgl/glsl-tokenizer)
* [stackgl/glsl-token-depth](http://github.com/stackgl/glsl-token-depth)

## License

MIT. See [LICENSE.md](http://github.com/stackgl/glsl-token-scope/blob/master/LICENSE.md) for details.
