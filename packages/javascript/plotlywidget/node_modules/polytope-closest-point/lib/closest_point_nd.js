"use strict";

var numeric = require("numeric");
var EPSILON = 1e-6;

//General purpose algorithm, uses quadratic programming, very slow
function closestPointnd(c, positions, x, result) {
  var D = numeric.rep([c.length, c.length], 0.0);
  var dvec = numeric.rep([c.length], 0.0);
  for(var i=0; i<c.length; ++i) {
    var pi = positions[c[i]];
    dvec[i] = numeric.dot(pi, x);
    for(var j=0; j<c.length; ++j) {
      var pj = positions[c[j]];
      D[i][j] = D[j][i] = numeric.dot(pi, pj);
    }
  }
  var A = numeric.rep([c.length, c.length+2], 0.0);
  var b = numeric.rep([c.length+2], 0.0);
  b[0] = 1.0-EPSILON;
  b[1] = -(1.0+EPSILON);
  for(var i=0; i<c.length; ++i) {
    A[i][0]   = 1;
    A[i][1]   = -1
    A[i][i+2] = 1;
  }
  for(var attempts=0; attempts<15; ++attempts) {
    var fortran_poop = numeric.solveQP(D, dvec, A, b);
    if(fortran_poop.message.length > 0) {
      //Quadratic form may be singular, perturb and resolve
      for(var i=0; i<c.length; ++i) {
        D[i][i] += 1e-8;
      }
      continue;
    } else if(isNaN(fortran_poop.value[0])) {
      break;
    } else {
      //Success!
      var solution = fortran_poop.solution;
      for(var i=0; i<x.length; ++i) {
        result[i] = 0.0;
        for(var j=0; j<solution.length; ++j) {
          result[i] += solution[j] * positions[c[j]][i];
        }
      }
      return 2.0 * fortran_poop.value[0] + numeric.dot(x,x);
    }
  }
  for(var i=0; i<x.length; ++i) {
    result[i] = Number.NaN;
  }
  return Number.NaN;
}

module.exports = closestPointnd;