'use strict'

const isPlainObject = require('is-plain-obj');
const extend = require('object-assign');
const getProgram = require('./program')
const WeakMap = require('weak-map');

let attributesCache = setAttribute.cache = new WeakMap();
let attributesIdx = new WeakMap();

module.exports = setAttribute;

function setAttribute (gl, name, options, program) {
	if (!gl) throw Error('WebGL context is not provided');

	if (options instanceof WebGLProgram) {
		program = options;
		options = null;
	}
	else if (!program) {
		program = getProgram(gl, program);
	}

	if (!program) throw Error('Context has no active program');

	//object with attributes passed
	if (name && typeof name != 'string') {
		let result = {};
		let attributes = name;

		for (let name in attributes) {
			result[name] = setAttribute(gl, name, attributes[name], program);
		}

		return result;
	}

	let attributes = attributesCache.has(program) ? attributesCache.get(program) : attributesCache.set(program, {}).get(program);

	//return all attribs if no name provided
	if (!name) return attributes;

	let attribute = attributes[name];

	//if attribute exists and ony the data passed - just update buffer data
	if (attribute) {
		if (options && attribute.data && !isPlainObject(options) && options.length <= attribute.data.length) {

			if (attribute.target === gl.ELEMENT_ARRAY_BUFFER) {
				attribute.data = new Uint16Array(options);
			}
			else if (attribute.type === gl.FLOAT) {
				attribute.data = new Float32Array(options);
			}
			else if (attribute.type === gl.UNSIGNED_BYTE) {
				attribute.data = new Uint8Array(options);
			}

			gl.bindBuffer(attribute.target, attribute.buffer);
			gl.bufferSubData(attribute.target, 0, attribute.data);

			//FIXME: sort out why do we need to set pointer every program switch
			// gl.enableVertexAttribArray(attribute.index);
			gl.vertexAttribPointer(attribute.index, attribute.size, attribute.type, attribute.normalized, attribute.stride, attribute.offset);
			// gl.bindAttribLocation(program, attribute.index, attribute.name);

			return attribute;
		}
	}

	//autoinit attribute(s)
	else {
		let count = gl.getProgramParameter(program, gl.ACTIVE_ATTRIBUTES);

		for (var i=0; i < count; ++i) {
			let info = gl.getActiveAttrib(program, i);
			if (!info) continue;
			let type = info.type, size = info.size;
			switch (info.type) {
				case gl.FLOAT_VEC2:
				case gl.FLOAT_VEC3:
				case gl.FLOAT_VEC4:
				case gl.FLOAT_MAT2:
				case gl.FLOAT_MAT3:
				case gl.FLOAT_MAT4:
					type = gl.FLOAT;
					break;
				case gl.INT_VEC2:
				case gl.INT_VEC3:
				case gl.INT_VEC4:
				case gl.INT_MAT2:
				case gl.INT_MAT3:
				case gl.INT_MAT4:
					type = gl.UNSIGNED_INT;
					break;
			}
			switch (info.type) {
				case gl.FLOAT_VEC2:
				case gl.INT_VEC2:
						size = 2;
						break;
				case gl.FLOAT_VEC3:
				case gl.INT_VEC3:
						size = 3;
						break;
				case gl.FLOAT_VEC4:
				case gl.INT_VEC4:
				case gl.FLOAT_MAT2:
						size = 4;
						break;
				case gl.FLOAT_MAT3:
						size = 9;
						break;
				case gl.FLOAT_MAT4:
						size = 16;
						break;
			}
			attributes[info.name] = {name: info.name, type: type, size: size, data: []}
		}

		if (!attributes[name]) attributes[name] = {name: name, data: [], type: null, size: null}

		attribute = attributes[name];
	}

	//if no options passed - just return known attribute info
	if (options == null) return attribute;

	if (!isPlainObject(options)) options = {data: options};
	extend(attribute, options);

	//detect target
	if (!attribute.target) {
		attribute.target = gl.ARRAY_BUFFER;
	}

	if (!attribute.buffer) {
		attribute.buffer = gl.createBuffer();
	}

	if (!attribute.usage) {
		attribute.usage = gl.STATIC_DRAW;
	}

	//set index if undefined
	if (attribute.index == null) {
		let topIndex = attributesIdx.get(program) || 0;
		attribute.index = topIndex++;
		topIndex = Math.max(topIndex, attribute.index);
		attributesIdx.set(program, topIndex);
	}

	if (!attribute.size) {
		attribute.size = 2;
	}

	if (!attribute.type) {
		attribute.type = attribute.target === gl.ELEMENT_ARRAY_BUFFER ? gl.UNSIGNED_SHORT : gl.FLOAT;
	}

	if (Array.isArray(attribute.data)) {
		if (attribute.type === gl.FLOAT) {
			attribute.data = new Float32Array(attribute.data);
		}
		else if (attribute.type === gl.UNSIGNED_BYTE) {
			attribute.data = new Uint8Array(attribute.data);
		}
		else if (attribute.type === gl.UNSIGNED_SHORT) {
			attribute.data =  new Uint16Array(attribute.data);
		}
	}

	if (attribute.normalized == null) {
		attribute.normalized = false;
	}

	if (attribute.stride == null) {
		attribute.stride = 0;
	}

	if (attribute.offset == null) {
		attribute.offset = 0;
	}

	gl.bindBuffer(attribute.target, attribute.buffer);
	gl.bufferData(attribute.target, attribute.data, attribute.usage);

	gl.enableVertexAttribArray(attribute.index);
	gl.vertexAttribPointer(attribute.index, attribute.size, attribute.type, attribute.normalized, attribute.stride, attribute.offset);
	gl.bindAttribLocation(program, attribute.index, attribute.name);

	return attribute;
}
