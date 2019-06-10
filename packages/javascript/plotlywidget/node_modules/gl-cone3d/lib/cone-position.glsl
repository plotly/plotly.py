precision highp float;

vec3 getOrthogonalVector(vec3 v) {
  // Return up-vector for only-z vector.
  // Return ax + by + cz = 0, a point that lies on the plane that has v as a normal and that isn't (0,0,0).
  // From the above if-statement we have ||a|| > 0  U  ||b|| > 0.
  // Assign z = 0, x = -b, y = a:
  // a*-b + b*a + c*0 = -ba + ba + 0 = 0
  if (v.x*v.x > v.z*v.z || v.y*v.y > v.z*v.z) {
    return normalize(vec3(-v.y, v.x, 0.0));
  } else {
    return normalize(vec3(0.0, v.z, -v.y));
  }
}

// Calculate the cone vertex and normal at the given index.
//
// The returned vertex is for a cone with its top at origin and height of 1.0,
// pointing in the direction of the vector attribute.
//
// Each cone is made up of a top vertex, a center base vertex and base perimeter vertices.
// These vertices are used to make up the triangles of the cone by the following:
//   segment + 0 top vertex
//   segment + 1 perimeter vertex a+1
//   segment + 2 perimeter vertex a
//   segment + 3 center base vertex
//   segment + 4 perimeter vertex a
//   segment + 5 perimeter vertex a+1
// Where segment is the number of the radial segment * 6 and a is the angle at that radial segment.
// To go from index to segment, floor(index / 6)
// To go from segment to angle, 2*pi * (segment/segmentCount)
// To go from index to segment index, index - (segment*6)
//
vec3 getConePosition(vec3 d, float rawIndex, float coneOffset, out vec3 normal) {

  const float segmentCount = 8.0;

  float index = rawIndex - floor(rawIndex /
    (segmentCount * 6.0)) *
    (segmentCount * 6.0);

  float segment = floor(0.001 + index/6.0);
  float segmentIndex = index - (segment*6.0);

  normal = -normalize(d);

  if (segmentIndex > 2.99 && segmentIndex < 3.01) {
    return mix(vec3(0.0), -d, coneOffset);
  }

  float nextAngle = (
    (segmentIndex > 0.99 &&  segmentIndex < 1.01) ||
    (segmentIndex > 4.99 &&  segmentIndex < 5.01)
  ) ? 1.0 : 0.0;
  float angle = 2.0 * 3.14159 * ((segment + nextAngle) / segmentCount);

  vec3 v1 = mix(d, vec3(0.0), coneOffset);
  vec3 v2 = v1 - d;

  vec3 u = getOrthogonalVector(d);
  vec3 v = normalize(cross(u, d));

  vec3 x = u * cos(angle) * length(d)*0.25;
  vec3 y = v * sin(angle) * length(d)*0.25;
  vec3 v3 = v2 + x + y;
  if (segmentIndex < 3.0) {
    vec3 tx = u * sin(angle);
    vec3 ty = v * -cos(angle);
    vec3 tangent = tx + ty;
    normal = normalize(cross(v3 - v1, tangent));
  }

  if (segmentIndex == 0.0) {
    return mix(d, vec3(0.0), coneOffset);
  }
  return v3;
}

#pragma glslify: export(getConePosition)
