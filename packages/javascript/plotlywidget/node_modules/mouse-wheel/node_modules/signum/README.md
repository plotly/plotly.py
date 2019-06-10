signum
======
Returns the sign of a floating point number

# Example

```javascript
var sgn = require("signum")

console.log(sgn(-0.00001))
console.log(sng(0))
console.log(sng(Infinity))
```

Output:

```javascript
-1
0
1
```

# Install

```
npm install signum
```

# API

### `require("signum")(x)`
Returns the sign of `x`

* `x` is a number

**Returns** One of the following values

* `-1` if `x<0`
* `1` if `x>0`
* `0` otherwise

# Credits
(c) 2014 Mikola Lysenko. MIT License
