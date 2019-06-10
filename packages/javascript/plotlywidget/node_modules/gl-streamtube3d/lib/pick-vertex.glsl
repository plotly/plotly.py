precision highp float;

#pragma glslify: getTubePosition = require(./tube-position.glsl)

attribute vec4 vector;
attribute vec4 position;
attribute vec4 id;

uniform mat4 model, view, projection;
uniform float tubeScale;

varying vec3 f_position;
varying vec4 f_id;

void main() {
  vec3 normal;
  vec3 XYZ = getTubePosition(mat3(model) * (tubeScale * vector.w * normalize(vector.xyz)), position.w, normal);
  vec4 tubePosition = model * vec4(position.xyz, 1.0) + vec4(XYZ, 0.0);

  gl_Position = projection * view * tubePosition;
  f_id        = id;
  f_position  = position.xyz;
}
