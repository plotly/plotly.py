'use strict'

module.exports = float2rat

var rat = require('big-rat')

function float2rat(v) {
  var result = new Array(v.length)
  for(var i=0; i<v.length; ++i) {
    result[i] = rat(v[i])
  }
  return result
}
