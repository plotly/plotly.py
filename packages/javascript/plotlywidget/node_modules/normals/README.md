normals
=======
Estimates normals for surface meshes.

Installation
============
Using [npm](https://npmjs.org/):

    npm install normals
    
Example
=======
Here is how to compute the vertex and face normals for the Stanford bunny:

```js
    var bunny = require("bunny");
    bunny.vertexNormals = require("normals").vertexNormals(bunny.cells, bunny.positions[,epsilon]);
    bunny.faceNormals = require("normals").faceNormals(bunny.cells, bunny.positions[,epsilon]);
```

`require("normals").vertexNormals(cells, positions[,epsilon])`
----------------------------------------------------
This estimates the vertex normals for an oriented mesh.

* `cells` is an array of indexed vertex positions
* `positions` is an array of vertex positions

Returns: An array of length = `positions.length` of the per-vertex normals.


`require("normals").faceNormals(cells, positions[,epsilon])`
----------------------------------------------------
This estimates the face normals for an oriented mesh.

* `cells` is an array of indexed vertex positions
* `positions` is an array of vertex positions

Returns: An array of length = `cells.length` of the per-face normals.


Credits
=======
(c) 2013 Mikola Lysenko. BSD
