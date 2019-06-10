'use strict';

/**
* FUNCTION: matrixLike( value )
*	Validates if a value is matrix-like.
*
* @param {*} value - value to be validated
* @returns {Boolean} boolean indicating if a value is matrix-like
*/
function matrixLike( v ) {
	return v !== null &&
		typeof v === 'object' &&
		typeof v.data === 'object' &&
		typeof v.shape === 'object' &&
		typeof v.offset === 'number' &&
		typeof v.strides === 'object' &&
		typeof v.dtype === 'string' &&
		typeof v.length === 'number';
} // end FUNCTION matrixLike()


// EXPORTS //

module.exports = matrixLike;
