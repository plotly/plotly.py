precision highp float;

#pragma glslify: packFloat = require(glsl-read-float)
#pragma glslify: outOfRange = require(glsl-out-of-range)

uniform float pickId;
uniform vec3 clipBounds[2];

varying vec3 worldPosition;
varying float pixelArcLength;
varying vec4 fragColor;

void main() {
  if (outOfRange(clipBounds[0], clipBounds[1], worldPosition)) discard;

  gl_FragColor = vec4(pickId/255.0, packFloat(pixelArcLength).xyz);
}