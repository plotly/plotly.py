'use strict'

var bn2num = require('./lib/bn-to-num')
var ctz = require('./lib/ctz')

module.exports = roundRat

// Round a rational to the closest float
function roundRat (f) {
  var a = f[0]
  var b = f[1]
  if (a.cmpn(0) === 0) {
    return 0
  }
  var h = a.abs().divmod(b.abs())
  var iv = h.div
  var x = bn2num(iv)
  var ir = h.mod
  var sgn = (a.negative !== b.negative) ? -1 : 1
  if (ir.cmpn(0) === 0) {
    return sgn * x
  }
  if (x) {
    var s = ctz(x) + 4
    var y = bn2num(ir.ushln(s).divRound(b))
    return sgn * (x + y * Math.pow(2, -s))
  } else {
    var ybits = b.bitLength() - ir.bitLength() + 53
    var y = bn2num(ir.ushln(ybits).divRound(b))
    if (ybits < 1023) {
      return sgn * y * Math.pow(2, -ybits)
    }
    y *= Math.pow(2, -1023)
    return sgn * y * Math.pow(2, 1023 - ybits)
  }
}
