precision mediump float;

attribute vec2 position;
attribute vec4 pickId;
attribute vec2 weight;

uniform vec2 shape;
uniform mat3 viewTransform;

varying vec4 fragId;
varying vec2 vWeight;

void main() {
  vWeight = weight;

  fragId = pickId;

  vec3 vPosition = viewTransform * vec3( position + (weight-.5)/(shape-1.) , 1.0);
  gl_Position = vec4(vPosition.xy, 0, vPosition.z);
}
