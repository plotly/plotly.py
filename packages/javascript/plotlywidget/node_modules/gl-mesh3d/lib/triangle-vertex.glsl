precision highp float;

attribute vec3 position, normal;
attribute vec4 color;
attribute vec2 uv;

uniform mat4 model
           , view
           , projection
           , inverseModel;
uniform vec3 eyePosition
           , lightPosition;

varying vec3 f_normal
           , f_lightDirection
           , f_eyeDirection
           , f_data;
varying vec4 f_color;
varying vec2 f_uv;

vec4 project(vec3 p) {
  return projection * view * model * vec4(p, 1.0);
}

void main() {
  gl_Position      = project(position);

  //Lighting geometry parameters
  vec4 cameraCoordinate = view * vec4(position , 1.0);
  cameraCoordinate.xyz /= cameraCoordinate.w;
  f_lightDirection = lightPosition - cameraCoordinate.xyz;
  f_eyeDirection   = eyePosition - cameraCoordinate.xyz;
  f_normal  = normalize((vec4(normal, 0.0) * inverseModel).xyz);

  f_color          = color;
  f_data           = position;
  f_uv             = uv;
}
