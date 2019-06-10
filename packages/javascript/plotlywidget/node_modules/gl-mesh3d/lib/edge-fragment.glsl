precision highp float;

#pragma glslify: outOfRange = require(glsl-out-of-range)

uniform vec3 clipBounds[2];
uniform sampler2D texture;
uniform float opacity;

varying vec4 f_color;
varying vec3 f_data;
varying vec2 f_uv;

void main() {
  if (outOfRange(clipBounds[0], clipBounds[1], f_data)) discard;

  gl_FragColor = f_color * texture2D(texture, f_uv) * opacity;
}