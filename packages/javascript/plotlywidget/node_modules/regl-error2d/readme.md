# regl-error2d [![experimental](https://img.shields.io/badge/stability-unstable-green.svg)](http://github.com/badges/stability-badges)

Draw error bars for a set of points with regl.

![regl-error2d](https://github.com/dy/regl-error2d/blob/master/preview.png?raw=true)

Remake on [gl-error2d](https://github.com/gl-vis/gl-error2d):

* `color` may define per-bar colors.
* max number of points extended 40 times (from `1e5` to `4e6`) via instanced draw.
* `lineWidth` and `capSize` are adjusted to actual pixels.
* enhanced performance via vertex shader.

[Demo](https://dy.github.io/regl-error2d).

## Usage

[![npm install regl-error2d](https://nodei.co/npm/regl-error2d.png?mini=true)](https://npmjs.org/package/regl-error2d/)

```js
let regl = require('regl')({extensions: 'angle_instanced_arrays'})
let createError2d = require('regl-error2d')

let error2d = createError2d(regl)

error2d({
  positions: [0,0, .5,0, ...],
  errors: [.5,.5,.5,.6, .2,.3,.4,.1, ...],
  color: 'rgba(0, 100, 200, .75)'
})
```

### `createError2d(regl, options?)`

Create new error2d instance from `regl` and initial `options`. Note that `regl` instance should have `ANGLE_instanced_arrays` extension enabled.

### `error2d(options|list?)`

Draw errors, update options.

Option | Default | Description
---|---|---
`positions`, `points`, `data` | `[]` | An array of unrolled xy coordinates of the points as `[x,y, x,y, ...]` or array of points `[[x,y], [x,y], ...]`.
`errors`, `error` | `[]` | Array with error values corresponding to the points `[e0l,e0r,e0b,e0t, e1l,e1r,e1b,e1t, ...]`
`capSize`, `cap` | `5` | Error bar cap size, in pixels
`lineWidth`, `thickness` | `1` | Error bar line width, in pixels
`color`, `colors` | `'red'` | Color or array with colors. Each color can be a css color string or an array with float `0..1` values.
`opacity` | `1` | Error bars opacity.
`range`, `dataBox` | `null` | Visible data range.
`viewport`, `viewBox` | `null` | Output area within the canvas.

A list of options can be passed for batch rendering:

```js
error2d([options1, options2, ...])
```

### `error2d.update(options|list)`

Update options, not incurring redraw.

### `error2d.draw(id?)`

Draw errors based on last options. `id` integer can specify a list item to redraw from batch update.

### `error2d.destroy()`

Dispose error2d and associated resources.


## License

(c) 2017 Dima Yv. MIT License

Development supported by plot.ly.
