precision highp float;

#pragma glslify: beckmann = require(glsl-specular-beckmann)
#pragma glslify: outOfRange = require(glsl-out-of-range)

uniform vec3 lowerBound, upperBound;
uniform float contourTint;
uniform vec4 contourColor;
uniform sampler2D colormap;
uniform vec3 clipBounds[2];
uniform float roughness, fresnel, kambient, kdiffuse, kspecular, opacity;
uniform float vertexColor;

varying float value, kill;
varying vec3 worldCoordinate;
varying vec3 lightDirection, eyeDirection, surfaceNormal;
varying vec4 vColor;

void main() {
  if ((kill > 0.0) ||
      (outOfRange(clipBounds[0], clipBounds[1], worldCoordinate))) discard;

  vec3 N = normalize(surfaceNormal);
  vec3 V = normalize(eyeDirection);
  vec3 L = normalize(lightDirection);

  if(gl_FrontFacing) {
    N = -N;
  }

  float specular = max(beckmann(L, V, N, roughness), 0.);
  float diffuse  = min(kambient + kdiffuse * max(dot(N, L), 0.0), 1.0);

  //decide how to interpolate color — in vertex or in fragment
  vec4 surfaceColor =
    step(vertexColor, .5) * texture2D(colormap, vec2(value, value)) +
    step(.5, vertexColor) * vColor;

  vec4 litColor = surfaceColor.a * vec4(diffuse * surfaceColor.rgb + kspecular * vec3(1,1,1) * specular,  1.0);

  gl_FragColor = mix(litColor, contourColor, contourTint) * opacity;
}
