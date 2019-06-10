precision mediump float;

uniform sampler2D accumBuffer;
varying vec2 uv;

void main() {
  vec4 accum = texture2D(accumBuffer, 0.5 * (uv + 1.0));
  gl_FragColor = min(vec4(1,1,1,1), accum);
}