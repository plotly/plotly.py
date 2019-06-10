bool outOfRange(float a, float b, float p) {
  return ((p > max(a, b)) || 
          (p < min(a, b)));
}

bool outOfRange(vec2 a, vec2 b, vec2 p) {
  return (outOfRange(a.x, b.x, p.x) ||
          outOfRange(a.y, b.y, p.y));
}

bool outOfRange(vec3 a, vec3 b, vec3 p) {
  return (outOfRange(a.x, b.x, p.x) ||
          outOfRange(a.y, b.y, p.y) ||
          outOfRange(a.z, b.z, p.z));
}

bool outOfRange(vec4 a, vec4 b, vec4 p) {
  return outOfRange(a.xyz, b.xyz, p.xyz);
}

#pragma glslify: export(outOfRange)
