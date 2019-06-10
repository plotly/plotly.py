precision mediump float;

const float pi = 3.14;
uniform vec2 P;

#pragma glslify: run = require('./unsuffixable-source.glsl', d = pi, h = P.x)

void main() {
  run(gl_FragCoord.xy);
}
