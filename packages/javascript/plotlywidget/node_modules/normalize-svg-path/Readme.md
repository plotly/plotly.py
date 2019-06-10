
# normalize-svg-path

  Convert all segments in a path to curves. Usefull if you intend to animate one shape to another. By defining all segments with curves instead of a mix of lines, arcs, and curves tweening becomes much simpler. It could also help you rewrite your SVG code according to the principles of [narcissistic design](//vimeo.com/77199361).

## Installation

With your favourite package manager:

- [packin](//github.com/jkroso/packin): `packin add normalize-svg-path`
- [component](//github.com/component/component#installing-packages): `component install jkroso/normalize-svg-path`
- [npm](//npmjs.org/doc/cli/npm-install.html): `npm install normalize-svg-path`

then in your app:

```js
var normalize = require('normalize-svg-path')
```

## API

### normalize(path)

  Translate each segment in `path` to an equivalent cubic bézier curve. The input `path` must be [absolute](//github.com/jkroso/abs-svg-path).

```js
normalize([['L',1,2]]) // => [['C',0,0,1,2,1,2]]
```
