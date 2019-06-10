precision mediump float;

attribute vec2 position;
attribute vec4 pickId;

uniform mat3 matrix;
uniform float pointSize;
uniform vec4 pickOffset;

varying vec4 fragId;

void main() {
  vec3 hgPosition = matrix * vec3(position, 1);
  gl_Position  = vec4(hgPosition.xy, 0, hgPosition.z);
  gl_PointSize = pointSize;

  vec4 id = pickId + pickOffset;
  id.y += floor(id.x / 256.0);
  id.x -= floor(id.x / 256.0) * 256.0;

  id.z += floor(id.y / 256.0);
  id.y -= floor(id.y / 256.0) * 256.0;

  id.w += floor(id.z / 256.0);
  id.z -= floor(id.z / 256.0) * 256.0;

  fragId = id;
}
