# glsl-token-defines

[![experimental](http://badges.github.io/stability-badges/dist/experimental.svg)](http://github.com/badges/stability-badges)

Retrieve the values defined with preprocessor statements in a selection of
[GLSL tokens](http://github.com/stackgl/glsl-tokenizer).

Doesn't handle full function-style macros for the time being. Patches welcome!

## Usage

[![NPM](https://nodei.co/npm/glsl-token-defines.png)](https://nodei.co/npm/glsl-token-defines/)

### `defs = defines(tokens)`

Where `tokens` is an array of tokens produced by
[glsl-tokenizer](http://github.com/stackgl/glsl-tokenizer).

Returns an dictionary object where keys are the name of the defined variable,
and values are the values of the defined variable. If a variable is not
assigned a value, this will be an empty string.

For example, the following:

``` glsl
#define PI 3.14
#define TAU (PI*2.)
#define VEC vec3(1.)
#define EMPTY
```

Would yield:

``` javascript
{
  PI: '3.14',
  TAU: '(PI*2.)',
  VEC: 'vec3(1.)',
  EMPTY: ''
}
```

## Contributing

See [stackgl/contributing](https://github.com/stackgl/contributing) for details.

## License

MIT. See [LICENSE.md](http://github.com/stackgl/glsl-token-defines/blob/master/LICENSE.md) for details.
