#pragma glslify: distribution = require(./distribution.glsl)

float beckmannSpecular(
  vec3 lightDirection,
  vec3 viewDirection,
  vec3 surfaceNormal,
  float roughness) {
  return distribution(dot(surfaceNormal, normalize(lightDirection + viewDirection)), roughness);
}

#pragma glslify: export(beckmannSpecular)