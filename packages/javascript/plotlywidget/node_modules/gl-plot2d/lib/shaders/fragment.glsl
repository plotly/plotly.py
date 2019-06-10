precision lowp float;
uniform vec4 color;
void main() {
  gl_FragColor = vec4(color.xyz * color.w, color.w);
}
