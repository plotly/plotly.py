precision mediump float;

attribute vec3 dataCoord;

uniform vec2 dataAxis, dataShift, dataScale, screenOffset, tickScale;

void main() {
  vec2 pos = dataAxis * (dataScale * dataCoord.x + dataShift);
  gl_Position = vec4(pos + tickScale*dataCoord.yz + screenOffset, 0, 1);
}
