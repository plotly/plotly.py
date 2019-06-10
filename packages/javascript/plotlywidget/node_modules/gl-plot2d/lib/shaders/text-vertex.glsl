attribute vec3 textCoordinate;

uniform vec2 dataScale, dataShift, dataAxis, screenOffset, textScale;
uniform float angle;

void main() {
  float dataOffset  = textCoordinate.z;
  vec2 glyphOffset  = textCoordinate.xy;
  mat2 glyphMatrix = mat2(cos(angle), sin(angle), -sin(angle), cos(angle));
  vec2 screenCoordinate = dataAxis * (dataScale * dataOffset + dataShift) +
    glyphMatrix * glyphOffset * textScale + screenOffset;
  gl_Position = vec4(screenCoordinate, 0, 1);
}
