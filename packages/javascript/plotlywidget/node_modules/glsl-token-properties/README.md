# glsl-token-properties

[![experimental](http://badges.github.io/stability-badges/dist/experimental.svg)](http://github.com/badges/stability-badges)

Takes an array of GLSL tokens and determines whether or not they're a property
of another identifier.

## Usage

[![NPM](https://nodei.co/npm/glsl-token-properties.png)](https://nodei.co/npm/glsl-token-properties/)

### `properties(tokens)`

Takes an array of GLSL `tokens` from
[`glsl-tokenizer`](http://github.com/stackgl/glsl-tokenizer) and sets a
`property` boolean for whether or not the token is a property.

``` javascript
var tokenizer  = require('glsl-tokenizer/string')
var properties = require('glsl-token-properties')

var src = 'some.value[2];'
var tokens = tokenizer(src)

// determine which tokens are properties
properties(tokens)

tokens[0].data     // "some"
tokens[0].property // false
tokens[2].data     // "value"
tokens[2].property // true
tokens[4].data     // "2"
tokens[4].property // false
```

## See Also

* [glsl-tokenizer](http://github.com/stackgl/glsl-tokenizer)
* [glsl-token-scope](http://github.com/stackgl/glsl-token-scope)
* [glsl-token-depth](http://github.com/stackgl/glsl-token-depth)
* [glsl-token-assignments](http://github.com/stackgl/glsl-token-assignments)

## License

MIT. See [LICENSE.md](http://github.com/stackgl/glsl-token-properties/blob/master/LICENSE.md) for details.
