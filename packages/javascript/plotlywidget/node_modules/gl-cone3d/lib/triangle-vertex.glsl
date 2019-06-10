precision highp float;

#pragma glslify: getConePosition = require(./cone-position.glsl)

attribute vec3 vector;
attribute vec4 color, position;
attribute vec2 uv;
uniform float vectorScale;
uniform float coneScale;

uniform float coneOffset;

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
  vec3 XYZ = getConePosition(mat3(model) * ((vectorScale * coneScale) * vector), position.w, coneOffset, normal);
  vec4 conePosition = model * vec4(position.xyz, 1.0) + vec4(XYZ, 0.0);

  //Lighting geometry parameters
  vec4 cameraCoordinate = view * conePosition;
  cameraCoordinate.xyz /= cameraCoordinate.w;
  f_lightDirection = lightPosition - cameraCoordinate.xyz;
  f_eyeDirection   = eyePosition - cameraCoordinate.xyz;
  f_normal = normalize((vec4(normal,0.0) * inverseModel).xyz);

  // vec4 m_position  = model * vec4(conePosition, 1.0);
  vec4 t_position  = view * conePosition;
  gl_Position      = projection * t_position;

  f_color          = color;
  f_data           = conePosition.xyz;
  f_position       = position.xyz;
  f_uv             = uv;
}
