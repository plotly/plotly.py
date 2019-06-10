module.exports = tokenScope

function tokenScope(tokens) {
  var stack  = [0]
  var inc    = stack[0]
  var ldepth = 0

  if (!tokens || !tokens.length) return tokens
  if (!('depth' in tokens[0])) {
    throw new Error('glsl-token-scope: No scope depth defined on tokens! Use glsl-token-depth on these tokens first')
  }

  for (var i = 0; i < tokens.length; i++) {
    var token = tokens[i]
    var depth = token.depth

    if (depth > ldepth) {
      stack.push(++inc)
    } else
    if (depth < ldepth) {
      stack.splice(-1, 1)
    }

    token.scope = stack[stack.length - 1]
    token.stack = stack.slice()
    ldepth = token.depth
  }

  return tokens
}
