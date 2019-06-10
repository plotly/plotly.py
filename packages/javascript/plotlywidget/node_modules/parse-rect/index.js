'use strict'

var pick = require('pick-by-alias')

module.exports = parseRect

function parseRect (arg) {
  var rect

  // direct arguments sequence
  if (arguments.length > 1) {
    arg = arguments
  }

  // svg viewbox
  if (typeof arg === 'string') {
    arg = arg.split(/\s/).map(parseFloat)
  }
  else if (typeof arg === 'number') {
    arg = [arg]
  }

  // 0, 0, 100, 100 - array-like
  if (arg.length && typeof arg[0] === 'number') {
    // [w, w]
    if (arg.length === 1) {
      rect = {
        width: arg[0],
        height: arg[0],
        x: 0, y: 0
      }
    }
    // [w, h]
    else if (arg.length === 2) {
      rect = {
        width: arg[0],
        height: arg[1],
        x: 0, y: 0
      }
    }
    // [l, t, r, b]
    else {
      rect = {
        x: arg[0],
        y: arg[1],
        width: (arg[2] - arg[0]) || 0,
        height: (arg[3] - arg[1]) || 0
      }
    }
  }
  // {x, y, w, h} or {l, t, b, r}
  else if (arg) {
    arg = pick(arg, {
      left: 'x l left Left',
      top: 'y t top Top',
      width: 'w width W Width',
      height: 'h height W Width',
      bottom: 'b bottom Bottom',
      right: 'r right Right'
    })

    rect = {
      x: arg.left || 0,
      y: arg.top || 0
    }

    if (arg.width == null) {
      if (arg.right) rect.width = arg.right - rect.x
      else rect.width = 0
    }
    else {
      rect.width = arg.width
    }

    if (arg.height == null) {
      if (arg.bottom) rect.height = arg.bottom - rect.y
      else rect.height = 0
    }
    else {
      rect.height = arg.height
    }
  }

  return rect
}
