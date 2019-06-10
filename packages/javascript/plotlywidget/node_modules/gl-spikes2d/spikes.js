'use strict'

module.exports = createSpikes2D

function GLSpikes2D(plot) {
  this.plot = plot
  this.enable = [true, true, false, false]
  this.width  = [1, 1, 1, 1]
  this.color  = [[0,0,0,1],
                 [0,0,0,1],
                 [0,0,0,1],
                 [0,0,0,1]]
  this.center = [Infinity, Infinity]
}

var proto = GLSpikes2D.prototype

proto.update = function(options) {
  options = options || {}
  this.enable = (options.enable || [true,true,false,false]).slice()
  this.width  = (options.width || [1,1,1,1]).slice()
  this.color  = (options.color || [
                  [0,0,0,1],
                  [0,0,0,1],
                  [0,0,0,1],
                  [0,0,0,1]]).map(function(x) { return x.slice() })
  this.center = (options.center || [Infinity,Infinity]).slice()
  this.plot.setOverlayDirty()
}

proto.draw = function() {
  var spikeEnable = this.enable
  var spikeWidth  = this.width
  var spikeColor  = this.color
  var spikeCenter = this.center
  var plot        = this.plot
  var line        = plot.line

  var dataBox     = plot.dataBox
  var viewPixels  = plot.viewBox

  line.bind()

  if(dataBox[0] <= spikeCenter[0] && spikeCenter[0] <= dataBox[2] &&
     dataBox[1] <= spikeCenter[1] && spikeCenter[1] <= dataBox[3]) {

    var centerX = viewPixels[0] + (spikeCenter[0] - dataBox[0]) / (dataBox[2] - dataBox[0]) * (viewPixels[2] - viewPixels[0])
    var centerY = viewPixels[1] + (spikeCenter[1] - dataBox[1]) / (dataBox[3] - dataBox[1]) * (viewPixels[3] - viewPixels[1])

    if(spikeEnable[0]) {
     line.drawLine(
       centerX, centerY,
       viewPixels[0], centerY,
       spikeWidth[0], spikeColor[0])
    }
    if(spikeEnable[1]) {
     line.drawLine(
       centerX, centerY,
       centerX, viewPixels[1],
       spikeWidth[1], spikeColor[1])
    }
    if(spikeEnable[2]) {
      line.drawLine(
        centerX, centerY,
        viewPixels[2], centerY,
        spikeWidth[2], spikeColor[2])
    }
    if(spikeEnable[3]) {
      line.drawLine(
        centerX, centerY,
        centerX, viewPixels[3],
        spikeWidth[3], spikeColor[3])
    }
  }
}

proto.dispose = function() {
  this.plot.removeOverlay(this)
}

function createSpikes2D(plot, options) {
  var spikes = new GLSpikes2D(plot)
  spikes.update(options)
  plot.addOverlay(spikes)
  return spikes
}
