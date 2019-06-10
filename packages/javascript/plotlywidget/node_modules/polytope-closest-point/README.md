polytope-closest-point
======================
Computes the closest point in a convex polytope to a given point.

Install
=======
Using npm, type the following command into your shell:

    npm install polytope-closest-point

Usage
=====
Here is an example of how to find the closest point to a triangle in a mesh:

    var mesh = require("bunny");
    var result = new Array(3);
    var sqr_distance = require("polytope-closest-point")(
                          mesh.cells[0],
                          mesh.positions,
                          [0,0,0],
                          result);

Which computes the closest point in the first facet of the mesh to the point `[0,0,0]`, storing the resulting point in `result` and the squared distance in `sqr_distance`.

For more examples, see test/simple.js.

### `require("polytope-closest-point")(cell, positions, x[, result])`

Computes the closest point in a polytope to `x`, storing the result in `result`.

* `cell` is a list of indices into a positions representing the vertices of the polytope.
* `positions` is an array of tuples representing the vertices of the polytope
* `x` is the point we are querying against
* `result` (optional) is the array to store the closest point in.

Returns a float representing the squared Euclidean distance from x to the polytope.  If no such point can be found, it returns Number.NaN

Notes:  For polytopes with fewer than 4 vertices, the code uses hand optimized routines derived from WildMagick.  For higher dimensions, it falls back to a general purpose quadratic programming solver that is ported from somewhat slower R/FORTRAN codes.  If you are planning on using this code to do distance queries on meshed surfaces, it is recommend you triangulate all your polygons first.

Credits
=======
Triangle/tetrahedra closest point code derived from WildMagick (c) David Eberly 1998-2012.

Other dimensions, (c) 2013 Mikola Lysenko

BOOST License.
