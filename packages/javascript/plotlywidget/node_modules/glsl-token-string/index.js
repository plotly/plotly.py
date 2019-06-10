module.exports = toString

function toString(tokens) {
  var output = []

  for (var i = 0; i < tokens.length; i++) {
    if (tokens[i].type === 'eof') continue
    output.push(tokens[i].data)
  }

  return output.join('')
}
