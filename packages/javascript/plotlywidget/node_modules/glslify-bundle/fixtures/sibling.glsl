#pragma glslify: another_thing = require(./another, t = v = 4.0, u = uVec.x)
#pragma glslify: LightStruct   = require(./struct)

float sibling(float a) {
  LightStruct b = LightStruct(vec3(0), vec4(0));
  return a * another_thing(b.color + 2.0);
}

#pragma glslify: export(sibling)
