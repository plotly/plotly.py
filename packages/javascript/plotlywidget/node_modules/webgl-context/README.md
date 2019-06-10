# webgl-context

[![stable](http://badges.github.io/stability-badges/dist/stable.svg)](http://github.com/badges/stability-badges)

Grabs a WebGLRenderingContext, returning null if it doesn't exist. Similar to [2d-context](https://nodei.co/npm/2d-context/).

```js
//get a webgl context, will be null if not found
var gl = require('webgl-context')()

if (gl) {
    document.body.appendChild(gl.canvas)
    //do something...
}
```

Or, with options:

```js
//or with optional settings...
var gl = require('webgl-context')({
    canvas: canvas, //the canvas DOM element to use
    width: 400, //resizes the canvas..
    height: 200, 
    antialias: true //can specify custom attributes here
})
```

## Usage

[![NPM](https://nodei.co/npm/webgl-context.png)](https://nodei.co/npm/webgl-context/)

#### `ctx = require('webgl-context')([opt])`

Gets a new canvas context with optional parameters:

- `canvas` a canvas element to use, otherwise creates a new element
- `width` a width to set, otherwise no change
- `height` a height to set, otherwise no change
- other attributes are passed to the getContext call, like `alpha` and `antialias`

You can then get a reference of the canvas element with `ctx.canvas`. 

## See Also

- [get-canvas-context](https://www.npmjs.com/package/get-canvas-context)
- [2d-context](https://www.npmjs.com/package/2d-context)

## License

MIT, see [LICENSE.md](http://github.com/mattdesl/webgl-context/blob/master/LICENSE.md) for details.
