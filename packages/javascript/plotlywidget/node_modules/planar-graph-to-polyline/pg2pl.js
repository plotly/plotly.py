'use strict'

module.exports = planarGraphToPolyline

var e2a = require('edges-to-adjacency-list')
var planarDual = require('planar-dual')
var preprocessPolygon = require('point-in-big-polygon')
var twoProduct = require('two-product')
var robustSum = require('robust-sum')
var uniq = require('uniq')
var trimLeaves = require('./lib/trim-leaves')

function makeArray(length, fill) {
  var result = new Array(length)
  for(var i=0; i<length; ++i) {
    result[i] = fill
  }
  return result
}

function makeArrayOfArrays(length) {
  var result = new Array(length)
  for(var i=0; i<length; ++i) {
    result[i] = []
  }
  return result
}


function planarGraphToPolyline(edges, positions) {

  //Trim leaves
  var result = trimLeaves(edges, positions)
  edges = result[0]
  positions = result[1]

  var numVertices = positions.length
  var numEdges = edges.length

  //Calculate adjacency list, check manifold
  var adj = e2a(edges, positions.length)
  for(var i=0; i<numVertices; ++i) {
    if(adj[i].length % 2 === 1) {
      throw new Error('planar-graph-to-polyline: graph must be manifold')
    }
  }

  //Get faces
  var faces = planarDual(edges, positions)

  //Check orientation of a polygon using exact arithmetic
  function ccw(c) {
    var n = c.length
    var area = [0]
    for(var j=0; j<n; ++j) {
      var a = positions[c[j]]
      var b = positions[c[(j+1)%n]]
      var t00 = twoProduct(-a[0], a[1])
      var t01 = twoProduct(-a[0], b[1])
      var t10 = twoProduct( b[0], a[1])
      var t11 = twoProduct( b[0], b[1])
      area = robustSum(area, robustSum(robustSum(t00, t01), robustSum(t10, t11)))
    }
    return area[area.length-1] > 0
  }

  //Extract all clockwise faces
  faces = faces.filter(ccw)

  //Detect which loops are contained in one another to handle parent-of relation
  var numFaces = faces.length
  var parent = new Array(numFaces)
  var containment = new Array(numFaces)
  for(var i=0; i<numFaces; ++i) {
    parent[i] = i
    var row = new Array(numFaces)
    var loopVertices = faces[i].map(function(v) {
      return positions[v]
    })
    var pmc = preprocessPolygon([loopVertices])
    var count = 0
    outer:
    for(var j=0; j<numFaces; ++j) {
      row[j] = 0
      if(i === j) {
        continue
      }
      var c = faces[j]
      var n = c.length
      for(var k=0; k<n; ++k) {
        var d = pmc(positions[c[k]])
        if(d !== 0) {
          if(d < 0) {
            row[j] = 1
            count += 1
          }
          continue outer
        }
      }
      row[j] = 1
      count += 1
    }
    containment[i] = [count, i, row]
  }
  containment.sort(function(a,b) {
    return b[0] - a[0]
  })
  for(var i=0; i<numFaces; ++i) {
    var row = containment[i]
    var idx = row[1]
    var children = row[2]
    for(var j=0; j<numFaces; ++j) {
      if(children[j]) {
        parent[j] = idx
      }
    }
  }

  //Initialize face adjacency list
  var fadj = makeArrayOfArrays(numFaces)
  for(var i=0; i<numFaces; ++i) {
    fadj[i].push(parent[i])
    fadj[parent[i]].push(i)
  }

  //Build adjacency matrix for edges
  var edgeAdjacency = {}
  var internalVertices = makeArray(numVertices, false)
  for(var i=0; i<numFaces; ++i) {
    var c = faces[i]
    var n = c.length
    for(var j=0; j<n; ++j) {
      var a = c[j]
      var b = c[(j+1)%n]
      var key = Math.min(a,b) + ":" + Math.max(a,b)
      if(key in edgeAdjacency) {
        var neighbor = edgeAdjacency[key]
        fadj[neighbor].push(i)
        fadj[i].push(neighbor)
        internalVertices[a] = internalVertices[b] = true
      } else {
        edgeAdjacency[key] = i
      }
    }
  }

  function sharedBoundary(c) {
    var n = c.length
    for(var i=0; i<n; ++i) {
      if(!internalVertices[c[i]]) {
        return false
      }
    }
    return true
  }

  var toVisit = []
  var parity = makeArray(numFaces, -1)
  for(var i=0; i<numFaces; ++i) {
    if(parent[i] === i && !sharedBoundary(faces[i])) {
      toVisit.push(i)
      parity[i] = 0
    } else {
      parity[i] = -1
    }
  }

  //Using face adjacency, classify faces as in/out
  var result = []
  while(toVisit.length > 0) {
    var top = toVisit.pop()
    var nbhd = fadj[top]
    uniq(nbhd, function(a,b) {
      return a-b
    })
    var nnbhr = nbhd.length
    var p = parity[top]
    var polyline
    if(p === 0) {
      var c = faces[top]
      polyline = [c]
    }
    for(var i=0; i<nnbhr; ++i) {
      var f = nbhd[i]
      if(parity[f] >= 0) {
        continue
      }
      parity[f] = p^1
      toVisit.push(f)
      if(p === 0) {
        var c = faces[f]
        if(!sharedBoundary(c)) {
          c.reverse()
          polyline.push(c)
        }
      }
    }
    if(p === 0) {
      result.push(polyline)
    }
  }

  return result
}