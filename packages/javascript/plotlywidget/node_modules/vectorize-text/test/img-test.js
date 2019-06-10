var getPixels = require('get-pixels')
var savePixels = require('save-pixels')
var tape = require('tape')
var dataURL = require('./image.json')
var processPixels = require('../lib/vtext').processPixels
var imshow = require('ndarray-imshow')
var fs = require('fs')

tape('image-test', function(t) {
  getPixels(dataURL, function(err,data) {
    var graph = processPixels(
      data.pick(-1,-1,0).transpose(1,0), 
      {
        triangles: true,
        font: [
          '"Open Sans", verdana, arial, sans-serif',
          '"Open Sans", verdana, arial, sans-serif',
          '"Open Sans", verdana, arial, sans-serif'
        ],
        textAlign: 'left',
        textBaseline: 'top'
      }, 64)
    t.end()
  })
})