# glslify-bundle

[![experimental](http://badges.github.io/stability-badges/dist/experimental.svg)](http://github.com/badges/stability-badges)

Bundle a [glslify-deps](http://github.com/stackgl/glslify-deps) dependency tree into
a GLSL source string.

This has been separated from *glslify-deps* such that you can prebundle a dependency
tree server-side, but then still modify shader file contents in a browser.

## Usage

[![NPM](https://nodei.co/npm/glslify-bundle.png)](https://nodei.co/npm/glslify-bundle/)

### `source = bundle(deps)`

Takes the output object from [glslify-deps](http://github.com/stackgl/glslify-deps)
and returns a bundled GLSL string.

``` javascript
var bundle = require('glslify-bundle')
var deps   = require('glslify-deps')
var path   = require('path')

var file = path.join(__dirname, 'index.glsl')

deps().add(file, function(err, tree) {
  if (err) throw err

  var glsl = bundle(tree)

  console.log(glsl)
})
```

## Contributing

See [stackgl/contributing](https://github.com/stackgl/contributing) for details.

## License

MIT. See [LICENSE.md](http://github.com/stackgl/glslify-bundle/blob/master/LICENSE.md) for details.
