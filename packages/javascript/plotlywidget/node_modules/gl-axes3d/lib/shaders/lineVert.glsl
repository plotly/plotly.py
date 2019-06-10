precision highp float;

attribute vec3 position;

uniform mat4 model, view, projection;
uniform vec3 offset, majorAxis, minorAxis, screenAxis;
uniform float lineWidth;
uniform vec2 screenShape;

vec3 project(vec3 p) {
  vec4 pp = projection * view * model * vec4(p, 1.0);
  return pp.xyz / max(pp.w, 0.0001);
}

void main() {
  vec3 major = position.x * majorAxis;
  vec3 minor = position.y * minorAxis;

  vec3 vPosition = major + minor + offset;
  vec3 pPosition = project(vPosition);
  vec3 offset = project(vPosition + screenAxis * position.z);

  vec2 screen = normalize((offset - pPosition).xy * screenShape) / screenShape;

  gl_Position = vec4(pPosition + vec3(0.5 * screen * lineWidth, 0), 1.0);
}
