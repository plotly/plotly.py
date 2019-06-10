"use strict"

var tape = require("tape")
var preprocessPolygon = require("../pnp-big.js")
var rpnp = require("robust-point-in-polygon")
var sgn = require("signum")

tape("point-in-big-polygon", function(t) {

  var pp0 = preprocessPolygon([
    [ [1, 2], [2, 2], [2, 1] ]
  ], true)

  t.ok(pp0([2,0]) > 0)
  t.ok(pp0([1.75,1.75]) < 0)
  t.ok(pp0([1,1]) > 0)
  t.ok(pp0([1.5,1.5]) === 0)
  
  var classifyPoint = preprocessPolygon([
    [ [-11, -10], [-10, 10], [10, 10], [10, -10] ],
    [ [-1, -1], [1, -1], [1, 1], [-1, 1] ]
  ], true)

  t.ok(classifyPoint([0, 0]) > 0)
  t.ok(classifyPoint([5, 2]) < 0)
  t.ok(classifyPoint([1, 0]) == 0)
  t.ok(classifyPoint([-1000, 0]) > 0)

  function xform(pt, d) {
    switch(d) {
      case 0:
        return pt
      case 1:
        return [-pt[1], pt[0]]
      case 2:
        return [-pt[0], -pt[1]]
      case 3:
        return [pt[1], -pt[0]]
    }
  }

  function verifyPoints(npolygon, points) {
    for(var d=0; d<4; ++d) {
      var polygon = npolygon.map(function(pt) {
        return xform(pt, d)
      })
      var pmc = preprocessPolygon([polygon])
      for(var i=0; i<points.length; ++i) {
        var pt = xform(points[i], d)
        t.equals(pmc(pt), rpnp(polygon, pt), 'd=' + d + '; pt=' + pt.join())
      }
    }
  }

  verifyPoints(
    [
      [0, 0],
      [0, 1],
      [1, 1],
      [1, 0]
    ],
    [
      [0, 0],
      [0, 1],
      [1, 1],
      [1, 0],
      [0.5, 0],
      [0, 0.5],
      [1, 0.5],
      [0.5, 1],
      [0.25, 0.75],
      [0.5, 0.5],
      [10, 10],
      [-1, -1],
      [0.5, -1]      
    ])

  function testCircle(n) {
    var loop = new Array(n)
    for(var i=0; i<n; ++i) {
      var theta = 2.0 * Math.PI * i / n
      loop[i] = [Math.cos(n), Math.sin(n)]
    }
    var points = [ [0,0] ].concat(loop)
    for(var j=0; j<=n; ++j) {
      points.push([points[j][0]+0.00001*(0.5-Math.random()),
                   points[j][0]+0.00001*(0.5-Math.random())])
    }
    for(var i=0; i<100; ++i) {
      points.push( [1.0-2.0*Math.random(), 1.0-2.0*Math.random()] )
    }
    verifyPoints(loop, points)
  }

  testCircle(10)
  testCircle(100)
  

  t.end()
})