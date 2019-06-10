planar-graph-to-polyline
========================
Converts a planar graph to a collection of nested polylines (as would be consumed in a GeoJSON/TopoJSON file for example).

# Example

```javascript
var graphToPolygons = require("planar-graph-to-polyline")

var edges = []
var positions = []

for(var i=1; i<=3; ++i) {
  var v0 = positions.length
  for(var j=0; j<10; ++j) {
    var theta = 2.0 * Math.PI * j / 10
    positions.push([ i * Math.cos(theta), i * Math.sin(theta) ])
    edges.push([ v0+j, v0+((j+1)%10) ])
  }
}

console.log(graphToPolygons(edges, positions))
```

Output:

```javascript
[ [ [ 20, 29, 28, 27, 26, 25, 24, 23, 22, 21 ],
    [ 11, 12, 13, 14, 15, 16, 17, 18, 19, 10 ] ],
  [ [ 0, 9, 8, 7, 6, 5, 4, 3, 2, 1 ] ] ]
```

# Install

```
npm install planar-graph-to-polyline
```

# API

#### `require("planar-graph-to-polyline")(edges, positions)`
Converts a planar graph into a collection of nested polylines

* `edges` are the edges of the graph
* `positions` are the locations of the vertices in the plane

**Returns** A list of loops encoding the regions bounded by the graph

# Credits
(c) 2014 Mikola Lysenko. MIT License