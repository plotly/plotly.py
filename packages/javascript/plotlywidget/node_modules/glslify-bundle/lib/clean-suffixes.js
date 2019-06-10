module.exports = clean

var suffix = /^([^_]+)_(\d{4,})$/

function clean (tokens) {
  var blacklist = {}
  var index = {}

  for (var i = 0; i < tokens.length; i++) {
    var token = tokens[i]
    if (token.type !== 'ident') continue
    var match = token.data.match(suffix)
    if (!match) {
      blacklist[token.data] = true
      continue
    }

    var pre = match[1]
    var suf = match[2]

    index[pre] = index[pre] || {}
    index[pre][suf] = index[pre][suf] || []
    index[pre][suf].push(token)
  }

  Object.keys(index).forEach(function (prefix) {
    var suffixes = Object.keys(index[prefix])
    if (suffixes.length === 1 && !blacklist[prefix]) {
      var tokens = index[prefix][suffixes[0]]
      for (var i = 0; i < tokens.length; i++) {
        tokens[i].data = prefix
      }

      return
    }

    suffixes.forEach(function (suffix, i) {
      var token = index[prefix][suffix]
      var rename = prefix + '_' + i
      if (blacklist[rename]) return
      for (var j = 0; j < token.length; j++) {
        token[j].data = rename
      }
    })
  })

  return tokens
}
