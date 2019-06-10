# color-id [![unstable](https://img.shields.io/badge/stability-unstable-green.svg)](http://github.com/badges/stability-badges) [![Build Status](https://img.shields.io/travis/colorjs/color-id.svg)](https://travis-ci.org/colorjs/color-id)

Convert color channels to single integer and back. Useful to get an id for a color.

[![npm install color-id](https://nodei.co/npm/color-id.png?mini=true)](https://npmjs.org/package/color-id/)

```js
const colorId = require('color-id');

colorId([.1, .5, .5, .1]); // 0x197f7f19
```

## `colorId(channels, normalized=true)`

Get id for normalized to 0..1 rgb[a] channel values. Optionally pass normalized flag to indicate that values are normalized to 0..1 range, defaults to `true`.

## `colorId.from(number, normalized=true)`

Get color channels values from the color id. Optionally pass normalized flag to align values to `0..1` range.

## Related

> [color-interpolate](https://github.com/dfcreative/color-interpolate) — interpolate color over palette, colormap or gradient.<br/>
> [color-rgba](https://github.com/dfcreative/color-rgba) — convert color string to rgba array.<br/>
> [color-alpha](https://github.com/dfcreative/color-alpha) — change alpha channel for a color.
