module.exports = trim

function trim (tokens, everything) {
  return trim[everything ? 'all' : 'newlines'](collapse(tokens))
}

function collapse (tokens) {
  for (var i = 1; i < tokens.length; i++) {
    var curr = tokens[i]
    if (curr.type !== 'whitespace') continue
    var prev = tokens[i - 1]
    if (prev.type !== 'whitespace') continue
    tokens.splice(--i, 1)
    curr.data = prev.data + curr.data
  }

  return tokens
}

var newlines = /(?:\n|\r\n|\r){2,}/g

trim.newlines = function (tokens) {
  for (var i = 0; i < tokens.length; i++) {
    var token = tokens[i]
    if (token.type !== 'whitespace') continue
    token.data = token.data.replace(newlines, '\n\n')
  }

  return tokens
}

var all = /\s+/g

trim.all = function (tokens) {
  var l = tokens.length

  for (var i = 0; i < l; i++) {
    var token = tokens[i]
    if (token.type !== 'whitespace') continue
    var next = tokens[i + 1]
    var prev = tokens[i - 1]

    if (next && next.type === 'preprocessor' || prev && prev.type === 'preprocessor') {
      token.data = token.data.replace(all, '\n')
    } else {
      token.data = token.data.replace(all, ' ')

      switch (next && next.data) {
        case '(': case ';': case ')':
        case '{': case '=': case '}': case ',':
          token.data = token.data.replace(all, '')
      }

      switch (prev && prev.data) {
        case '(': case ';': case ')':
        case '{': case '=': case '}': case ',':
          token.data = token.data.replace(all, '')
      }
    }
  }

  return tokens
}
