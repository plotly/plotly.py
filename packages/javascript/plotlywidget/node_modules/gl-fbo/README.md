gl-fbo
======
WebGL framebuffer object wrapper

## Example

[Try this in your browser if you have WebGL](http://stackgl.github.io/gl-fbo/)

```javascript
var shell = require("gl-now")()
var createFBO = require("gl-fbo")
var glslify = require("glslify")
var ndarray = require("ndarray")
var fill = require("ndarray-fill")
var fillScreen = require("a-big-triangle")

var createUpdateShader = glslify({
  vertex: "\
    attribute vec2 position;\
    varying vec2 uv;\
    void main() {\
      gl_Position = vec4(position,0.0,1.0);\
      uv = 0.5 * (position+1.0);\
    }",
  fragment: "\
    precision mediump float;\
    uniform sampler2D buffer;\
    uniform vec2 dims;\
    varying vec2 uv;\
    void main() {\
      float n = 0.0;\
      for(int dx=-1; dx<=1; ++dx)\
      for(int dy=-1; dy<=1; ++dy) {\
        n += texture2D(buffer, uv+vec2(dx,dy)/dims).r;\
      }\
      float s = texture2D(buffer, uv).r;\
      if(n > 3.0+s || n < 3.0) {\
        gl_FragColor = vec4(0,0,0,1);\
      } else {\
        gl_FragColor = vec4(1,1,1,1);\
      }\
    }",
  inline: true
})

var createDrawShader = glslify({
  vertex: "\
    attribute vec2 position;\
    varying vec2 uv;\
    void main() {\
      gl_Position = vec4(position,0.0,1.0);\
      uv = 0.5 * (position+1.0);\
    }",
  fragment: "\
    precision mediump float;\
    uniform sampler2D buffer;\
    varying vec2 uv;\
    void main() {\
      gl_FragColor = texture2D(buffer, uv);\
    }",
  inline: true
})

var state, updateShader, drawShader, current = 0

shell.on("gl-init", function() {
  var gl = shell.gl
  
  //Turn off depth test
  gl.disable(gl.DEPTH_TEST)

  //Initialize shaders
  updateShader = createUpdateShader(gl)
  drawShader = createDrawShader(gl)

  //Allocate buffers
  state = [ createFBO(gl, [512, 512]), createFBO(gl, [512, 512]) ]
  
  //Initialize state buffer
  var initial_conditions = ndarray(new Uint8Array(512*512*4), [512, 512, 4])
  fill(initial_conditions, function(x,y,c) {
    if(c === 3) {
      return 255
    }
    return Math.random() > 0.9 ? 255 : 0
  })
  state[0].color[0].setPixels(initial_conditions)
  
  //Set up vertex pointers
  drawShader.attributes.position.location = updateShader.attributes.position.location = 0
})

shell.on("tick", function() {
  var gl = shell.gl
  var prevState = state[current]
  var curState = state[current ^= 1]

  //Switch to state fbo
  curState.bind()
  
  //Run update shader
  updateShader.bind()
  updateShader.uniforms.buffer = prevState.color[0].bind()
  updateShader.uniforms.dims = prevState.shape
  fillScreen(gl)
})

shell.on("gl-render", function(t) {
  var gl = shell.gl
  
  //Render contents of buffer to screen
  drawShader.bind()
  drawShader.uniforms.buffer = state[current].color[0].bind()
  fillScreen(gl)
})
```

Result:

<img src="https://raw.github.com/stackgl/gl-fbo/master/screenshot.png">


## Install

Install using npm:

    npm install gl-fbo

# API

### `var createFBO = require("gl-fbo")`

## Constructor
There is currently only one default way to create a Framebuffer object.  You can construct a framebuffer using the following syntax:

### `var fbo = createFBO(gl, shape[, options])`
Creates a wrapped framebuffer object

* `gl` is a handle to a WebGL context
* `shape` is a length 2 array encoding the `[width, height]` of the frame buffer
* `options` is an object containing the following optional properties:

    + `options.preferFloat` Upgrade to floating point if available, otherwise fallback to 8bit. (default `false`)
    + `options.float` Use floating point textures (default `false`)
    + `options.color`  The number of color buffers to create (default `1`)
    + `options.depth` If fbo has a depth buffer (default: `true`)
    + `options.stencil` If fbo has a stencil buffer (default: `false`)

## Methods

### `fbo.bind()`
Binds the framebuffer object to the display.  To rebind the original drawing buffer, you can just call WebGL directly:

```javascript
//Bind the drawing buffer
gl.bindFramebuffer(gl.FRAMEBUFFER, null)
```

### `fbo.dispose()`
Destroys the framebuffer object and releases all associated resources

## Properties


### `fbo.shape`
Returns the shape of the frame buffer object.  Writing to this property resizes the framebuffer.  For example,

```javascript
fbo.shape = [ newWidth, newHeight ]
```

### `fbo.gl`
A reference to the WebGL context

### `fbo.handle`
A handle to the underlying Framebuffer object.

### `fbo.color`
An array containing [`gl-texture2d`](https://github.com/stackgl/gl-texture2d) objects representing the buffers.  

### `fbo.depth`
The depth/stencil component of the FBO.  Stored as a [`gl-texture2d`](https://github.com/stackgl/gl-texture2d).  If not present, is `null`.

Credits
=======
(c) 2013-2014 Mikola Lysenko. MIT License