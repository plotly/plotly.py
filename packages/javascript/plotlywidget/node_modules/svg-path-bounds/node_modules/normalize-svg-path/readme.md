# normalize-svg-path [![build](https://travis-ci.org/jkroso/normalize-svg-path.svg?branch=master)](https://travis-ci.org/jkroso/normalize-svg-path)


  Convert all segments in a path to curves. Usefull if you intend to animate one shape to another. By defining all segments with curves instead of a mix of lines, arcs, and curves tweening becomes much simpler. It could also help you rewrite your SVG code according to the principles of [narcissistic design](//vimeo.com/77199361).

## Usage

[![npm install normalize-svg-path](https://nodei.co/npm/normalize-svg-path.png?mini=true)](https://npmjs.org/package/normalize-svg-path/)

```js
var parse = require('parse-svg-path')
var abs = require('abs-svg-path')
var normalize = require('normalize-svg-path')

var segments = normalize(abs(parse('M0 0L10 10A10 10 0 0 0 20 20Z')))
```

## API

### normalize(path)

  Translate each segment in `path` to an equivalent cubic bézier curve. The input `path` must be [absolute](//github.com/jkroso/abs-svg-path).

```js
normalize([['L',1,2]]) // => [['C',0,0,1,2,1,2]]
```
