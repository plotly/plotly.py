permutation-parity
==================
Computes the [parity of a permutation](http://en.wikipedia.org/wiki/Parity_of_a_permutation).

# Example

```javascript
var sgn = require("permutation-parity")

console.log(sgn([0, 1, 2]), sgn([0, 2, 1]))
```

# Install

```
npm install permutation-parity
```

# API

#### `require("permutation-parity")(p)`
Determines the sign of a permutation

* `p` is a permutation

**Returns** The sign of the permutation:

* `1` if `p` is odd
* `-1` if `p` is even
* `0` if `p` is not a permutation

# Credits
(c) 2014 Mikola Lysenko. MIT License