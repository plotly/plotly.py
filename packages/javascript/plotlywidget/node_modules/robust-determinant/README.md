robust-determinant
==================
Computes the determinant of an nxn matrix as a non-overlapping increasing sequence.

## Example

```javascript
var robustDeterminant = require("robust-determinant")

console.log(robustDeterminant([[1,2,3], [4,5,6], [7,8,9]])
```

Output:

```javascript
[ 0 ]
```

### Install

```
npm install robust-determinant
```

### `require("robust-determinant")(m)`
Exactly computes the determinant of a floating point matrix `m`

* `m` is a square matrix

**Returns** The determinant of `m` as a non-increasing overlapping sequence

**Note** For matrices with up to `5` rows, you can avoid an extra dispatch by calling `robustDeterminant[n]`, where `n` is the number of rows.  For example,

```javascript
robustDeterminant[2]([[1,2],[3,4]]) === robustDeterminant([[1,2],[3,4]])
```

## Credits
(c) 2013 Mikola Lysenko. MIT License