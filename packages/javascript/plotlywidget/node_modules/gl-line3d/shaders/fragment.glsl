precision highp float;

#pragma glslify: outOfRange = require(glsl-out-of-range)

uniform vec3      clipBounds[2];
uniform sampler2D dashTexture;
uniform float     dashScale;
uniform float     opacity;

varying vec3    worldPosition;
varying float   pixelArcLength;
varying vec4    fragColor;

void main() {
  if (
    outOfRange(clipBounds[0], clipBounds[1], worldPosition) ||
    fragColor.a * opacity == 0.
  ) discard;

  float dashWeight = texture2D(dashTexture, vec2(dashScale * pixelArcLength, 0)).r;
  if(dashWeight < 0.5) {
    discard;
  }
  gl_FragColor = fragColor * opacity;
}
