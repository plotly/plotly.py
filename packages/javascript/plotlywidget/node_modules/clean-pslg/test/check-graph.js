'use strict'

var segseg = require('robust-segment-intersect')

module.exports = checkGraph

function checkUnique(tape, list, compare) {
  var sorted = list.slice().sort(compare)
  for(var i=1; i<sorted.length; ++i) {
    tape.ok(compare(sorted[i-1], sorted[i]),
      'sorted ' + sorted[i-1] + ' and ' + sorted[i] + ' are distinct')
  }
}

function checkGraph(tape, points, edges) {
  //1.  Check no duplicate points
  checkUnique(tape, points, function(a, b) {
    return a[0] - b[0] || a[1] - b[1]
  })

  //2.  Check no duplicate edges
  checkUnique(tape, edges, function(a, b) {
    return Math.min(a[0], a[1]) - Math.min(b[0], b[1]) ||
           Math.max(a[0], a[1]) - Math.max(b[0], b[1])
  })

  //3.  Check no crossings
  for(var i=0; i<edges.length; ++i) {
    var e = edges[i]
    var a = points[e[0]]
    var b = points[e[1]]
    for(var j=0; j<i; ++j) {
      var f = edges[j]
      var c = points[f[0]]
      var d = points[f[1]]
      if(a === c || a === d ||
         b === c || b === d) {
           continue
      }
      tape.ok(!segseg(a, b, c, d), 'segments ' + e + ' and ' + f + ' are disjoint')
    }
  }

  //4.  Check no tjunctions
  for(var i=0; i<edges.length; ++i) {
    var e = edges[i]
    var a = points[e[0]]
    var b = points[e[1]]
    for(var j=0; j<points.length; ++j) {
      var p = points[j]
      if(p === a || p === b) {
        continue
      }
      tape.ok(!segseg(a, b, p, p), 'no tjunction ' + e + ' with ' + p)
    }
  }
}
