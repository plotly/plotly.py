precision highp float;

attribute vec4 uv;
attribute vec3 f;
attribute vec3 normal;

uniform vec3 objectOffset;
uniform mat4 model, view, projection, inverseModel;
uniform vec3 lightPosition, eyePosition;
uniform sampler2D colormap;

varying float value, kill;
varying vec3 worldCoordinate;
varying vec2 planeCoordinate;
varying vec3 lightDirection, eyeDirection, surfaceNormal;
varying vec4 vColor;

void main() {
  vec3 localCoordinate = vec3(uv.zw, f.x);
  worldCoordinate = objectOffset + localCoordinate;
  vec4 worldPosition = model * vec4(worldCoordinate, 1.0);
  vec4 clipPosition = projection * view * worldPosition;
  gl_Position = clipPosition;
  kill = f.y;
  value = f.z;
  planeCoordinate = uv.xy;

  vColor = texture2D(colormap, vec2(value, value));

  //Lighting geometry parameters
  vec4 cameraCoordinate = view * worldPosition;
  cameraCoordinate.xyz /= cameraCoordinate.w;
  lightDirection = lightPosition - cameraCoordinate.xyz;
  eyeDirection   = eyePosition - cameraCoordinate.xyz;
  surfaceNormal  = normalize((vec4(normal,0) * inverseModel).xyz);
}
