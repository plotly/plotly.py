precision mediump float;

attribute vec2 vertex;

uniform vec2 cornerA, cornerB;

void main() {
  gl_Position = vec4(mix(cornerA, cornerB, vertex), 0, 1);
}
