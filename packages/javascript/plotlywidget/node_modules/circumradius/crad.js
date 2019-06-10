module.exports = circumradius

var circumcenter = require('circumcenter')

function circumradius(points) {
  var center = circumcenter(points)
  var avgDist = 0.0
  for(var i=0; i<points.length; ++i) {
    var p = points[i]
    for(var j=0; j<center.length; ++j) {
      avgDist += Math.pow(p[j] - center[j], 2)
    }
  }
  return Math.sqrt(avgDist / points.length)
}