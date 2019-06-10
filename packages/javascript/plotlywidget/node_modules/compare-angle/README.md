compare-angle
=============
Let A, B, C and D be four points in the plan.  Then of the pair of angles ABC and ABD, determine which is larger.

```
  C
  *      D
   \     *
    \ABC/
     \ / ABD
      *-------------*
      B             A
```

Example
=======

```javascript
var compareAngle = require("compare-angle")

var A = [2, 0]
var B = [0, 0]
var C = [-1, 2]
var D = [1, 1]

console.log(compareAngle(A, B, C, D),  compareAngle(A, B, D, C))
```

Output:

```
1   -1
```

Install
=======

```
npm install compare-angle
```

API
===

#### `require("compare-angle")(a, b, c, d)`
Compares the angles ABC and ABD to determine which is greater.

* `a`, `b` are the base points of the angle
* `c` is the end of the first angle
* `d` is the end of the second angle

**Returns** A number indicating which angle is larger

* `+1` if angle ABC is greater than angle ABD
* `0` if the angles are equal
* `-1` if angle ABD is greater than angle ABC

Credits
=======
(c) 2014 Mikola Lysenko. MIT License