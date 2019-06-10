module.exports = verifyTriangulation

var hull = require('convex-hull')
var uniq = require('uniq')
var flip = require('flip-orientation')
var tritri2d = require('robust-triangle-triangle-2d-intersect')
var cellOrientation = require('cell-orientation')
var orient = require('robust-orientation')

function compareLex(a, b) {
  return (a[0] - b[0]) || (a[1] - b[1])
}

function setIntersect(s, t) {
  for(var i=0; i<s.length; ++i) {
    if(t.indexOf(s[i]) >= 0) {
      return true
    }
  }
  return false
}

function verifyTriangulation(tape, points, edges, triangles) {
  function unpack(i) {
    return triangles[i].map(function(x) {
      return points[x]
    })
  }

  //  3. no degenerate triangles
  for(var i=0; i<triangles.length; ++i) {
    tape.ok(cellOrientation(triangles[i]) !== 0, 'non degenerate: ' + triangles[i].join())
  }

  //  2. the intersection of any two triangles is contained in their boundary
  for(var i=0; i<triangles.length; ++i) {
    var A = unpack(i)
    for(var j=0; j<i; ++j) {
      if(setIntersect(triangles[i], triangles[j])) {
        continue
      }
      var B = unpack(j)
      tape.ok(!tritri2d(A, B), 'non-intersecting: ' + triangles[i].join() + ' (' + A.join(' ') + ') - ' + triangles[j].join() + ' (' + B.join(' ') + ')')
    }
  }

  //  4. every point is contained in at least one triangle
  if(hull(points).length > 0) {
    var pts = []
    for(var i=0; i<triangles.length; ++i) {
      var tri = triangles[i]
      pts.push(tri[0], tri[1], tri[2])
    }
    uniq(pts, function(a,b) { return a - b })
    tape.equals(pts.length, points.length)
    for(var i=0; i<pts.length; ++i) {
      tape.equals(pts[i], i)
    }
  } else {
    tape.equals(triangles.length, 0)
  }

  //  5. every triangle is positively oriented
  for(var i=0; i<triangles.length; ++i) {
    var tri = triangles[i]
    tape.ok(orient(
      points[tri[0]],
      points[tri[1]],
      points[tri[2]]) <= 0, 'orientation: ' + tri.join() + ' <= 0')
  }

  //  6. Check edge constraints are satisifed
  var edgeSet = {}
  triangles.forEach(function(tri) {
    for(var i=0; i<3; ++i) {
      var u = tri[i], v = tri[(i+1)%3]
      edgeSet[Math.min(u, v) + ',' + Math.max(u, v)] = true
    }
  })
  edges.forEach(function(e) {
    var str = Math.min(e[0], e[1]) + ',' + Math.max(e[0], e[1])
    tape.ok(str in edgeSet, 'edge constraint ' + e + ' satisfied')
  })
}
