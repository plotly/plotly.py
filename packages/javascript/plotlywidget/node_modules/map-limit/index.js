var once = require('once')
var noop = function noop(){}

module.exports = mapLimit

function mapLimit(arr, limit, iterator, callback) {
  var complete = 0
  var aborted = false
  var results = []
  var queued = 0
  var l = arr.length
  var i = 0

  callback = once(callback || noop)
  if (typeof iterator !== 'function') throw new Error(
    'Iterator function must be passed as the third argument'
  )

  for (var r = 0; r < l; r++) {
    results[r] = null
  }

  flush()

  function flush() {
    if (complete === l)
      return callback(null, results)

    while (queued < limit) {
      if (aborted) break
      if (i === l) break
      push()
    }
  }

  function abort(err) {
    aborted = true
    return callback(err)
  }

  function push() {
    var idx = i++

    queued += 1

    iterator(arr[idx], function(err, result) {
      if (err) return abort(err)
      results[idx] = result
      complete += 1
      queued -= 1
      flush()
    })
  }
}
