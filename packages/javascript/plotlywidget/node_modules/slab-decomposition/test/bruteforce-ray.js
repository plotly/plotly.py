"use strict"

module.exports = bruteForceRayQuery

var orient = require("robust-orientation")
var orderSegments = require("../lib/order-segments")

function bruteForceRayQuery(segments, point) {
  var closestSegment = -1
  for(var i=0; i<segments.length; ++i) {
    var s = segments[i]
    var hasHit = false
    if(s[0][0] < s[1][0]) {
      if(s[0][0] <= point[0] && point[0] < s[1][0]) {
        if(orient(s[0], s[1], point) >= 0) {
          hasHit = true
        }
      }
    } else if(s[0][0] > s[1][0]) {
      if(s[1][0] < point[0] && point[0] <= s[0][0]) {
        if(orient(s[1], s[0], point) >= 0) {
          hasHit = true
        }
      }
    } else if(s[0][0] === s[1][0]) {
      if(s[0][0] === point[0]) {
        if(s[0][1] < s[1][1]) {
          if((s[0][1] <= point[1]) && (point[1] < s[1][1])) {
            return i
          }
          if(point[1] < s[1][1]) {
            hasHit = true
          }
        } else if(s[0][1] > s[1][1]) {
          if(s[1][1] < point[1] && point[1] <= s[0][1]) {
            return i
          }
          if(point[1] <= s[0][1]) {
            hasHit = true
          }
        }
      }
    }
    if(hasHit) {
      if(closestSegment < 0) {
        closestSegment = i
      } else {
        if(orderSegments(segments[closestSegment], s) < 0) {
          closestSegment = i
        }
      }
    }
  }
  return closestSegment
}