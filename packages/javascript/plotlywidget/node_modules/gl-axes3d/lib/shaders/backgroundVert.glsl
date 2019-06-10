precision highp float;

attribute vec3 position;
attribute vec3 normal;

uniform mat4 model, view, projection;
uniform vec3 enable;
uniform vec3 bounds[2];

varying vec3 colorChannel;

void main() {

  vec3 signAxis = sign(bounds[1] - bounds[0]);

  vec3 realNormal = signAxis * normal;

  if(dot(realNormal, enable) > 0.0) {
    vec3 minRange = min(bounds[0], bounds[1]);
    vec3 maxRange = max(bounds[0], bounds[1]);
    vec3 nPosition = mix(minRange, maxRange, 0.5 * (position + 1.0));
    gl_Position = projection * view * model * vec4(nPosition, 1.0);
  } else {
    gl_Position = vec4(0,0,0,0);
  }

  colorChannel = abs(realNormal);
}