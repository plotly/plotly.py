precision mediump float;

#pragma glslify: RayResult = require('./complex-ray-result')
#pragma glslify: Ray = require('./complex-ray')

RayResult doModel(vec3 p);

#pragma glslify: march = require('./complex-march', map = doModel)

RayResult doModel(vec3 p) {
  float d = length(p);
  float id = 1.0;

  return RayResult(d, id, true);
}

void main() {
  vec3 color = vec3(0);
  vec3 rd = normalize(vec3(1));
  vec3 ro = vec3(0);

  RayResult t = march(Ray(ro, rd));

  if (t.hit) {
    color = vec3(t.d);
  }

  gl_FragColor = vec4(color, 1);
}
