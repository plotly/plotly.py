'use strict'


const rgba = require('color-normalize')
const getBounds = require('array-bounds')
const extend = require('object-assign')
const glslify = require('glslify')
const pick = require('pick-by-alias')
const flatten = require('flatten-vertex-data')
const triangulate = require('earcut')
const normalize = require('array-normalize')
const { float32, fract32 } = require('to-float32')
const WeakMap = require('es6-weak-map')
const parseRect = require('parse-rect')


module.exports = Line2D


/** @constructor */
function Line2D (regl, options) {
	if (!(this instanceof Line2D)) return new Line2D(regl, options)

	if (typeof regl === 'function') {
		if (!options) options = {}
		options.regl = regl
	}
	else {
		options = regl
	}
	if (options.length) options.positions = options
	regl = options.regl

	if (!regl.hasExtension('ANGLE_instanced_arrays')) {
		throw Error('regl-error2d: `ANGLE_instanced_arrays` extension should be enabled');
	}

	// persistent variables
	this.gl = regl._gl
	this.regl = regl

	// list of options for lines
	this.passes = []

	// cached shaders instance
	this.shaders = Line2D.shaders.has(regl) ? Line2D.shaders.get(regl) : Line2D.shaders.set(regl, Line2D.createShaders(regl)).get(regl)


	// init defaults
	this.update(options)
}


Line2D.dashMult = 2
Line2D.maxPatternLength = 256
Line2D.precisionThreshold = 3e6
Line2D.maxPoints = 1e4
Line2D.maxLines = 2048


// cache of created draw calls per-regl instance
Line2D.shaders = new WeakMap()


// create static shaders once
Line2D.createShaders = function (regl) {
	let offsetBuffer = regl.buffer({
		usage: 'static',
		type: 'float',
		data: [0,1, 0,0, 1,1, 1,0]
	})

	let shaderOptions = {
		primitive: 'triangle strip',
		instances: regl.prop('count'),
		count: 4,
		offset: 0,

		uniforms: {
			miterMode: (ctx, prop) => prop.join === 'round' ? 2 : 1,
			miterLimit: regl.prop('miterLimit'),
			scale: regl.prop('scale'),
			scaleFract: regl.prop('scaleFract'),
			translateFract: regl.prop('translateFract'),
			translate: regl.prop('translate'),
			thickness: regl.prop('thickness'),
			dashPattern: regl.prop('dashTexture'),
			opacity: regl.prop('opacity'),
			pixelRatio: regl.context('pixelRatio'),
			id: regl.prop('id'),
			dashSize: regl.prop('dashLength'),
			viewport: (c, p) => [p.viewport.x, p.viewport.y, c.viewportWidth, c.viewportHeight],
			depth: regl.prop('depth')
		},

		blend: {
			enable: true,
			color: [0,0,0,0],
			equation: {
				rgb: 'add',
				alpha: 'add'
			},
			func: {
				srcRGB: 'src alpha',
				dstRGB: 'one minus src alpha',
				srcAlpha: 'one minus dst alpha',
				dstAlpha: 'one'
			}
		},
		depth: {
			enable: (c, p) => {
				return !p.overlay
			}
		},
		stencil: {enable: false},
		scissor: {
			enable: true,
			box: regl.prop('viewport')
		},
		viewport: regl.prop('viewport')
	}


	// simplified rectangular line shader
	let drawRectLine = regl(extend({
		vert: glslify('./rect-vert.glsl'),
		frag: glslify('./rect-frag.glsl'),

		attributes: {
			// if point is at the end of segment
			lineEnd: {
				buffer: offsetBuffer,
				divisor: 0,
				stride: 8,
				offset: 0
			},
			// if point is at the top of segment
			lineTop: {
				buffer: offsetBuffer,
				divisor: 0,
				stride: 8,
				offset: 4
			},
			// beginning of line coordinate
			aCoord: {
				buffer: regl.prop('positionBuffer'),
				stride: 8,
				offset: 8,
				divisor: 1
			},
			// end of line coordinate
			bCoord: {
				buffer: regl.prop('positionBuffer'),
				stride: 8,
				offset: 16,
				divisor: 1
			},
			aCoordFract: {
				buffer: regl.prop('positionFractBuffer'),
				stride: 8,
				offset: 8,
				divisor: 1
			},
			bCoordFract: {
				buffer: regl.prop('positionFractBuffer'),
				stride: 8,
				offset: 16,
				divisor: 1
			},
			color: {
				buffer: regl.prop('colorBuffer'),
				stride: 4,
				offset: 0,
				divisor: 1
			}
		}
	}, shaderOptions))

	// create regl draw
	let drawMiterLine

	try {
		drawMiterLine = regl(extend({
			// culling removes polygon creasing
			cull: {
				enable: true,
				face: 'back'
			},

			vert: glslify('./miter-vert.glsl'),
			frag: glslify('./miter-frag.glsl'),

			attributes: {
				// is line end
				lineEnd: {
					buffer: offsetBuffer,
					divisor: 0,
					stride: 8,
					offset: 0
				},
				// is line top
				lineTop: {
					buffer: offsetBuffer,
					divisor: 0,
					stride: 8,
					offset: 4
				},
				// left color
				aColor: {
					buffer: regl.prop('colorBuffer'),
					stride: 4,
					offset: 0,
					divisor: 1
				},
				// right color
				bColor: {
					buffer: regl.prop('colorBuffer'),
					stride: 4,
					offset: 4,
					divisor: 1
				},
				prevCoord: {
					buffer: regl.prop('positionBuffer'),
					stride: 8,
					offset: 0,
					divisor: 1
				},
				aCoord: {
					buffer: regl.prop('positionBuffer'),
					stride: 8,
					offset: 8,
					divisor: 1
				},
				bCoord: {
					buffer: regl.prop('positionBuffer'),
					stride: 8,
					offset: 16,
					divisor: 1
				},
				nextCoord: {
					buffer: regl.prop('positionBuffer'),
					stride: 8,
					offset: 24,
					divisor: 1
				}
			}
		}, shaderOptions))
	} catch (e) {
		// IE/bad Webkit fallback
		drawMiterLine = drawRectLine
	}

	// fill shader
	let drawFill = regl({
		primitive: 'triangle',
		elements: (ctx, prop) => prop.triangles,
		offset: 0,

		vert: glslify('./fill-vert.glsl'),
		frag: glslify('./fill-frag.glsl'),

		uniforms: {
			scale: regl.prop('scale'),
			color: regl.prop('fill'),
			scaleFract: regl.prop('scaleFract'),
			translateFract: regl.prop('translateFract'),
			translate: regl.prop('translate'),
			opacity: regl.prop('opacity'),
			pixelRatio: regl.context('pixelRatio'),
			id: regl.prop('id'),
			viewport: (ctx, prop) => [prop.viewport.x, prop.viewport.y, ctx.viewportWidth, ctx.viewportHeight]
		},

		attributes: {
			position: {
				buffer: regl.prop('positionBuffer'),
				stride: 8,
				offset: 8
			},
			positionFract: {
				buffer: regl.prop('positionFractBuffer'),
				stride: 8,
				offset: 8
			}
		},

		blend: shaderOptions.blend,

		depth: { enable: false },
		scissor: shaderOptions.scissor,
		stencil: shaderOptions.stencil,
		viewport: shaderOptions.viewport
	})

	return {
		fill: drawFill, rect: drawRectLine, miter: drawMiterLine
	}
}


