'use strict'


const createScatter = require('regl-scatter2d')
const pick = require('pick-by-alias')
const getBounds = require('array-bounds')
const raf = require('raf')
const arrRange = require('array-range')
const rect = require('parse-rect')
const flatten = require('flatten-vertex-data')


module.exports = SPLOM


// @constructor
function SPLOM (regl, options) {
	if (!(this instanceof SPLOM)) return new SPLOM(regl, options)

	// render passes
	this.traces = []

	// passes for scatter, combined across traces
	this.passes = {}

	this.regl = regl

	// main scatter drawing instance
	this.scatter = createScatter(regl)

	this.canvas = this.scatter.canvas
}


// update & draw passes once per frame
SPLOM.prototype.render = function (...args) {
	if (args.length) {
		this.update(...args)
	}

	if (this.regl.attributes.preserveDrawingBuffer) return this.draw()

	// make sure draw is not called more often than once a frame
	if (this.dirty) {
		if (this.planned == null) {
			this.planned = raf(() => {
				this.draw()
				this.dirty = true
				this.planned = null
			})
		}
	}
	else {
		this.draw()
		this.dirty = true
		raf(() => {
			this.dirty = false
		})
	}

	return this
}


// update passes
SPLOM.prototype.update = function (...args) {
	if (!args.length) return

	for (let i = 0; i < args.length; i++) {
		this.updateItem(i, args[i])
	}

	// remove nulled passes
	this.traces = this.traces.filter(Boolean)

	// FIXME: update passes independently
	let passes = []
	let offset = 0
	for (let i = 0; i < this.traces.length; i++) {
		let trace = this.traces[i]
		let tracePasses = this.traces[i].passes
		for (let j = 0; j < tracePasses.length; j++) {
			passes.push(this.passes[tracePasses[j]])
		}
		// save offset of passes
		trace.passOffset = offset
		offset += trace.passes.length
	}

	this.scatter.update(...passes)

	return this
}


// update trace by index, not supposed to be called directly
SPLOM.prototype.updateItem = function (i, options) {
	let { regl } = this

	// remove pass if null
	if (options === null) {
		this.traces[i] = null
		return this
	}

	if (!options) return this

	let o = pick(options, {
		data: 'data items columns rows values dimensions samples x',
		snap: 'snap cluster',
		size: 'sizes size radius',
		color: 'colors color fill fill-color fillColor',
		opacity: 'opacity alpha transparency opaque',
		borderSize: 'borderSizes borderSize border-size bordersize borderWidth borderWidths border-width borderwidth stroke-width strokeWidth strokewidth outline',
		borderColor: 'borderColors borderColor bordercolor stroke stroke-color strokeColor',
		marker: 'markers marker shape',
		range: 'range ranges databox dataBox',
		viewport: 'viewport viewBox viewbox',
		domain: 'domain domains area areas',
		padding: 'pad padding paddings pads margin margins',
		transpose: 'transpose transposed',
		diagonal: 'diagonal diag showDiagonal',
		upper: 'upper up top upperhalf upperHalf showupperhalf showUpper showUpperHalf',
		lower: 'lower low bottom lowerhalf lowerHalf showlowerhalf showLowerHalf showLower'
	})

	// we provide regl buffer per-trace, since trace data can be changed
	let trace = (this.traces[i] || (this.traces[i] = {
		id: i,
		buffer: regl.buffer({
			usage: 'dynamic',
			type: 'float',
			data: new Uint8Array()
		}),
		color: 'black',
		marker: null,
		size: 12,
		borderColor: 'transparent',
		borderSize: 1,
		viewport:  rect([regl._gl.drawingBufferWidth, regl._gl.drawingBufferHeight]),
		padding: [0, 0, 0, 0],
		opacity: 1,
		diagonal: true,
		upper: true,
		lower: true
	}))


	// save styles
	if (o.color != null) {
		trace.color = o.color
	}
	if (o.size != null) {
		trace.size = o.size
	}
	if (o.marker != null) {
		trace.marker = o.marker
	}
	if (o.borderColor != null) {
		trace.borderColor = o.borderColor
	}
	if (o.borderSize != null) {
		trace.borderSize = o.borderSize
	}
	if (o.opacity != null) {
		trace.opacity = o.opacity
	}
	if (o.viewport) {
		trace.viewport = rect(o.viewport)
	}
	if (o.diagonal != null) trace.diagonal = o.diagonal
	if (o.upper != null) trace.upper = o.upper
	if (o.lower != null) trace.lower = o.lower

	// put flattened data into buffer
	if (o.data) {
		trace.buffer(flatten(o.data))
		trace.columns = o.data.length
		trace.count = o.data[0].length

		// detect bounds per-column
		trace.bounds = []

		for (let i = 0; i < trace.columns; i++) {
			trace.bounds[i] = getBounds(o.data[i], 1)
		}
	}

	// add proper range updating markers
	let multirange
	if (o.range) {
		trace.range = o.range
		multirange = trace.range && typeof trace.range[0] !== 'number'
	}

	if (o.domain) {
		trace.domain = o.domain
	}
	let multipadding = false
	if (o.padding != null) {
		// multiple paddings
		if (Array.isArray(o.padding) && o.padding.length === trace.columns && typeof o.padding[o.padding.length - 1] === 'number') {
			trace.padding = o.padding.map(getPad)
			multipadding = true
		}
		// single padding
		else {
			trace.padding = getPad(o.padding)
		}
	}

	// create passes
	let m = trace.columns
	let n = trace.count

	let w = trace.viewport.width
	let h = trace.viewport.height
	let left = trace.viewport.x
	let top = trace.viewport.y
	let iw = w / m
	let ih = h / m

	trace.passes = []

	for (let i = 0; i < m; i++) {
		for (let j = 0; j < m; j++) {
			if (!trace.diagonal && j === i) continue
			if (!trace.upper && i > j) continue
			if (!trace.lower && i < j) continue

			let key = passId(trace.id, i, j)

			let pass = this.passes[key] || (this.passes[key] = {})

			if (o.data) {
				if (o.transpose) {
					pass.positions = {
						x: {buffer: trace.buffer, offset: j, count: n, stride: m},
						y: {buffer: trace.buffer, offset: i, count: n, stride: m}
					}
				}
				else {
					pass.positions = {
						x: {buffer: trace.buffer, offset: j * n, count: n},
						y: {buffer: trace.buffer, offset: i * n, count: n}
					}
				}

				pass.bounds = getBox(trace.bounds, i, j)
			}

			if (o.domain || o.viewport || o.data) {
				let pad = multipadding ? getBox(trace.padding, i, j) : trace.padding
				if (trace.domain) {
					let [lox, loy, hix, hiy] = getBox(trace.domain, i, j)

					pass.viewport = [
						left + lox * w + pad[0],
						top + loy * h + pad[1],
						left + hix * w - pad[2],
						top + hiy * h - pad[3]
					]
				}
				// consider auto-domain equipartial
				else {
					pass.viewport = [
						left + j * iw + iw * pad[0],
						top + i * ih + ih * pad[1],
						left + (j + 1) * iw - iw * pad[2],
						top + (i + 1) * ih - ih * pad[3]
					]
				}
			}

			if (o.color) pass.color = trace.color
			if (o.size) pass.size = trace.size
			if (o.marker) pass.marker = trace.marker
			if (o.borderSize) pass.borderSize = trace.borderSize
			if (o.borderColor) pass.borderColor = trace.borderColor
			if (o.opacity) pass.opacity = trace.opacity

			if (o.range) {
				pass.range = multirange ? getBox(trace.range, i, j) : trace.range || pass.bounds
			}

			trace.passes.push(key)
		}
	}

	return this
}


