'use strict';

// MODULES //

var isArrayLike = require( 'validate.io-array-like' );
var isInteger = require( 'validate.io-integer-primitive' );


// INDEXOF //

/**
* FUNCTION: indexOf( arr, searchElement[, fromIndex] )
*	Returns the first index at which a given element can be found.
*
* @param {Array|String|Object} arr - array-like object
* @param {*} searchElement - element to find
* @param {Number} [fromIndex] - starting index (if negative, the start index is determined relative to last element)
* @returns {Number} index or -1
*/
function indexOf( arr, searchElement, fromIndex ) {
	var len;
	var i;
	if ( !isArrayLike( arr ) ) {
		throw new TypeError( 'invalid input argument. First argument must be an array-like object. Value: `' + arr + '`.' );
	}
	len = arr.length;
	if ( len === 0 ) {
		return -1;
	}
	if ( arguments.length === 3 ) {
		if ( !isInteger( fromIndex ) ) {
			throw new TypeError( 'invalid input argument. `fromIndex` must be an integer. Value: `' + fromIndex + '`.' );
		}
		if ( fromIndex >= 0 ) {
			if ( fromIndex >= len ) {
				return -1;
			}
			i = fromIndex;
		} else {
			i = len + fromIndex;
			if ( i < 0 ) {
				i = 0;
			}
		}
	} else {
		i = 0;
	}
	if ( searchElement !== searchElement ) { // check for NaN
		for ( ; i < len; i++ ) {
			if ( arr[ i ] !== arr[ i ] ) {
				return i;
			}
		}
	} else {
		for ( ; i < len; i++ ) {
			if ( arr[ i ] === searchElement ) {
				return i;
			}
		}
	}
	return -1;
} // end FUNCTION indexOf()


// EXPORTS //

module.exports = indexOf;
