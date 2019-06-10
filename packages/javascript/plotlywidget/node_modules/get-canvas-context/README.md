# get-canvas-context

[![stable](http://badges.github.io/stability-badges/dist/stable.svg)](http://github.com/badges/stability-badges)

Creates a new HTML5 Canvas Context with the given dimensions and options. Returns `null` if not supported.

Supports `'webgl'`, `'webgl2'` and `'2d'`, handles vendor prefixing, and runs in Node and the Browser.

## Install

```sh
npm install get-canvas-context --save
```

## Example

```js
var getContext = require('get-canvas-context')

// create a new 50x50 2D canvas
var ctx = getContext('2d', {
  width: 50,
  height: 50
})

// add to DOM
document.body.appendChild(ctx.canvas)

// draw to it
ctx.fillRect(0, 0, 50, 50)
```

Or, WebGL using an existing canvas:

```js
var canvas = document.createElement('canvas')

var gl = getContext('webgl', {
  canvas: canvas,
  antialias: true
})

if (!gl) {
  throw new Error('webgl not supported')
}
```

## Usage

[![NPM](https://nodei.co/npm/get-canvas-context.png)](https://www.npmjs.com/package/get-canvas-context)

#### `ctx = createContext(type, [opt])`

Returns a new canvas context for the given `type`, a string which is either `'2d'`, `'webgl'` or `'webgl2'`. The options:

- `canvas` - an existing canvas element to re-use rather than creating a new one
- `width` - if specified, will set the canvas width
- `height` - if specified, will set the canvas height
- `{...contextAttributes}` any other options for the rendering context, like `alpha`

Handles vendor prefixing for WebGL contexts. Returns `null` if we are not in a browser, or if the context is not available, or if there was an error creating the context.

**Note:** As of the time of writing (Jun 2015), `"webgl2"` is only supported through special flags in Chrome Canary and FireFox Nightly.

## License

MIT, see [LICENSE.md](http://github.com/Jam3/get-canvas-context/blob/master/LICENSE.md) for details.
