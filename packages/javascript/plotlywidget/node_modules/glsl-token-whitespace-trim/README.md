# glsl-token-whitespace-trim

[![stable](http://badges.github.io/stability-badges/dist/stable.svg)](http://github.com/badges/stability-badges)

Trim the whitespace within an array of GLSL tokens provided by [glsl-tokenizer](https://github.com/stackgl/glsl-tokenizer). Useful for minimising shader source size, especially after heavy processing steps such as seen in [glslify](http://github.com/stackgl/glslify) or as part of a GLSL minifier.

## Usage

[![NPM](https://nodei.co/npm/glsl-token-whitespace-trim.png)](https://www.npmjs.com/package/glsl-token-whitespace-trim)

### `trim(tokens, [all])`

Trims the whitespace in an array of GLSL `tokens`. By default, this will trim repeated to newlines such that no more than two newlines will appear in a row.

If you're more concerned about size than aesthetics, you can pass `true` as the second argument to remove *all* extraneous whitespace (more or less).

``` javascript
const tokenize = require('glsl-tokenizer')
const string = require('glsl-token-string')
const trim = require('glsl-token-whitespace-trim')
const fs = require('fs')

const src = fs.readFileSync('shader.glsl', 'utf8')
const tokens = tokenize(src)

trim(tokens, true)

const trimmed = string(tokens)
```

## License

MIT, see [LICENSE.md](http://github.com/hughsk/glsl-token-whitespace-trim/blob/master/LICENSE.md) for details.
