'use strict'

module.exports = createTextElements

var createBuffer = require('gl-buffer')
var createShader = require('gl-shader')
var getText      = require('text-cache')
var bsearch      = require('binary-search-bounds')
var shaders      = require('./shaders')

function TextElements(plot, vbo, shader) {
  this.plot         = plot
  this.vbo          = vbo
  this.shader       = shader
  this.tickOffset   = [[],[]]
  this.tickX        = [[],[]]
  this.labelOffset  = [0,0]
  this.labelCount   = [0,0]
}

var proto = TextElements.prototype

proto.drawTicks = (function() {
  var DATA_AXIS = [0,0]
  var SCREEN_OFFSET = [0,0]
  var ZERO_2 = [0,0]

  return function(axis) {
    var plot        = this.plot
    var shader      = this.shader
    var tickX       = this.tickX[axis]
    var tickOffset  = this.tickOffset[axis]
    var gl          = plot.gl
    var viewBox     = plot.viewBox
    var dataBox     = plot.dataBox
    var screenBox   = plot.screenBox
    var pixelRatio  = plot.pixelRatio
    var tickEnable  = plot.tickEnable
    var tickPad     = plot.tickPad
    var textColor   = plot.tickColor
    var textAngle   = plot.tickAngle
    // todo check if this should be used (now unused)
    // var tickLength  = plot.tickMarkLength

    var labelEnable = plot.labelEnable
    var labelPad    = plot.labelPad
    var labelColor  = plot.labelColor
    var labelAngle  = plot.labelAngle
    var labelOffset = this.labelOffset[axis]
    var labelCount  = this.labelCount[axis]

    var start = bsearch.lt(tickX, dataBox[axis])
    var end   = bsearch.le(tickX, dataBox[axis+2])

    DATA_AXIS[0]    = DATA_AXIS[1] = 0
    DATA_AXIS[axis] = 1

    SCREEN_OFFSET[axis] = (viewBox[2+axis] + viewBox[axis]) / (screenBox[2+axis] - screenBox[axis]) - 1.0

    var screenScale = 2.0 / screenBox[2+(axis^1)] - screenBox[axis^1]

    SCREEN_OFFSET[axis^1] = screenScale * viewBox[axis^1] - 1.0
    if(tickEnable[axis]) {
      SCREEN_OFFSET[axis^1] -= screenScale * pixelRatio * tickPad[axis]
      if(start < end && tickOffset[end] > tickOffset[start]) {
        shader.uniforms.dataAxis     = DATA_AXIS
        shader.uniforms.screenOffset = SCREEN_OFFSET
        shader.uniforms.color        = textColor[axis]
        shader.uniforms.angle        = textAngle[axis]
        gl.drawArrays(
          gl.TRIANGLES,
          tickOffset[start],
          tickOffset[end] - tickOffset[start])
      }
    }
    if(labelEnable[axis] && labelCount) {
      SCREEN_OFFSET[axis^1] -= screenScale * pixelRatio * labelPad[axis]
      shader.uniforms.dataAxis     = ZERO_2
      shader.uniforms.screenOffset = SCREEN_OFFSET
      shader.uniforms.color        = labelColor[axis]
      shader.uniforms.angle        = labelAngle[axis]
      gl.drawArrays(
        gl.TRIANGLES,
        labelOffset,
        labelCount)
    }

    SCREEN_OFFSET[axis^1] = screenScale * viewBox[2+(axis^1)] - 1.0
    if(tickEnable[axis+2]) {
      SCREEN_OFFSET[axis^1] += screenScale * pixelRatio * tickPad[axis+2]
      if(start < end && tickOffset[end] > tickOffset[start]) {
        shader.uniforms.dataAxis     = DATA_AXIS
        shader.uniforms.screenOffset = SCREEN_OFFSET
        shader.uniforms.color        = textColor[axis+2]
        shader.uniforms.angle        = textAngle[axis+2]
        gl.drawArrays(
          gl.TRIANGLES,
          tickOffset[start],
          tickOffset[end] - tickOffset[start])
      }
    }
    if(labelEnable[axis+2] && labelCount) {
      SCREEN_OFFSET[axis^1] += screenScale * pixelRatio * labelPad[axis+2]
      shader.uniforms.dataAxis     = ZERO_2
      shader.uniforms.screenOffset = SCREEN_OFFSET
      shader.uniforms.color        = labelColor[axis+2]
      shader.uniforms.angle        = labelAngle[axis+2]
      gl.drawArrays(
        gl.TRIANGLES,
        labelOffset,
        labelCount)
    }

  }
})()

