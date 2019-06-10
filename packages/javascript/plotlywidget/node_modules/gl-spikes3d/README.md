gl-spikes3d
===========
Draws axis spikes compatible with gl-axes3d.  This can be useful to illustrate selections or specific points in a point cloud

## Example

[Try it out here](https://mikolalysenko.github.io/gl-spikes)

```javascript
var shell = require("gl-now")({ clearColor: [0,0,0,0], tickRate: 5 })
var camera = require("game-shell-orbit-camera")(shell)
var mat4 = require("gl-matrix").mat4
var createAxes = require("gl-axes")
var createSpikes = require("gl-spikes")

//Bounds on function to plot
var bounds = [[-1,-1,-1], [1,1,1]]

//camera.lookAt([-15,20,-15], [0,0,0], [0, 1, 0])
camera.lookAt([2, 2, 2], [0,0,0], [0,1,0])

//State variables
var axes, spikes

shell.on("gl-init", function() {
  var gl = shell.gl
  
  axes = createAxes(gl, {
    bounds: bounds,
    tickSpacing: [0.1,0.1,0.1],
    textSize: 0.05
  })

  spikes = createSpikes(gl, {
    bounds: bounds,
    colors: [[1,0,0,1], [0,1,0,1], [0,0,1,1]],
    position: [0,0,0]
  })
})

shell.on("gl-render", function() {
  var gl = shell.gl
  gl.enable(gl.DEPTH_TEST)

  //Compute camera parameters
  var cameraParameters = {
    view: camera.view(),
    projection: mat4.perspective(
        mat4.create(),
        Math.PI/4.0,
        shell.width/shell.height,
        0.1,
        1000.0)
  }


  //Update spike position
  var t = 0.001*Date.now()
  spikes.position = [Math.cos(t), Math.sin(t), Math.cos(2*t+0.1)]

  //Draw objects
  axes.draw(cameraParameters)
  spikes.draw(cameraParameters)
})
```

## Install

```
npm install gl-spikes
```

## API

### `var spikes = require('gl-spikes')(gl, options)`
Creates a new spike object.

* `gl` is a WebGL context
* `options` is a list of optional parameters which are passed along

### Methods

#### `spikes.draw(camera)`
Draws the axis spikes using the given camera coordinates.

* `camera.model` is the model matrix for the camera
* `camera.view` is the view matrix
* `camera.projection` is the projection matrix

#### `spikes.update(options)`
Updates the parameters of the axes spikes. `options` is an object with the following properties:

* `position` the position of the spike ball in data coordinates
* `bounds` the bounds of the axes object
* `colors` an array of 3 length 4 arrays encoding the RGBA colors for the spikes along the x/y/z directions
* `enabled` an array of 3 flags which if set turns on or off the spikes
* `drawSides` an array of 3 flag which if set turns on or off the projected spikes in each data plane
* `lineWidth` an array of 3 numbers giving the thickness of the spikes for each axis

#### `spikes.dispose()`
Destroys the spike object and releases all associated resources.

## Credits
(c) 2014 Mikola Lysenko. MIT License