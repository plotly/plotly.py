gl-state
========
Preserves WebGL state variables using a stack. This gives similar capabilities to OpenGL 1.0's pushAttrib/popAttrib, only with finer control over the variables which are stored. These methods are useful when writing simple hierarchical rendering functions, or for debugging operations in the middle of the pipeline.

# Example

```javascript
var shell = require("gl-now")()
var createStateStack = require("gl-state")

var stack

shell.on("gl-init", function() {

  //Create stack for saving state
  stack = createStateStack(shell.gl)

  //Push variables onto stack here
  stack.push()
  //... clobber stuff here ...
  shell.gl.clearColor(1, 0, 1, 0);

  //Context states can also be nested
  stack.push()
  // ... clobbber more stuff
  shell.gl.clearColor(0, 1, 0, 1)
  stack.pop()

  //Color back to previous value
  console.log(shell.gl.getParameter(shell.gl.COLOR_CLEAR_VALUE))

  //Restore state
  stack.pop()

  //Now state is completely restored
})
```

# Install

```
npm install gl-state
```

# API

## Constructor

### `var stack = require("gl-state")(gl[, variables])`
Constructs a new state stack object that saves some subset of the global WebGL state for the context `gl`

* `gl` is a WebGL context
* `variables` is an optional list of state variables as defined in the specification of [`gl.getParameter`](http://www.khronos.org/registry/webgl/specs/latest/1.0/#5.14.3). If not specified, the entire state will be saved

**Returns** A new WebGL state stack object

**Note on performance** Modifying the WebGL state is expensive, especially if you update more of it. In general, you should avoid creating too many full context state changes. To do this, you should only specify a list of variables which you plan on actually modifying in the course of your code.  For example, to save only state variables associated with the depth buffer, you could do the following:


```javascript
var depthStack = createStack(gl, [
  gl.DEPTH_CLEAR_VALUE,
  gl.DEPTH_RANGE,
  gl.DEPTH_TEST,
  gl.DEPTH_WRITEMASK
])
```

In this way you don't have to save and update more of the WebGL context than is necessary.

**Note on textures** Also the texture unit state is handled in a slightly different way. To specify saving the texture state, you can do:

```javascript
var textureStack = createStack(gl, [
  gl.TEXTURE,
  gl.ACTIVE_TEXTURE
])
```

This will save the texture state associated to all currently active texture units.

**Note on support** Currently support for saving the state of shaders, uniforms and attributes is somewhat limited. If you are using these features and want to preserve the state of the rendering context you must do this yourself.

## Methods
The following methods are exposed by the stack object:

### `stack.push()`
Saves the current state of the WebGL context onto the stack

### `stack.pop()`
Restores the last pushed state from the stack.

# Credits
(c) 2014 Mikola Lysenko. MIT License