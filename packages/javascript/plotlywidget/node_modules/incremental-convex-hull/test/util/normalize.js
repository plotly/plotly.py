"use strict"

var sc = require("simplicial-complex")
var parity = require("permutation-parity")

module.exports = toNormalForm
module.exports.compare = compareCells

function toNormalForm(cells) {
  var ncells = sc.normalize(cells.slice())
  for(var i=0; i<ncells.length; ++i) {
    var c = ncells[i].slice()
    var p = parity(c)
    c.sort()
    if(p < 0) {
      var t = p[0]
      p[0] = p[1]
      p[1] = t
    }
    ncells[i] = c
  }
  return ncells
}

function compareCells(t, a, b, msg) {
  t.same(toNormalForm(a), toNormalForm(b), msg)
}