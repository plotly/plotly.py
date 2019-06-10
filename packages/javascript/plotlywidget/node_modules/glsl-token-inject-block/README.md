# glsl-token-inject-block

[![unstable](http://badges.github.io/stability-badges/dist/unstable.svg)](http://github.com/badges/stability-badges)

Injects a "block" of GLSL tokens into a shader, after any `#version`, `#extension` and `precision` statements. This will pad the new tokens with the necessary amount of newlines (but no more).

This module ignores token `line`, `column` and `position`.

## Example

Your source:

```js
var tokenizer = require('glsl-tokenizer')
var inject = require('glsl-token-inject-block')
var stringify = require('glsl-token-string')

var tokens = tokenizer(shaderInput)
var newToken = { 
  type: 'preprocessor', 
  data: '#define FOOBAR' 
}

var source = stringify(inject(tokens, newToken))
console.log(source)
```

The following shader input:

```glsl
// some comment
#version 300 es
#extension SOME_EXTENSION : enable

void main() {}
```

Results in the following injected define:

```glsl
// some comment
#version 300 es
#extension SOME_EXTENSION : enable
#define FOOBAR

void main() {}
```

## Usage

[![NPM](https://nodei.co/npm/glsl-token-inject-block.png)](https://www.npmjs.com/package/glsl-token-inject-block)

#### `tokens = inject(tokens, newTokens)`

For the given shader source (`tokens`), injects `newTokens` into them, assuming the new tokens are a "block" of code that should be placed on its own line. 

`newTokens` can be a single token object, or an array of token objects.

Modifies `tokens` in place and returns it.

## License

MIT, see [LICENSE.md](http://github.com/Jam3/glsl-token-inject-block/blob/master/LICENSE.md) for details.
