const through = require('through2')

module.exports = function () {
  return through(function () {
    var stream = this

    setTimeout(function () {
      stream.emit('error', new Error('Hello world!'))
    }, 500)
  })
}
