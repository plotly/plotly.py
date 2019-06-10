'use strict'

const isBrowser = require('is-browser')
const isPlainObject = require('is-plain-obj')
const getProgram = require('./program')
const WeakMap = require('weak-map')

let texturesCache = setTexture.cache = new WeakMap()
let texturesIdx = new WeakMap()


module.exports = setTexture


function setTexture (gl, name, options) {
	if (!gl) throw Error('WebGL context is not provided')

	let program
	if (gl instanceof WebGLProgram) {
		program = gl
		gl = program.gl
	}
	else {
		program = getProgram(gl)
	}

	if (!program) throw Error('Context has no active program')

	// object with textures passed
	if (name && typeof name != 'string') {
		let result = {}
		let textures = name

		for (let name in textures) {
			result[name] = setTexture(gl, name, textures[name], program)
		}

		return result
	}

	let textures = texturesCache.has(gl) ? texturesCache.get(gl) : texturesCache.set(gl, {}).get(gl)

	// return all textures if no name provided
	if (!name) return textures

	let texture = textures[name]

	// autoinit texture(s)
	if (!texture) {
		let count = gl.getProgramParameter(program, gl.ACTIVE_UNIFORMS)

		for (let i=0; i < count; ++i) {
			let info = gl.getActiveUniform(program, i)
			if (!info) continue
			if (info.type === gl.SAMPLER_2D || info.type === gl.SAMPLER_CUBE) {
				if (!textures[info.name]) {
					textures[info.name] = {name: info.name}
				}
			}
		}

		if (!textures[name]) textures[name] = {name: name, data: null}

		texture = textures[name]
	}

	// detect location
	if (texture.locations == null) {
		texture.locations = new WeakMap()
	}
	if (!texture.locations.has(program)) {
		texture.locations.set(program, gl.getUniformLocation(program, name))
	}

	// if no options passed - just return known texture info
	if (options == null) {
		return texture
	}

	if (!isPlainObject(options)) options = {data: options}


	if (texture.index == null || options.index != null) {
		let textureCount = texturesIdx.get(program) || 0
		texture.index = options.index != null ? options.index : textureCount++
		textureCount = Math.max(textureCount, texture.index)
		texturesIdx.set(program, textureCount)
		gl.uniform1i(texture.locations.get(program), texture.index)
	}

	if (!texture.texture) {
		texture.texture = gl.createTexture()
	}

	gl.activeTexture(gl.TEXTURE0 + texture.index)
	gl.bindTexture(gl.TEXTURE_2D, texture.texture)

	if (options.wrap || options.wrapS || !texture.wrapS) {
		texture.wrapS = options.wrap && options.wrap[0] || options.wrapS || options.wrap || texture.wrapS || gl.CLAMP_TO_EDGE
		gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_S, texture.wrapS)
	}

	if (options.wrap || options.wrapT || !texture.wrapT) {
		texture.wrapT = options.wrap && options.wrap[1] || options.wrapT || options.wrap || texture.wrapT || gl.CLAMP_TO_EDGE
		gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_T, texture.wrapT)
	}

	if (options.filter || options.minFilter || !texture.minFilter) {
		texture.minFilter = options.minFilter || options.filter || texture.minFilter || gl.NEAREST
		gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MIN_FILTER, texture.minFilter)
	}

	if (options.filter || options.magFilter || !texture.magFilter) {
		texture.magFilter = options.magFilter || options.filter || texture.magFilter || gl.NEAREST
		gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MAG_FILTER, texture.magFilter)
	}

	if (!texture.type || options.type) {
		texture.type = options.type || texture.type || gl.UNSIGNED_BYTE
	}

	if (!texture.format || options.format) {
		texture.format = options.format || texture.format || gl.RGBA
	}


	let data = options.data || null
	let image
	if (isBrowser) {
		// url for image
		if (typeof data === 'string') {
			if (data === (texture.data && texture.data._src) || data === (texture.data && texture.data.src)) {
				return texture
			}
			image = new Image
			image.src = data
			image._src = data
		}
		else if ('Image' in self && data instanceof Image && !data.complete) {
			image = data
		}

		if (image) {
			if (image.complete && image === texture.data || (texture.data && image.src === texture.data.src)) {
				return texture
			}
			image.addEventListener('load', () => {
				setTexture(gl, name, image, program)
			})
			data = null
		}
	}

	if (texture.level == null) texture.level = 0

	// handle raw data case
	if (data == null || Array.isArray(data) || ArrayBuffer.isView(data)) {
		if (options && options.shape) {
			if (texture.width == null) texture.width = options.shape[0]
			if (texture.height == null) texture.height = options.shape[1]
		}
		else {
			let len = data && data.length || 1
			if (options.width != null) texture.width = options.width
			else if (texture.width == null) texture.width = data && data.width || (texture.format === gl.ALPHA ? len : Math.max(len / 4, 1))
			if (options.height != null) texture.height = options.height
			else if (texture.height == null) texture.height = (data && data.height) || 1
		}
		texture.data = data == null ? null : texture.type === gl.FLOAT ? new Float32Array(data) : texture.type === gl.UNSIGNED_SHORT ? new Uint16Array(data) : new Uint8Array(data)

		// TODO: use texSubImage2D here, it is possible
		gl.texImage2D(gl.TEXTURE_2D, texture.level, texture.format, texture.width, texture.height, 0, texture.format, texture.type, texture.data)
	} else {
		texture.width = data && data.width || 1
		texture.height = data && data.height || 1
		texture.data = data
		gl.texImage2D(gl.TEXTURE_2D, texture.level, texture.format, texture.format, texture.type, texture.data)
	}

	return texture;
}
