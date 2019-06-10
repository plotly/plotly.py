simplify-planar-graph
=====================
Simplifies a planar graph by removing small or nearly flat corners.

# Example

```javascript
var simplify = require("simplify-planar-graph")

//Create a circle
var positions = []
var edges = []
for(var i=0; i<100; ++i) {
  var theta = i / 100 * Math.PI * 2.0
  positions.push([Math.cos(theta), Math.sin(theta)])
  edges.push([i, (i+1)%100])
}

//Simplify it
console.log(simplify(edges, positions, 0.1))
```

Output:

```javascript
{ positions:
   [ [ 0.9921147013144779, 0.12533323356430426 ],
     [ 0.8090169943749475, 0.5877852522924731 ],
     [ 0.48175367410171516, 0.8763066800438637 ],
     [ -0.30901699437494734, 0.9510565162951536 ],
     [ -0.7705132427757891, 0.6374239897486899 ],
     [ -0.9980267284282716, 0.06279051952931358 ],
     [ -0.9510565162951535, -0.30901699437494773 ],
     [ -0.5877852522924732, -0.8090169943749473 ],
     [ -0.18738131458572463, -0.9822872507286887 ],
     [ 0.535826794978996, -0.8443279255020155 ],
     [ 0.7705132427757894, -0.6374239897486896 ] ],
  edges:
   [ [ 0, 1 ],
     [ 1, 2 ],
     [ 2, 3 ],
     [ 3, 4 ],
     [ 4, 5 ],
     [ 10, 0 ],
     [ 5, 6 ],
     [ 6, 7 ],
     [ 7, 8 ],
     [ 8, 9 ],
     [ 9, 10 ] ] }
```

# Install

```
npm install simplify-planar-graph
```

# API

#### `require("simplify-planar-graph")(edges, positions, tolerance)`
Simplies a planar graph to a given tolerance

* `edges` are the edges of the graph represented by pairs of vertex indices
* `positions` is a list of vertex coordinates encoded as an array of 2D arrays
* `tolerance` controls the target aspect ratio of the corners of the mesh

**Returns** A new planar graph encoded as a JSON object with two properties:

* `edges` is an array of edges encoded as pairs of indices
* `positions` is an array of positions for the simplicial complex

**Note** The current implementation does not detect the removal of features which cross existing line segments.  Picking a high tolerance value may result in destroying the planarity of the resulting graph.  Eventually if it becomes a priority I may go back and implement code to detect and handle these cases.

# Credits
(c) 2014 Mikola Lysenko. MIT License