precision mediump float;

attribute vec2 coord;

uniform vec4 screenBox;
uniform vec2 start, end;
uniform float width;

vec2 perp(vec2 v) {
  return vec2(v.y, -v.x);
}

vec2 screen(vec2 v) {
  return 2.0 * (v - screenBox.xy) / (screenBox.zw - screenBox.xy) - 1.0;
}

void main() {
  vec2 delta = normalize(perp(start - end));
  vec2 offset = mix(start, end, 0.5 * (coord.y+1.0));
  gl_Position = vec4(screen(offset + 0.5 * width * delta * coord.x), 0, 1);
}
