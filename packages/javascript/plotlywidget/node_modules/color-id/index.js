/** @module  color-id */

'use strict'

var clamp = require('clamp')

module.exports = toNumber
module.exports.to = toNumber
module.exports.from = fromNumber

function toNumber (rgba, normalized) {
	if(normalized == null) normalized = true

	var r = rgba[0], g = rgba[1], b = rgba[2], a = rgba[3]

	if (a == null) a = normalized ? 1 : 255

	if (normalized) {
		r *= 255
		g *= 255
		b *= 255
		a *= 255
	}

	r = clamp(r, 0, 255) & 0xFF
	g = clamp(g, 0, 255) & 0xFF
	b = clamp(b, 0, 255) & 0xFF
	a = clamp(a, 0, 255) & 0xFF

	//hi-order shift converts to -1, so we can't use <<24
	var n = (r * 0x01000000) + (g << 16) + (b << 8) + (a)

	return n
}

function fromNumber (n, normalized) {
	n = +n

	var r = n >>> 24
	var g = (n & 0x00ff0000) >>> 16
	var b = (n & 0x0000ff00) >>> 8
	var a = n & 0x000000ff

	if (normalized === false) return [r, g, b, a]

	return [r/255, g/255, b/255, a/255]
}
