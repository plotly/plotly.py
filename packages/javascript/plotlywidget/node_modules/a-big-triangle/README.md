a-big-triangle
==============
Draws a big triangle that covers the entire viewport. Useful for GPGPU or when applying fullscreen postprocessing effects.

If you're wondering *why* a big triangle and not a big square made from two smaller triangles, there are potentially significant [performance advantages](http://michaldrobot.com/2014/04/01/gcn-execution-patterns-in-full-screen-passes/) in taking the former approach.

## Example

```javascript
var shell = require("gl-now")()
var drawTriangle = require("a-big-triangle")
var createShader = require("gl-shader")

var shader

shell.on("gl-init", function() {
  shader = createShader(shell.gl, 
  "precision mediump float;\
  attribute vec2 position;\
  varying vec2 uv;\
  void main() {\
    uv = position.xy;\
    gl_Position = vec4(position.xy, 0.0, 1.0);\
  }",
  "precision mediump float;\
  varying vec2 uv;\
  void main() {\
    gl_FragColor = vec4(uv, 0, 1);\
  }")
})

shell.on("gl-render", function() {
  shader.bind()
  drawTriangle(shell.gl)
})
```

[Check it out in your browser](http://mikolalysenko.github.io/a-big-triangle/)

## Install

```sh
npm install a-big-triangle
```

## API

### `require("a-big-triangle")(gl)`
Draws a fullscreen triangle.

* `gl` is a WebGL context

## Credits
(c) 2013
