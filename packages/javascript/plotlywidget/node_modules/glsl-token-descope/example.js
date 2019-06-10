var tokenize  = require('glsl-tokenizer/string')
var descope   = require('./')
var stringify = require('glsl-token-string')

var src =
[ 'precision mediump float;'
,
, 'uniform mat4  top1;'
, 'uniform float top2;'
,
, 'void main() {'
,   '  float x = 1.0;'
,   '  gl_FragColor = vec4(vec3(x), top2);'
, '}'
].join('\n')

var tokens = tokenize(src)

console.log(stringify(descope(tokens)))
