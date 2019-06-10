"use strict";

var EPSILON = 1e-8;

//Computes closest point to a line segment
function closestPoint1d(a, b, x, result) {
  var denom = 0.0;
  var numer = 0.0;
  for(var i=0; i<x.length; ++i) {
    var ai = a[i];
    var bi = b[i];
    var xi = x[i];
    var dd = ai - bi;
    numer += dd * (xi - bi);
    denom += dd * dd;
  }
  var t = 0.0;
  if(Math.abs(denom) > EPSILON) {
    t = numer / denom;
    if(t < 0.0) {
      t = 0.0;
    } else if(t > 1.0) {
      t = 1.0;
    }
  }  
  var ti = 1.0 - t;
  var d = 0;
  for(var i=0; i<x.length; ++i) {
    var r = t * a[i] + ti * b[i];
    result[i] = r;
    var s = x[i] - r;
    d += s * s;
  }
  return d;
}

module.exports = closestPoint1d;