precision mediump float;
#define GLSLIFY 1
struct Thing{float b;float c;};vec4 someFunction(vec2 b,vec2 c,vec3 d){return vec4(d,c.y);}void main(){gl_FragColor=someFunction(vec2(0),vec2(1),vec3(2));}
