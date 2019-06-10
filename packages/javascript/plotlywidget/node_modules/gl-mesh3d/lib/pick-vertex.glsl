precision highp float;

attribute vec3 position;
attribute vec4 id;

uniform mat4 model, view, projection;

varying vec3 f_position;
varying vec4 f_id;

void main() {
  gl_Position = projection * view * model * vec4(position, 1.0);
  f_id        = id;
  f_position  = position;
}