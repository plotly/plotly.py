#pragma glslify: Ray = require('./complex-ray.glsl')
#pragma glslify: RayResult = require('./complex-ray-result.glsl')

RayResult rayBail() {
  return RayResult(0.0, 0.0, false);
}

RayResult march(Ray source, float maxd, float precis) {
  float latest = precis * 2.0;
  float dist = +0.0;
  float type = -1.0;
  RayResult res = rayBail();

  for (int i = 0; i < 99; i++) {
    if (latest < precis || dist > maxd) break;

    res = map(source.ro + source.rd * dist);
    dist += res.d;
  }

  if(dist >= maxd) {
    return rayBail();
  }

  return res;
}

RayResult march(Ray ray) {
  return march(ray, 20.0, 0.001);
}

#pragma glslify: export(march)
