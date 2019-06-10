precision mediump float;

uniform mat4 uProj;
uniform mat4 uView;

float x = 0.0;
float y = 0.0;

struct Thing {
  float prop1;
  float prop2;
  float prop3;
};

uniform Thing uniformThing;
uniform struct Another {
  float prop1;
} uniformAnother;

float _dim(float x, float y);
float _dim(float x, float y) {
  return x + y;
}

void main() {
  Thing y = Thing(sin(.0), .5, 1.);

  y.prop1;
  y.prop2;
  y.prop3;

  uniformThing.prop1;
  uniformThing.prop2;
  uniformThing.prop3 = 2.0;
  uniformAnother.prop1;

  for (int i = 0; i < 3; i++) {
    vec[i];

    float x = 10.0;
    Thing uniformThing;
    uniformThing.prop1;
  }

  uProj[0].x;
  gl_FragColor = vec4(x, vec3(1));
}
