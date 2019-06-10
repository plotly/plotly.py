module.exports = properties

function properties(tokens) {
  for (var i = 0; i < tokens.length; i++) {
    var token = tokens[i]
    token.property = false

    if (token.type !== 'ident') continue

    var j = i
    while (tokens[--j] && tokens[j].type === 'whitespace');
    if (!tokens[j]) continue
    if (tokens[j].type !== 'operator') continue
    if (tokens[j].data !== '.') continue

    token.property = true
  }

  return tokens
}
