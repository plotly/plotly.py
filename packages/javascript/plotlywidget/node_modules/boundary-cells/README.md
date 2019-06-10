boundary-cells
==============
Computes a basis for the collection of all boundary cells in a cell complex.  This is not the same as the boundary operator for a cell complex.

# Example

```javascript
var bnd = require('boundary-cells')

console.log(bnd([
  [0, 1, 2],
  [2, 1, 3]
]))
```

# Install

```
npm i boundary-cells
```

# API

#### `require('boundary-cells')(cells)`
Extracts the boundary of all cells in a cell complex

* `cells` is a cell complex

**Returns** An array of all boundary cells in the complex

Credits
=======
(c) 2013-2015 Mikola Lysenko. MIT License
