"use strict"

var pool = require("typedarray-pool")
var inverse = require("invert-permutation")

function rank(permutation) {
  var n = permutation.length
  switch(n) {
    case 0:
    case 1:
      return 0
    case 2:
      return permutation[1]
    default:
      break
  }
  var p = pool.mallocUint32(n)
  var pinv = pool.mallocUint32(n)
  var r = 0, s, t, i
  inverse(permutation, pinv)
  for(i=0; i<n; ++i) {
    p[i] = permutation[i]
  }
  for(i=n-1; i>0; --i) {
    t = pinv[i]
    s = p[i]
    p[i] = p[t]
    p[t] = s
    pinv[i] = pinv[s]
    pinv[s] = t
    r = (r + s) * i
  }
  pool.freeUint32(pinv)
  pool.freeUint32(p)
  return r
}

function unrank(n, r, p) {
  switch(n) {
    case 0:
      if(p) { return p }
      return []
    case 1:
      if(p) {
        p[0] = 0
        return p
      } else {
        return [0]
      }
    case 2:
      if(p) {
        if(r) {
          p[0] = 0
          p[1] = 1
        } else {
          p[0] = 1
          p[1] = 0
        }
        return p
      } else {
        return r ? [0,1] : [1,0]
      }
    default:
      break
  }
  p = p || new Array(n)
  var s, t, i, nf=1
  p[0] = 0
  for(i=1; i<n; ++i) {
    p[i] = i
    nf = (nf*i)|0
  }
  for(i=n-1; i>0; --i) {
    s = (r / nf)|0
    r = (r - s * nf)|0
    nf = (nf / i)|0
    t = p[i]|0
    p[i] = p[s]|0
    p[s] = t|0
  }
  return p
}

exports.rank = rank
exports.unrank = unrank
