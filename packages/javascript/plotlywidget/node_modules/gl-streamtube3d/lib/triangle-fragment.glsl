#extension GL_OES_standard_derivatives : enable

precision highp float;

#pragma glslify: cookTorrance = require(glsl-specular-cook-torrance)
#pragma glslify: outOfRange = require(glsl-out-of-range)

uniform vec3 clipBounds[2];
uniform float roughness
            , fresnel
            , kambient
            , kdiffuse
            , kspecular
            , opacity;
uniform sampler2D texture;

varying vec3 f_normal
           , f_lightDirection
           , f_eyeDirection
           , f_data
           , f_position;
varying vec4 f_color;
varying vec2 f_uv;

void main() {
  if (outOfRange(clipBounds[0], clipBounds[1], f_position)) discard;
  vec3 N = normalize(f_normal);
  vec3 L = normalize(f_lightDirection);
  vec3 V = normalize(f_eyeDirection);

  if(gl_FrontFacing) {
    N = -N;
  }

  float specular = min(1.0, max(0.0, cookTorrance(L, V, N, roughness, fresnel)));
  float diffuse  = min(kambient + kdiffuse * max(dot(N, L), 0.0), 1.0);

  vec4 surfaceColor = f_color * texture2D(texture, f_uv);
  vec4 litColor = surfaceColor.a * vec4(diffuse * surfaceColor.rgb + kspecular * vec3(1,1,1) * specular,  1.0);

  gl_FragColor = litColor * opacity;
}
