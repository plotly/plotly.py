var assignments = require('./assignments')
var ignoredKeywords = require('./ignored')

module.exports = assigns

// Here be dragons. Apologies in advance for the hairy code!
function assigns(tokens) {
  var idx = 0

  // Determine if a value has been assigned, e.g.
  // x = 1.0;
  // float x = 1.0;
  for (var i = 0; i < tokens.length; i++) {
    var token = tokens[i]
    var type  = token.type

    token.assignment = false
    token.declaration = false
    if (type !== 'ident' && type !== 'builtin') continue
    idx = i + 1

    skipWhitespace(+1)
    if (tokens[idx].type !== 'operator') continue
    if (!assignments[tokens[idx].data]) continue
    token.assignment = true
  }

  // Determine if a value is being defined, e.g.
  // float x;
  // float x, y, z;
  // float x, y = vec3(sin(1.0 + 3.0)), z;
  // float[3][2] x, y = vec3(sin(1.0 + 3.0)), z;
  // float[][2] x, y = vec3(sin(1.0 + 3.0)), z;
  // float x[2], y = vec3(sin(1.0 + 3.0)), z[4];
  // float x(float y, float z) {};
  // float x(float y[2], Thing[3] z) {};
  // Thing x[2], y = Another(sin(1.0 + 3.0)), z[4];
  for (var i = 0; i < tokens.length; i++) {
    var datatype = tokens[i]
    var type     = datatype.type
    var data     = datatype.data

    datatype.declaration = false

    if (type === 'keyword') {
      if (ignoredKeywords[data]) continue
    } else
    if (type !== 'ident') continue

    idx = i + 1

    skipArrayDimensions()
    if (tokens[idx].type !== 'ident') continue
    tokens[idx++].declaration = true
    skipArrayDimensions()

    // Function arguments/parameters
    if (tokens[idx].data === '(') {
      idx++

      skipWhitespace(+1)
      while (tokens[idx] && tokens[idx].data !== ')') {
        if (tokens[idx].type !== 'keyword' && tokens[idx].type !== 'ident') break
        idx++
        skipWhitespace(+1)
        if (tokens[idx].type !== 'ident') continue
        tokens[idx++].declaration = true
        skipWhitespace(+1)
        skipArrayDimensions()
        skipWhitespace(+1)
        if (tokens[idx].data !== ',') continue
        idx++
        skipWhitespace(+1)
      }

      i = idx
      continue
    }

    // Declaration Lists
    while (tokens[idx] && tokens[idx].data !== ';') {
      if (tokens[idx].data === ',') {
        idx++
        skipWhitespace(+1)
        if (tokens[idx].declaration = tokens[idx].type === 'ident') idx++
      } else {
        skipWhitespace(+1)
        skipParens()
        skipWhitespace(+1)
        idx++
      }
    }

    i = idx
  }

  // Handle struct declarations:
  // struct declaration {
  //   float x, y, z;
  //   Other w;
  // } declaration;
  for (var i = 0; i < tokens.length; i++) {
    var token = tokens[i]
    if (token.type !== 'keyword') continue
    if (token.data !== 'struct') continue
    idx = i + 1
    skipWhitespace(+1)
    if (tokens[idx].type !== 'ident') continue

    idx++
    skipWhitespace(+1)
    if (tokens[idx++].data !== '{') continue
    skipWhitespace(+1)

    while (tokens[idx].type === 'ident' || tokens[idx].type === 'keyword') {
      do {
        idx++
        skipWhitespace(+1)
        tokens[idx].structMember = true
        tokens[idx].declaration = false
        idx++
        skipArrayDimensions()
      } while (tokens[idx].data === ',')

      if (tokens[idx].data === ';') idx++
      skipWhitespace()
    }

    idx++
    skipWhitespace(+1)
    if (tokens[idx].type !== 'ident') continue
    tokens[idx].declaration = true
    skipWhitespace(+1)

    while (tokens[++idx].data === ',') {
      skipWhitespace(+1)
      idx++
      skipWhitespace(+1)
      if (tokens[idx].type === 'ident') tokens[idx].declaration = true
      skipWhitespace(+1)
    }
  }

  return tokens

  function skipWhitespace(n) {
    while (tokens[idx] && tokens[idx].type === 'whitespace') idx++
  }

  function skipArrayDimensions() {
    while (tokens[idx] && (
         tokens[idx].type === 'integer'
      || tokens[idx].data === '['
      || tokens[idx].data === ']'
      || tokens[idx].type === 'whitespace'
    )) idx++
  }

  function skipParens() {
    if (!tokens[idx]) return
    if (tokens[idx].data !== '(') return
    var depth = 0
    var a = idx
    do {
      if (tokens[idx].data === ';') break
      if (tokens[idx].data === '(') depth++
      if (tokens[idx].data === ')') depth--
    } while(depth && tokens[++idx])
  }
}
