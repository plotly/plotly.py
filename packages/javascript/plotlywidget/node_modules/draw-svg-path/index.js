var abs = require('abs-svg-path')
var normalize = require('normalize-svg-path')

var methods = {
  'M': 'moveTo',
  'C': 'bezierCurveTo'
}

module.exports = function(context, segments) {
  context.beginPath()

  // Make path easy to reproduce.
  normalize(abs(segments)).forEach(
    function(segment) {
      var command = segment[0]
      var args = segment.slice(1)

      // Convert the path command to a context method.
      context[methods[command]].apply(context, args)
    }
  )

  context.closePath()
}
