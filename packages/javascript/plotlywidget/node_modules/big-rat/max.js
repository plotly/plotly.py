'use strict'

var cmp = require('./cmp')

module.exports = max

function max(a, b) {
  if(cmp(a, b) > 0) {
    return [a[0].clone(), a[1].clone()]
  } else {
    return [b[0].clone(), b[1].clone()]
  }
}
