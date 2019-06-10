module.exports = defines

function defines(tokens) {
  var definitions = {}

  for (var i = 0; i < tokens.length; i++) {
    var token = tokens[i]
    if (token.type !== 'preprocessor') continue
    var datum = token.data.trim()
    if (datum.indexOf('#define')) continue
    var parts = datum.match(/#define\s+([^\s]+)(.+)?$/i)
    if (!parts) continue
    var name  = (parts[1] || '').trim()
    var value = (parts[2] || '').trim()

    definitions[name] = value
  }

  return definitions
}
