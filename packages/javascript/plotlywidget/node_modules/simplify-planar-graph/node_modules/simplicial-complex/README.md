simplicial-complex
==================

This CommonJS module implements basic topological operations and indexing for [abstract simplicial complexes](http://en.wikipedia.org/wiki/Abstract_simplicial_complex) (ie graphs, triangular and tetrahedral meshes, etc.) in JavaScript.

What is an (abstract) simplicial complex?
-----------------------------------------

An [abstract simplicial complex](http://en.wikipedia.org/wiki/Abstract_simplicial_complex) is a higher dimensional generalization of the concept of a [(directed) graph](http://en.wikipedia.org/wiki/Graph_\(mathematics\)), and it plays a fundamental role in computational geometry.  Recall that a graph is represented by a pair of sets called:

* [vertices](http://en.wikipedia.org/wiki/Vertex_\(graph_theory\)) : A finite collection of labels/indices.
* [edges](http://en.wikipedia.org/wiki/Edge_\(graph_theory\)) : A finite collection of ordered pairs of vertices.

In an oriented abstract simplicial complex, the edges of a graph are replaced by higher dimensional structures called *cells* or *simplices*, which are represented by ordered tuples of vertices.  And so we can represent a simplicial complex using the following data:

* [vertices](http://en.wikipedia.org/wiki/Vertex_\(graph_theory\)) : A finite collection of labels/indices. (Same as before)
* [cells](http://en.wikipedia.org/wiki/Simplex) : A finite collection of ordered [tuples](http://en.wikipedia.org/wiki/Tuple) of vertices.

We say that the dimension of each cell is one less than the length of its tuple.  For example, here are some common names for various n-dimensional cells:

* -1 - cells: The empty cell
* 0 - cells: Vertices
* 1 - cells: Edges
* 2 - cells: Faces/triangles
* 3 - cells: Volumes/tetrahedra/solids
*  ...
* n-cells: n-simplices/facets

You probably already know of many examples of simplicial complexes.  Triangular meshes (as commonly used in computer graphics) are just 2d simplicial complexes; as are [Delaunay triangulations](http://en.wikipedia.org/wiki/Delaunay_triangulation).  A more restricted example of a simplicial complex is the notion of a [hypergraph](http://en.wikipedia.org/wiki/Hypergraph), which is basically what you get when you forget the ordering of each cell.

How does this library work?
---------------------------

Recall that for graphs, there are two basic ways we can represent them:

* [Adjacency Lists](http://en.wikipedia.org/wiki/Adjacency_list): A list of edges
* [Adjacency Matrices](http://en.wikipedia.org/wiki/Adjacency_matrix): A table of all edge-vertex incidences

The first form is better for sparse graphs, while the latter may be more efficient if the graph is dense.  These techniques directly generalize to simplicial complexes as well, and suggest two basic strategies:

* **Adjacency List**: A flat list of cells
* **Adjacency Tensor**: As a (n+1)^d dimensional tensor, where the each entry represents a cell

The first approach generalizes the [adjacency list](http://en.wikipedia.org/wiki/Adjacency_list) storage format for a graph, while the second form generalizes the [adjacency matrix](http://en.wikipedia.org/wiki/Adjacency_matrix).  In the first case, the storage scales linearly as O(v + d * c), while in the later case the storage scales as O(v^d).  When the total number of cells is very large and d is very small, adjacency matrix representations may be acceptable.  On the other hand, for large values of d adjacency lists scale far better.  As a result, we categorically adopt the first form as our representation.

In an adjacency list, it is trivial to test if a lower dimensional cell is incident to a higher dimensional.  However, if executed naively the reverse operation can be very inefficient.  (For example, finding all of the edges incident to a particular vertex would take O(number of edges) time if no preprocessing were used.)  To avoid having to do this, we introduce the concept of a *topological index*.  A topological index is basically a table that records the collection of all cells incident to a particular cell.  Building these tables can be done in linear time, and once complete they can answer any topological query in O(1).  To use these tools, please look at the `incidence` and `dual` functions.

Usage
=====

First, you need to install the library using [npm](https://npmjs.org/):

    npm install simplical-complex
    
And then in your scripts, you can just require it like usual:

```javascript
var top = require("simplicial-complex")
```

`simplicial-complex` represents cell complexes as arrays of arrays of vertex indices.  For example, here is a triangular mesh:

```javascript
var tris = [
    [0,1,2],
    [1,2,3],
    [2,3,4]
  ]
```

And here is how you would compute its edges:

```javascript
var edges = top.unique(top.skeleton(tris, 1))

//Result:
//  edges = [ [0,1],
//            [0,2],
//            [1,2],
//            [1,3],
//            [2,3],
//            [2,4],
//            [3,4] ]
```

The functionality in this library can be broadly grouped into the following categories:

Structural
----------

### `dimension(cells)`
**Returns:** The dimension of the cell complex.

**Time complexity:** `O(cells.length)`

### `countVertices(cells)`
**Returns:** The number of vertices in the cell complex

**Time complexity:**  `O(cells.length * dimension(cells))`

### `cloneCells(cells)`
Makes a copy of a cell complex

* `cells` is an array of cells

**Returns:** A deep copy of the cell complex

**Time complexity:** `O(cells.length * dimension(cells))`


### `compareCells(a, b)`
Ranks a pair of cells relative to one another up to permutation.

* `a` is a cell
* `b` is a cell

**Returns** a signed integer representing the relative rank:
* < 0 : `a` comes before `b`
* = 0 : `a = b` up to permutation
* > 0 : `b` comes before `a`

**Time complexity:** `O( a.length * log(a.length) )`

### `normalize(cells[, attr])`
Canonicalizes a cell complex so that it is possible to compute `findCell` queries.  Note that this function is done **in place**.  `cells` will be mutated.  If this is not acceptable, you should make a copy first using `cloneCells`.

* `cells` is a complex.
* `attr` is an optional array of per-cell properties which is permuted alongside `cells`

**Returns:** `cells`

**Time complexity:** `O(dimension(cells) * cells.length * log(cells.length) )`

### `unique(cells)`
Removes all duplicate cells from the complex.  Note that this is done **in place**.  `cells` will be mutated.  If this is not acceptable, make a copy of `cells` first.

* `cells` is a `normalize`d complex

**Returns:** `cells`

**Time complexity:** `O(cells.length)`

### `findCell(cells, c)`
Finds a lower bound on the first index of cell `c` in a `normalize`d array of cells.

* `cells` is a `normalize`'d array of cells
* `c` is a cell represented by an array of vertex indices

**Returns:** The index of `c` in the array if it exists, otherwise -1

**Time complexity:** `O(d * log(d) * log(cells.length))`, where `d = max(dimension(cells), c.length)`

Topological
-----------

### `explode(cells)`
Enumerates all cells in the complex, with duplicates

* `cells` is an array of cells

**Returns:** A normalized list of all cells in the complex

**Time complexity:** `O(2^dimension(cells) * dimension(cells) * cells.length * log(cells.length))`

### `skeleton(cells, n)`
Enumerates all n cells in the complex, with duplicates

* `cells` is an array of cells
* `n` is the dimension of the cycles to compute

**Returns:**  A normalized list of all n-cells

**Time complexity:** `O(dimension(cells)^n * cells.length * log(cells.length))`

### `boundary(cells)`
Enumerates all boundary cells of the cell complex

* `cells` is an array of cells

**Returns:** A normalized list of cells

**Time complexity:** `O(dimension(cells) * cells.length * log(cells.length))`

### `incidence(from_cells, to_cells)`
Builds an index for [neighborhood queries](http://en.wikipedia.org/wiki/Polygon_mesh#Summary_of_mesh_representation) (aka a sparse incidence matrix).  This allows you to quickly find the cells in `to_cells` which are incident to cells in `from_cells`.

* `from_cells` a `normalize`d array of cells
* `to_cells` a list of cells which we are going to query against

**Returns:** An array with the same length as `from_cells`, the `i`th entry of which is an array of indices into `to_cells` which are incident to `from_cells[i]`.

**Time complexity:** `O(from_cells.length + d * 2^d * log(from_cells.length) * to_cells.length)`, where `d = max(dimension(from_cells), dimension(to_cells))`.

### `dual(cells[, vertex_count])`
Computes the [dual](http://en.wikipedia.org/wiki/Hypergraph#Incidence_matrix) of the complex.  An important application of this is that it gives a more optimized way to build an index for vertices for cell complexes with sequentially enumerated vertices.  For example,

```javascript
dual(cells)
```

Is equivalent to finding the incidence relation for all vertices, or in other words doing:

```javascript
incidence(unique(skeleton(cells, 0)), cells)
```

For the arguments:

* `cells` is a cell complex
* `vertex_count` is an optional parameter giving the number of vertices in the cell complex.  If not specified, then it calls `top.incidence(top.unique(top.skeleton(cells, 0)), cells)`

**Returns:** An array of elements with the same length as `vertex_count` (if specified) or `unique(skeleton(cells,0))` otherwise giving the [vertex stars of the mesh](http://en.wikipedia.org/wiki/Star_(graph_theory\)) as indexed arrays of cells.

**Time complexity:** `O(dimension(cells) * cells.length)`

### `connectedComponents(cells[, vertex_count])`
Splits a simplicial complex into its <a href="http://en.wikipedia.org/wiki/Connected_component_(topology)">connected components</a>.  If `vertex_count` is specified, we assume that the cell complex is dense -- or in other words the vertices of the cell complex is the set of integers [0, vertex_count).  This allows for a slightly more efficient implementation.  If unspecified, a more general but less efficient sparse algorithm is used.

* `cells` is an array of cells
* `vertex_count` (optional) is the result of calling `countVertices(cells)` or in other words is the total number of vertices.

**Returns:** An array of cell complexes, one per each connected component.  Note that these complexes are not normalized.

**Time complexity:**

* If `vertex_count` is specified:  `O(vertex_count + dimension(cells)^2 * cells.length)`
* If `vertex_count` is not specified: `O(dimension(cells)^3 * log(cells.length) * cells.length)`

Credits
=======
(c) 2013 Mikola Lysenko.  MIT License

