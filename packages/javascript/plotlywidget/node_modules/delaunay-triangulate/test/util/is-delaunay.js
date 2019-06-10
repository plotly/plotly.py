"use strict"

var inSphere = require("robust-in-sphere")
var orient = require("robust-orientation")

module.exports = isDelaunay

function isDelaunay(t, cells, points) {
  for(var i=0; i<cells.length; ++i) {
    var cell = cells[i]
    var tuple = new Array(cell.length+1)
    for(var j=0; j<cell.length; ++j) {
      tuple[j] = points[cell[j]]
    }
    for(var j=0; j<points.length; ++j) {
      tuple[cell.length] = points[j]
      t.ok(inSphere.apply(void 0, tuple) >= 0, "check in sphere: " + cell + " - " + j)
      t.ok(orient.apply(void 0, tuple.slice(0, cell.length)) >= 0, "check orientation")
    }
  }
}