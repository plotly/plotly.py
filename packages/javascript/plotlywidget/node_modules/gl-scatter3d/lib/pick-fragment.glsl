precision highp float;

#pragma glslify: outOfRange = require(glsl-out-of-range)

uniform vec3 fragClipBounds[2];
uniform float pickGroup;

varying vec4 pickId;
varying vec3 dataCoordinate;

void main() {
  if (outOfRange(fragClipBounds[0], fragClipBounds[1], dataCoordinate)) discard;

  gl_FragColor = vec4(pickGroup, pickId.bgr);
}