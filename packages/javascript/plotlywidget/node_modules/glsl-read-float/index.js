module.exports = decodeFloat

var UINT8_VIEW = new Uint8Array(4)
var FLOAT_VIEW = new Float32Array(UINT8_VIEW.buffer)

function decodeFloat(x, y, z, w) {
  UINT8_VIEW[0] = w
  UINT8_VIEW[1] = z
  UINT8_VIEW[2] = y
  UINT8_VIEW[3] = x
  return FLOAT_VIEW[0]
}
