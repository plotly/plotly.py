precision mediump float;

uniform vec4 color, borderColor;
uniform float centerFraction;
uniform float pointCloud;

void main() {
  float radius;
  vec4 baseColor;
  if(pointCloud != 0.0) { // pointCloud is truthy
    if(centerFraction == 1.0) {
      gl_FragColor = color;
    } else {
      gl_FragColor = mix(borderColor, color, centerFraction);
    }
  } else {
    radius = length(2.0 * gl_PointCoord.xy - 1.0);
    if(radius > 1.0) {
      discard;
    }
    baseColor = mix(borderColor, color, step(radius, centerFraction));
    gl_FragColor = vec4(baseColor.rgb * baseColor.a, baseColor.a);
  }
}
