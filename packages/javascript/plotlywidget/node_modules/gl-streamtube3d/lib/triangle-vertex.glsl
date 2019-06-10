precision highp float;

#pragma glslify: getTubePosition = require(./tube-position.glsl)

attribute vec4 vector;
attribute vec4 color, position;
attribute vec2 uv;
uniform float vectorScale;
uniform float tubeScale;

uniform mat4 model
           , view
           , projection
           , inverseModel;
uniform vec3 eyePosition
           , lightPosition;

varying vec3 f_normal
           , f_lightDirection
           , f_eyeDirection
           , f_data
           , f_position;
varying vec4 f_color;
varying vec2 f_uv;

void main() {
  // Scale the vector magnitude to stay constant with
  // model & view changes.
  vec3 normal;
  vec3 XYZ = getTubePosition(mat3(model) * (tubeScale * vector.w * normalize(vector.xyz)), position.w, normal);
  vec4 tubePosition = model * vec4(position.xyz, 1.0) + vec4(XYZ, 0.0);

  //Lighting geometry parameters
  vec4 cameraCoordinate = view * tubePosition;
  cameraCoordinate.xyz /= cameraCoordinate.w;
  f_lightDirection = lightPosition - cameraCoordinate.xyz;
  f_eyeDirection   = eyePosition - cameraCoordinate.xyz;
  f_normal = normalize((vec4(normal,0.0) * inverseModel).xyz);

  // vec4 m_position  = model * vec4(tubePosition, 1.0);
  vec4 t_position  = view * tubePosition;
  gl_Position      = projection * t_position;

  f_color          = color;
  f_data           = tubePosition.xyz;
  f_position       = position.xyz;
  f_uv             = uv;
}
