var tokenize = require('glsl-tokenizer')
var stringify = require('glsl-token-string')
var inject = require('glsl-token-inject-block')

module.exports = function glslInjectDefine (source, defines) {
  if (!defines) {
    return source
  }

  var keys = Object.keys(defines)
  if (keys.length === 0) {
    return source
  }

  var tokens = tokenize(source)
  for (var i=keys.length-1; i>=0; i--) {
    var key = keys[i]
    var val = String(defines[key])
    if (val) { // allow empty value
      val = ' ' + val
    }

    inject(tokens, {
      type: 'preprocessor',
      data: '#define ' + key + val
    })
  }
  
  return stringify(tokens)
}
