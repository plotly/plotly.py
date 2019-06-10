precision mediump float;

varying vec4 fragId;
varying vec2 vWeight;

uniform vec2 shape;
uniform vec4 pickOffset;

void main() {
  vec2 d = step(.5, vWeight);
  vec4 id = fragId + pickOffset;
  id.x += d.x + d.y*shape.x;

  id.y += floor(id.x / 256.0);
  id.x -= floor(id.x / 256.0) * 256.0;

  id.z += floor(id.y / 256.0);
  id.y -= floor(id.y / 256.0) * 256.0;

  id.w += floor(id.z / 256.0);
  id.z -= floor(id.z / 256.0) * 256.0;

  gl_FragColor = id/255.;
}
