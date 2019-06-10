#pragma glslify: LightStruct = require(./struct)
#pragma glslify: export(another)

float alongside() {
  return 0.0;
}

float another(float n) {
  LightStruct b = LightStruct(vec3(0), vec4(0));
  return n * n + b.position + alongside() + t + u;
}

float another(float n, float c) {
  LightStruct b = LightStruct(vec3(0), vec4(0));
  return n * n + b.position + another(c) + t + u - v;
}
