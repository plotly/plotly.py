# glsl-token-descope

[![experimental](http://badges.github.io/stability-badges/dist/experimental.svg)](http://github.com/badges/stability-badges)

"Descope" an array of GLSL tokens such that they can be safely inlined alongside
within another shader without causing any global variable conflicts.

Useful for modularising GLSL source files, e.g. as is done in
[glslify](http://github.com/stackgl/glslify), but should be useful in other
tools too.

Written with WebGL's GLSL syntax in mind – all the same, pull requests to
support other variants would be much appreciated :)

## Usage

[![NPM](https://nodei.co/npm/glsl-token-descope.png)](https://nodei.co/npm/glsl-token-descope/)

### `descope(tokens, [rename(name)])`

Takes an array of GLSL `tokens` produced by
[glsl-tokenizer](http://github.com/stackgl/glsl-tokenizer) and renames variables
to avoid global conflicts by modifying their "data" property in-place.

For example:

``` javascript
var tokenize  = require('glsl-tokenizer/string')
var descope   = require('glsl-token-descope')
var stringify = require('glsl-token-string')

var src = `
precision mediump float;

uniform mat4  top1;
uniform float top2;

void main() {
  float x = 1.0;
  gl_FragColor = vec4(vec3(x), top2);
}
`.trim()

var tokens = tokenize(src)

console.log(stringify(descope(tokens)))
```

Which should rename `main`, `top1` and `top2` to result in this output:

``` glsl
precision mediump float;

uniform mat4  top1_0;
uniform float top2_1;

void main_2() {
  float x = 1.0;
  gl_FragColor = vec4(vec3(x), top2_1);
}
```

Optionally, you may pass in a custom `rename` function as `descope`'s second
argument to choose how you rename your variables. For example, adding a custom
`rename` function to the previous function:

``` javascript
descope(tokens, function(name) {
  return 'a_' + name
})
```

Would result in the following shader:

``` glsl
precision mediump float;

uniform mat4  a_top1;
uniform float a_top2;

void a_main() {
  float x = 1.0;
  gl_FragColor = vec4(vec3(x), a_top2);
}
```

## See Also

* [glslify](http://github.com/stackgl/glslify)
* [glsl-token-scope](http://github.com/stackgl/glsl-token-scope)
* [glsl-token-depth](http://github.com/stackgl/glsl-token-depth)
* [glsl-token-properties](http://github.com/stackgl/glsl-token-properties)
* [glsl-token-assignments](http://github.com/stackgl/glsl-token-assignments)
* [glsl-token-string](http://github.com/stackgl/glsl-token-string)

## License

MIT. See [LICENSE.md](http://github.com/stackgl/glsl-token-descope/blob/master/LICENSE.md) for details.
