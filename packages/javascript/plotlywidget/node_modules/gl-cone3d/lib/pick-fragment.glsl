precision highp float;

#pragma glslify: outOfRange = require(glsl-out-of-range)

uniform vec3  clipBounds[2];
uniform float pickId;

varying vec3 f_position;
varying vec4 f_id;

void main() {
  if (outOfRange(clipBounds[0], clipBounds[1], f_position)) discard;

  gl_FragColor = vec4(pickId, f_id.xyz);
}