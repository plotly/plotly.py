"use strict"

module.exports = extractPlanes

function extractPlanes(M, zNear, zFar) {
  var z  = zNear || 0.0
  var zf = zFar || 1.0
  return [
    [ M[12] + M[0], M[13] + M[1], M[14] + M[2], M[15] + M[3] ],
    [ M[12] - M[0], M[13] - M[1], M[14] - M[2], M[15] - M[3] ],
    [ M[12] + M[4], M[13] + M[5], M[14] + M[6], M[15] + M[7] ],
    [ M[12] - M[4], M[13] - M[5], M[14] - M[6], M[15] - M[7] ],
    [ z*M[12] + M[8], z*M[13] + M[9], z*M[14] + M[10], z*M[15] + M[11] ],
    [ zf*M[12] - M[8], zf*M[13] - M[9], zf*M[14] - M[10], zf*M[15] - M[11] ]
  ]
}