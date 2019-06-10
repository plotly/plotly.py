/* eslint-disable no-redeclare */

var hash = require('murmurhash-js/murmurhash3_gc')
var trim = require('glsl-token-whitespace-trim')
var tokenize = require('glsl-tokenizer/string')
var inject = require('glsl-inject-defines')
var defines = require('glsl-token-defines')
var descope = require('glsl-token-descope')
var clean = require('./lib/clean-suffixes')
var string = require('glsl-token-string')
var scope = require('glsl-token-scope')
var depth = require('glsl-token-depth')
var topoSort = require('./lib/topo-sort')
var copy = require('shallow-copy')

module.exports = function (deps) {
  return inject(Bundle(deps).src, {
    GLSLIFY: 1
  })
}

function Bundle (deps) {
  if (!(this instanceof Bundle)) return new Bundle(deps)

  // Reorder dependencies topologically
  deps = topoSort(deps)

  this.depList = deps
  this.depIndex = indexBy(deps, 'id')
  this.exported = {}
  this.cache = {}
  this.varCounter = 0

  this.src = []

  for (var i = 0; i < deps.length; i++) {
    this.preprocess(deps[i])
  }

  for (var i = 0; i < deps.length; i++) {
    if (deps[i].entry) {
      this.src = this.src.concat(this.bundle(deps[i]))
    }
  }

  this.src = string(this.src)
  this.src = string(clean(trim(tokenize(this.src))))
}

var proto = Bundle.prototype

proto.preprocess = function (dep) {
  var tokens = tokenize(dep.source)
  var imports = []
  var exports = null

  depth(tokens)
  scope(tokens)

  for (var i = 0; i < tokens.length; i++) {
    var token = tokens[i]
    if (token.type !== 'preprocessor') continue
    if (!glslifyPreprocessor(token.data)) continue

    var exported = glslifyExport(token.data)
    var imported = glslifyImport(token.data)

    if (exported) {
      exports = exported[1]
      tokens.splice(i--, 1)
    } else if (imported) {
      var name = imported[1]
      var maps = imported[2].split(/\s?,\s?/g)
      var path = maps.shift()
        .trim()
        .replace(/^'|'$/g, '')
        .replace(/^"|"$/g, '')
      var target = this.depIndex[dep.deps[path]]
      imports.push({
        name: name,
        path: path,
        target: target,
        maps: toMapping(maps),
        index: i
      })
      tokens.splice(i--, 1)
    }
  }

  var eof = tokens[tokens.length - 1]
  if (eof && eof.type === 'eof') {
    tokens.pop()
  }

  if (dep.entry) {
    exports = exports || 'main'
  }

  if (!exports) {
    throw new Error(dep.file + ' does not export any symbols')
  }

  dep.parsed = {
    tokens: tokens,
    imports: imports,
    exports: exports
  }
}

proto.bundle = function (entry) {
  var resolved = {}
  var result = resolve(entry, [])[1]

  return result

  function resolve (dep, bindings) {
    // Compute suffix for module
    bindings.sort()
    var ident = bindings.join(':') + ':' + dep.id
    var suffix = '_' + hash(ident)

    if (dep.entry) {
      suffix = ''
    }

    // Test if export is already resolved
    var exportName = dep.parsed.exports + suffix
    if (resolved[exportName]) {
      return [exportName, []]
    }

    // Initialize map for variable renamings based on bindings
    var rename = {}
    for (var i = 0; i < bindings.length; ++i) {
      var binding = bindings[i]
      rename[binding[0]] = binding[1]
    }

    // Resolve all dependencies
    var imports = dep.parsed.imports
    var edits = []
    for (var i = 0; i < imports.length; ++i) {
      var data = imports[i]

      var importMaps = data.maps
      var importName = data.name
      var importTarget = data.target

      var importBindings = Object.keys(importMaps).map(function (id) {
        var value = importMaps[id]

        // floats/ints should not be renamed
        if (value.match(/^\d+(?:\.\d+?)?$/g)) {
          return [id, value]
        }

        // properties (uVec.x, ray.origin, ray.origin.xy etc.) should
        // have their host identifiers renamed
        var parent = value.match(/^([^.]+)\.(.+)$/)
        if (parent) {
          return [id, (rename[parent[1]] || (parent[1] + suffix)) + '.' + parent[2]]
        }

        return [id, rename[value] || (value + suffix)]
      })

      var importTokens = resolve(importTarget, importBindings)
      rename[importName] = importTokens[0]
      edits.push([data.index, importTokens[1]])
    }

    // Rename tokens
    var parsedTokens = dep.parsed.tokens.map(copy)
    var parsedDefs = defines(parsedTokens)
    var tokens = descope(parsedTokens, function (local, token) {
      if (parsedDefs[local]) return local
      if (rename[local]) return rename[local]

      return local + suffix
    })

    // Insert edits
    edits.sort(function (a, b) {
      return b[0] - a[0]
    })

    for (var i = 0; i < edits.length; ++i) {
      var edit = edits[i]
      tokens = tokens.slice(0, edit[0])
        .concat(edit[1])
        .concat(tokens.slice(edit[0]))
    }

    resolved[exportName] = true
    return [exportName, tokens]
  }
}

function glslifyPreprocessor (data) {
  return /#pragma glslify:/.test(data)
}

function glslifyExport (data) {
  return /#pragma glslify:\s*export\(([^)]+)\)/.exec(data)
}

function glslifyImport (data) {
  return /#pragma glslify:\s*([^=\s]+)\s*=\s*require\(([^)]+)\)/.exec(data)
}

function indexBy (deps, key) {
  return deps.reduce(function (deps, entry) {
    deps[entry[key]] = entry
    return deps
  }, {})
}

function toMapping (maps) {
  if (!maps) return false

  return maps.reduce(function (mapping, defn) {
    defn = defn.split(/\s?=\s?/g)

    var expr = defn.pop()

    defn.forEach(function (key) {
      mapping[key] = expr
    })

    return mapping
  }, {})
}
