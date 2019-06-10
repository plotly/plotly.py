precision mediump float;

attribute vec3 dataCoord;

uniform vec2 dataAxis, dataShift, dataScale;
uniform float lineWidth;

void main() {
  vec2 pos = dataAxis * (dataScale * dataCoord.x + dataShift);
  pos += 10.0 * dataCoord.y * vec2(dataAxis.y, -dataAxis.x) + dataCoord.z * lineWidth;
  gl_Position = vec4(pos, 0, 1);
}