// used to for new lines instances
Line2D.defaults = {
	dashes: null,
	join: 'miter',
	miterLimit: 1,
	thickness: 10,
	cap: 'square',
	color: 'black',
	opacity: 1,
	overlay: false,
	viewport: null,
	range: null,
	close: false,
	fill: null
}


Line2D.prototype.render = function (...args) {
	if (args.length) {
		this.update(...args)
	}

	this.draw()
}


Line2D.prototype.draw = function (...args) {
	// render multiple polylines via regl batch
	(args.length ? args : this.passes).forEach((s, i) => {
		// render array pass as a list of passes
		if (s && Array.isArray(s)) return this.draw(...s)

		if (typeof s === 'number') s = this.passes[s]

		if (!(s && s.count > 1 && s.opacity)) return

		this.regl._refresh()

		if (s.fill && s.triangles && s.triangles.length > 2) {
			this.shaders.fill(s)
		}

		if (!s.thickness) return

		// high scale is only available for rect mode with precision
		if (s.scale[0] * s.viewport.width > Line2D.precisionThreshold || s.scale[1] * s.viewport.height > Line2D.precisionThreshold) {
			this.shaders.rect(s)
		}

		// thin this.passes or too many points are rendered as simplified rect shader
		else if (s.join === 'rect' || (!s.join && (s.thickness <= 2 || s.count >= Line2D.maxPoints))) {
			this.shaders.rect(s)
		}
		else {
			this.shaders.miter(s)
		}
	})

	return this
}

