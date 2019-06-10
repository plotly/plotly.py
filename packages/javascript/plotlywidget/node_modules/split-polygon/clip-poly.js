"use strict"

var robustDot = require("robust-dot-product")
var robustSum = require("robust-sum")

module.exports = splitPolygon
module.exports.positive = positive
module.exports.negative = negative

function planeT(p, plane) {
  var r = robustSum(robustDot(p, plane), [plane[plane.length-1]])
  return r[r.length-1]
}


//Can't do this exactly and emit a floating point result
function lerpW(a, wa, b, wb) {
  var d = wb - wa
  var t = -wa / d
  if(t < 0.0) {
    t = 0.0
  } else if(t > 1.0) {
    t = 1.0
  }
  var ti = 1.0 - t
  var n = a.length
  var r = new Array(n)
  for(var i=0; i<n; ++i) {
    r[i] = t * a[i] + ti * b[i]
  }
  return r
}

function splitPolygon(points, plane) {
  var pos = []
  var neg = []
  var a = planeT(points[points.length-1], plane)
  for(var s=points[points.length-1], t=points[0], i=0; i<points.length; ++i, s=t) {
    t = points[i]
    var b = planeT(t, plane)
    if((a < 0 && b > 0) || (a > 0 && b < 0)) {
      var p = lerpW(s, b, t, a)
      pos.push(p)
      neg.push(p.slice())
    }
    if(b < 0) {
      neg.push(t.slice())
    } else if(b > 0) {
      pos.push(t.slice())
    } else {
      pos.push(t.slice())
      neg.push(t.slice())
    }
    a = b
  }
  return { positive: pos, negative: neg }
}

function positive(points, plane) {
  var pos = []
  var a = planeT(points[points.length-1], plane)
  for(var s=points[points.length-1], t=points[0], i=0; i<points.length; ++i, s=t) {
    t = points[i]
    var b = planeT(t, plane)
    if((a < 0 && b > 0) || (a > 0 && b < 0)) {
      pos.push(lerpW(s, b, t, a))
    }
    if(b >= 0) {
      pos.push(t.slice())
    }
    a = b
  }
  return pos
}

function negative(points, plane) {
  var neg = []
  var a = planeT(points[points.length-1], plane)
  for(var s=points[points.length-1], t=points[0], i=0; i<points.length; ++i, s=t) {
    t = points[i]
    var b = planeT(t, plane)
    if((a < 0 && b > 0) || (a > 0 && b < 0)) {
      neg.push(lerpW(s, b, t, a))
    }
    if(b <= 0) {
      neg.push(t.slice())
    }
    a = b
  }
  return neg
}