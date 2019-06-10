# glsl-token-assignments

[![experimental](http://badges.github.io/stability-badges/dist/experimental.svg)](http://github.com/badges/stability-badges)

Take an array of GLSL tokens and determine which tokens are either assignments
or variable declarations.

## Usage

[![NPM](https://nodei.co/npm/glsl-token-assignments.png)](https://nodei.co/npm/glsl-token-assignments/)

### `assignments(tokens)`

Takes an array of GLSL tokens from
[`glsl-tokenizer`](http://github.com/stackgl/glsl-tokenizer) and sets the
following boolean values for each `ident` token, i.e. any variable names:

#### `token.assignment`

If the value of the variable is being changed here.

#### `token.declaration`

If a new variable is being defined here for this scope.

#### `token.structMember`

If this token is specifying a new struct member, e.g.:

``` glsl
struct X {
  float member1;
  float member2;
};
```

The `tokens` array will be modified in-place.

## License

MIT. See [LICENSE.md](http://github.com/stackgl/glsl-token-assignments/blob/master/LICENSE.md) for details.
