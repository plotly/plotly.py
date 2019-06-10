precision highp float;

varying vec4 fragColor, fragBorderColor;
varying float fragWidth, fragBorderColorLevel, fragColorLevel;

uniform sampler2D marker;
uniform float pixelRatio, opacity;

float smoothStep(float x, float y) {
  return 1.0 / (1.0 + exp(50.0*(x - y)));
}

void main() {
  float dist = texture2D(marker, gl_PointCoord).r, delta = fragWidth;

  // max-distance alpha
  if (dist < 0.003) discard;

  // null-border case
  if (fragBorderColorLevel == fragColorLevel || fragBorderColor.a == 0.) {
    float colorAmt = smoothstep(.5 - delta, .5 + delta, dist);
    gl_FragColor = vec4(fragColor.rgb, colorAmt * fragColor.a * opacity);
  }
  else {
    float borderColorAmt = smoothstep(fragBorderColorLevel - delta, fragBorderColorLevel + delta, dist);
    float colorAmt = smoothstep(fragColorLevel - delta, fragColorLevel + delta, dist);

    vec4 color = fragBorderColor;
    color.a *= borderColorAmt;
    color = mix(color, fragColor, colorAmt);
    color.a *= opacity;

    gl_FragColor = color;
  }

}
