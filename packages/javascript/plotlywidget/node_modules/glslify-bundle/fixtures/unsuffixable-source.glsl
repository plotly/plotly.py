struct Ray {
  vec3 origin;
  vec3 direction;
} ray1;

const Ray ray2 = Ray(vec3(0), vec3(0, 1, 0));
const vec2 vec = vec2(0.0);
const float pi = 6.28;

#pragma glslify: n = require('./unsuffixable-child', a = vec.x, b = 5.0, c = vec, e = 2, f = ray1.origin.xy, t = pi, g = ray2.direction)

void runner(in vec2 fragCoord) {
  gl_FragColor = vec4(n(fragCoord + vec2(d + h)), 1.0);
}


#pragma glslify: export(runner)
