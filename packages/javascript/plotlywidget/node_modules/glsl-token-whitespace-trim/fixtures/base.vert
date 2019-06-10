precision mediump float;

attribute vec2 position;

void main() {
  gl_Position = vec4(position, 1, 1);
}
