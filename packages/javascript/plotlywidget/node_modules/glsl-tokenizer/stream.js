var through  = require('through2').obj
var tokenize = require('./index')

module.exports = createStream

function createStream(opt) {
  var generator = tokenize(opt)

  return through(write, end)

  function write(chunk, _, next) {
    flush(this, chunk)
    next()
  }

  function end() {
    flush(this, null)
    this.push(null)
  }

  function flush(stream, chunk) {
    var tokens = generator(chunk)
    for (var i = 0; i < tokens.length; i++) {
      stream.push(tokens[i])
    }
  }
}
