'use strict'

var isRat = require('big-rat/is-rat')

module.exports = isVec

function isVec(a) {
  if(!Array.isArray(a)) {
    return false
  }
  for(var i=0; i<a.length; ++i) {
    if(!isRat(a[i])) {
      return false
    }
  }
  return true
}
