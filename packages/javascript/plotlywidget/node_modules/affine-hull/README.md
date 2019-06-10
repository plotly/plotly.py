affine-hull
===========
Computes the lexicographically smallest basis for the affine hull of a point set.

# Example

```javascript
var aff = require('affine-hull')

console.log(aff([
  [0, 0, 0],
  [1, 0, 0],
  [2, 0, 0],
  [3, 0, 0],
  [0, 1, 0],
  [0, 0, 2]
]))
```

Output:

```javascript
[0, 1, 4, 5]
```

# Install

```
npm install affine-hull
```

# API

#### `require('affine-hull')(points)`
Computes a basis for the affine hull of the set of points `points`.

* `points` is a list of points encoded by d-tuples of numbers

**Returns** A list of indices for the generators of the affine hull of the point set

# Credits
(c) 2014 Mikola Lysenko. MIT License