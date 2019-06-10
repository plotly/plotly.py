const readJSON = require('read-package-json')
const multipipe = require('multipipe')
const from2 = require('from2-array')
const resolve = require('resolve')
const map = require('map-limit')
const findup = require('findup')
const path = require('path')
const bl = require('bl')

module.exports = loader

function loader (source) {
  const filename = this.resourcePath
  const dirname = this.context
  const done = this.async()
  const self = this

  this.cacheable(true)

  findup(dirname, 'package.json', foundPackage)

  function foundPackage (err, pkgDir) {
    if (err) return done(err)
    if (!pkgDir) return done(null, source)

    const pkgFile = path.join(pkgDir, 'package.json')

    readJSON(pkgFile, function (err, json) {
      if (err) return done(err)

      const pkgTransforms = [].concat(
        json.browserify && json.browserify.transform
      ).filter(Boolean)

      map(pkgTransforms, 10, function (transform, next) {
        transform = Array.isArray(transform) ? transform : [transform]

        const name = transform[0]
        const opts = transform[1] || {}
        opts._flags = opts._flags || []

        if (typeof name === 'function') {
          return next(null, name(filename, opts))
        }

        resolve(name, {
          basedir: pkgDir
        }, function (err, name) {
          if (err) return next(err)

          const TransformStream = require(name)

          if (typeof TransformStream !== 'function') {
            return next(new Error(
              'Browserify transform at ' + name + ' did not export a function'
            ))
          }

          next(null, TransformStream(filename, opts))
        })
      }, function (err, transforms) {
        if (err) return done(err)

        transforms.forEach(function (tr) {
          tr.on('file', function (file) {
            self.addDependency(file)
          })
        })

        transforms = []
          .concat(from2([source]))
          .concat(transforms)

        multipipe.apply(this, transforms)
          .pipe(bl(done))
      })
    })
  }
}
