precision mediump float;

uniform vec2 uVec;

#pragma glslify: a = require( "./sibling" )

void main() {
  gl_FragColor = vec4(a(1.0));
}
