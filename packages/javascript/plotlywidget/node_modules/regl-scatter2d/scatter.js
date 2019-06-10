'use strict'

const rgba = require('color-normalize')
const getBounds = require('array-bounds')
const colorId = require('color-id')
const cluster = require('point-cluster')
const extend = require('object-assign')
const glslify = require('glslify')
const pick = require('pick-by-alias')
const updateDiff = require('update-diff')
const flatten = require('flatten-vertex-data')
const ie = require('is-iexplorer')
const f32 = require('to-float32')
const parseRect = require('parse-rect')


module.exports = Scatter


function Scatter (regl, options) {
	if (!(this instanceof Scatter)) return new Scatter(regl, options)

	if (typeof regl === 'function') {
		if (!options) options = {}
		options.regl = regl
	}
	else {
		options = regl
		regl = null
	}

	if (options && options.length) options.positions = options

	regl = options.regl

	// persistent variables
	let gl = regl._gl, paletteTexture, palette = [], paletteIds = {},

		// state
		groups = [],

		// textures for marker keys
		markerTextures = [null],
		markerCache = [null]

	const maxColors = 255, maxSize = 100

	// direct color buffer mode
	// IE does not support palette anyways
	this.tooManyColors = ie

	// texture with color palette
	paletteTexture = regl.texture({
		data: new Uint8Array(maxColors * 4),
		width: maxColors,
		height: 1,
		type: 'uint8',
		format: 'rgba',
		wrapS: 'clamp',
		wrapT: 'clamp',
		mag: 'nearest',
		min: 'nearest'
	})

	extend(this, {
		regl,
		gl,
		groups,
		markerCache,
		markerTextures,
		palette,
		paletteIds,
		paletteTexture,
		maxColors,
		maxSize,
		canvas: gl.canvas
	})

	this.update(options)

	// common shader options
	let shaderOptions = {
		uniforms: {
			pixelRatio: regl.context('pixelRatio'),
			palette: paletteTexture,
			paletteSize: (ctx, prop) => [this.tooManyColors ? 0 : maxColors, paletteTexture.height],
			scale: regl.prop('scale'),
			scaleFract: regl.prop('scaleFract'),
			translate: regl.prop('translate'),
			translateFract: regl.prop('translateFract'),
			opacity: regl.prop('opacity'),
			marker: regl.prop('markerTexture'),
		},

		attributes: {
			// FIXME: optimize these parts
			x: (ctx, prop) => prop.xAttr || {
				buffer: prop.positionBuffer,
				stride: 8,
				offset: 0
			},
			y: (ctx, prop) => prop.yAttr || {
				buffer: prop.positionBuffer,
				stride: 8,
				offset: 4
			},
			xFract: (ctx, prop) => prop.xAttr ? { constant: [0, 0] } : {
				buffer: prop.positionFractBuffer,
				stride: 8,
				offset: 0
			},
			yFract: (ctx, prop) => prop.yAttr ? { constant: [0, 0] } : {
				buffer: prop.positionFractBuffer,
				stride: 8,
				offset: 4
			},
			size: (ctx, prop) => prop.size.length ? {
				buffer: prop.sizeBuffer,
				stride: 2,
				offset: 0
			} : {
				constant: [ Math.round(prop.size * 255 / this.maxSize) ]
			},
			borderSize: (ctx, prop) => prop.borderSize.length ? {
				buffer: prop.sizeBuffer,
				stride: 2,
				offset: 1
			} : {
				constant: [ Math.round(prop.borderSize * 255 / this.maxSize) ]
			},
			colorId: (ctx, prop) => prop.color.length ? {
				buffer: prop.colorBuffer,
				stride: this.tooManyColors ? 8 : 4,
				offset: 0
			} : {
				constant: this.tooManyColors ? palette.slice(prop.color * 4, prop.color * 4 + 4) : [ prop.color ]
			},
			borderColorId: (ctx, prop) => prop.borderColor.length ? {
				buffer: prop.colorBuffer,
				stride: this.tooManyColors ? 8 : 4,
				offset: this.tooManyColors ? 4 : 2
			} : {
				constant: this.tooManyColors ? palette.slice(prop.borderColor * 4, prop.borderColor * 4 + 4) : [ prop.borderColor ]
			},
			isActive: (ctx, prop) => prop.activation === true ? { constant: [1] } : prop.activation ? prop.activation : { constant: [0] }
		},

		blend: {
			enable: true,
			color: [0,0,0,1],

			// photoshop blending
			func: {
				srcRGB: 'src alpha',
				dstRGB: 'one minus src alpha',
				srcAlpha: 'one minus dst alpha',
				dstAlpha: 'one'
			}
		},

		scissor: {
			enable: true,
			box: regl.prop('viewport')
		},
		viewport: regl.prop('viewport'),

		stencil: {enable: false},
		depth: {enable: false},

		elements: regl.prop('elements'),
		count: regl.prop('count'),
		offset: regl.prop('offset'),

		primitive: 'points'
	}

	// draw sdf-marker
	let markerOptions = extend({}, shaderOptions)
	markerOptions.frag = glslify('./marker-frag.glsl')
	markerOptions.vert = glslify('./marker-vert.glsl')

	this.drawMarker = regl(markerOptions)

	// draw circle
	let circleOptions = extend({}, shaderOptions)
	circleOptions.frag = glslify('./circle-frag.glsl')
	circleOptions.vert = glslify('./circle-vert.glsl')

	// polyfill IE
	if (ie) {
		circleOptions.frag = circleOptions.frag.replace('smoothstep', 'smoothStep')
		markerOptions.frag = markerOptions.frag.replace('smoothstep', 'smoothStep')
	}

	this.drawCircle = regl(circleOptions)
}

