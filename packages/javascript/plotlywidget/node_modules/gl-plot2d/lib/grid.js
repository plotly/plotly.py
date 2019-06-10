'use strict'

module.exports = createGrid

var createBuffer  = require('gl-buffer')
var createShader  = require('gl-shader')
var bsearch       = require('binary-search-bounds')
var shaders       = require('./shaders')

function Grid(plot, vbo, shader, tickShader) {
  this.plot   = plot
  this.vbo    = vbo
  this.shader = shader
  this.tickShader = tickShader
  this.ticks  = [[], []]
}

function compareTickNum(a, b) {
  return a - b
}

var proto = Grid.prototype

proto.draw = (function() {

  var DATA_SHIFT = [0,0]
  var DATA_SCALE = [0,0]
  var DATA_AXIS  = [0,0]

  return function() {
    var plot       = this.plot
    var vbo        = this.vbo
    var shader     = this.shader
    var ticks      = this.ticks
    var gl         = plot.gl
    var bounds     = plot._tickBounds
    var dataBox    = plot.dataBox
    var viewPixels = plot.viewBox
    var lineWidth  = plot.gridLineWidth
    var gridColor  = plot.gridLineColor
    var gridEnable = plot.gridLineEnable
    var pixelRatio = plot.pixelRatio

    for(var i=0; i<2; ++i) {
      var lo = bounds[i]
      var hi = bounds[i+2]
      var boundScale = hi - lo
      var dataCenter  = 0.5 * (dataBox[i+2] + dataBox[i])
      var dataWidth   = dataBox[i+2] - dataBox[i]
      DATA_SCALE[i] = 2.0 * boundScale / dataWidth
      DATA_SHIFT[i] = 2.0 * (lo - dataCenter) / dataWidth
    }

    shader.bind()
    vbo.bind()
    shader.attributes.dataCoord.pointer()
    shader.uniforms.dataShift = DATA_SHIFT
    shader.uniforms.dataScale = DATA_SCALE

    var offset = 0
    for(var i=0; i<2; ++i) {
      DATA_AXIS[0] = DATA_AXIS[1] = 0
      DATA_AXIS[i] = 1
      shader.uniforms.dataAxis  = DATA_AXIS
      shader.uniforms.lineWidth = lineWidth[i] / (viewPixels[i+2] - viewPixels[i]) * pixelRatio
      shader.uniforms.color     = gridColor[i]

      var size = ticks[i].length * 6
      if(gridEnable[i] && size) {
        gl.drawArrays(gl.TRIANGLES, offset, size)
      }
      offset += size
    }
  }
})()

