'use strict'

var stringifyFont = require('css-font/stringify')
var defaultChars = [32, 126]

module.exports = atlas

function atlas(options) {
  options = options || {}

  var shape  = options.shape ? options.shape : options.canvas ? [options.canvas.width, options.canvas.height] : [512, 512]
  var canvas = options.canvas || document.createElement('canvas')
  var font   = options.font
  var step   = typeof options.step === 'number' ? [options.step, options.step] : options.step || [32, 32]
  var chars  = options.chars || defaultChars

  if (font && typeof font !== 'string') font = stringifyFont(font)

  if (!Array.isArray(chars)) {
    chars = String(chars).split('')
  } else
  if (chars.length === 2
    && typeof chars[0] === 'number'
    && typeof chars[1] === 'number'
  ) {
    var newchars = []

    for (var i = chars[0], j = 0; i <= chars[1]; i++) {
      newchars[j++] = String.fromCharCode(i)
    }

    chars = newchars
  }

  shape = shape.slice()
  canvas.width  = shape[0]
  canvas.height = shape[1]

  var ctx = canvas.getContext('2d')

  ctx.fillStyle = '#000'
  ctx.fillRect(0, 0, canvas.width, canvas.height)

  ctx.font = font
  ctx.textAlign = 'center'
  ctx.textBaseline = 'middle'
  ctx.fillStyle = '#fff'

  var x = step[0] / 2
  var y = step[1] / 2
  for (var i = 0; i < chars.length; i++) {
    ctx.fillText(chars[i], x, y)
    if ((x += step[0]) > shape[0] - step[0]/2) (x = step[0]/2), (y += step[1])
  }

  return canvas
}
