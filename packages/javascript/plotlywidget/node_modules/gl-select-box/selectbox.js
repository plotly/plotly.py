'use strict'

var createShader = require('gl-shader')
var createBuffer = require('gl-buffer')

var SHADERS = require('./lib/shaders')

module.exports = createSelectBox

function SelectBox(plot, boxBuffer, boxShader) {
  this.plot = plot
  this.boxBuffer = boxBuffer
  this.boxShader = boxShader

  this.enabled = true

  this.selectBox = [Infinity,Infinity,-Infinity,-Infinity]

  this.borderColor = [0,0,0,1]
  this.innerFill   = false
  this.innerColor  = [0,0,0,0.25]
  this.outerFill   = true
  this.outerColor  = [0,0,0,0.5]
  this.borderWidth = 10
}

var proto = SelectBox.prototype

proto.draw = function() {
  if(!this.enabled) {
    return
  }

  var plot         = this.plot
  var selectBox    = this.selectBox
  var lineWidth    = this.borderWidth

  var innerFill    = this.innerFill
  var innerColor   = this.innerColor
  var outerFill    = this.outerFill
  var outerColor   = this.outerColor
  var borderColor  = this.borderColor

  var boxes        = plot.box
  var screenBox    = plot.screenBox
  var dataBox      = plot.dataBox
  var viewBox      = plot.viewBox
  var pixelRatio   = plot.pixelRatio

  //Map select box into pixel coordinates
  var loX = (selectBox[0]-dataBox[0])*(viewBox[2]-viewBox[0])/(dataBox[2]-dataBox[0])+viewBox[0]
  var loY = (selectBox[1]-dataBox[1])*(viewBox[3]-viewBox[1])/(dataBox[3]-dataBox[1])+viewBox[1]
  var hiX = (selectBox[2]-dataBox[0])*(viewBox[2]-viewBox[0])/(dataBox[2]-dataBox[0])+viewBox[0]
  var hiY = (selectBox[3]-dataBox[1])*(viewBox[3]-viewBox[1])/(dataBox[3]-dataBox[1])+viewBox[1]

  loX = Math.max(loX, viewBox[0])
  loY = Math.max(loY, viewBox[1])
  hiX = Math.min(hiX, viewBox[2])
  hiY = Math.min(hiY, viewBox[3])

  if(hiX < loX || hiY < loY) {
    return
  }

  boxes.bind()

  //Draw box
  var screenWidth  = screenBox[2] - screenBox[0]
  var screenHeight = screenBox[3] - screenBox[1]

  if(this.outerFill) {
    boxes.drawBox(0, 0, screenWidth, loY, outerColor)
    boxes.drawBox(0, loY, loX, hiY, outerColor)
    boxes.drawBox(0, hiY, screenWidth, screenHeight, outerColor)
    boxes.drawBox(hiX, loY, screenWidth, hiY, outerColor)
  }

  if(this.innerFill) {
    boxes.drawBox(loX, loY, hiX, hiY, innerColor)
  }

  //Draw border
  if(lineWidth > 0) {

    //Draw border
    var w = lineWidth * pixelRatio
    boxes.drawBox(loX-w, loY-w, hiX+w, loY+w, borderColor)
    boxes.drawBox(loX-w, hiY-w, hiX+w, hiY+w, borderColor)
    boxes.drawBox(loX-w, loY-w, loX+w, hiY+w, borderColor)
    boxes.drawBox(hiX-w, loY-w, hiX+w, hiY+w, borderColor)
  }
}

proto.update = function(options) {
  options = options || {}

  this.innerFill    = !!options.innerFill
  this.outerFill    = !!options.outerFill
  this.innerColor   = (options.innerColor   || [0,0,0,0.5]).slice()
  this.outerColor   = (options.outerColor   || [0,0,0,0.5]).slice()
  this.borderColor  = (options.borderColor || [0,0,0,1]).slice()
  this.borderWidth  = options.borderWidth || 0
  this.selectBox    = (options.selectBox || this.selectBox).slice()
}

proto.dispose = function() {
  this.boxBuffer.dispose()
  this.boxShader.dispose()
  this.plot.removeOverlay(this)
}

function createSelectBox(plot, options) {
  var gl = plot.gl
  var buffer = createBuffer(gl, [
    0, 0,
    0, 1,
    1, 0,
    1, 1 ])
  var shader = createShader(gl, SHADERS.boxVertex, SHADERS.boxFragment)
  var selectBox = new SelectBox(plot, buffer, shader)
  selectBox.update(options)
  plot.addOverlay(selectBox)
  return selectBox
}
