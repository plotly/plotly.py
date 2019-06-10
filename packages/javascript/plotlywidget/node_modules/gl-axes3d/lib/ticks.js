'use strict'

exports.create   = defaultTicks
exports.equal    = ticksEqual

function prettyPrint(spacing, i) {
  var stepStr = spacing + ""
  var u = stepStr.indexOf(".")
  var sigFigs = 0
  if(u >= 0) {
    sigFigs = stepStr.length - u - 1
  }
  var shift = Math.pow(10, sigFigs)
  var x = Math.round(spacing * i * shift)
  var xstr = x + ""
  if(xstr.indexOf("e") >= 0) {
    return xstr
  }
  var xi = x / shift, xf = x % shift
  if(x < 0) {
    xi = -Math.ceil(xi)|0
    xf = (-xf)|0
  } else {
    xi = Math.floor(xi)|0
    xf = xf|0
  }
  var xis = "" + xi 
  if(x < 0) {
    xis = "-" + xis
  }
  if(sigFigs) {
    var xs = "" + xf
    while(xs.length < sigFigs) {
      xs = "0" + xs
    }
    return xis + "." + xs
  } else {
    return xis
  }
}

function defaultTicks(bounds, tickSpacing) {
  var array = []
  for(var d=0; d<3; ++d) {
    var ticks = []
    var m = 0.5*(bounds[0][d]+bounds[1][d])
    for(var t=0; t*tickSpacing[d]<=bounds[1][d]; ++t) {
      ticks.push({x: t*tickSpacing[d], text: prettyPrint(tickSpacing[d], t)})
    }
    for(var t=-1; t*tickSpacing[d]>=bounds[0][d]; --t) {
      ticks.push({x: t*tickSpacing[d], text: prettyPrint(tickSpacing[d], t)})
    }
    array.push(ticks)
  }
  return array
}

function ticksEqual(ticksA, ticksB) {
  for(var i=0; i<3; ++i) {
    if(ticksA[i].length !== ticksB[i].length) {
      return false
    }
    for(var j=0; j<ticksA[i].length; ++j) {
      var a = ticksA[i][j]
      var b = ticksB[i][j]
      if(
        a.x !== b.x ||
        a.text !== b.text ||
        a.font !== b.font ||
        a.fontColor !== b.fontColor ||
        a.fontSize !== b.fontSize ||
        a.dx !== b.dx ||
        a.dy !== b.dy
      ) {
        return false
      }
    }
  }
  return true
}