"use strict"

module.exports = permutationSign

var BRUTE_FORCE_CUTOFF = 32

var pool = require("typedarray-pool")

function permutationSign(p) {
  var n = p.length
  if(n < BRUTE_FORCE_CUTOFF) {
    //Use quadratic algorithm for small n
    var sgn = 1
    for(var i=0; i<n; ++i) {
      for(var j=0; j<i; ++j) {
        if(p[i] < p[j]) {
          sgn = -sgn
        } else if(p[i] === p[j]) {
          return 0
        }
      }
    }
    return sgn
  } else {
    //Otherwise use linear time algorithm
    var visited = pool.mallocUint8(n)
    for(var i=0; i<n; ++i) {
      visited[i] = 0
    }
    var sgn = 1
    for(var i=0; i<n; ++i) {
      if(!visited[i]) {
        var count = 1
        visited[i] = 1
        for(var j=p[i]; j!==i; j=p[j]) {
          if(visited[j]) {
            pool.freeUint8(visited)
            return 0
          }
          count += 1
          visited[j] = 1
        }
        if(!(count & 1)) {
          sgn = -sgn
        }
      }
    }
    pool.freeUint8(visited)
    return sgn
  }
}