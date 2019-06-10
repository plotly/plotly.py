module.exports = glslTokenInject

var newline = { data: '\n', type: 'whitespace' }
var regex = /[^\r\n]$/

function glslTokenInject (tokens, newTokens) {
  if (!Array.isArray(newTokens))
    newTokens = [ newTokens ]
  var start = getStartIndex(tokens)
  var last = start > 0 ? tokens[start-1] : null
  if (last && regex.test(last.data)) {
    tokens.splice(start++, 0, newline)
  }
  tokens.splice.apply(tokens, [ start, 0 ].concat(newTokens))
  
  var end = start + newTokens.length
  if (tokens[end] && /[^\r\n]$/.test(tokens[end].data)) {
    tokens.splice(end, 0, newline)
  }
  return tokens
}

function getStartIndex (tokens) {
  // determine starting index for attributes
  var start = -1
  for (var i = 0; i < tokens.length; i++) {
    var token = tokens[i]
    if (token.type === 'preprocessor') {
      if (/^#(extension|version)/.test(token.data)) {
        start = Math.max(start, i)
      }
    } else if (token.type === 'keyword' && token.data === 'precision') {
      var semi = findNextSemicolon(tokens, i)
      if (semi === -1) {
        throw new Error('precision statement not followed by any semicolons!')
      }
      start = Math.max(start, semi)
    }
  }
  return start + 1
}

function findNextSemicolon (tokens, start) {
  for (var i = start; i < tokens.length; i++) {
    if (tokens[i].type === 'operator' && tokens[i].data === ';') {
      return i
    }
  }
  return -1
}