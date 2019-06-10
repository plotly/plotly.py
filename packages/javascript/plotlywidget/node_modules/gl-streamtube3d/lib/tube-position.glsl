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

// Calculate the tube vertex and normal at the given index.
//
// The returned vertex is for a tube ring with its center at origin, radius of length(d), pointing in the direction of d.
//
// Each tube segment is made up of a ring of vertices.
// These vertices are used to make up the triangles of the tube by connecting them together in the vertex array.
// The indexes of tube segments run from 0 to 8.
//
vec3 getTubePosition(vec3 d, float index, out vec3 normal) {
  float segmentCount = 8.0;

  float angle = 2.0 * 3.14159 * (index / segmentCount);

  vec3 u = getOrthogonalVector(d);
  vec3 v = normalize(cross(u, d));

  vec3 x = u * cos(angle) * length(d);
  vec3 y = v * sin(angle) * length(d);
  vec3 v3 = x + y;

  normal = normalize(v3);

  return v3;
}

#pragma glslify: export(getTubePosition)
