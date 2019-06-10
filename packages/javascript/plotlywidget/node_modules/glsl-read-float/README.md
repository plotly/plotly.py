glsl-read-float
===============
Workaround for reading floating point values back from the GPU using GLSL.

## Example

```javascript
var triangle     = require('a-big-triangle')
var fit          = require('canvas-fit')
var getContext   = require('gl-context')
var glslify      = require('glslify')
var unpackFloat  = require("glsl-read-float")

var canvas     = document.body.appendChild(document.createElement('canvas'))
var gl         = getContext(canvas, render)

window.addEventListener('resize', fit(canvas), false)

var shader = glslify({
  vert: "\
attribute vec2 position;\
void main() {\
  gl_Position = vec4(position, 0, 1);\
}",
  frag: "\
#pragma glslify: packFloat = require(glsl-read-float)\n\
uniform highp float f;\
void main() {\
  gl_FragColor = packFloat(f);\
}",
  inline: true
})(gl)

function render() {
  var num = Math.random()

  //Draw shader
  shader.bind()
  shader.uniforms.f = num
  triangle(gl)

  //Read back the float
  var buffer = new Uint8Array(4)
  gl.readPixels(0, 0, 1, 1, gl.RGBA, gl.UNSIGNED_BYTE, buffer)
  var unpacked = unpackFloat(buffer[0], buffer[1], buffer[2], buffer[3])

  //Log output to console
  console.log("expected:", num, "got:", unpacked)
}
```

## Install

```
npm install glsl-read-float
```

## API

### GLSL

```glsl
#pragma glslify: packFloat = require(glsl-read-float)
```

#### `vec4 packed = packFloat(float f)`
Packs a floating point number into an 8bit RGBA color vector, which can be written to the display using `gl_FragColor`, for example.

* `f` is a `float` number

**Returns** A packed `vec4` encoding the value of `f`

### JavaScript

```javascript
var unpackFloat = require("glsl-read-float")
```

#### `var f = unpackFloat(x, y, z, w)`
Unpacks a packed `vec4` into a single floating point value.

* `x` is the first component of the packed float
* `y` is the second component of the packed float
* `z` is the third component of the packed float
* `w` is the fourth component of the packed float

**Returns** A number which is the unpacked value of the floating point input.

**Note** This module doesn't handle denormals or floats larger than `Math.pow(2, 127)`

## Credits

Originally based on a routine by @ultraist. You can find his blog here: http://ultraist.hatenablog.com/

Newer version rewritten by Mikola Lysenko.  MIT License (c) 2014