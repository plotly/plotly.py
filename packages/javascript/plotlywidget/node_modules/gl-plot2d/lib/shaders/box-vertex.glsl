precision mediump float;

attribute vec2 coord;

uniform vec4 screenBox;
uniform vec2 lo, hi;

vec2 screen(vec2 v) {
  return 2.0 * (v - screenBox.xy) / (screenBox.zw - screenBox.xy) - 1.0;
}

void main() {
  gl_Position = vec4(screen(mix(lo, hi, coord)), 0, 1);
}
