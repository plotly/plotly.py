precision mediump float;

float source1(vec3 p);
float source2(vec3 p);

#pragma glslify: map1 = require('./multiple-mapped-child', map = source1)
#pragma glslify: map2 = require('./multiple-mapped-child', map = source2)
#pragma glslify: map3 = require('./multiple-mapped-child', map = source1)

float source1(vec3 p) {
  return length(p) - 1.0;
}

float source2(vec3 p) {
  return length(p) - 2.0;
}

void main() {
  gl_FragColor = vec4(map1(), map2(), map3(), 1);
}
