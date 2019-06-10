# glsl-inverse
Invert a matrix in GLSL.

# Example

```glsl
#pragma glslify: inverse = require(glsl-inverse)

void main() {
  mat3 m = mat3(1, 2, -3,
                4, 0, 6,
                7.1, 8, 9);

  mat3 mi = inverse(m);

  //now mi is the inverse of m
}
```

# Usage

Install with npm:

```
npm install glsl-inverse
```

Then use with [glslify](https://github.com/stackgl/glslify).

# API

```glsl
#pragma glslify: inverse = require(glsl-inverse)
```

### `mi = inverse(float|mat2|mat3|mat4 m)`
Computes inverse of m

* `m` is a matrix to invert, either `float, mat2, mat3` or `mat4`

**Returns** The inverse of `m`

# License
(c) 2014 Mikola Lysenko. MIT License