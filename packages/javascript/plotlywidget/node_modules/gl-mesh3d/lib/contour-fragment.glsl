precision highp float;

uniform vec3 contourColor;

void main() {
  gl_FragColor = vec4(contourColor, 1.0);
}
