precision highp float;

attribute vec3 position, nextPosition;
attribute float arcLength, lineWidth;
attribute vec4 color;

uniform vec2 screenShape;
uniform float pixelRatio;
uniform mat4 model, view, projection;

varying vec4 fragColor;
varying vec3 worldPosition;
varying float pixelArcLength;

vec4 project(vec3 p) {
  return projection * view * model * vec4(p, 1.0);
}

void main() {
  vec4 startPoint = project(position);
  vec4 endPoint   = project(nextPosition);

  vec2 A = startPoint.xy / startPoint.w;
  vec2 B =   endPoint.xy /   endPoint.w;

  float clipAngle = atan(
    (B.y - A.y) * screenShape.y,
    (B.x - A.x) * screenShape.x
  );

  vec2 offset = 0.5 * pixelRatio * lineWidth * vec2(
    sin(clipAngle),
    -cos(clipAngle)
  ) / screenShape;

  gl_Position = vec4(startPoint.xy + startPoint.w * offset, startPoint.zw);

  worldPosition = position;
  pixelArcLength = arcLength;
  fragColor = color;
}
