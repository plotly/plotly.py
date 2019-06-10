'use strict';

// MODULES //

var isArray = require( 'validate.io-array' );
var isNonNegativeInteger = require( 'validate.io-nonnegative-integer' );
var PINF = require( 'const-pinf-float64' );
var deepCopy = require( './deepcopy.js' );


// COPY //

/**
* FUNCTION: createCopy( value[, level] )
*	Copy or deep clone a value to an arbitrary depth.
*
* @param {*} value - value to be copied
* @param {Number} [level=+infinity] - option to control copy depth. For example, set to `0` for a shallow copy. Default behavior returns a full deep copy.
* @returns {*} copy
*/
function createCopy( val, level ) {
	var copy;
	if ( arguments.length > 1 ) {
		if ( !isNonNegativeInteger( level ) ) {
			throw new TypeError( 'invalid input argument. Level must be a nonnegative integer. Value: `' + level + '`.' );
		}
		if ( level === 0 ) {
			return val;
		}
	} else {
		level = PINF;
	}
	copy = ( isArray(val) ) ? [] : {};
	return deepCopy( val, copy, [val], [copy], level );
} // end FUNCTION createCopy()


// EXPORTS //

module.exports = createCopy;
