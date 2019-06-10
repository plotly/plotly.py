precision highp float;

#pragma glslify: outOfRange = require(glsl-out-of-range)

attribute vec3 position;
attribute vec4 color;
attribute vec2 uv;
attribute float pointSize;

uniform mat4 model, view, projection;
uniform vec3 clipBounds[2];

varying vec4 f_color;
varying vec2 f_uv;

void main() {
  if (outOfRange(clipBounds[0], clipBounds[1], position)) {

    gl_Position = vec4(0.0, 0.0 ,0.0 ,0.0);
  } else {
    gl_Position = projection * view * model * vec4(position, 1.0);
  }
  gl_PointSize = pointSize;
  f_color = color;
  f_uv = uv;
}