'use strict';

/**
* FUNCTION: isBuffer( value )
*	Validates if a value is a Buffer object.
*
* @param {*} value - value to validate
* @returns {Boolean} boolean indicating if a value is a Buffer object
*/
function isBuffer( val ) {
	return typeof val === 'object' &&
		val !== null &&
		(
			val._isBuffer || // for envs missing Object.prototype.constructor (e.g., Safari 5-7)
			(
				val.constructor &&
				typeof val.constructor.isBuffer === 'function' &&
				val.constructor.isBuffer( val )
			)
		);
} // end FUNCTION isBuffer()


// EXPORTS //

module.exports = isBuffer;
