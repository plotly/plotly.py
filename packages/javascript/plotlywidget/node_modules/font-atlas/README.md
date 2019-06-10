# font-atlas [![experimental](http://badges.github.io/stability-badges/dist/experimental.svg)](http://github.com/badges/stability-badges)

Populate a `<canvas>` element with a font texture atlas – can be used to quickly generate bitmap fonts.

## Usage

[![NPM](https://nodei.co/npm/font-atlas.png)](https://nodei.co/npm/font-atlas/)

### canvas = fontAtlas([options])

Populates and returns a `<canvas>` element with a font texture atlas. Takes
the following options:

* `canvas`: use an existing `<canvas>` element. By default, a new one will
  be created for you.
* `font`: the font family to use when drawing the text. Can be a [css font](https://developer.mozilla.org/en-US/docs/Web/CSS/font) string or an object with font properties: `size`, `family`, `style`, `weight`, `variant`, `stretch`.
* `shape`: an array containing the `[width, height]` for the canvas in pixels.
  Default: `[512, 512]`.
* `step`: an array containing the `[width, height]` for each cell in pixels.
  Default: `[32, 32]`.
* `chars`: may be one of either:
  * a string containing all of the characters to use.
  * an array of all the characters to use.
  * an array specifying the `[start, end]` character codes to use. By default,
    this is `[32, 126]`.

## See also

* [font-atlas-sdf](https://npmjs.org/package/font-atlas-sdf)

## License

MIT. See [LICENSE.md](http://github.com/hughsk/font-atlas/blob/master/LICENSE.md) for details.

![font-atlas](http://imgur.com/FWLDbPP.png)
