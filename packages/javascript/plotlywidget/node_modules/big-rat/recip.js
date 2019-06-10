'use strict'

module.exports = recip

function recip(f) {
  return [f[1].clone(), f[0].clone()]
}
