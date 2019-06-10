vectorize-text
==============
Convert a string of text into a vectorized geometric representation. Works in both node.js and [browserify](http://browserify.org/).

# Example

This module is capable of outputting geometry in several formats.

### Planar graphs

The default (and fastest) output from the module is a planar graph:

```javascript
var vectorizeText = require("vectorize-text")

var graph = vectorizeText("Hello world! 你好", {
  width: 500,
  textBaseline: "hanging"
})

var svg = ['<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"  width="500"  height="80" >']
graph.edges.forEach(function(e) {
  var p0 = graph.positions[e[0]]
  var p1 = graph.positions[e[1]]
  svg.push('<line x1="' + p0[0] + '" y1="' + p0[1] +
    '" x2="' + p1[0] + '" y2="' + p1[1] +
    '" stroke-width="1" stroke="black" />')
})
svg.push("</svg>")

console.log(svg.join(""))
```

Output:

<img src="https://mikolalysenko.github.io/vectorize-text/example/hello-graph.svg">

### Polygons

You can also configure the module to emit polygons instead:

```javascript
var vectorizeText = require("vectorize-text")

var polygons = vectorizeText("Hello world! 你好", {
  polygons: true,
  width: 500,
  textBaseline: "hanging"
})

var svg = []
svg.push('<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"  width="500"  height="80" >')
polygons.forEach(function(loops) {
  svg.push('<path d="')
  loops.forEach(function(loop) {
    var start = loop[0]
    svg.push('M ' + start[0] + ' ' + start[1])
    for(var i=1; i<loop.length; ++i) {
      var p = loop[i]
      svg.push('L ' + p[0] + ' ' + p[1])
    }
    svg.push('L ' + start[0] + ' ' + start[1])
  })
  svg.push('" fill-rule="even-odd" stroke-width="1" fill="red"></path>')
})
svg.push('</svg>')

console.log(svg)
```

Output:

<img src="https://mikolalysenko.github.io/vectorize-text/example/hello-polygon.svg">


### Triangulations

Finally, the module can output a triangulation (which is compatible with WebGL for example):

```javascript
var vectorizeText = require("vectorize-text")

var complex = vectorizeText("Hello world! 你好", {
  triangles: true,
  width: 500,
  textBaseline: "hanging"
})

var svg = ['<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"  width="500"  height="80" >']
complex.cells.forEach(function(c) {
  for(var j=0; j<3; ++j) {
    var p0 = complex.positions[c[j]]
    var p1 = complex.positions[c[(j+1)%3]]
    svg.push('<line x1="' + p0[0] + '" y1="' + p0[1] +
      '" x2="' + p1[0] + '" y2="' + p1[1] +
      '" stroke-width="1" stroke="black" />')
  }
})
svg.push("</svg>")

console.log(svg)
```

Output:

<img src="https://mikolalysenko.github.io/vectorize-text/example/hello-triangles.svg">

# Install

```sh
npm install vectorize-text
```

# API

#### `require("vectorize-text")(string[,options])`
Renders a string to a 2D cell complex

* `string` is a string of text (single line)
* `options` is an optional object of parameters

    + `options.font` is the font family to use (default: `"normal"`)
    + `options.fontStyle` if set, determines the [font-style](https://developer.mozilla.org/en-US/docs/Web/CSS/font-style)
    + `options.fontVariant` if set, determines the [font-variant](https://developer.mozilla.org/en-US/docs/Web/CSS/font-variant)
    + `options.fontWeight` if set, determines the [font-weight](https://developer.mozilla.org/en/docs/Web/CSS/font-weight)
    + `options.size` is the [font-size](https://developer.mozilla.org/en-US/docs/Web/CSS/font-size) used for the rasterization step (determines level of detail of the mesh)
    + `options.textBaseline` determines the baseline, same semantics as the canvas [textBaseline](https://developer.mozilla.org/en-US/docs/Drawing_text_using_a_canvas#Attributes) property.  Default: `"alphabetic"`
    + `options.textAlign` determines the alignment for the text, same semantics as canvas [textAlign](https://developer.mozilla.org/en-US/docs/Drawing_text_using_a_canvas#Attributes).  Default: `"start"`
    + `options.lineHeight` determines the height of a line.  Default: `1.0`
    + `options.width` determines the width of the text, overrides `lineHeight` if specified
    + `options.height` determines the height of the text, overrides `lineHeight` if specified
    + `options.triangles` if set, then output a triangulation
    + `options.polygons` if set, output a list of polygons
    + `options.orientation` determines the orientation of any output triangles/polygon curves.  Must be either `"cw"` for clockwise or `"ccw"` for counter clockwise.  Default is `"cw"`.
    + `options.canvas` an optional canvas element
    + `options.context` an optional canvas 2D context
    + `options.styletags.breaklines` if set, break-line tags i.e. < br > could be used in the input to enter new lines.
    + `options.styletags.bolds` if set, parts of the input i.e. between < b > and < /b > would be presented <b>bold</b>.
    + `options.styletags.italics` if set, parts of the input i.e. between < i > and < /i > would be presented <i>italic</i>.
    + `options.styletags.superscripts` if set, parts of the input i.e. between < sup > and < /sup > would be presented in as superscript. Multiple superscipts are also allowded. For example Line 0<sup>Line 1<sup>Line 2</sup></sup>.
    + `options.styletags.subscripts` if set, parts of the input i.e. between < sub > and < /sub > would be presented in as subscript. Multiple subscipts are also allowded. For example: Line 0<sub>Line 1<sub>Line 2</sub></sub>. Note: it is also possible to combine sub and superscripts: A<sub>B<sup>C</sup></sub>.

**Returns** The returned value depends on the type of geometry

* *Planar graph*: This is the fastest output format. A JSON object encoding the embedding of an oriented planar graph, with the following properties:

    + `edges` are the edges of the graph
    + `positions` are the positions

* *Polygon list*: A list of complex polygons encoded as arrays of positions.  This format is most suitable for SVG and GeoJSON output

* *Triangulation*: This format may be most suitable for WebGL/rendering applications. A 2D oriented simplicial complex encoded as a list of cells and positions, represented by a JSON object with two properties

    + `cells` are the faces of the triangulation, encoded as triples of indices into the vertex array
    + `positions` are the positions of the vertices in the triangulation

**Note** In node.js, this library requires Cairo. For more information on how to set this up, look at the documentation for the [canvas module](https://www.npmjs.org/package/canvas).

# Credits
(c) 2014 Mikola Lysenko. MIT License
