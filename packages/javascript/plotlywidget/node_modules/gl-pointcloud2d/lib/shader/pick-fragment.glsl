precision mediump float;

varying vec4 fragId;

void main() {
  float radius = length(2.0 * gl_PointCoord.xy - 1.0);
  if(radius > 1.0) {
    discard;
  }
  gl_FragColor = fragId / 255.0;
}