// single pass defaults
Scatter.defaults = {
	color: 'black',
	borderColor: 'transparent',
	borderSize: 0,
	size: 12,
	opacity: 1,
	marker: undefined,
	viewport: null,
	range: null,
	pixelSize: null,
	count: 0,
	offset: 0,
	bounds: null,
	positions: [],
	snap: 1e4
}


// update & redraw
Scatter.prototype.render = function (...args) {
	if (args.length) {
		this.update(...args)
	}

	this.draw()

	return this
}


// draw all groups or only indicated ones
Scatter.prototype.draw = function (...args) {
	let { groups } = this

	// if directly array passed - treat as passes
	if (args.length === 1 && Array.isArray(args[0])  && (args[0][0] === null || Array.isArray(args[0][0]))) {
		args = args[0]
	}

	// FIXME: remove once https://github.com/regl-project/regl/issues/474 resolved
	this.regl._refresh()

	if (args.length) {
		for (let i = 0; i < args.length; i++) {
			this.drawItem(i, args[i])
		}
	}
	// draw all passes
	else {
		groups.forEach((group, i) => {
			this.drawItem(i)
		})
	}

	return this
}

// draw specific scatter group
Scatter.prototype.drawItem = function (id, els) {
	let { groups } = this
	let group = groups[id]

	// debug viewport
	// let { viewport } = group
	// gl.enable(gl.SCISSOR_TEST);
	// gl.scissor(viewport.x, viewport.y, viewport.width, viewport.height);
	// gl.clearColor(0, 0, 0, .5);
	// gl.clear(gl.COLOR_BUFFER_BIT);

	if (typeof els === 'number') {
		id = els
		group = groups[els]
		els = null
	}

	if (!(group && group.count && group.opacity)) return

	// draw circles
	if (group.activation[0]) {
		// TODO: optimize this performance by making groups and regl.this props
		this.drawCircle(this.getMarkerDrawOptions(0, group, els))
	}

	// draw all other available markers
	let batch = []

	for (let i = 1; i < group.activation.length; i++) {
		if (!group.activation[i] || (group.activation[i] !== true && !group.activation[i].data.length)) continue

		batch.push(...this.getMarkerDrawOptions(i, group, els))
	}

	if (batch.length) {
		this.drawMarker(batch)
	}
}

