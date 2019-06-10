'use strict'

module.exports = measure

measure.canvas = document.createElement('canvas')
measure.cache = {}

function measure (font, o) {
	if (!o) o = {}

	if (typeof font === 'string' || Array.isArray(font)) {
		o.family = font
	}

	var family = Array.isArray(o.family) ? o.family.join(', ') : o.family
	if (!family) throw Error('`family` must be defined')

	var fs = o.size || o.fontSize || o.em || 48
	var weight = o.weight || o.fontWeight || ''
	var style = o.style || o.fontStyle || ''
	var font = [style, weight, fs].join(' ') + 'px ' + family
	var origin = o.origin || 'top'

	if (measure.cache[family]) {
		// return more precise values if cache has them
		if (fs <= measure.cache[family].em) {
			return applyOrigin(measure.cache[family], origin)
		}
	}

	var canvas = o.canvas || measure.canvas
	var ctx = canvas.getContext('2d')
	var chars = {
		upper: o.upper !== undefined ? o.upper : 'H',
		lower: o.lower !== undefined ? o.lower : 'x',
		descent: o.descent !== undefined ? o.descent : 'p',
		ascent: o.ascent !== undefined ? o.ascent : 'h',
		tittle: o.tittle !== undefined ? o.tittle : 'i',
		overshoot: o.overshoot !== undefined ? o.overshoot : 'O'
	}
	var l = Math.ceil(fs * 1.5)
	canvas.height = l
	canvas.width = l * .5
	ctx.font = font

	var char = 'H'
	var result = {
		top: 0
	}

	// measure line-height
	ctx.clearRect(0, 0, l, l)
	ctx.textBaseline = 'top'
	ctx.fillStyle = 'black'
	ctx.fillText(char, 0, 0)
	var topPx = firstTop(ctx.getImageData(0, 0, l, l))
	ctx.clearRect(0, 0, l, l)
	ctx.textBaseline = 'bottom'
	ctx.fillText(char, 0, l)
	var bottomPx = firstTop(ctx.getImageData(0, 0, l, l))
	result.lineHeight =
	result.bottom = l - bottomPx + topPx

	// measure baseline
	ctx.clearRect(0, 0, l, l)
	ctx.textBaseline = 'alphabetic'
	ctx.fillText(char, 0, l)
	var baselinePx = firstTop(ctx.getImageData(0, 0, l, l))
	var baseline = l - baselinePx - 1 + topPx
	result.baseline =
	result.alphabetic = baseline

	// measure median
	ctx.clearRect(0, 0, l, l)
	ctx.textBaseline = 'middle'
	ctx.fillText(char, 0, l * .5)
	var medianPx = firstTop(ctx.getImageData(0, 0, l, l))
	result.median =
	result.middle = l - medianPx - 1 + topPx - l * .5

	// measure hanging
	ctx.clearRect(0, 0, l, l)
	ctx.textBaseline = 'hanging'
	ctx.fillText(char, 0, l * .5)
	var hangingPx = firstTop(ctx.getImageData(0, 0, l, l))
	result.hanging = l - hangingPx - 1 + topPx - l * .5

	// measure ideographic
	ctx.clearRect(0, 0, l, l)
	ctx.textBaseline = 'ideographic'
	ctx.fillText(char, 0, l)
	var ideographicPx = firstTop(ctx.getImageData(0, 0, l, l))
	result.ideographic = l - ideographicPx - 1 + topPx

	// measure cap
	if (chars.upper) {
		ctx.clearRect(0, 0, l, l)
		ctx.textBaseline = 'top'
		ctx.fillText(chars.upper, 0, 0)
		result.upper = firstTop(ctx.getImageData(0, 0, l, l))
		result.capHeight = (result.baseline - result.upper)
	}

	// measure x
	if (chars.lower) {
		ctx.clearRect(0, 0, l, l)
		ctx.textBaseline = 'top'
		ctx.fillText(chars.lower, 0, 0)
		result.lower = firstTop(ctx.getImageData(0, 0, l, l))
		result.xHeight = (result.baseline - result.lower)
	}

	// measure tittle
	if (chars.tittle) {
		ctx.clearRect(0, 0, l, l)
		ctx.textBaseline = 'top'
		ctx.fillText(chars.tittle, 0, 0)
		result.tittle = firstTop(ctx.getImageData(0, 0, l, l))
	}

	// measure ascent
	if (chars.ascent) {
		ctx.clearRect(0, 0, l, l)
		ctx.textBaseline = 'top'
		ctx.fillText(chars.ascent, 0, 0)
		result.ascent = firstTop(ctx.getImageData(0, 0, l, l))
	}

	// measure descent
	if (chars.descent) {
		ctx.clearRect(0, 0, l, l)
		ctx.textBaseline = 'top'
		ctx.fillText(chars.descent, 0, 0)
		result.descent = firstBottom(ctx.getImageData(0, 0, l, l))
	}

	// measure overshoot
	if (chars.overshoot) {
		ctx.clearRect(0, 0, l, l)
		ctx.textBaseline = 'top'
		ctx.fillText(chars.overshoot, 0, 0)
		var overshootPx = firstBottom(ctx.getImageData(0, 0, l, l))
		result.overshoot = overshootPx - baseline
	}

	// normalize result
	for (var name in result) {
		result[name] /= fs
	}

	result.em = fs
	measure.cache[family] = result

	return applyOrigin(result, origin)
}

function applyOrigin(obj, origin) {
	var res = {}
	if (typeof origin === 'string') origin = obj[origin]
	for (var name in obj) {
		if (name === 'em') continue
		res[name] = obj[name] - origin
	}
	return res
}

function firstTop(iData) {
	var l = iData.height
	var data = iData.data
	for (var i = 3; i < data.length; i+=4) {
		if (data[i] !== 0) {
			return Math.floor((i - 3) *.25 / l)
		}
	}
}

function firstBottom(iData) {
	var l = iData.height
	var data = iData.data
	for (var i = data.length - 1; i > 0; i -= 4) {
		if (data[i] !== 0) {
			return Math.floor((i - 3) *.25 / l)
		}
	}
}
