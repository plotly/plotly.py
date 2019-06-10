var tokenize = require('glsl-tokenizer/string')
var findup   = require('@choojs/findup')
var fs       = require('graceful-fs')
var map      = require('map-limit')
var inherits = require('inherits')
var Emitter  = require('events/')
var path     = require('path')

var glslResolve = require('glsl-resolve')
var nodeResolve = require('resolve')

var inlineName   = '__INLINE__' + Math.random()
var inlineSource = ''

module.exports = Depper

/**
 * Creates a new instance of glslify-deps. Generally, you'll
 * want to use one instance per bundle.
 *
 * @class
 * @param {String} cwd The root directory of your shader. Defaults to process.cwd()
 */
inherits(Depper, Emitter)
function Depper(opts) {
  if (!(this instanceof Depper)) return new Depper(opts)
  Emitter.call(this)

  opts = typeof opts === 'string' ? { cwd: opts } : opts
  opts = opts || {}

  this._deps       = []
  this._cwd        = opts.cwd || process.cwd()
  this._cache      = {}
  this._i          = 0
  this._transforms = []
  this._trCache    = {}
  this._fileCache  = opts.files || {}

  this._globalTransforms = []

  this._readFile = cacheWrap(opts.readFile || defaultRead, this._fileCache)
  this.resolve   = opts.resolve || glslResolve

  if (typeof this._cwd !== 'string') {
    throw new Error('glslify-deps: cwd must be a string path')
  }
}

Depper.prototype.inline = function(source, basedir, done) {
  var inlineFile = path.resolve(basedir || process.cwd(), inlineName)

  inlineSource = source

  this.add(inlineFile, function(err, tree) {
    done && done(err, !err && tree)
  })
}

/**
 * Adds a transform to use on your local dependencies.
 * Note that this should be used before calling `add`.
 *
 * Transforms are handled using a different API to browserify, e.g.:
 *
 * ``` js
 * module.exports = function transform(filename, src, opts, done) {
 *   done(null, src.toUpperCase())
 * }
 * ```
 *
 * Where `filename` is the absolute file path, `src` is the shader source
 * as a string, `opts` is an options object for configuration, and `done`
 * is a callback which takes the transformed shader source.
 *
 * @param {String|Function} transform
 * @param {Object} opts
 */
Depper.prototype.transform = function(transform, opts) {
  var name = typeof transform === 'string' ? transform : null
  var list = opts && opts.global
    ? this._globalTransforms
    : this._transforms

  // post transforms are ignored by glslify-deps, to be handled
  // by glslify after the file has been bundled.
  if (opts && opts.post) return this

  transform = this.resolveTransform(transform)
  list.push({ tr: transform, opts: opts, name: name })

  return this
}

/**
 * Adds a shader file to the graph, including its dependencies
 * which are resolved in this step. Transforms are also applied
 * in the process too, as they may potentially add or remove dependent
 * modules.
 *
 * @param {String} filename The absolute path of this file.
 * @param {String} src The shader source for this file.
 * @param {Function} done(err, deps)
 *
 * The `done` callback will be called when the entire graph has been
 * resolved, and will include an array of dependencies discovered
 * so far as its second argument.
 */
Depper.prototype.add = function(filename, done) {
  var basedir = path.dirname(filename = path.resolve(filename))
  var cache   = this._cache
  var self    = this
  var exports = []
  var imports = []

  var dep = {
      id: this._i++
    , deps: {}
    , file: filename
    , source: null
    , entry: this._i === 1
  }

  this._deps.push(dep)
  this.readFile(filename, function(err, src) {
    if (err) return done(err)

    self.getTransformsForFile(filename, function(err, trs) {
      if (err) return done(err)

      self.emit('file', filename)
      self.applyTransforms(filename, src, trs, function(err, src) {
        if (err) return done(err)

        dep.source = src
        extractPreprocessors()
        resolveImports(function(err) {
          setTimeout(function() {
            done && done(err, !err && self._deps)
          })
        })
      })
    })
  })

  return dep

  function extractPreprocessors() {
    var tokens = tokenize(dep.source)

    for (var i = 0; i < tokens.length; i++) {
      var token = tokens[i]
      if (token.type !== 'preprocessor') continue

      var data = token.data
      if (!glslifyPreprocessor(data)) continue

      var exp = glslifyExport(data)
      var imp = glslifyImport(data)
      if (exp) exports.push(exp[1])
      if (imp) imports.push(imp[2])
    }
  }

  function resolveImports(resolved) {
    map(imports, 10, function(imp, next) {
      var importName = imp.split(/\s*,\s*/).shift()

      importName = importName.trim()
      importName = importName.replace(/^'|'$/g, '')
      importName = importName.replace(/^"|"$/g, '')

      self.resolve(importName, { basedir: basedir }, function(err, resolved) {
        if (err) return next(err)

        if (cache[resolved]) {
          dep.deps[importName] = cache[resolved].id
          return next()
        }

        cache[resolved] = self.add(resolved, function(err) {
          if (err) return next(err)
          dep.deps[importName] = cache[resolved].id
          next()
        })
      })
    }, resolved)
  }
}

