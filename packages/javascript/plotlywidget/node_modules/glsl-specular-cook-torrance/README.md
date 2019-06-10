# glsl-specular-cook-torrance

Computes the specular power in the Cook-Torrance model.

# Example

```glsl
#pragma glslify: cookTorranceSpec = require(glsl-specular-cook-torrance)

uniform vec3 eyePosition;
uniform vec3 lightPosition;

uniform float roughness, fresnel;

varying vec3 surfacePosition, surfaceNormal;

void main() {
  //Light and view geometry
  vec3 viewDirection = normalize(eyePosition - surfacePosition);
  vec3 lightDirection = normalize(lightPosition - surfacePosition);

  //Surface properties
  vec3 normal = normalize(surfaceNormal);
  
  //Compute specular power
  float power = cookTorranceSpec(
    lightDirection, 
    viewDirection, 
    normal, 
    roughness,
    fresnel);

  gl_FragColor = vec4(power,power,power,1.0);
}
```

# Usage

Install with npm:

```
npm install glsl-specular-phong
```

Then use with [glslify](https://github.com/stackgl/glslify).

# API

```glsl
#pragma glslify: cookTorrance = require(glsl-specular-cook-torrance)
```

##### `float cookTorrance(vec3 lightDir, vec3 eyeDir, vec3 normal, float roughness, float fresnel)`
Computes the specular power in the Cook-Torrance

* `lightDir` is a *unit length* `vec3` pointing from the surface point toward the light
* `eyeDir` is a *unit length* `vec3` pointing from the surface point toward the camera
* `normal` is the *unit length* surface normal at the sample point
* `roughness` is the surface roughness parameter, between 0 and 1.  0 means surface is perfectly smooth, 1 means surface is matte
* `fresnel` the Fresnel exponent.  0 = no Fresnel, higher values create a rim effect around objects

**Returns** A `float` representing the specular power

**Note** Unlike the usual Cook-Torrance model, the light power is not scaled by 1/(normal . lightDirection).  This avoids an unnecessary numerically unstable division, but requires modifying how diffuse light is calculated.

# License
(c) 2014 Mikola Lysenko. MIT License