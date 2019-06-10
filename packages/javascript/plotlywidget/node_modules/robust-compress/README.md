robust-compress
===============
Quickly compress a non-overlapping increasing sequence.  This does not normalize the sequence, but can be useful in some situations.  Based on the algorithm in:

Jonathan Shewchuk, ["Adaptive precision floating-point arithmetic and fast robust predicates for computational geometry"](http://www.cs.cmu.edu/~quake/robust.html)

# Example

```javascript
var compress = require("robust-compress")

var seq = [1, 2]

compress(seq)

console.log(seq)
```

Output:

```javascript
[ 3 ]
```

# Install

```
npm install robust-compress
```

# API

#### `require("robust-compress")(seq)`
Approximately compress a non-overlapping increasing floating point expansion in place.

* `seq` is a robust sequence

**Returns** `seq`

**Note** This method updates `seq` in place

# Credits
(c) 2014 Mikola Lysenko.  MIT License