// get options for the marker ids
Scatter.prototype.getMarkerDrawOptions = function(markerId, group, elements) {
	let { range, tree, viewport, activation, selectionBuffer, count } = group
	let { regl } = this

	// direct points
	if (!tree) {
		// if elements array - draw unclustered points
		if (elements) {
			return [extend({}, group, {
				markerTexture: this.markerTextures[markerId],
				activation: activation[markerId],
				count: elements.length,
				elements,
				offset: 0
			})]
		}

		return [ extend({}, group, {
			markerTexture: this.markerTextures[markerId],
			activation: activation[markerId],
			offset: 0
		}) ]
	}

	// clustered points
	let batch = []

	let lod = tree.range(range, { lod: true, px: [
		(range[2] - range[0]) / viewport.width,
		(range[3] - range[1]) / viewport.height
	]})

	// enable elements by using selection buffer
	if (elements) {
		let markerActivation = activation[markerId]
		let mask = markerActivation.data
		let data = new Uint8Array(count)
		for (let i = 0; i < elements.length; i++) {
			let id = elements[i]
			data[id] = mask ? mask[id] : 1
		}
		selectionBuffer.subdata(data)
	}

	for (let l = lod.length; l--;) {
		let [from, to] = lod[l]

		batch.push(extend({}, group, {
			markerTexture: this.markerTextures[markerId],
			activation: elements ? selectionBuffer : activation[markerId],
			offset: from,
			count: to - from
		}))
	}

	return batch
}

