var fs = require('fs')
var exec = require('child_process').exec
var common = require('./common')
var mapshaper = './node_modules/mapshaper/bin/mapshaper'

fs.readFile(common.pathToConfig, 'utf8', main)

function main (err, configFile) {
  if (err) throw err

  var config = JSON.parse(configFile)
  var toposToWrite = common.getToposToWrite(config)

  var bar = common.makeBar(
    'Converting shapefiles to GeoJSON: [:bar] :current/:total',
    [toposToWrite, config.vectors]
  )

  function scopeBaseShapefile (r, s) {
    var specs = s.specs

    var filter

    var cmd

    function getFilter (specs) {
      return [
        "'",
        '$.properties.',
        specs.key,
        ' === ',
        '"', specs.val, '"',
        "'"
      ].join('')
    }

    filter = getFilter(specs)
    cmd = [
      mapshaper,
      common.wgetDir + common.srcPrefix + common.bn(r, specs.src, 'shp'),
      'encoding=utf8',
      '-filter',
      filter,
      '-o',
      common.wgetDir + common.tn(r, s.name, specs.src, 'tmp.shp'),
      'force',
      '&&',
      'ogr2ogr',
      '-overwrite',
      '-clipsrc',
      specs.bounds.join(' '),
      common.wgetDir + common.tn(r, s.name, specs.src, 'shp'),
      common.wgetDir + common.tn(r, s.name, specs.src, 'tmp.shp')
    ].join(' ')

    if (common.DEBUG) console.log(cmd + '\n')
    return cmd
  }

  function convertToGeoJSON (r, s, v, clip) {
    var specs = s.specs

    var cmd

    // use ogr2ogr for clip around bound
    // use mapshaper for clip around shapefile polygons

    function getCmd (program, opt) {
      var cmd,
        expr

      if (program === 'ogr2ogr') {
        if (opt === 'where') {
          expr = [
            '-where ',
            '"', specs.key, ' IN ',
            "('", specs.val, "')\" ",
            '-clipsrc ',
            specs.bounds.join(' ')
          ].join('')
        } else if (opt === 'clipsrc') {
          expr = [
            '-clipsrc ',
            specs.bounds.join(' ')
          ].join('')
        } else expr = ''

        cmd = [
          'ogr2ogr -f GeoJSON',
          expr,
          common.geojsonDir + common.tn(r, s.name, v.name, 'geo.json'),
          common.wgetDir + common.srcPrefix + common.bn(r, v.src, 'shp')
        ].join(' ')
      } else if (program === 'mapshaper') {
        cmd = [
          mapshaper,
          common.wgetDir + common.srcPrefix + common.bn(r, v.src, 'shp'),
          'encoding=utf8',
          '-clip',
          common.wgetDir + common.tn(r, s.name, specs.src, 'shp'),
          '-filter remove-empty',
          '-o',
          common.geojsonDir + common.tn(r, s.name, v.name, 'geo.json')
        ].join(' ')
      }

      return cmd
    }

    if (clip && specs && specs.src !== v.name) {
      if (v.src === specs.src) {
        cmd = getCmd('ogr2ogr', 'where')
      } else if (s.name === 'usa' && v.name === 'rivers') {
        // for 'usa' scope,
        // clip rivers with base shp instead of bounds
        cmd = getCmd('mapshaper')
      } else if (v.scopeWith === 'src') {
        cmd = getCmd('mapshaper')
      } else if (v.scopeWith === 'bounds') {
        cmd = getCmd('ogr2ogr', 'clipsrc')
      }
    } else cmd = getCmd('ogr2ogr', false)

    if (common.DEBUG) console.log(cmd + '\n')
    return cmd
  }

  function vectorLoop (r, s, clip) {
    config.vectors.forEach(function (v) {
      exec(convertToGeoJSON(r, s, v, clip), function (err) {
        if (err) throw err
        bar.tick()
      })
    })
  }

  toposToWrite.forEach(function (topo) {
    var r = topo.r

    var s = topo.s

    if (s.specs === false) vectorLoop(r, s, false)
    else {
      exec(scopeBaseShapefile(r, s), function (err) {
        if (err) throw err
        setTimeout(function () {
          vectorLoop(r, s, true)
        }, 1000)
      })
    }
  })
}
