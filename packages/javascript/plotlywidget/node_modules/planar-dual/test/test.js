"use strict"

var tape = require("tape")
var getFaces = require("../loops")
var dup = require("dup")
var randPerm = require("random-permutation")
var invert = require("invert-permutation")
var shuffle = require("shuffle-array")

tape("planar-dual", function(t) {

  function canonicalizeCycle(cycle) {
    var lo = 0
    for(var i=0; i<cycle.length; ++i) {
      for(var j=0; j<cycle.length; ++j) {
        var d = cycle[(i+j)%cycle.length] - cycle[(lo+j)%cycle.length]
        if(d < 0) {
          lo = i
        }
        if(d) {
          break
        }
      }
    }
    return cycle.slice(lo).concat(cycle.slice(0, lo))
  }

  function compareCycles(a, b) {
    var ca = a.map(canonicalizeCycle)
    var cb = b.map(canonicalizeCycle)
    ca.sort()
    cb.sort()
    t.same(ca, cb)
  }

  function verify(edges, positions, expected) {
    compareCycles(getFaces(edges, positions), expected)

    //Do shuffles
    for(var i=0; i<30; ++i) {
      var perm = randPerm(positions.length)
      var npositions = invert(perm).map(function(v) {
        return positions[v]
      })
      var nedges = shuffle(edges.map(function(e) {
        return [perm[e[0]], perm[e[1]]]
      }))

      var nexpected = expected.map(function(c) {
        return c.map(function(v) {
          return perm[v]
        })
      })      
      compareCycles(getFaces(nedges, npositions), nexpected)
    }
  }

  function makeCircle(n) {
    return {
      edges: dup(n).map(function(a,i) {
        return [i, (i+1)%n]
      }),
      positions: dup(n).map(function(a,i) {
        var t = 2.0*Math.PI*i/n
        return [Math.cos(t), Math.sin(t)]
      })
    }
  }
  var circ = makeCircle(10)
  verify(circ.edges, circ.positions, [
      [0,1,2,3,4,5,6,7,8,9],
      [9,8,7,6,5,4,3,2,1,0]
    ])

  verify([ [0, 1] ], [ [0, 0], [1, 0] ], [ [0, 1] ])


  //Two circles
  var c1 = makeCircle(5)
  var c2 = makeCircle(5)
  for(var i=0; i<5; ++i) {
    c1.positions[i][0] -= 2
    c2.positions[i][0] += 2
    for(var j=0; j<2; ++j) {
      c1.edges[i][j] += 1
      c2.edges[i][j] += 6
    }
  }
  var nedges = [ [0,1], [0,6] ].concat(c1.edges).concat(c2.edges)
  var npositions = [ [0,0] ].concat(c1.positions).concat(c2.positions)
  verify(nedges, npositions, 
    [ [ 0, 1, 2, 3, 4, 5, 1, 0, 6, 10, 9, 8, 7, 6 ],
      [ 1, 5, 4, 3, 2 ],
      [ 6, 7, 8, 9, 10 ] ])

  //Tri force!
  var tpositions = [
    [0, 0],
    [-1, -1],
    [0, 1],
    [1, -1]
  ]
  var tedges = [
    [1, 2],
    [2, 3],
    [3, 1],
    [0, 1],
    [0, 2],
    [0, 3]
  ]
  verify(tedges, tpositions, [ [ 0, 1, 2 ], [ 0, 2, 3 ], [ 0, 3, 1 ], [ 1, 3, 2 ] ])
  
  //Single vertex
  verify([], [[0,0]], [ [0] ])

  function earring(n, theta) {
    var ringEdges = []
    var ringVertices = [ [0,0] ]
    var ringFaces = []
    var prevFace = []
    for(var nn=0; nn<n; ++nn) {
      var base = ringVertices.length-1
      ringEdges.push([0,ringVertices.length])
      var cFace = [0]
      var ntheta = theta + n-nn
      for(var i=1; i<ntheta; ++i) {
        var x = 2.0 * Math.PI * i / ntheta
        var c = 1 - Math.cos(x)
        var s = Math.sin(x)
        var r = 1.0 / (nn+1)
        ringVertices.push([r*c, r*s])
        cFace.push(i+base)
        if(i === ntheta-1) {
          break
        }
        ringEdges.push([i+base,((i+1)%ntheta)+base])
      }
      ringEdges.push([ringVertices.length-1, 0])
      prevFace.push(0)
      cFace.reverse()
      ringFaces.push(prevFace.concat(cFace.slice(0, cFace.length-1)))
      cFace.reverse()
      prevFace = cFace
    }
    ringFaces.push(prevFace)
    verify(ringEdges, ringVertices, ringFaces)
  }

  for(var i=1; i<=10; ++i) {
    earring(i, 3)
  }

  t.end()
})