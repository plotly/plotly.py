"use strict";

var closestPoint0d = require("./lib/closest_point_0d.js");
var closestPoint1d = require("./lib/closest_point_1d.js");
var closestPoint2d = require("./lib/closest_point_2d.js");
var closestPointnd = require("./lib/closest_point_nd.js");

var TMP_BUFFER = new Float64Array(4);

function closestPoint(cell, positions, x, result) {
  if(!result) {
    if(TMP_BUFFER.length < x.length) {
      TMP_BUFFER = new Float64Array(x.length);
    }
    result = TMP_BUFFER;
  }
  switch(cell.length) {
    case 0:
      for(var i=0; i<x.length; ++i) {
        result[i] = Number.NaN;
      }
      return Number.NaN;
    case 1:
      return closestPoint0d(positions[cell[0]], x, result);
    case 2:
      return closestPoint1d(positions[cell[0]], positions[cell[1]], x, result);
    case 3:
      return closestPoint2d(positions[cell[0]], positions[cell[1]], positions[cell[2]], x, result);
    default:
      return closestPointnd(cell, positions, x, result);
  }
}
module.exports = closestPoint;
