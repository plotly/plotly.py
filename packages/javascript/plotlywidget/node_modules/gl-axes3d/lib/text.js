"use strict"

module.exports = createTextSprites

var createBuffer  = require('gl-buffer')
var createVAO     = require('gl-vao')
var vectorizeText = require('vectorize-text')
var createShader  = require('./shaders').text

var globals = window || process.global || {}
var __TEXT_CACHE  = globals.__TEXT_CACHE || {}
globals.__TEXT_CACHE = {}

//Vertex buffer format for text is:
//
/// [x,y,z] = Spatial coordinate
//

var VERTEX_SIZE = 3

function TextSprites(
  gl,
  shader,
  buffer,
  vao) {
  this.gl           = gl
  this.shader       = shader
  this.buffer       = buffer
  this.vao          = vao
  this.tickOffset   =
  this.tickCount    =
  this.labelOffset  =
  this.labelCount   = null
}

var proto = TextSprites.prototype

//Bind textures for rendering
var SHAPE = [0,0]
proto.bind = function(model, view, projection, pixelScale) {
  this.vao.bind()
  this.shader.bind()
  var uniforms = this.shader.uniforms
  uniforms.model = model
  uniforms.view = view
  uniforms.projection = projection
  uniforms.pixelScale = pixelScale
  SHAPE[0] = this.gl.drawingBufferWidth
  SHAPE[1] = this.gl.drawingBufferHeight
  this.shader.uniforms.resolution = SHAPE
}

proto.unbind = function() {
  this.vao.unbind()
}

proto.update = function(bounds, labels, labelFont, ticks, tickFont) {
  var data = []

  function addItem(t, text, font, size, lineSpacing, styletags) {
    var fontcache = __TEXT_CACHE[font]
    if(!fontcache) {
      fontcache = __TEXT_CACHE[font] = {}
    }
    var mesh = fontcache[text]
    if(!mesh) {
      mesh = fontcache[text] = tryVectorizeText(text, {
        triangles: true,
        font: font,
        textAlign: 'center',
        textBaseline: 'middle',
        lineSpacing: lineSpacing,
        styletags: styletags
      })
    }
    var scale = (size || 12) / 12
    var positions = mesh.positions
    var cells = mesh.cells
    for(var i=0, nc=cells.length; i<nc; ++i) {
      var c = cells[i]
      for(var j=2; j>=0; --j) {
        var p = positions[c[j]]
        data.push(scale*p[0], -scale*p[1], t)
      }
    }
  }

  //Generate sprites for all 3 axes, store data in texture atlases
  var tickOffset  = [0,0,0]
  var tickCount   = [0,0,0]
  var labelOffset = [0,0,0]
  var labelCount  = [0,0,0]
  var lineSpacing = 1.25
  var styletags = {
    breaklines:true,
    bolds: true,
    italics: true,
    subscripts:true,
    superscripts:true
  }
  for(var d=0; d<3; ++d) {

    //Generate label
    labelOffset[d] = (data.length/VERTEX_SIZE)|0
    addItem(
      0.5*(bounds[0][d]+bounds[1][d]),
      labels[d],
      labelFont[d],
      12, // labelFontSize
      lineSpacing,
      styletags
    )
    labelCount[d] = ((data.length/VERTEX_SIZE)|0) - labelOffset[d]

    //Generate sprites for tick marks
    tickOffset[d] = (data.length/VERTEX_SIZE)|0
    for(var i=0; i<ticks[d].length; ++i) {
      if(!ticks[d][i].text) {
        continue
      }
      addItem(
        ticks[d][i].x,
        ticks[d][i].text,
        ticks[d][i].font || tickFont,
        ticks[d][i].fontSize || 12,
        lineSpacing,
        styletags
      )
    }
    tickCount[d] = ((data.length/VERTEX_SIZE)|0) - tickOffset[d]
  }

  this.buffer.update(data)
  this.tickOffset = tickOffset
  this.tickCount = tickCount
  this.labelOffset = labelOffset
  this.labelCount = labelCount
}

//Draws the tick marks for an axis
proto.drawTicks = function(d, scale, angle, offset, color, axis, alignDir, alignOpt) {
  if(!this.tickCount[d]) {
    return
  }

  this.shader.uniforms.axis = axis
  this.shader.uniforms.color = color
  this.shader.uniforms.angle = angle
  this.shader.uniforms.scale = scale
  this.shader.uniforms.offset = offset
  this.shader.uniforms.alignDir = alignDir
  this.shader.uniforms.alignOpt = alignOpt
  this.vao.draw(this.gl.TRIANGLES, this.tickCount[d], this.tickOffset[d])
}

//Draws the text label for an axis
proto.drawLabel = function(d, scale, angle, offset, color, axis, alignDir, alignOpt) {
  if(!this.labelCount[d]) {
    return
  }

  this.shader.uniforms.axis = axis
  this.shader.uniforms.color = color
  this.shader.uniforms.angle = angle
  this.shader.uniforms.scale = scale
  this.shader.uniforms.offset = offset
  this.shader.uniforms.alignDir = alignDir
  this.shader.uniforms.alignOpt = alignOpt
  this.vao.draw(this.gl.TRIANGLES, this.labelCount[d], this.labelOffset[d])
}

//Releases all resources attached to this object
proto.dispose = function() {
  this.shader.dispose()
  this.vao.dispose()
  this.buffer.dispose()
}

function tryVectorizeText(text, options) {
  try {
    return vectorizeText(text, options)
  } catch(e) {
    console.warn('error vectorizing text:"' + text + '" error:', e)
    return {
      cells: [],
      positions: []
    }
  }
}

function createTextSprites(
    gl,
    bounds,
    labels,
    labelFont,
    ticks,
    tickFont) {

  var buffer = createBuffer(gl)
  var vao = createVAO(gl, [
    { "buffer": buffer,
      "size": 3
    }
  ])

  var shader = createShader(gl)
  shader.attributes.position.location = 0

  var result = new TextSprites(
    gl,
    shader,
    buffer,
    vao)

  result.update(bounds, labels, labelFont, ticks, tickFont)

  return result
}
