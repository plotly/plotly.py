vec3 child(vec2 coord) {
  return vec3(g.zx - a * coord + b - c + float(e) * f, t);
}

#pragma glslify: export(child)
