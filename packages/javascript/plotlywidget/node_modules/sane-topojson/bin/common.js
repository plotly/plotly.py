var fs = require('fs')
var path = require('path')
var ProgressBar = require('progress')

var common = module.exports = {}

common.DEBUG = process.env.SANE_TOPOJSON_DEBUG
common.pathToConfig = path.join(__dirname, '../config.json')
common.wgetDir = path.join(__dirname, '../build/')
common.geojsonDir = path.join(__dirname, '../build/')
common.topojsonDir = path.join(__dirname, '../dist/')
common.pathToStats = path.join(__dirname, '..', 'STATS.md')
common.urlBase = 'https://www.naturalearthdata.com/http//www.naturalearthdata.com/download/'
common.srcPrefix = 'ne_'

// base file name
common.bn = function bn (r, vName, ext) {
  return r + 'm_' + vName + '.' + ext
}

// temporary file name
common.tn = function tn (r, sName, vName, ext) {
  return r + 'm_' + sName + '_' + vName + '.' + ext
}

// aggregated topojson
common.out = function out (r, sName) {
  return sName + '_' + r + 'm.json'
}

// make Progress bar
common.makeBar = function (str, components) {
  function getTotal () {
    var total = 1
    components.forEach(function (c) {
      total *= c.length
    })
    return total
  }
  return new ProgressBar(
    str,
    {
      incomplete: ' ',
      total: getTotal()
    }
  )
}

// get list of topojsons to write
common.getToposToWrite = function (config) {
  var toposToWrite = []

  config.resolutions.forEach(function (r) {
    config.scopes.forEach(function (s) {
      var path = config.topojson_dir + common.out(r, s.name)
      if (!fs.existsSync(path)) {
        toposToWrite.push({ r: r, s: s })
      }
    })
  })

  return toposToWrite
}