Depper.prototype.readFile = function(filename, done) {
  if (path.basename(filename) !== inlineName)
    return this._readFile(filename, done)

  return done(null, inlineSource)
}

/**
 * Determines which transforms to use for a particular file.
 * The rules here are the same you see in browserify:
 *
 * - your shader files will have your specified transforms applied to them
 * - shader files in node_modules do not get local transforms
 * - all files will apply transforms specified in `glslify.transform` in your
 *   `package.json` file, albeit after any transforms you specified using
 *   `depper.transform`.
 *
 * @param {String} filename The absolute path of the file in question.
 */
Depper.prototype.getTransformsForFile = function(filename, done) {
  var self  = this
  var entry = this._deps[0]

  if (!entry) return done(new Error(
    'getTransformsForFile may only be called after adding your entry file'
  ))

  var entryDir     = path.dirname(path.resolve(entry.file))
  var fileDir      = path.dirname(path.resolve(filename))
  var relative     = path.relative(entryDir, fileDir).split(path.sep)
  var node_modules = relative.indexOf('node_modules') !== -1
  var trLocal      = node_modules ? [] : this._transforms
  var trCache      = this._trCache

  if (trCache[fileDir]) {
    return done(null, trCache[fileDir])
  }

  findup(fileDir, 'package.json', function(err, found) {
    var notFound = err && err.message === 'not found'
    if (notFound) return register([])
    if (err) return done(err)

    var pkg = path.join(found, 'package.json')

    self.readFile(pkg, function(err, pkgjson) {
      if (err) return done(err)

      try {
        pkgjson = JSON.parse(pkgjson)
      } catch(e) { return done(e) }

      var transforms = (
           pkgjson['glslify']
        && pkgjson['glslify']['transform']
        || []
      )

      transforms = transforms.map(function(key) {
        var transform = Array.isArray(key)
          ? key
          : [key, {}]

        var key = transform[0]
        var opt = transform[1]

        if (opt) {
          delete opt.global
          delete opt.post
        }

        return { tr: key, opts: opt, name: key }
      }).map(function(tr) {
        tr.tr = self.resolveTransform(tr.tr)
        return tr
      })

      register(transforms)
    })
  })

  function register(transforms) {
    done(null, trCache[fileDir] = trLocal
      .concat(transforms)
      .concat(self._globalTransforms))
  }
}

/**
 * Resolves a transform.
 *
 * Functions are retained as-is.
 * Strings are resolved using node's `require` resolution algorithm,
 * and then required directly.
 *
 * @param {String|Function} transform
 */
Depper.prototype.resolveTransform = function(transform) {
  if (typeof transform === 'string') {
    transform = nodeResolve.sync(transform, {
      basedir: this._cwd
    })

    transform = require(transform)
  }

  return transform
}

/**
 * Applies a transform to a string.
 *
 * Note that transforms here are passed in differently to other methods:
 * - `tr.tr` should point to the transform function.
 * - `tr.opts` should contain the options for the transform, if applicable.
 *
 * @param {String} filename The absolute path of the file you're transforming.
 * @param {String} src The shader source you'd like to transform.
 * @param {Array} transforms The transforms you'd like to apply.
 * @param {Function} done(err, transformed)
 */
Depper.prototype.applyTransforms = function(filename, src, transforms, done) {
  var i = 0

  next(null, src)
  function next(err, updated) {
    if (err) return done(err)
    if (i >= transforms.length) return done(null, updated)

    var tr = transforms[i++]
    var opts = tr.opts

    if (!opts || typeof opts !== 'object') opts = {}
    tr.tr(filename, updated+'', tr.opts, next)
  }
}

function glslifyPreprocessor(data) {
  return /#pragma glslify:/.test(data)
}

function glslifyExport(data) {
  return /#pragma glslify:\s*export\(([^\)]+)\)/.exec(data)
}

function glslifyImport(data) {
  return /#pragma glslify:\s*([^=\s]+)\s*=\s*require\(([^\)]+)\)/.exec(data)
}

function defaultRead(src, done) {
  fs.readFile(src, 'utf8', done)
}

function cacheWrap(read, cache) {
  // resolve all cached files such that they match
  // all of the paths glslify handles, which are otherwise
  // absolute
  cache = Object.keys(cache).reduce(function(newCache, file) {
    newCache[path.resolve(file)] = cache[file]
    return newCache
  }, {})

  return function readFromCache(filename, done) {
    if (!cache[filename]) {
      return read(filename, done)
    }

    process.nextTick(function() {
      done(null, cache[filename])
    })
  }
}
