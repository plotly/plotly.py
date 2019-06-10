permutation-rank
================
Ranks and unranks permutations.  Based on the following paper:

W. Myrvold, F. Ruskey. (2000) "[Ranking and Unranking Permutations in Linear Time](http://webhome.cs.uvic.ca/~ruskey/Publications/RankPerm/RankPerm.html)". Information Processing Letters.  

Usage
=====
First install using npm:

    npm install permutation-rank

Then you can use it like this:

```javascript
var prank = require("permutation-rank")
var perm = [0,3,1,2]
var r = prank.rank(perm)
console.log("r = ", r)
var u = prank.unrank(perm.length, r)
console.log("u = ", u)

//Prints:
//        r =  15
//        u =  [ 0, 3, 1, 2 ]
```

`prank.rank(permutation)`
-----------------------------------------------
Computes an integer representing the colexicographic rank of the permutation

* `permutation` is an array encoding some permutation

**Returns** An integer representing the ranked encoding of the permutation


`prank.unrank(length, rank[, result])`
--------------------------------------------------
Computes a permutation from a rank order with the given length

* `length` is the length of the permuation
* `rank` is the index of the permutation
* `result` is an optional argument which stores the result of the inversion

**Returns** The permutation at the given rank

Credits
=======
(c) 2013 Mikola Lysenko. MIT License