var resolver = require('resolve')
var xtend    = require('xtend')
var path     = require('path')

var core = {}
var exts = [
    '.glsl'
  , '.vert'
  , '.frag'
  , '.geom'
  , '.vs'
  , '.fs'
  , '.gs'
  , '.vsh'
  , '.fsh'
  , '.gsh'
  , '.vshader'
  , '.fshader'
  , '.gshader'
]

module.exports      = resolve
module.exports.sync = resolveSync

function resolve(target, opts, next) {
  return resolver(target
    , glslOpts(opts || {})
    , next
  )
}

function resolveSync(target, opts) {
  return resolver.sync(target
    , glslOpts(opts || {})
  )
}

function glslOpts(opts) {
  return xtend(opts, {
      modules: core
    , extensions: exts
    , packageFilter: packageFilter
  })
}

// find the "glslify", "main", or assume main == "index.glsl"
// if main is a .js file then ignore it.
function packageFilter(pkg, root) {
  pkg.main = pkg.glslify || (
    path.extname(pkg.main || '') !== '.js' &&
    pkg.main
  ) || 'index.glsl'

  return pkg
}
