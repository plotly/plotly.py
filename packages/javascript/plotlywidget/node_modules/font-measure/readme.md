# font-measure [![unstable](https://img.shields.io/badge/stability-unstable-green.svg)](http://github.com/badges/stability-badges)

Calculate metrics for a font.

[![npm install font-measure](https://nodei.co/npm/font-measure.png?mini=true)](https://npmjs.org/package/font-measure/)

```js
let measure = requrie('font-measure')

measure('Roboto')

/*
{
  top: 0,
  median: 0.640625,
  middle: 0.640625,
  bottom: 1.3125,
  alphabetic: 1.03125,
  baseline: 1.03125,
  upper: 0.328125,
  lower: 0.515625,
  capHeight: 0.703125,
  xHeight: 0.515625
  ascent: 0.28125,
  descent: 1.234375,
  hanging: 0.203125,
  ideographic: 1.296875,
  lineHeight: 1.3125,
  overshoot: 0.015625,
  tittle: 0.28125,
}
 */

```

## API

### `let metrics = measure(family, options?)`

Get metrics data for a font family or [CSS font string](), possibly with custom options. Font can be a string or an array with fonts.

#### `metrics`:

<img src="https://github.com/dy/font-measure/raw/master/sphinx.svg?sanitize=true" width="720"/>


#### `options`:

Property | Default | Meaning
---|---|---
`origin` | `top` | Origin for metrics. Can be changed to `baseline` or any other metric.
`fontSize` | `64` | Font-size to use for calculations. Larger size gives higher precision with slower performance.
`fontWeight` | `normal` | Font weight to use for calculations, eg. `bold`, `700` etc.
`fontStyle` | `normal` | Font style to use for calculations, eg. `italic`, `oblique`.
`canvas` | `measure.canvas` | Canvas to use for measurements.
`tittle` | `i` | Character to detect tittle. `null` disables calculation.
`descent` | `p` | Character to detect descent line. `null` disables calculation.
`ascent` | `h` | Character to detect ascent line. `null` disables calculation.
`overshoot` | `O` | Character to detect overshoot. `null` disables calculation.
`upper` | `H` | Character to detect upper line / cap-height. `null` disables calculation.
`lower` | `x` | Character to detect lower line / x-height. `null` disables calculation.


## See also

* [optical-properties](https://ghub.io/optical-properties) − calculate image/character optical center and bounding box.
* [detect-kerning](https://ghub.io/detect-kerning) − calculate kerning pairs for a font.

## Related

There are many text / font measuring packages for the moment, but most of them don't satisfy basic quality requirements. Special thanks to @soulwire
 for [fontmetrics](https://ghub.io/fontmetrics) as model implementation.

## License

© 2018 Dima Yv. MIT License

Development supported by plot.ly.
