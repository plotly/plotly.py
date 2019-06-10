marching-simplex-table
======================
Constructs a look up table for the marching simplex isosurface extraction algorithm.  The entries of this table correspond to the different topologies that can occur for marching simplices.

# Example

```javascript
var makeTable = require('marching-simplex-table')

console.log(makeTable(2))
console.log(makeTable(3))
```

# Install

```
npm install marching-simplex-table
```

# API

#### `require('marching-simplex-table')(d)`
Constructs the marching simplex table for all simplices of dimension `d`.  The result is a table with 2^(d+1) entries, each corresponding to the (d-1) dimensional cells needed to generate the boundary of the simplex.  Each (d-1) cell is coded as an ordered list of edges in the original simplex giving the vertices of the resulting simplex.

* `d` is the dimension of the table to generate

**Returns** A table of simplex topologies

# Credits
(c) 2014 Mikola Lysenko. MIT License