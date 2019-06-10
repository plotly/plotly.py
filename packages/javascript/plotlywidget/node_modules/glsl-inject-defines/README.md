# glsl-inject-defines

[![stable](http://badges.github.io/stability-badges/dist/stable.svg)](http://github.com/badges/stability-badges)

Safely inject `#define` statements into a shader source. 

If the shader contains any `#version` or `#extension` statements, the defines are added after them. 

## Example

```glsl
// Your cool shader
#version 330
#extension GL_OES_standard_derivatives : enable

void main() {
  #ifdef BLUE
    gl_FragColor = vec4(0.0, 0.0, 1.0, 1.0);
  #else
    gl_FragColor = vec4(0.0);
  #endif
}
```

You can process it at runtime, like so:

```js
var injectDefines = require('glsl-inject-defines')
var fs = require('fs')

var source = fs.readFileSync(__dirname + '/shader.glsl', 'utf8')

var transformed = injectDefines(source, {
  PI: 3.14,
  BLUE: ''
})
console.log(transformed)
```

The resulting shader:

```glsl
// Your cool shader
#version 330
#extension GL_OES_standard_derivatives : enable
#define PI 3.14
#define BLUE 

void main() {
  #ifdef BLUE
    gl_FragColor = vec4(0.0, 0.0, 1.0, 1.0);
  #else
    gl_FragColor = vec4(0.0);
  #endif
}
```

Works in the browser with browserify and [glslify](https://www.npmjs.com/package/glslify).

## Install

```sh
npm install glsl-inject-defines
```

## Usage

[![NPM](https://nodei.co/npm/glsl-inject-defines.png)](https://www.npmjs.com/package/glsl-inject-defines)

#### `newSource = injectDefines(source, defines)`

Injects the set of `defines`, an object with `<name, value>` pairs that will get turned into strings for the shader source.

Returns the transformed source, with defines injected after extension and version statements.

## License

MIT. See [LICENSE.md](http://github.com/stackgl/glsl-inject-defines/blob/master/LICENSE.md) for details.
