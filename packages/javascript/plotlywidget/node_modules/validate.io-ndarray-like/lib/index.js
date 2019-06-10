'use strict';

/**
* FUNCTION: ndarrayLike( value )
*	Validates if a value is ndarray-like.
*
* @param {*} value - value to be validated
* @returns {Boolean} boolean indicating if a value is ndarray-like
*/
function ndarrayLike( v ) {
	return v !== null &&
		typeof v === 'object' &&
		typeof v.data === 'object' &&
		typeof v.shape === 'object' &&
		typeof v.strides === 'object' &&
		typeof v.offset === 'number' &&
		typeof v.dtype === 'string' &&
		typeof v.length === 'number';
} // end FUNCTION ndarrayLike()


// EXPORTS //

module.exports = ndarrayLike;