proto.drawTickMarks = (function() {
  var DATA_SHIFT = [0,0]
  var DATA_SCALE = [0,0]
  var X_AXIS     = [1,0]
  var Y_AXIS     = [0,1]
  var SCR_OFFSET = [0,0]
  var TICK_SCALE = [0,0]

  return function() {
    var plot       = this.plot
    var vbo        = this.vbo
    var shader     = this.tickShader
    var ticks      = this.ticks
    var gl         = plot.gl
    var bounds     = plot._tickBounds
    var dataBox    = plot.dataBox
    var viewBox    = plot.viewBox
    var pixelRatio = plot.pixelRatio
    var screenBox  = plot.screenBox

    var screenWidth  = screenBox[2] - screenBox[0]
    var screenHeight = screenBox[3] - screenBox[1]
    var viewWidth    = viewBox[2]   - viewBox[0]
    var viewHeight   = viewBox[3]   - viewBox[1]

    for(var i=0; i<2; ++i) {
      var lo = bounds[i]
      var hi = bounds[i+2]
      var boundScale = hi - lo
      var dataCenter  = 0.5 * (dataBox[i+2] + dataBox[i])
      var dataWidth   = (dataBox[i+2] - dataBox[i])
      DATA_SCALE[i] = 2.0 * boundScale / dataWidth
      DATA_SHIFT[i] = 2.0 * (lo - dataCenter) / dataWidth
    }

    DATA_SCALE[0] *= viewWidth / screenWidth
    DATA_SHIFT[0] *= viewWidth / screenWidth

    DATA_SCALE[1] *= viewHeight / screenHeight
    DATA_SHIFT[1] *= viewHeight / screenHeight

    shader.bind()
    vbo.bind()

    shader.attributes.dataCoord.pointer()

    var uniforms = shader.uniforms
    uniforms.dataShift = DATA_SHIFT
    uniforms.dataScale = DATA_SCALE

    var tickMarkLength = plot.tickMarkLength
    var tickMarkWidth  = plot.tickMarkWidth
    var tickMarkColor  = plot.tickMarkColor

    var xTicksOffset = 0
    var yTicksOffset = ticks[0].length * 6

    var xStart = Math.min(bsearch.ge(ticks[0], (dataBox[0] - bounds[0]) / (bounds[2] - bounds[0]), compareTickNum), ticks[0].length)
    var xEnd   = Math.min(bsearch.gt(ticks[0], (dataBox[2] - bounds[0]) / (bounds[2] - bounds[0]), compareTickNum), ticks[0].length)
    var xOffset = xTicksOffset + 6 * xStart
    var xCount  = 6 * Math.max(0, xEnd - xStart)

    var yStart = Math.min(bsearch.ge(ticks[1], (dataBox[1] - bounds[1]) / (bounds[3] - bounds[1]), compareTickNum), ticks[1].length)
    var yEnd   = Math.min(bsearch.gt(ticks[1], (dataBox[3] - bounds[1]) / (bounds[3] - bounds[1]), compareTickNum), ticks[1].length)
    var yOffset = yTicksOffset + 6 * yStart
    var yCount  = 6 * Math.max(0, yEnd - yStart)

    SCR_OFFSET[0]         = 2.0 * (viewBox[0] - tickMarkLength[1]) / screenWidth - 1.0
    SCR_OFFSET[1]         = (viewBox[3] + viewBox[1]) / screenHeight - 1.0
    TICK_SCALE[0]         = tickMarkLength[1] * pixelRatio / screenWidth
    TICK_SCALE[1]         = tickMarkWidth[1]  * pixelRatio / screenHeight

    if(yCount) {
      uniforms.color        = tickMarkColor[1]
      uniforms.tickScale    = TICK_SCALE
      uniforms.dataAxis     = Y_AXIS
      uniforms.screenOffset = SCR_OFFSET
      gl.drawArrays(gl.TRIANGLES, yOffset, yCount)
    }

    SCR_OFFSET[0]         = (viewBox[2] + viewBox[0]) / screenWidth - 1.0
    SCR_OFFSET[1]         = 2.0 * (viewBox[1] - tickMarkLength[0]) / screenHeight - 1.0
    TICK_SCALE[0]         = tickMarkWidth[0]  * pixelRatio / screenWidth
    TICK_SCALE[1]         = tickMarkLength[0] * pixelRatio / screenHeight

    if(xCount) {
      uniforms.color        = tickMarkColor[0]
      uniforms.tickScale    = TICK_SCALE
      uniforms.dataAxis     = X_AXIS
      uniforms.screenOffset = SCR_OFFSET
      gl.drawArrays(gl.TRIANGLES, xOffset, xCount)
    }

    SCR_OFFSET[0]         = 2.0 * (viewBox[2] + tickMarkLength[3]) / screenWidth - 1.0
    SCR_OFFSET[1]         = (viewBox[3] + viewBox[1]) / screenHeight - 1.0
    TICK_SCALE[0]         = tickMarkLength[3] * pixelRatio / screenWidth
    TICK_SCALE[1]         = tickMarkWidth[3]  * pixelRatio / screenHeight

    if(yCount) {
      uniforms.color        = tickMarkColor[3]
      uniforms.tickScale    = TICK_SCALE
      uniforms.dataAxis     = Y_AXIS
      uniforms.screenOffset = SCR_OFFSET
      gl.drawArrays(gl.TRIANGLES, yOffset, yCount)
    }

    SCR_OFFSET[0]         = (viewBox[2] + viewBox[0]) / screenWidth - 1.0
    SCR_OFFSET[1]         = 2.0 * (viewBox[3] + tickMarkLength[2]) / screenHeight - 1.0
    TICK_SCALE[0]         = tickMarkWidth[2]  * pixelRatio / screenWidth
    TICK_SCALE[1]         = tickMarkLength[2] * pixelRatio / screenHeight

    if(xCount) {
      uniforms.color        = tickMarkColor[2]
      uniforms.tickScale    = TICK_SCALE
      uniforms.dataAxis     = X_AXIS
      uniforms.screenOffset = SCR_OFFSET
      gl.drawArrays(gl.TRIANGLES, xOffset, xCount)
    }
  }
})()

proto.update = (function() {
  var OFFSET_X = [1,  1, -1, -1,  1, -1]
  var OFFSET_Y = [1, -1,  1,  1, -1, -1]

  return function(options) {
    var ticks  = options.ticks
    var bounds = options.bounds
    var data   = new Float32Array(6 * 3 * (ticks[0].length + ticks[1].length))

    var zeroLineEnable = this.plot.zeroLineEnable

    var ptr    = 0
    var gridTicks = [[], []]
    for(var dim=0; dim<2; ++dim) {
      var localTicks = gridTicks[dim]
      var axisTicks = ticks[dim]
      var lo = bounds[dim]
      var hi = bounds[dim+2]
      for(var i=0; i<axisTicks.length; ++i) {
        var x = (axisTicks[i].x - lo) / (hi - lo)
        localTicks.push(x)
        for(var j=0; j<6; ++j) {
          data[ptr++] = x
          data[ptr++] = OFFSET_X[j]
          data[ptr++] = OFFSET_Y[j]
        }
      }
    }

    this.ticks = gridTicks
    this.vbo.update(data)
  }
})()

proto.dispose = function() {
  this.vbo.dispose()
  this.shader.dispose()
  this.tickShader.dispose()
}

function createGrid(plot) {
  var gl     = plot.gl
  var vbo    = createBuffer(gl)
  var shader = createShader(gl, shaders.gridVert, shaders.gridFrag)
  var tickShader = createShader(gl, shaders.tickVert, shaders.gridFrag)
  var grid   = new Grid(plot, vbo, shader, tickShader)
  return grid
}