// update groups options
Scatter.prototype.update = function (...args) {
	if (!args.length) return

	// passes are as single array
	if (args.length === 1 && Array.isArray(args[0])) args = args[0]

	let { groups, gl, regl, maxSize, maxColors, palette } = this

	this.groups = groups = args.map((options, i) => {
		let group = groups[i]

		if (options === undefined) return group

		if (options === null) options = { positions: null }
		else if (typeof options === 'function') options = { ondraw: options }
		else if (typeof options[0] === 'number') options = { positions: options }

		// copy options to avoid mutation & handle aliases
		options = pick(options, {
			positions: 'positions data points',
			snap: 'snap cluster lod tree',
			size: 'sizes size radius',
			borderSize: 'borderSizes borderSize border-size bordersize borderWidth borderWidths border-width borderwidth stroke-width strokeWidth strokewidth outline',
			color: 'colors color fill fill-color fillColor',
			borderColor: 'borderColors borderColor stroke stroke-color strokeColor',
			marker: 'markers marker shape',
			range: 'range dataBox databox',
			viewport: 'viewport viewPort viewBox viewbox',
			opacity: 'opacity alpha transparency',
			bounds: 'bound bounds boundaries limits',
			tooManyColors: 'tooManyColors palette paletteMode optimizePalette enablePalette'
		})

		if (options.positions === null) options.positions = []

		if (options.tooManyColors != null) this.tooManyColors = options.tooManyColors

		if (!group) {
			groups[i] = group = {
				id: i,
				scale: null,
				translate: null,
				scaleFract: null,
				translateFract: null,

				// buffers for active markers
				activation: [],

				// buffer for filtered markers
				selectionBuffer: regl.buffer({
					data: new Uint8Array(0),
					usage: 'stream',
					type: 'uint8'
				}),

				// buffers with data: it is faster to switch them per-pass
				// than provide one congregate buffer
				sizeBuffer: regl.buffer({
					data: new Uint8Array(0),
					usage: 'dynamic',
					type: 'uint8'
				}),
				colorBuffer: regl.buffer({
					data: new Uint8Array(0),
					usage: 'dynamic',
					type: 'uint8'
				}),
				positionBuffer: regl.buffer({
					data: new Uint8Array(0),
					usage: 'dynamic',
					type: 'float'
				}),
				positionFractBuffer: regl.buffer({
					data: new Uint8Array(0),
					usage: 'dynamic',
					type: 'float'
				})
			}
			options = extend({}, Scatter.defaults, options)
		}

		// force update triggers
		if (options.positions && !('marker' in options)) {
			options.marker = group.marker
			delete group.marker
		}

		// updating markers cause recalculating snapping
		if (options.marker && !('positions' in options)) {
			options.positions = group.positions
			delete group.positions
		}

		// global count of points
		let hasSize = 0, hasColor = 0

		updateDiff(group, options, [{
			snap: true,
			size: (s, group) => {
				if (s == null) s = Scatter.defaults.size
				hasSize += s && s.length ? 1 : 0
				return s
			},
			borderSize: (s, group) => {
				if (s == null) s = Scatter.defaults.borderSize
				hasSize += s && s.length ? 1 : 0
				return s
			},
			opacity: parseFloat,

			// add colors to palette, save references
			color: (c, group) => {
				if (c == null) c = Scatter.defaults.color
				c = this.updateColor(c)
				hasColor++
				return c
			},

			borderColor: (c, group) => {
				if (c == null) c = Scatter.defaults.borderColor
				c = this.updateColor(c)
				hasColor++
				return c
			},

			bounds: (bounds, group, options) => {
				if (!('range' in options)) options.range = null
				return bounds
			},

			positions: (positions, group, options) => {
				let { snap } = group
				let { positionBuffer, positionFractBuffer, selectionBuffer } = group

				// separate buffers for x/y coordinates
				if (positions.x || positions.y) {
					if (positions.x.length) {
						group.xAttr = {
							buffer: regl.buffer(positions.x),
							offset: 0,
							stride: 4,
							count: positions.x.length
						}
					}
					else {
						group.xAttr = {
							buffer: positions.x.buffer,
							offset: positions.x.offset * 4 || 0,
							stride: (positions.x.stride || 1) * 4,
							count: positions.x.count
						}
					}
					if (positions.y.length) {
						group.yAttr = {
							buffer: regl.buffer(positions.y),
							offset: 0,
							stride: 4,
							count: positions.y.length
						}
					}
					else {
						group.yAttr = {
							buffer: positions.y.buffer,
							offset: positions.y.offset * 4 || 0,
							stride: (positions.y.stride || 1) * 4,
							count: positions.y.count
						}
					}
					group.count = Math.max(group.xAttr.count, group.yAttr.count)

					return positions
				}

				positions = flatten(positions, 'float64')

				let count = group.count = Math.floor(positions.length / 2)
				let bounds = group.bounds = count ? getBounds(positions, 2) : null

				// if range is not provided updated - recalc it
				if (!options.range && !group.range) {
					delete group.range
					options.range = bounds
				}

				// reset marker
				if (!options.marker && !group.marker) {
					delete group.marker;
					options.marker = null;
				}

				// build cluster tree if required
				if (snap && (snap === true || count > snap)) {
					group.tree = cluster(positions, { bounds })
				}
				// existing tree instance
				else if (snap && snap.length) {
					group.tree = snap
				}

				if (group.tree) {
					let opts = {
						primitive: 'points',
						usage: 'static',
						data: group.tree,
						type: 'uint32'
					}
					if (group.elements) group.elements(opts)
					else group.elements = regl.elements(opts)
				}

				// update position buffers
				positionBuffer({
					data: f32.float(positions),
					usage: 'dynamic'
				})
				positionFractBuffer({
					data: f32.fract(positions),
					usage: 'dynamic'
				})

				// expand selectionBuffer
				selectionBuffer({
					data: new Uint8Array(count),
					type: 'uint8',
					usage: 'stream'
				})

				return positions
			}
		}, {
			// create marker ids corresponding to known marker textures
			marker: (markers, group, options) => {
				let { activation } = group

				// reset marker elements
				activation.forEach(buffer => buffer && buffer.destroy && buffer.destroy())
				activation.length = 0

				// single sdf marker
				if (!markers || typeof markers[0] === 'number') {
					let id = this.addMarker(markers)
					activation[id] = true
				}

				// per-point markers use mask buffers to enable markers in vert shader
				else {
					let markerMasks = []

					for (let i = 0, l = Math.min(markers.length, group.count); i < l; i++) {
						let id = this.addMarker(markers[i])

						if (!markerMasks[id]) markerMasks[id] = new Uint8Array(group.count)

						// enable marker by default
						markerMasks[id][i] = 1
					}

					for (let id = 0; id < markerMasks.length; id++) {
						if (!markerMasks[id]) continue

						let opts = {
							data: markerMasks[id],
							type: 'uint8',
							usage: 'static'
						}
						if (!activation[id]) {
							activation[id] = regl.buffer(opts)
						}
						else {
							activation[id](opts)
						}

						activation[id].data = markerMasks[id]
					}
				}

				return markers
			},

			range: (range, group, options) => {
				let bounds = group.bounds

				// FIXME: why do we need this?
				if (!bounds) return
				if (!range) range = bounds

				group.scale = [1 / (range[2] - range[0]), 1 / (range[3] - range[1])]
				group.translate = [-range[0], -range[1]]

				group.scaleFract = f32.fract(group.scale)
				group.translateFract = f32.fract(group.translate)

				return range
			},

			viewport: vp => {
				let rect = parseRect(vp || [
					gl.drawingBufferWidth,
					gl.drawingBufferHeight
				])

				// normalize viewport to the canvas coordinates
				// rect.y = gl.drawingBufferHeight - rect.height - rect.y

				return rect
			}
		}])

		// update size buffer, if needed
		if (hasSize) {
			let { count, size, borderSize, sizeBuffer } = group

			let sizes = new Uint8Array(count*2)
			if (size.length || borderSize.length) {
				for (let i = 0; i < count; i++) {
					// we downscale size to allow for fractions
					sizes[i*2] = Math.round((size[i] == null ? size : size[i]) * 255 / maxSize)
					sizes[i*2 + 1] = Math.round((borderSize[i] == null ? borderSize : borderSize[i]) * 255 / maxSize)
				}
			}
			sizeBuffer({
				data: sizes,
				usage: 'dynamic'
			})
		}

		// update color buffer if needed
		if (hasColor) {
			let {count, color, borderColor, colorBuffer } = group
			let colors

			// if too many colors - put colors to buffer directly
			if (this.tooManyColors) {
				if (color.length || borderColor.length) {
					colors = new Uint8Array(count * 8)
					for (let i = 0; i < count; i++) {
						let colorId = color[i]
						colors[i*8] = palette[colorId*4]
						colors[i*8 + 1] = palette[colorId*4 + 1]
						colors[i*8 + 2] = palette[colorId*4 + 2]
						colors[i*8 + 3] = palette[colorId*4 + 3]

						let borderColorId = borderColor[i]
						colors[i*8 + 4] = palette[borderColorId*4]
						colors[i*8 + 5] = palette[borderColorId*4 + 1]
						colors[i*8 + 6] = palette[borderColorId*4 + 2]
						colors[i*8 + 7] = palette[borderColorId*4 + 3]
					}
				}
			}

			// if limited amount of colors - keep palette color picking
			// that saves significant memory
			else {
				if (color.length || borderColor.length) {
					// we need slight data increase by 2 due to vec4 borderId in shader
					colors = new Uint8Array(count * 4 + 2)
					for (let i = 0; i < count; i++) {
						// put color coords in palette texture
						if (color[i] != null) {
							colors[i*4] = color[i] % maxColors
							colors[i*4 + 1] = Math.floor(color[i] / maxColors)
						}
						if (borderColor[i] != null) {
							colors[i*4 + 2] = borderColor[i] % maxColors
							colors[i*4 + 3] = Math.floor(borderColor[i] / maxColors)
						}
					}
				}
			}

			colorBuffer({
				data: colors || new Uint8Array(0),
				type: 'uint8',
				usage: 'dynamic'
			})
		}

		return group
	})
}


