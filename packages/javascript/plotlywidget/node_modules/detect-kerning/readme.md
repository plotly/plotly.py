# detect-kerning [![unstable](https://img.shields.io/badge/stability-unstable-green.svg)](http://github.com/badges/stability-badges) [![Build Status](https://img.shields.io/travis/dy/detect-kerning.svg)](https://travis-ci.org/dy/detect-kerning)

Calculate kerning pairs for a font.

[![npm install detect-kerning](https://nodei.co/npm/detect-kerning.png?mini=true)](https://npmjs.org/package/detect-kerning/)

```js
const kerning = require('detect-kerning')

let pairs = kerning('Roboto')

/*
{
	'A”': -10,
	'W.': -5,
	'P,': -3,
	...
}
*/

// get px kerning for 16px font-size
let px = 16 * pairs['AV'] / 1000
```

### `pairs = kerning(family|familyList, pairs|range|options?)`

Detect kerning pairs for the font family or stack of families and return their kerning in 1000 units/em. Optionally pass specific kerning pairs to check, or a unicode range, by default all printable ASCII character pairs are detected from the `[32, 126]` range. Alternatively, an options object can define:

* `options.pairs` - specific pairs to check;
* `options.range` - unicode range to detect pairs from;
* `options.fontSize` - base font size to use for check. Can affect performance, by default 16.
* `options.threshold` - font size (em) ratio to detect kerning, by default 0.05. Values below that number can bloat kerning table size.


## Related

* [css-font](https://npmjs.org/css-font) for parsing font-family from css font string.

## License

© 2018 Dmitry Yv. MIT License
