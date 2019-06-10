circumradius
============
Computes the radius of the circumcircle of a simplex.

# Example

```javascript
var circumradius = require('circumradius')
var points = [[1, 0], [0,1], [1,1]]
console.log(circumradius(points))
```

# Install

```
npm i circumradius
```

# API

#### `var rad = require('circumradius')(points)`
Computes the radius of the circumcircle of the given simplex

* `points` is a set of points describing the vertices of a simplex.

**Returns** The radius of the circumcircle of the simplex.

**Notes** This module is not robust

# License
(c) 2015 Mikola Lysenko. MIT