var glslify = require('glslify')

exports.pointVertex       = glslify('./shader/point-vertex.glsl')
exports.pointFragment     = glslify('./shader/point-fragment.glsl')
exports.pickVertex        = glslify('./shader/pick-vertex.glsl')
exports.pickFragment      = glslify('./shader/pick-fragment.glsl')
