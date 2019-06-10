precision highp float;

attribute vec3 position;
attribute vec4 color;
attribute vec2 uv;

uniform mat4 model, view, projection;

varying vec4 f_color;
varying vec3 f_data;
varying vec2 f_uv;

void main() {
  gl_Position = projection * view * model * vec4(position, 1.0);
  f_color = color;
  f_data  = position;
  f_uv    = uv;
}