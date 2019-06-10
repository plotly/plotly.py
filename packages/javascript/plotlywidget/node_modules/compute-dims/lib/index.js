'use strict';

// MODULES //

var isPositiveInteger = require( 'validate.io-positive-integer' ),
	isArray = require( 'validate.io-array' ),
	ndarrayLike = require( 'validate.io-ndarray-like' ),
	createCopy = require( 'utils-copy' );


// DIMS //

/**
* FUNCTION: dims( x, d, max )
*	Computes array dimensions.
*
* @private
* @param {Array} arr - input array
* @param {Array} d - dimensions array
* @param {Number} max - max number of dimensions
* @returns {Array} dimensions array
*/
function dims( arr, d, max ) {
	if ( max && d.length === max ) {
		return;
	}
	if ( !isArray( arr[0] ) ) {
		return;
	}
	d.push( arr[0].length );
	dims( arr[ 0 ], d, max );
} // end FUNCTION dims()

/**
* FUNCTION: check( arr, d )
*	Checks that all array elements have the same dimensions.
*
* @private
* @param {Array} arr - input array
* @param {Array} d - dimensions array
* @returns {Boolean} boolean indicating if all array elements have the same dimensions
*/
function check( arr, d ) {
	var len = arr.length,
		dim = d.shift(),
		nDims = d.length,
		val,
		flg;

	for ( var i = 0; i < len; i++ ) {
		val = arr[ i ];
		if ( !isArray( val ) || val.length !== dim ) {
			return false;
		}
		if ( nDims ) {
			flg = check( val, d.slice() );
			if ( !flg ) {
				return false;
			}
		}
	}
	return true;
} // end FUNCTION check()

/**
* FUNCTION: compute( x[, max] )
*	Computes dimensions.
*
* @param {Array} x - input object
* @param {Number} [max] - limits the number of dimensions returned
* @returns {Array|null} array of dimensions or null
*/
function compute( x, max ) {

	var d, flg;

	if ( arguments.length > 1 ) {
		if ( !isPositiveInteger( max ) ) {
			throw new TypeError( 'dims()::invalid input argument. `max` option must be a positive integer.' );
		}
	}

	if ( ndarrayLike( x ) === true ) {
	 	d = createCopy( x.shape );
		if ( max && max <= d.length ) {
			d.length = max;
		}
		return d;
	}

	if ( isArray( x ) ) {
		// [0] Initialize the dimensions array:
		d = [ x.length ];

		// [1] Recursively determine array dimensions:
		dims( x, d, max );

		// [2] Check that all array element dimensions are consistent...
		if ( d.length > 1 ) {
			flg = check( x, d.slice( 1 ) );
			if ( !flg ) {
				return null;
			}
		}
		return d;
	}

	throw new TypeError( 'dims()::invalid input argument. Must provide an array, matrix or ndarray.' );
} // end FUNCTION compute()


// EXPORTS //

module.exports = compute;
