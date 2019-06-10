var fs = require('fs')
var gzipSize = require('gzip-size')
var prettySize = require('prettysize')
var common = require('./common')

fs.readFile(common.pathToConfig, 'utf8', main)

function main (err, configFile) {
  if (err) throw err

  var config = JSON.parse(configFile)
  var toposToWrite = common.getToposToWrite(config)

  var readBar = common.makeBar(
    'Measuring topojson size: [:bar] :current/:total',
    [toposToWrite]
  )

  var header = [
    '# sane-topojson file stats',
    '',
    '| dist name | raw size | gzip size |',
    '| --------- | -------- | --------- |'
  ]

  var footer = [
    '',
    '------------',
    '_This is generated via `npm run stats`. Do not modify it directly._',
    ''
  ]

  var lines = new Array(toposToWrite.length)

  toposToWrite.forEach(function (topo, i) {
    var r = topo.r
    var s = topo.s
    var inPath = common.topojsonDir + common.out(r, s.name)

    fs.readFile(inPath, 'utf-8', function (err, code) {
      if (err) throw err

      lines[i] = '| ' + [
        common.out(r, s.name),
        prettySize(code.length),
        prettySize(gzipSize.sync(code))
      ].join(' | ') + ' |'

      readBar.tick()

      if (readBar.complete) {
        var content = [].concat(header).concat(lines).concat(footer)

        fs.writeFile(common.pathToStats, content.join('\n'), function (err) {
          if (err) throw err
        })
      }
    })
  })
}
