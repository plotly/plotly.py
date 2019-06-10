precision highp float;

attribute vec3 position, offset;
attribute vec4 color;
uniform mat4 model, view, projection;
uniform float capSize;
varying vec4 fragColor;
varying vec3 fragPosition;

void main() {
  vec4 worldPosition  = model * vec4(position, 1.0);
  worldPosition       = (worldPosition / worldPosition.w) + vec4(capSize * offset, 0.0);
  gl_Position         = projection * view * worldPosition;
  fragColor           = color;
  fragPosition        = position;
}