// get (and create) marker texture id
Scatter.prototype.addMarker = function (sdf) {
	let { markerTextures, regl, markerCache } = this

	let pos = sdf == null ? 0 : markerCache.indexOf(sdf)

	if (pos >= 0) return pos

	// convert sdf to 0..255 range
	let distArr
	if (sdf instanceof Uint8Array || sdf instanceof Uint8ClampedArray) {
		distArr = sdf
	}
	else {
		distArr = new Uint8Array(sdf.length)
		for (let i = 0, l = sdf.length; i < l; i++) {
			distArr[i] = sdf[i] * 255
		}
	}

	let radius = Math.floor(Math.sqrt(distArr.length))

	pos = markerTextures.length

	markerCache.push(sdf)
	markerTextures.push(regl.texture({
		channels: 1,
		data: distArr,
		radius: radius,
		mag: 'linear',
		min: 'linear'
	}))

	return pos
}

// register color to palette, return it's index or list of indexes
Scatter.prototype.updateColor = function (colors) {
	let { paletteIds, palette, maxColors } = this

	if (!Array.isArray(colors)) {
		colors = [colors]
	}

	let idx = []

	// if color groups - flatten them
	if (typeof colors[0] === 'number') {
		let grouped = []

		if (Array.isArray(colors)) {
			for (let i = 0; i < colors.length; i+=4) {
				grouped.push(colors.slice(i, i+4))
			}
		}
		else {
			for (let i = 0; i < colors.length; i+=4) {
				grouped.push(colors.subarray(i, i+4))
			}
		}

		colors = grouped
	}

	for (let i = 0; i < colors.length; i++) {
		let color = colors[i]

		color = rgba(color, 'uint8')

		let id = colorId(color, false)

		// if new color - save it
		if (paletteIds[id] == null) {
			let pos = palette.length
			paletteIds[id] = Math.floor(pos / 4)
			palette[pos] = color[0]
			palette[pos+1] = color[1]
			palette[pos+2] = color[2]
			palette[pos+3] = color[3]
		}

		idx[i] = paletteIds[id]
	}

	// detect if too many colors in palette
	if (!this.tooManyColors && palette.length > maxColors * 4) this.tooManyColors = true

	// limit max color
	this.updatePalette(palette)

	// keep static index for single-color property
	return idx.length === 1 ? idx[0] : idx
}

