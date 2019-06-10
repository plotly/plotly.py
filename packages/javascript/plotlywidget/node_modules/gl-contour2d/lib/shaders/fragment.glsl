precision lowp float;
varying vec4 fragColor;
void main() {
  gl_FragColor = vec4(fragColor.rgb * fragColor.a, fragColor.a);
}
