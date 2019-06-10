'use strict'

module.exports = boundary

function boundary (cells) {
  var i, j, k
  var n = cells.length
  var sz = 0
  for (i = 0; i < n; ++i) {
    sz += cells[i].length
  }
  var result = new Array(sz)
  var ptr = 0
  for (i = 0; i < n; ++i) {
    var c = cells[i]
    var d = c.length
    for (j = 0; j < d; ++j) {
      var b = result[ptr++] = new Array(d - 1)
      var p = 0
      for (k = 0; k < d; ++k) {
        if (k === j) {
          continue
        }
        b[p++] = c[k]
      }
      if (j & 1) {
        var tmp = b[1]
        b[1] = b[0]
        b[0] = tmp
      }
    }
  }
  return result
}
