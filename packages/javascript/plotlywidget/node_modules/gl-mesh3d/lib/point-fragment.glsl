precision highp float;

uniform sampler2D texture;
uniform float opacity;

varying vec4 f_color;
varying vec2 f_uv;

void main() {
  vec2 pointR = gl_PointCoord.xy - vec2(0.5, 0.5);
  if(dot(pointR, pointR) > 0.25) {
    discard;
  }
  gl_FragColor = f_color * texture2D(texture, f_uv) * opacity;
}