Scatter.prototype.updatePalette = function (palette) {
	if (this.tooManyColors) return

	let { maxColors, paletteTexture } = this

	let requiredHeight = Math.ceil(palette.length * .25 / maxColors)

	// pad data
	if (requiredHeight > 1) {
		palette = palette.slice()
		for (let i = (palette.length * .25) % maxColors; i < requiredHeight * maxColors; i++) {
			palette.push(0, 0, 0, 0)
		}
	}

	// ensure height
	if (paletteTexture.height < requiredHeight) {
		paletteTexture.resize(maxColors, requiredHeight)
	}

	// update full data
	paletteTexture.subimage({
		width: Math.min(palette.length * .25, maxColors),
		height: requiredHeight,
		data: palette
	}, 0, 0)
}

// remove unused stuff
Scatter.prototype.destroy = function () {
	this.groups.forEach(group => {
		group.sizeBuffer.destroy()
		group.positionBuffer.destroy()
		group.positionFractBuffer.destroy()
		group.colorBuffer.destroy()
		group.activation.forEach(b => b && b.destroy && b.destroy())
		group.selectionBuffer.destroy()

		if (group.elements) group.elements.destroy()
	})
	this.groups.length = 0

	this.paletteTexture.destroy()

	this.markerTextures.forEach(txt => txt && txt.destroy && txt.destroy())

	return this
}
