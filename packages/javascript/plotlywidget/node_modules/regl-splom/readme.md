# regl-splom

Matrix of scatter plots. A wrapper over [regl-scatter2d](https://github.com/dy/regl-scatter2d) for optimized intersected data rendering.

* [x] minimal GPU memory footprint: N vs N*N in direct [regl-scatter2d](https://github.com/dy/regl-scatter2d) passes case.
* [ ] optimized performance due to binary trees for 1d point clustering, opposed to default 2d quad clustering.


## Usage

[![npm install regl-splom](https://nodei.co/npm/regl-splom.png?mini=true)](https://npmjs.org/package/regl-splom/)

```js
let regl = require('regl')({extensions: 'oes_element_index_uint'})
let createMatrix = require('regl-splom')

let scatterMatrix = createMatrix(regl)

// pass data and views to display
scatterMatrix.update(
	{ data: [[], [], ...], ranges, domains, viewport, size, color, border },
	{ data: [[], [], ...], ranges, domains, viewport, size, color, border }
)

// draw views by ids
scatterMatrix.draw(0, 1, ...views)
```

## API

### `splom = createSplom(regl)`

Creates scatter matrix instance.

### `splom.update(trace1, trace2, ...traces)`

Define passes for `draw` method. Every trace can include the following options:

Option | Description
---|---
`data` | An array with arrays for the columns.
`range` | Array with data ranges corresponding to `data`. Every range can be an array `[min, max]` or `[minX, minY, maxX, maxY]`. If undefined - detected automatically.
`domain` | Array with domains for the data, ie. the area data dimension holds  within the `viewport`. Each domain can be an array `[min, max]` for symmetric placement or `[minX, minY, maxX, maxY]` for precise position. Domain values are from `0..1` interval, defining what area of the `viewport` a dimension holds. By default domains cover viewport evnely.
`padding` | Padding within domains (in px), or list of paddings per-domain. By default `[0,0,0,0]`. Can be a number, an array or any [rectangle](https://github.com/dy/parse-rect) format.
`color`, `size`, `borderColor`, `borderSize`, `opacity` | Points style.
`marker` | Points marker.
`diagonal` | Show or hide diagonal.
`upper` | Show or hide upper half matrix.
`lower` | Show or hide lower half matrix.
`viewport` | Area that the plot holds within the canvas. Can take any [rectangle](https://github.com/dy/parse-rect) format.
<!-- `transpose` | Use transposed view of data, ie. swap columns and rows. -->
<!-- `normalizeDomain` | Normalize domains to fit the viewport. -->
<!-- `snap` | Enable snapping for the points, ie. hide invisible points -->


### `splom.draw(...ids?|...points?)`

Draw all defined passes, or only selected ones provided by `ids`. Optionally define point indexes to render.

```js
// draw 1 and 3 passes
splom.draw(1, 3)

// draw 1, 2 and 3 points from the first pass and 3 point from the second pass
splom.draw([1, 2, 3], [3])
```

### `splom.destroy()`

Dispose renderer and all the associated resources

## Related

* [regl-scatter2d](https://github.com/dy/regl-scatter2d)
* [regl-line2d](https://github.com/dy/regl-line2d)
* [regl-error2d](https://github.com/dy/regl-error2d)


## License

© 2018 Dmitry Yv. MIT License

Development supported by [plot.ly](https://github.com/plotly/).
