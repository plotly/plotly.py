precision mediump float;

attribute vec2 position;
attribute vec2 tangent;
attribute vec4 color;

uniform mat3 viewTransform;
uniform vec2 screenShape;
uniform float lineWidth;
uniform float pointSize;

varying vec4 fragColor;

void main() {
  fragColor = color;

  vec3 vPosition = viewTransform * vec3(position, 1.0);
  vec2 vTangent = normalize(viewTransform * vec3(tangent, 0)).xy;
  vec2 offset = vec2(vTangent.y, -vTangent.x) / screenShape;

  gl_Position = vec4(
    vPosition.xy + offset * lineWidth * vPosition.z,
    0,
    vPosition.z);

  gl_PointSize = pointSize;
}