proto.drawTitle = (function() {
  var DATA_AXIS = [0,0]
  var SCREEN_OFFSET = [0,0]

  return function() {
    var plot        = this.plot
    var shader      = this.shader
    var gl          = plot.gl
    var screenBox   = plot.screenBox
    var titleCenter = plot.titleCenter
    var titleAngle  = plot.titleAngle
    var titleColor  = plot.titleColor
    var pixelRatio  = plot.pixelRatio

    if(!this.titleCount) {
      return
    }

    for(var i=0; i<2; ++i) {
      SCREEN_OFFSET[i] = 2.0 * (titleCenter[i]*pixelRatio - screenBox[i]) /
        (screenBox[2+i] - screenBox[i]) - 1
    }

    shader.bind()
    shader.uniforms.dataAxis      = DATA_AXIS
    shader.uniforms.screenOffset  = SCREEN_OFFSET
    shader.uniforms.angle         = titleAngle
    shader.uniforms.color         = titleColor

    gl.drawArrays(gl.TRIANGLES, this.titleOffset, this.titleCount)
  }
})()

proto.bind = (function() {
  var DATA_SHIFT = [0,0]
  var DATA_SCALE = [0,0]
  var TEXT_SCALE = [0,0]

  return function() {
    var plot      = this.plot
    var shader    = this.shader
    var bounds    = plot._tickBounds
    var dataBox   = plot.dataBox
    var screenBox = plot.screenBox
    var viewBox   = plot.viewBox

    shader.bind()

    //Set up coordinate scaling uniforms
    for(var i=0; i<2; ++i) {

      var lo = bounds[i]
      var hi = bounds[i+2]
      var boundScale = hi - lo
      var dataCenter  = 0.5 * (dataBox[i+2] + dataBox[i])
      var dataWidth   = (dataBox[i+2] - dataBox[i])

      var viewLo = viewBox[i]
      var viewHi = viewBox[i+2]
      var viewScale = viewHi - viewLo
      var screenLo = screenBox[i]
      var screenHi = screenBox[i+2]
      var screenScale = screenHi - screenLo

      DATA_SCALE[i] = 2.0 * boundScale / dataWidth * viewScale / screenScale
      DATA_SHIFT[i] = 2.0 * (lo - dataCenter) / dataWidth * viewScale / screenScale
    }

    TEXT_SCALE[1] = 2.0 * plot.pixelRatio / (screenBox[3] - screenBox[1])
    TEXT_SCALE[0] = TEXT_SCALE[1] * (screenBox[3] - screenBox[1]) / (screenBox[2] - screenBox[0])

    shader.uniforms.dataScale = DATA_SCALE
    shader.uniforms.dataShift = DATA_SHIFT
    shader.uniforms.textScale = TEXT_SCALE

    //Set attributes
    this.vbo.bind()
    shader.attributes.textCoordinate.pointer()
  }
})()

proto.update = function(options) {
  var vertices  = []
  var axesTicks = options.ticks
  var bounds    = options.bounds
  var i, j, k, data, scale, dimension

  for(dimension=0; dimension<2; ++dimension) {
    var offsets = [Math.floor(vertices.length/3)], tickX = [-Infinity]

    //Copy vertices over to buffer
    var ticks = axesTicks[dimension]
    for(i=0; i<ticks.length; ++i) {
      var tick  = ticks[i]
      var x     = tick.x
      var text  = tick.text
      var font  = tick.font || 'sans-serif'
      scale = (tick.fontSize || 12)

      var coordScale = 1.0 / (bounds[dimension+2] - bounds[dimension])
      var coordShift = bounds[dimension]

      var rows = text.split('\n')
      for(var r = 0; r < rows.length; r++) {
        data = getText(font, rows[r]).data
        for (j = 0; j < data.length; j += 2) {
          vertices.push(
              data[j] * scale,
              -data[j + 1] * scale - r * scale * 1.2,
              (x - coordShift) * coordScale)
        }
      }

      offsets.push(Math.floor(vertices.length/3))
      tickX.push(x)
    }

    this.tickOffset[dimension] = offsets
    this.tickX[dimension] = tickX
  }

  //Add labels
  for(dimension=0; dimension<2; ++dimension) {
    this.labelOffset[dimension] = Math.floor(vertices.length/3)

    data  = getText(options.labelFont[dimension], options.labels[dimension], { textAlign: 'center' }).data
    scale = options.labelSize[dimension]
    for(i=0; i<data.length; i+=2) {
      vertices.push(data[i]*scale, -data[i+1]*scale, 0)
    }

    this.labelCount[dimension] =
      Math.floor(vertices.length/3) - this.labelOffset[dimension]
  }

  //Add title
  this.titleOffset = Math.floor(vertices.length/3)
  data = getText(options.titleFont, options.title).data
  scale = options.titleSize
  for(i=0; i<data.length; i+=2) {
    vertices.push(data[i]*scale, -data[i+1]*scale, 0)
  }
  this.titleCount = Math.floor(vertices.length/3) - this.titleOffset

  //Upload new vertices
  this.vbo.update(vertices)
}

proto.dispose = function() {
  this.vbo.dispose()
  this.shader.dispose()
}

function createTextElements(plot) {
  var gl = plot.gl
  var vbo = createBuffer(gl)
  var shader = createShader(gl, shaders.textVert, shaders.textFrag)
  var text = new TextElements(plot, vbo, shader)
  return text
}
