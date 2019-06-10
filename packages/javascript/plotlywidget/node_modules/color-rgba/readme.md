# color-rgba [![Build Status](https://travis-ci.org/colorjs/color-rgba.png)](https://travis-ci.org/colorjs/color-rgba)

Convert color string to array with rgba channel values: `rgba(127,127,127,.1)` → `[127,127,127,.1]`.

## Usage

[![npm install color-rgba](https://nodei.co/npm/color-rgba.png?mini=true)](https://npmjs.org/package/color-rgba/)

```js
const rgba = require('color-rgba')

rgba('red') // [255, 0, 0, 1]
rgba('rgb(80, 120, 160)') // [80, 120, 160, 1]
rgba('rgba(80, 120, 160, .5)') // [80, 120, 160, .5]
rgba('hsla(109, 50%, 50%, .75)') // [87.125, 191.25, 63.75, .75]
```

## API

### `let [r, g, b, alpha] = rgba(color)`

Returns channels values as they are in the input `color` string argument. `alpha` is always from `0..1` range. `color` can be a CSS color string, an array with channel values, an object etc., see [color-parse](https://ghub.io/color-parse).

## Related

* [color-normalize](https://github.com/colorjs/color-normalize) − convert any input color argument into a defined output format.
* [color-alpha](https://github.com/colorjs/color-alpha) − change alpha of a color string.
* [color-interpolate](https://github.com/colorjs/color-interpolate) − interpolate by color palette.

## License

(c) 2017 Dima Yv. MIT License
