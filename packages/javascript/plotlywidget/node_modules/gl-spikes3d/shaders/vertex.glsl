precision mediump float;

attribute vec3 position, color;
attribute float weight;

uniform mat4 model, view, projection;
uniform vec3 coordinates[3];
uniform vec4 colors[3];
uniform vec2 screenShape;
uniform float lineWidth;

varying vec4 fragColor;

void main() {
  vec3 vertexPosition = mix(coordinates[0],
    mix(coordinates[2], coordinates[1], 0.5 * (position + 1.0)), abs(position));

  vec4 clipPos = projection * view * model * vec4(vertexPosition, 1.0);
  vec2 clipOffset = (projection * view * model * vec4(color, 0.0)).xy;
  vec2 delta = weight * clipOffset * screenShape;
  vec2 lineOffset = normalize(vec2(delta.y, -delta.x)) / screenShape;

  gl_Position   = vec4(clipPos.xy + clipPos.w * 0.5 * lineWidth * lineOffset, clipPos.z, clipPos.w);
  fragColor     = color.x * colors[0] + color.y * colors[1] + color.z * colors[2];
}
