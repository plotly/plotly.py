# glslify-deps

Walk the dependency graph of a [glslify](http://github.com/stackgl/glslify)
shader.

`glslify-deps` is responsible for resolving your shader's dependencies and
applying their transforms before the actual source modification occurs. You may
notice some parallels here with [browserify](http://browserify.org)'s
[module-deps](http://github.com/substack/module-deps) package.

While `glslify-deps` is an "internal" package for `glslify`, it may be useful
to use this package directly in specific cases, e.g. building a file tree
server-side but bundling the final shader on the client.

## Module API

There is an asynchronous and a synchronous API:

``` js
var glslifyDeps = require('glslify-deps')
var glslifyDepsSync = require('glslify-deps/sync')
```

The asynchronous API is documented below. For every method in the asychronous
API, instead of a `callback(err, result)`, the result is available as the return
value of the method.

### `depper = glslifyDeps([options])`

Creates a fresh `glslify-deps` instance. Accepts the following options:

* `cwd`: the current working directory to resolve relative file paths from.
* `readFile`: pass in a custom function reading files.
* `resolve`: pass in a custom function for resolving require calls. It has
  the same signature as [glsl-resolve](http://github.com/hughsk/glsl-resolve).
* `files`: a filename/source object mapping of files to prepopulate
  the file cache with. Useful for overriding particular file paths manually,
  most notably the "entry" file.

### `depper.transform(transform, [options])`

Adds a new transform – should be used before calling `depper.add`.

`transform` may either be a string (which is resolved like a `require` call),
or a function. More information on transforms can be found below.

### `depper.add(filename, [callback])`

Adds a new file to the dependency graph.

### `depper.inline(source, basedir, [callback])`

Adds a new inline file to the dependency graph, where `source` is the GLSL
source to include and `basedir` is the directory to pretend it's being
created in. A `basedir` is required to properly resolve requires and transforms,
and defaults to `process.cwd()`.

### `depper.on('file', cb(filename))`

Emitted whenever a new file has been included in the dependency graph.

## Example Output

``` json
[
  {
    "id": 0,
    "deps": { "glsl-random": 1 },
    "file": "index.glsl",
    "source": "precision mediump float;\n#pragma glslify: random = require(glsl-random)\n",
    "entry": true
  },
  {
    "id": 1,
    "deps": {},
    "file": "node_modules/glsl-random/index.glsl",
    "source": "highp float random(vec2 co)\n{\n    highp float a = 12.9898;\n    highp float b = 78.233;\n    highp float c = 43758.5453;\n    highp float dt= dot(co.xy ,vec2(a,b));\n    highp float sn= mod(dt,3.14);\n    return fract(sin(sn) * c);\n}\n\n#pragma glslify: export(random)",
    "entry": false
  }
]
```

## Transform API

The transform API has changed since glslify 1.0 to make it more "vanilla".

With the asynchronous API, transforms have this signature:

``` javascript
module.exports = function(file, source, options, done) {
  done(null, source.toUpperCase())
}
```

and using the synchronous API, transforms have this signature:

``` javascript
module.exports.sync = function(file, source, options) {
  return source.toUpperCase()
}
```

For an example that is compatible with both the async and sync APIs, here's
[glslify-hex](http://github.com/hughsk/glslify-hex)
rewritten using the new API:

``` javascript
var through = require('through')

var regexLong  = /#([a-f0-9]{2})([a-f0-9]{2})([a-f0-9]{2})([a-f0-9]{2})?/gi
var regexShort = /#([a-f0-9])([a-f0-9])([a-f0-9])([a-f0-9])?/gi

module.exports = transform
module.exports.sync = transform

function transform(filename, src, opts, done) {
  src = src.replace(regexShort, function(whole, r, g, b, a) {
    return !a
      ? '#' + r + r + g + g + b + b
      : '#' + r + r + g + g + b + b + a + a
  }).replace(regexLong, function(whole, r, g, b, a) {
    r = makeFloat(parseInt(r, 16) / 255)
    g = makeFloat(parseInt(g, 16) / 255)
    b = makeFloat(parseInt(b, 16) / 255)
    a = makeFloat(parseInt(a, 16) / 255)

    return isNaN(a)
      ? 'vec3('+[r,g,b].join(',')+')'
      : 'vec4('+[r,g,b,a].join(',')+')'
  })

  if (typeof done === 'function') done(null, src)
  return src
}

function makeFloat(n) {
  return String(n).indexOf('.') === -1
    ? n + '.'
    : n
}
```

## Transforms in `package.json`

Transforms now support options specified in `package.json`:

``` json
{
  "glslify": {
    "transform": [
       "glslify-hex",
      ["glslify-optimize", { "mangle": true }]
    ]
  }
}
```
