gl-line3d
============
A 3D WebGL line plot

# Example

[Try it out in your browser](http://gl-vis.github.io/gl-line3d)

```javascript
var createScene = require('gl-plot3d')
var createLine  = require('gl-line3d')

//Create the scene
var scene = createScene()

//Create a helix
var polyline = []
for(var i=0; i<100; ++i) {
  var theta = (i / 100.0) * Math.PI
  polyline.push([
      Math.cos(3*theta),
      Math.sin(3*theta),
      (i/50) - 1.0
    ])
}

//Create the line plot
var lines = createLines({
  gl:       scene.gl,
  position: polyline,
  color:    [1,0,0]
})

//Add the lines to the scene
scene.add(lines)
```

# Install

```
npm install gl-line3d
```

# Basic interface

## Constructor

#### `var lines = require('gl-line3d')(options)
Creates a new line plot

* `options.gl` A WebGL context
* `options.position` An array of position values for the points on the curve
* `options.color` An array of color values (or a singular color) for the curve
* `options.pickId` The selection ID for the line plot
* `options.lineWidth` The width of the line
* `options.dashes` An array of dash patterns representing the dash pattern.  For example, `[0.5,0.5,0.5]`
* `options.dashScale` The number of times to repeat the dash pattern
* `options.opacity` The opacity of the lines

## Updating

#### `lines.update(options)`
Updates the plot.  `options` has the same properties as in the constructor

## Properties

#### `lines.lineWidth`
The width of the lines

# Included example in the `example` directory

To run it, follow these steps:

```
git clone https://github.com/gl-vis/gl-line3d.git
cd gl-line3d
mkdir dist
browserify lines.js -o dist/bundle.js
browserify example/simple.js -o dist/simple_example_bundle.js
```
then open `simple.html` in the `example` directory.

# Credits
(c) 2014 Mikola Lysenko. MIT License
