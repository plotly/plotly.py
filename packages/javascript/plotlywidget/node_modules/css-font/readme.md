# css-font [![unstable](https://img.shields.io/badge/stability-unstable-orange.svg)](http://github.com/badges/stability-badges) [![Travis Build Status](https://img.shields.io/travis/dy/css-font.svg?label=build)](https://travis-ci.org/dy/css-font)

Parse or stringify the CSS [font property](https://developer.mozilla.org/en-US/docs/Web/CSS/font) string.

## Usage

[![npm install css-font](https://nodei.co/npm/css-font.png?mini=true)](https://npmjs.org/package/css-font/)

```js
var font = require('css-font');

var obj = font.parse('small-caps 1rem/1.2 "Roboto Condensed", sans-serif');

/*
{
	size: '1rem',
	lineHeight: 1.2,
	variant: 'small-caps',
	family: ['Roboto Condensed', 'sans-serif']
}
*/

font.stringify(obj)

// '1rem "Roboto Condensed", sans-serif'
```

See [the tests](https://github.com/dy/css-font/blob/master/test/index.js) for more scenarios.


## API

### obj = font.parse(str)

Return object with font properties from the CSS font string. Detected properties:

Property | Meaning
---|---
`style` | [Font-style](https://developer.mozilla.org/en-US/docs/Web/CSS/font-style) detected by [`css-font-style-keywords`](https://npmjs.org/package/css-font-style-keywords).
`variant` | [Font-variant](https://developer.mozilla.org/en-US/docs/Web/CSS/font#font-variant-css21), one of `normal` or `small-caps`.
`weight` | [Font-weight](https://developer.mozilla.org/en-US/docs/Web/CSS/font-weight) detected by [`css-font-weight-keywords`](https://npmjs.org/package/css-font-weight-keywords).
`stretch` | [Font-stretch](https://developer.mozilla.org/en-US/docs/Web/CSS/font-stretch) detected by [`css-font-stretch-keywords`](https://npmjs.org/package/css-font-stretch-keywords).
`size` | [Font-size](https://developer.mozilla.org/en-US/docs/Web/CSS/font-size) detected by [`css-font-size-keywords`](https://npmjs.org/package/css-font-size-keywords).
`lineHeight` | [Line-height](https://developer.mozilla.org/en-US/docs/Web/CSS/line-height) value.
`family` | [Font-family](https://developer.mozilla.org/en-US/docs/Web/CSS/font-family) array of values.

### str = font.stringify(obj)

Return string from the object with font properties by the [CSS font](https://developer.mozilla.org/en-US/docs/Web/CSS/font) syntax.

Stringified properties:

Property | Meaning
---|---
`style`, `fontStyle`, `distrinction` | Font-style value.
`variant`, `fontVariant`, `capitalization` | Font-variant value, one of `normal` or `small-caps`.
`weight`, `fontWeight` | Font-weight value, one of the set of weights (see above).
`stretch`, `fontStretch`, `width` | Font-stretch value, one of the set (see above).
`size` `fontSize`, `height` | Font-size value, number or a string. Number is considered a `px` units. If undefined, `1rem` is used.
`lineHeight`, `leading` | Line-height value, number or string. Number is considered a unitless ratio value.
`family`, `fontFamily`, `face` | Font-family, string or a list with strings. Not default strings are wrapped to quotes.
`system` | Reserved system word.


## Testing

```
$ npm test
```

This will run tests and generate a code coverage report. Anything less than 100% coverage will throw an error.


## Acknowledgement

* [Jed Mao](https://github.com/jedmao) for [parse-css-font](https://github.com/jedmao/parse-css-font) and set of related CSS packages.


## License

© 2018 Dmitry Yv. MIT License

Development supported by [plot.ly](https://github.com/plotly/).
