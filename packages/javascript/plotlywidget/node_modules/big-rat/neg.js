'use strict'

module.exports = neg

function neg(a) {
  return [ a[0].neg(), a[1].clone() ]
}
