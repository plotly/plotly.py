# regl-line2d [![experimental](https://img.shields.io/badge/stability-unstable-green.svg)](http://github.com/badges/stability-badges)

Draw polyline with regl.

![regl-line2d](https://github.com/dy/regl-line2d/blob/master/preview.png?raw=true)

Remake on [gl-line2d](https://github.com/gl-vis/gl-line2d):

* GPU join calculation.
* Bevel, round and rectangular joins.
* Dash patterns.
* Self-overlapping and sharp angles cases.
* Multiline rendering.
* Float64 precision.
* [`<polyline>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Element/polyline)-compatible API

[Demo](https://a-vis.github.io/regl-line2d).

## Usage

[![npm install regl-line2d](https://nodei.co/npm/regl-line2d.png?mini=true)](https://npmjs.org/package/regl-line2d/)

```js
let regl = require('regl')({extensions: 'angle_instanced_arrays'})
let line2d = require('regl-line2d')(regl)

// draw red triangle
line2d.render({ thickness: 4, points: [0,0, 1,1, 1,0], close: true, color: 'red' })
```

### `line2d.render(options|list?)`

Draw line or multiple lines and update options, once per frame at most.

Option | Default | Description
---|---|---
`positions`, `points`, `data` | `[]` | Point coordinates, eg. `[0,0, 1,1, 0,2, 1,-1]` or `[[0,0], [1,1], [0,2], [1,-1]]`.
`color`, `colors`, `stroke` | `black` | CSS color string or an array with `0..1` values, eg. `'red'` or `[0, 0, 0, 1]`.
`fill` | `null` | Fill area enclosed by line with defined color.
`opacity` | `1` | Line transparency regardless of color.
`thickness`, `lineWidth`, `width`, `strokeWidth` | `1` | Line width in px.
`dashes`, `dash`, `dasharray` | `null` | Array with dash lengths in px, altering color/space pairs, ie. `[2,10, 5,10, ...]`. `null` corresponds to solid line.
`join`, `type` | `bevel` | Join style: `'rect'`, `'round'`, `'bevel'`. Applied to caps too.
`miterLimit` | `1` | Max ratio of the join length to the thickness.
`close`, `closed`, `closePath` | `false` | Connect last point with the first point with a segment.
`overlay` | `false` | Enable overlay of line segments.
`range`, `dataBox` | `null` | Visible data range.
`viewport`, `viewBox` | `null` | Area within canvas, an array `[left, top, right, bottom]` or an object `{x, y, w, h}` or `{left, top, bottom, right}`.

To render multiple lines pass an array with options for every line as `list`:

```js
line2d.render([
  {thickness: 2, points: [0,0, 1,1], color: 'blue'},
  {thickness: 2, points: [0,1, 1,0], color: 'blue'}
])
```

`null` argument will destroy `line2d` instance and dispose resources.

### `line2d.update(options|list)`

Update line(s) not incurring redraw.

### `line2d.draw(id?)`

Draw lines from last updated options. `id` integer can specify a single line from the `list` to redraw.

### `line2d.destroy()`

Dispose `line2d` and associated resources.


## Related

* [regl-scatter2d](https://github.com/dy/regl-scatter2d)
* [regl-error2d](https://github.com/dy/regl-error2d)

## Similar

* [regl-line-builder](https://github.com/jpweeks/regl-line-builder)

## License

(c) 2017 Dima Yv. MIT License

Development supported by [plot.ly](https://github.com/plotly/).
