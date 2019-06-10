precision mediump float;

attribute vec3 aPosition;
attribute vec3 aNormal;

uniform mat4 uProj;
uniform mat4 uView;
uniform mat4 uModel;

varying float vLight;

struct x {
  float y;
  float z;
};

void main( void ) {
  vLight = dot(aNormal, vec3(0, 1, 0));
  gl_Position = uProj * uView * uModel * vec4(aPosition, 1);
}
