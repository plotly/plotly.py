slab-decomposition
==================
Given a collection of line segments, constructs a slab decomposition for the purpose of point location queries. This implementation uses a functional red-black tree to store the slabs, requires O(n log(n)) space and answers vertical ray queries in O(log(n)) time.

# Example

```javascript
var makeSlab = require("slab-decomposition")
var slabs = makeSlab([
  [[0, 0], [10, 10]],
  [[10,10], [20, 0]],
  [[5, 5], [20, 0]]
])

for(var i=-10; i<10; ++i) {
  console.log(slabs.castUp([i, -1]))
}
```

# Install

```
npm install slab-decomposition
```

# API

## Constructor

### `var slabs = require("slab-decomposition")(segments)`
Constructs a slab decomposition from the segments

* `segments` is a collection of line segments which only overlap at their end points

**Returns** A slab decomposition data structure

## Methods

### `slabs.castUp(point)`
Casts a vertical ray from `point` going upward along `[0,1]`.  Returns the index of the first segment hit.

* `point` is the base point of the ray

**Returns** The index of the first segment hit by point, otherwise -1 if no segment intersects the ray.

# Credits
(c) 2014 Mikola Lysenko. MIT License