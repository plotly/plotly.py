surface-nets
============
Extract a simplicial level set from an [ndarray](https://github.com/mikolalysenko/ndarray) in any dimension using naive surface nets.  This module works in both node.js and with [browserify](http://browserify.org/)!

# Example

Here is a 2D example:

```javascript
//Load modules
var surfaceNets = require("surface-nets")
var ndarray = require("ndarray")
var fill = require("ndarray-fill")

//Initialize array to a circle
var array = ndarray(new Float32Array(32*32), [32,32])
fill(array, function(i,j) {
  return Math.pow(i-16,2) + Math.pow(j-16,2)
})

//Extract 2D contour (this is all there is to it!)
var complex = surfaceNets(array, 15*15)

//Write SVG image to stdout
var svgFile = ['<svg xmlns="http://www.w3.org/2000/svg" width="320" height="320">']
complex.cells.forEach(function(cell) {
  var p0 = complex.positions[cell[0]]
  var p1 = complex.positions[cell[1]]
  svgFile.push('<line x1="', 10*p0[0], '" y1="', 10*p0[1], '" x2="', 10*p1[0], '" y2="', 10*p1[1], '" stroke="red" stroke-width="1" />')
})
complex.positions.forEach(function(p) {
  svgFile.push('<circle cx="', 10*p[0], '" cy="', 10*p[1], '" r="1" stroke="black" stroke-width="0.1" fill="black" />')
})
svgFile.push('</svg>')
console.log(svgFile.join(""))
```

And here is the output SVG:

<img src="https://mikolalysenko.github.io/surface-nets/example/2d.svg">

This module also works in 3D.  Here is an example:

```javascript
//Load modules
var surfaceNets = require("surface-nets")
var ndarray = require("ndarray")
var fill = require("ndarray-fill")
var mat4 = require("gl-matrix").mat4

//Initialize array
var array = ndarray(new Float32Array(32*32*32), [32,32,32])
fill(array, function(i,j,k) {
  return Math.pow(i-16,2) + Math.pow(j-16,2) + Math.pow(k-16,2)
})

//Generate surface! (again, just one line)
var complex = surfaceNets(array, 100)

//Render the implicit surface to stdout
console.log('<svg xmlns="http://www.w3.org/2000/svg" width="512" height="512" version="1.1">')
console.log(require("svg-3d-simplicial-complex")(
  complex.cells, 
  complex.positions, {
    view: mat4.lookAt(
      mat4.create(), 
      [32, 32, 32], 
      [16, 16, 16], 
      [0,1,0]),
    projection: mat4.perspective(mat4.create(),
      Math.PI/4.0,
      1.0,
      0.1,
      1000.0),
    viewport: [[0,0], [512,512]]
  }))
console.log("</svg>")
```

And here is the result:

<img src="https://mikolalysenko.github.io/surface-nets/example/3d.svg">

And while it is a bit trivial, you can also generate surfaces in 1D:

```javascript
var surfaceNets = require("surface-nets")
var ndarray = require("ndarray")

console.log(surfaceNets(ndarray([1, -1, 0, 5, -10])))
```

Output:

```javascript
{ positions: [ [ 0.5 ], [ 2 ], [ 3.3333333333333335 ] ],
  cells: [ [ 0 ], [ 1 ], [ 2 ] ] }
```

The code *should* work in 4D and higher dimensions, but this is not well tested and it is harder to visualize.  (Also, why would you want to bother!?!)

# Install

```
npm install surface-nets
```

# API

#### `require("surface-nets")(array[,level])`
Extracts the level set at `level` from `array` as a simplicial complex.

* `array` is an [ndarray](https://github.com/mikolalysenko/ndarray)
* `level` is an optional number which determines the level at which the levelset is evaluated (default `0`)

**Returns** An object with a pair of properties representing a simplicial complex:

* `positions` is an array encoding the positions of the vertices.  The coordinates of the positions are with respect to the indices in `array`.
* `cells` is an array encoding the cells of the simplicial complex as tuples of indices into the `position` array.

# Credits
(c) 2014 Mikola Lysenko. MIT License