robust-linear-solve
===================
An exact linear solver for low dimensional systems.

# Example

```javascript
var linSolve = require("robust-linear-solve")

var A = [ [1, 2, 3],
          [3, 2, 1],
          [0, 0, 1] ]

var b = [1, 2, 3]

console.log(linSolve(A, b))
```

Output:

```javascript
[ [ -14 ], [ 23 ], [ -12 ], [ -4 ] ]
```

# Install

```
npm install robust-linear-solve
```

# API

#### `require("robust-linear-solve")(A, b)`
Finds the exact solution to a linear system, `Ax = b`, using Cramer's rule.

* `A` is a `n`-by-`n` square matrix, encoded as an array of arrays
* `b` is an `n` dimensional vector encoded as a length `n` array

**Returns** A projective `n+1` dimensional vector of non-overlapping increasing sequences representing the exact solution to the system.  That is to say, if `x` is the returned solution then in psuedocode we have the following constraint:

`A [ x[0], x[1], ... ,  x[n-1] ] =  b * x[n]`

Or in other words, the solution is given by the quotient:

`[ x[0] / x[n], x[1] / x[n], .... , x[n-1] / x[n] ]`

If the system is not solvable, then the last coefficient, `x[n]` will be `0`.

**Note** For up to `n=5`, you can avoid the extra method look up by calling `linSolve[n]` directly.

# Credits
(c) 2014 Mikola Lysenko. MIT License