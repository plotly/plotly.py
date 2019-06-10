gl-error3d
=============
Draws error bars around data points

# Example

```javascript
var createScene = require('gl-plot3d')
var createScatter = require('gl-scatter3d')
var createErrorBars = require('gl-error3d')

var points = [ [0,0,0], [1,1,1], [-1, 2, -3] ]
var errors = [ 
  [[-0.5,-0.5,-0.5],[0.5,0.5,0.5]], 
  [[-0.1,-1,-2],[0,0,0]], 
  [[-0.1,-0.1,-0.1],[0.1,0.1,0.1]] 
]

var scene = createScene()

var scatter = createScatter({
  gl:           scene.gl,
  position:     points,
  size:         20,
  orthographic: true,
  lineColor:    [0,0,0],
  color:        [0.7,0.8,0.4],
  lineWidth:    1
})
scene.add(scatter)


var errorBars = createErrorBars({
  gl:       scene.gl,
  position: points,
  error:    errors,
  color:    [0.9, 0.3, 0.3]
})
scene.add(errorBars)
```

# API

## Constructor

#### `var errorBars = require('gl-error3d')(options)`
Creates a new error bar object.

* `gl` is a WebGL context
* `position` is the position of each point in the plot
* `error` is an array of error bounds represented as `[lo,hi]` for each point
* `color` a length 3 array of arrays giving the color of the error bars along each axis.
* `lineWidth` is the width of the error bar lines in pixels
* `capSize` is the size of the cap for error bars
* `clipBounds` is a box to which all error bars will be clipped

**Returns** A new error bar object

#### `errorBars.update(options)`
Updates the error bar object

#### `errorBars.dispose()`
Destroy the error bars and release all associated resources

# Credits
(c) 2014-2015 Mikola Lysenko. MIT License