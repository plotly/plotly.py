gl-cone3d
=====================
Visualization module for vector fields.

# Example

```javascript
var createScene    = require('gl-plot3d')
var createConePlot = require('gl-cone3d')
var createMesh     = createConePlot.createConeMesh

var wind           = require('dataset-wind')

var scene = createScene()

var bounds = [];

var conePlot = createConePlot({
    positions: wind.positions,
    vectors: wind.vectors,
    coneSize: 4,
    colormap: 'portland'
}, bounds)

var mesh = createMesh(gl, conePlot)

scene.add(mesh)
```

[Try out the example in your browser](http://gl-vis.github.io/gl-cone3d/)

# Install

```
npm i gl-cone3d
```

# Basic interface

## Constructor

#### `var conePlot = require('gl-cone3d')(params, bounds)`
Creates a cone plot of a vector field.

* `params` is an object that has the following properties:

    + `positions` *(Required)* An array of positions determining the location of the cones, encoded as arrays
    + `vectors` *(Required)* An array of vectors for the vector field, encoded as arrays
    + `meshgrid` Meshgrid for the vectors data array. Given as three arrays of numbers [xcoords, ycoords, zcoords]. E.g. meshgrid: [[1,2,3], [-1,0,1], [0,10,20,30,40,50]].
    + `coneSize` Size of the cones, scaled so that the reference cone size for the maximum vector magnitude is 1
    + `absoluteConeSize` Size of the cones, scaled so that the reference cone size for vector magnitude 1 is one grid unit.
    + `coneOffset` The position of the cone with regard to the cone location. Ranges from 0 to 1 where 0 puts the center of the cone base at the cone location, and 1 puts the tip at the cone location.
    + `colormap` Colormap for the cone plot.

**Returns** A cone plot object that can be passed to gl-mesh3d.

# Credits
(c) 2013-2017 Mikola Lysenko, Ilmari Heikkinen. MIT License
