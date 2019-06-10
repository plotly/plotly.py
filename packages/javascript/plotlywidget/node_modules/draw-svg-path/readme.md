# draw-svg-path
draw-svg-path draws a [parsed SVG path](https://github.com/jkroso/parse-svg-path) onto a canvas context.

[![Browser support](https://ci.testling.com/michaelrhodes/draw-svg-path.png)](https://ci.testling.com/michaelrhodes/draw-svg-path)

<small>Older browsers might require a polyfill for [Array.prototype.forEach](http://kangax.github.io/es5-compat-table/#Array.prototype.forEach).</small>

## Install
```sh
$ npm install michaelrhodes/draw-svg-path
```

## API
```js
draw(context, path)
```

### Example
``` js
var parse = require('parse-svg-path')
var draw = require('draw-svg-path')

var path = parse('M10 10 L15 15')
var canvas = document.querySelector('canvas')
var context = canvas.getContext('2d')

context.lineWidth = 1
context.strokeStyle = '#000000'
context.fillStyle = 'transparent'
// Do actual drawing
draw(context, path)
context.stroke()
```

### License
[MIT](http://opensource.org/licenses/MIT)