Line2D.prototype.update = function (options) {
	if (!options) return

	if (options.length != null) {
		if (typeof options[0] === 'number') options = [{positions: options}]
	}

	// make options a batch
	else if (!Array.isArray(options)) options = [options]

	let { regl, gl } = this

	// process per-line settings
	options.forEach((o, i) => {
		let state = this.passes[i]

		if (o === undefined) return

		// null-argument removes pass
		if (o === null) {
			this.passes[i] = null
			return
		}

		if (typeof o[0] === 'number') o = {positions: o}

		// handle aliases
		o = pick(o, {
			positions: 'positions points data coords',
			thickness: 'thickness lineWidth lineWidths line-width linewidth width stroke-width strokewidth strokeWidth',
			join: 'lineJoin linejoin join type mode',
			miterLimit: 'miterlimit miterLimit',
			dashes: 'dash dashes dasharray dash-array dashArray',
			color: 'color colour stroke colors colours stroke-color strokeColor',
			fill: 'fill fill-color fillColor',
			opacity: 'alpha opacity',
			overlay: 'overlay crease overlap intersect',
			close: 'closed close closed-path closePath',
			range: 'range dataBox',
			viewport: 'viewport viewBox',
			hole: 'holes hole hollow'
		})

		// init state
		if (!state) {
			this.passes[i] = state = {
				id: i,
				scale: null,
				scaleFract: null,
				translate: null,
				translateFract: null,
				count: 0,
				hole: [],
				depth: 0,

				dashLength: 1,
				dashTexture: regl.texture({
					channels: 1,
					data: new Uint8Array([255]),
					width: 1,
					height: 1,
					mag: 'linear',
					min: 'linear'
				}),

				colorBuffer: regl.buffer({
					usage: 'dynamic',
					type: 'uint8',
					data: new Uint8Array()
				}),
				positionBuffer: regl.buffer({
					usage: 'dynamic',
					type: 'float',
					data: new Uint8Array()
				}),
				positionFractBuffer: regl.buffer({
					usage: 'dynamic',
					type: 'float',
					data: new Uint8Array()
				})
			}

			o = extend({}, Line2D.defaults, o)
		}
		if (o.thickness != null) state.thickness = parseFloat(o.thickness)
		if (o.opacity != null) state.opacity = parseFloat(o.opacity)
		if (o.miterLimit != null) state.miterLimit = parseFloat(o.miterLimit)
		if (o.overlay != null) {
			state.overlay = !!o.overlay
			if (i < Line2D.maxLines) {
				state.depth = 2 * (Line2D.maxLines - 1 - i % Line2D.maxLines) / Line2D.maxLines - 1.;
			}
		}
		if (o.join != null) state.join = o.join
		if (o.hole != null) state.hole = o.hole
		if (o.fill != null) state.fill = !o.fill ? null : rgba(o.fill, 'uint8')
		if (o.viewport != null) state.viewport = parseRect(o.viewport)

		if (!state.viewport) {
			state.viewport = parseRect([
				gl.drawingBufferWidth,
				gl.drawingBufferHeight
			])
		}

		if (o.close != null) state.close = o.close

		// reset positions
		if (o.positions === null) o.positions = []
		if (o.positions) {
			let positions, count

			// if positions are an object with x/y
			if (o.positions.x && o.positions.y) {
				let xPos = o.positions.x
				let yPos = o.positions.y
				count = state.count = Math.max(
					xPos.length,
					yPos.length
				)
				positions = new Float64Array(count * 2)
				for (let i = 0; i < count; i++) {
					positions[i * 2] = xPos[i]
					positions[i * 2 + 1] = yPos[i]
				}
			}
			else {
				positions = flatten(o.positions, 'float64')
				count = state.count = Math.floor(positions.length / 2)
			}

			let bounds = state.bounds = getBounds(positions, 2)

			// create fill positions
			// FIXME: fill positions can be set only along with positions
			if (state.fill) {
				let pos = []

				// filter bad vertices and remap triangles to ensure shape
				let ids = {}
				let lastId = 0

				for (let i = 0, ptr = 0, l = state.count; i < l; i++) {
					let x = positions[i*2]
					let y = positions[i*2 + 1]
					if (isNaN(x) || isNaN(y) || x == null || y == null) {
						x = positions[lastId*2]
						y = positions[lastId*2 + 1]
						ids[i] = lastId
					}
					else {
						lastId = i
					}
					pos[ptr++] = x
					pos[ptr++] = y
				}

				let triangles = triangulate(pos, state.hole || [])

				for (let i = 0, l = triangles.length; i < l; i++) {
					if (ids[triangles[i]] != null) triangles[i] = ids[triangles[i]]
				}

				state.triangles = triangles
			}

			// update position buffers
			let npos = new Float64Array(positions)
			normalize(npos, 2, bounds)

			let positionData = new Float64Array(count * 2 + 6)

			// rotate first segment join
			if (state.close) {
				if (positions[0] === positions[count*2 - 2] &&
					positions[1] === positions[count*2 - 1]) {
					positionData[0] = npos[count*2 - 4]
					positionData[1] = npos[count*2 - 3]
				}
				else {
					positionData[0] = npos[count*2 - 2]
					positionData[1] = npos[count*2 - 1]
				}
			}
			else {
				positionData[0] = npos[0]
				positionData[1] = npos[1]
			}

			positionData.set(npos, 2)

			// add last segment
			if (state.close) {
				// ignore coinciding start/end
				if (positions[0] === positions[count*2 - 2] &&
					positions[1] === positions[count*2 - 1]) {
					positionData[count*2 + 2] = npos[2]
					positionData[count*2 + 3] = npos[3]
					state.count -= 1
				}
				else {
					positionData[count*2 + 2] = npos[0]
					positionData[count*2 + 3] = npos[1]
					positionData[count*2 + 4] = npos[2]
					positionData[count*2 + 5] = npos[3]
				}
			}
			// add stub
			else {
				positionData[count*2 + 2] = npos[count*2 - 2]
				positionData[count*2 + 3] = npos[count*2 - 1]
				positionData[count*2 + 4] = npos[count*2 - 2]
				positionData[count*2 + 5] = npos[count*2 - 1]
			}

			state.positionBuffer(float32(positionData))
			state.positionFractBuffer(fract32(positionData))
		}

		if (o.range) {
			state.range = o.range
		} else if (!state.range) {
			state.range = state.bounds
		}

		if ((o.range || o.positions) && state.count) {
			let bounds = state.bounds

			let boundsW = bounds[2] - bounds[0],
				boundsH = bounds[3] - bounds[1]

			let rangeW = state.range[2] - state.range[0],
				rangeH = state.range[3] - state.range[1]

			state.scale = [
				boundsW / rangeW,
				boundsH / rangeH
			]
			state.translate = [
				-state.range[0] / rangeW + bounds[0] / rangeW || 0,
				-state.range[1] / rangeH + bounds[1] / rangeH || 0
			]

			state.scaleFract = fract32(state.scale)
			state.translateFract = fract32(state.translate)
		}

		if (o.dashes) {
			let dashLength = 0., dashData

			if (!o.dashes || o.dashes.length < 2) {
				dashLength = 1.
				dashData = new Uint8Array([255, 255, 255, 255, 255, 255, 255, 255])
			}

			else {
				dashLength = 0.;
				for(let i = 0; i < o.dashes.length; ++i) {
					dashLength += o.dashes[i]
				}
				dashData = new Uint8Array(dashLength * Line2D.dashMult)
				let ptr = 0
				let fillColor = 255

				// repeat texture two times to provide smooth 0-step
				for (let k = 0; k < 2; k++) {
					for(let i = 0; i < o.dashes.length; ++i) {
						for(let j = 0, l = o.dashes[i] * Line2D.dashMult * .5; j < l; ++j) {
							dashData[ptr++] = fillColor
						}
						fillColor ^= 255
					}
				}
			}

			state.dashLength = dashLength
			state.dashTexture({
				channels: 1,
				data: dashData,
				width: dashData.length,
				height: 1,
				mag: 'linear',
				min: 'linear'
			}, 0, 0)
		}

		if (o.color) {
			let count = state.count
			let colors = o.color

			if (!colors) colors = 'transparent'

			let colorData = new Uint8Array(count * 4 + 4)

			// convert colors to typed arrays
			if (!Array.isArray(colors) || typeof colors[0] === 'number') {
				let c = rgba(colors, 'uint8')

				for (let i = 0; i < count + 1; i++) {
					colorData.set(c, i * 4)
				}
			} else {
				for (let i = 0; i < count; i++) {
					let c = rgba(colors[i], 'uint8')
					colorData.set(c, i * 4)
				}
				colorData.set(rgba(colors[0], 'uint8'), count * 4)
			}

			state.colorBuffer({
				usage: 'dynamic',
				type: 'uint8',
				data: colorData
			})
		}
	})

	// remove unmentioned passes
	if (options.length < this.passes.length) {
		for (let i = options.length; i < this.passes.length; i++) {
			let pass = this.passes[i]
			if (!pass) continue
			pass.colorBuffer.destroy()
			pass.positionBuffer.destroy()
			pass.dashTexture.destroy()
		}
		this.passes.length = options.length
	}

	// remove null items
	let passes = []
	for (let i = 0; i < this.passes.length; i++) {
		if (this.passes[i] !== null) passes.push(this.passes[i])
	}
	this.passes = passes

	return this
}

Line2D.prototype.destroy = function () {
	this.passes.forEach(pass => {
		pass.colorBuffer.destroy()
		pass.positionBuffer.destroy()
		pass.dashTexture.destroy()
	})

	this.passes.length = 0

	return this
}

