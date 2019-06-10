module.exports = getTokenDepth

function getTokenDepth(tokens) {
  var loop  = false
  var depth = 0

  for (var i = 0; i < tokens.length; i++) {
    loop = loop || (tokens[i].type === 'keyword' && (
      tokens[i].data === 'for'
    ))

    switch (tokens[i].data) {
      case '(': tokens[i].depth = loop ? depth++ : depth; break
      case '{': tokens[i].depth = loop ? depth : depth++; loop = false; break
      case '}': tokens[i].depth = --depth; break
      default:  tokens[i].depth = depth
    }
  }

  for (var i = 0; i < tokens.length; i++) {
    var token = tokens[i]
    var index = i + 1
    if (token.type !== 'ident' && token.type !== 'keyword') continue
    skipArrayArguments()
    if (tokens[index].type !== 'ident') continue
    skipArrayArguments()
    index++
    if (tokens[index].data !== '(') continue

    while (tokens[index] && tokens[index].data !== ';' && tokens[index].data !== '{') {
      tokens[index++].depth++
    }
    if (tokens[index] && tokens[index].data === '{') tokens[index].depth++
  }

  return tokens

  function skipArrayArguments() {
    while (tokens[index] && (
      tokens[index].type === 'whitespace' ||
      tokens[index].data === '[' ||
      tokens[index].data === ']' ||
      tokens[index].data === 'integer'
    )) index++
  }
}