// draw all or passed passes
SPLOM.prototype.draw = function (...args) {
	if (!args.length) {
		this.scatter.draw()
	}
	else {
		let idx = []
		for (let i = 0; i < args.length; i++) {
			// draw(0, 2, 5) - draw traces
			if (typeof args[i] === 'number' ) {
				let { passes, passOffset } = this.traces[args[i]]
				idx.push(...arrRange(passOffset, passOffset + passes.length))
			}
			// draw([0, 1, 2 ...], [3, 4, 5]) - draw points
			else if (args[i].length) {
				let els = args[i]
				let { passes, passOffset } = this.traces[i]
				passes = passes.map((passId, i) => {
					idx[passOffset + i] = els
				})
			}
		}
		this.scatter.draw(...idx)
	}

	return this
}


// dispose resources
SPLOM.prototype.destroy = function () {
	this.traces.forEach(trace => {
		if (trace.buffer && trace.buffer.destroy) trace.buffer.destroy()
	})
	this.traces = null
	this.passes = null

	this.scatter.destroy()

	return this
}


// return pass corresponding to trace i- j- square
function passId (trace, i, j) {
	let id = (trace.id != null ? trace.id : trace)
	let n = i
	let m = j
	let key = id << 16 | (n & 0xff) << 8 | m & 0xff

	return key
}


// return bounding box corresponding to a pass
function getBox (items, i, j) {
	let ilox, iloy, ihix, ihiy, jlox, jloy, jhix, jhiy
	let iitem = items[i], jitem = items[j]

	if (iitem.length > 2) {
		ilox = iitem[0]
		ihix = iitem[2]
		iloy = iitem[1]
		ihiy = iitem[3]
	}
	else if (iitem.length) {
		ilox = iloy = iitem[0]
		ihix = ihiy = iitem[1]
	}
	else {
		ilox = iitem.x
		iloy = iitem.y
		ihix = iitem.x + iitem.width
		ihiy = iitem.y + iitem.height
	}

	if (jitem.length > 2) {
		jlox = jitem[0]
		jhix = jitem[2]
		jloy = jitem[1]
		jhiy = jitem[3]
	}
	else if (jitem.length) {
		jlox = jloy = jitem[0]
		jhix = jhiy = jitem[1]
	}
	else {
		jlox = jitem.x
		jloy = jitem.y
		jhix = jitem.x + jitem.width
		jhiy = jitem.y + jitem.height
	}

	return [ jlox, iloy, jhix, ihiy ]
}


function getPad (arg) {
	if (typeof arg === 'number') return [arg, arg, arg, arg]
	else if (arg.length === 2) return [arg[0], arg[1], arg[0], arg[1]]
	else {
		let box = rect(arg)
		return [box.x, box.y, box.x + box.width, box.y + box.height]
	}
}
