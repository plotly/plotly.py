var fs = require('fs')
var exec = require('child_process').exec
var wget = require('node-wget')
var common = require('./common')

fs.readFile(common.pathToConfig, 'utf8', main)

function main (err, configFile) {
  if (err) throw err

  var config = JSON.parse(configFile)

  var bar = common.makeBar(
    'Downloading shapefiles: [:bar] :current/:total',
    [config.resolutions, config.vectors]
  )

  function unzip (r, v) {
    return [
      'unzip -o',
      common.wgetDir + common.srcPrefix + common.bn(r, v.src, 'zip'),
      '-d', common.wgetDir
    ].join(' ')
  }

  config.resolutions.forEach(function (r) {
    config.vectors.forEach(function (v) {
      var url = [
        common.urlBase,
        r, 'm/', v.type + '/',
        common.srcPrefix,
        common.bn(r, v.src, 'zip')
      ].join('')
      var dest = [
        common.wgetDir,
        common.srcPrefix,
        common.bn(r, v.src, 'zip')
      ].join('')

      if (common.DEBUG) console.log('wget ' + url + '\n')

      wget({ url: url, dest: dest }, function (err) {
        if (err) throw err
        setTimeout(function () {
          exec(unzip(r, v), function (err) {
            if (err) throw err
            bar.tick()
          })
        }, 1000)
      })
    })
  })
}
