"use strict";

//Closest point to a point is trivial
function closestPoint0d(a, x, result) {
  var d = 0.0;
  for(var i=0; i<x.length; ++i) {
    result[i] = a[i];
    var t = a[i] - x[i];
    d += t * t;
  }
  return d;
}

module.exports = closestPoint0d;