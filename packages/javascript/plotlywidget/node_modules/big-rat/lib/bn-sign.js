'use strict'

var BN = require('bn.js')

module.exports = sign

function sign (x) {
  return x.cmp(new BN(0))
}
