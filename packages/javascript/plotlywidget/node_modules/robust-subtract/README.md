robust-subtract
===============
Exactly computes the difference of two non-increasing overlapping sequences.  See [robust-sum for more details](https://github.com/mikolalysenko/robust-sum).

# Example

```javascript
var robustDiff = require("robust-subtract")

console.log(robustDiff([1], [1e-64]))
```

# Install

```
npm install robust-subtract
```

# API

### `require("robust-subtract")(a,b)`
Returns the difference of the sequences `a` and `b` encoded as a non-overlapping increasing sequence.

* `a` is the first number
* `b` is the second number

**Returns** The difference of `a` and `b`

## Credits
(c) 2014 Mikola Lysenko. MIT License