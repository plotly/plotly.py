# canvas-fit [![stable](http://badges.github.io/stability-badges/dist/stable.svg)](http://github.com/badges/stability-badges)

Small module for fitting a canvas element within the bounds of its parent.
Useful, for example, for making a canvas fill the screen. Works with SVG
elements too!

## Usage

[![NPM](https://nodei.co/npm/canvas-fit.png)](https://nodei.co/npm/canvas-fit/)

### resize = fit(canvas[, parent[, scale]])

Creates a `resize` function for your `canvas` element. Calling this function
will resize the canvas to fit its parent element.

Here's a simple example to make your canvas update its dimensions when
resizing the window:

``` javascript
var fit = require('canvas-fit')
var canvas = document.createElement('canvas')

window.addEventListener('resize', fit(canvas), false)
```

You might want to override the `parent` element that the canvas should be
fitting within: in which case, pass that element in as your second argument:

``` javascript
window.addEventListener('resize'
  , fit(canvas, window)
  , false
)
```

You can also set the scale of the canvas element relative to its styled size
on the page using the `scale` argument – for example, passing in
`window.devicePixelRatio` here will scale the canvas resolution up on retina
displays.


### `resize.scale = <Number>`

Dynamically change the canvas' target `scale`. Note that you still need to
manually trigger a resize after doing this.


### `resize.parent = <DOMElement>`

Dynamically change the canvas' `parent` element. Note that you still need
to manually trigger a resize after doing this.

### `resize.parent = () => [width, height]`

Instead of filling a given element, explicitly set the width and height
of the canvas. Note that this value will still be scaled up according
to `resize.scale`

``` javascript
resize.parent = function() {
  return [ window.innerWidth - 300, window.innerHeight ]
}
```

## License

MIT. See [LICENSE.md](http://github.com/hughsk/canvas-fit/blob/master/LICENSE.md) for details.
