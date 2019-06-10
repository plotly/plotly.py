precision highp float;

attribute vec3 position;

uniform mat4 model, view, projection;

void main() {
  gl_Position = projection * view * model * vec4(position, 1.0);
}