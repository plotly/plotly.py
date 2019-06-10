var getContext = require('get-canvas-context')

module.exports = function getWebGLContext (opt) {
  return getContext('webgl', opt)
}
