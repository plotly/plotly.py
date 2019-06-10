/**
 * @module  to-array-buffer
 */

'use strict'

var str2ab = require('string-to-arraybuffer')
var flat = require('flatten-vertex-data')
// var isBlob = require('is-blob')


module.exports = function toArrayBuffer (arg) {
	//zero-length or undefined-like
	if (!arg) return null

	//array buffer
	if (arg instanceof ArrayBuffer) return arg

	//try to decode data-uri
	if (typeof arg === 'string') {
		return str2ab(arg)
	}

	// File & Blob
	// if (isBlob(src) || (src instanceof global.File)) {
		// FIXME: we cannot use it here bc FileReader is async
	// }

	//array buffer view: TypedArray, DataView, Buffer etc
	if (ArrayBuffer.isView(arg)) {
		// if byteOffset is not 0, return sub-reference (slice is the only way)
		if (arg.byteOffset) {
			return arg.buffer.slice(arg.byteOffset, arg.byteOffset + arg.byteLength)
		}
		return arg.buffer
	}

	//buffer/data nested: NDArray, ImageData etc.
	//FIXME: NDArrays with custom data type may be invalid for this procedure
	if (arg.buffer || arg.data || arg._data) {
		var result = toArrayBuffer(arg.buffer || arg.data || arg._data)
		return result
	}

	// detect if flat
	if (Array.isArray(arg)) {
		for (var i = 0; i < arg.length; i++) {
			if (arg[i].length != null) {
				arg = flat(arg)
				break
			}
		}
	}

	//array-like or unknown
	//consider Uint8Array knows how to treat the input
	var result = new Uint8Array(arg)

	if (!result.length) return null
	return result.buffer
}
