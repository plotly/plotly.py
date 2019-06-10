'use strict';

// MODULES //

var deepCopy = require( 'utils-copy' );
var getKeys = require( 'object-keys' ).shim();


// COPY ERROR //

/**
* FUNCTION: copy( error )
*	Copies an error.
*
* @param {Error|TypeError|SyntaxError|URIError|ReferenceError|RangeError|RangeError|EvalError} error - error to copy
* @returns {Error|TypeError|SyntaxError|URIError|ReferenceError|RangeError|RangeError|EvalError} error copy
*/
function copy( error ) {
	/* jshint newcap:false */
	var keys;
	var desc;
	var key;
	var err;
	var i;
	if ( !( error instanceof Error ) ) {
		throw new TypeError( 'invalid input argument. Must provide an error object. Value: `' + error + '`.' );
	}
	// Create a new error...
	err = new error.constructor( error.message );

	// If a `stack` property is present, copy it over...
	if ( error.stack ) {
		err.stack = error.stack;
	}
	// Node.js specific (system errors)...
	if ( error.code ) {
		err.code = error.code;
	}
	if ( error.errno ) {
		err.errno = error.errno;
	}
	if ( error.syscall ) {
		err.syscall = error.syscall;
	}
	// Any enumerable properties...
	keys = getKeys( error );
	for ( i = 0; i < keys.length; i++ ) {
		key = keys[ i ];
		desc = Object.getOwnPropertyDescriptor( error, key );
		if ( desc.hasOwnProperty( 'value' ) ) {
			desc.value = deepCopy( error[ key ] );
		}
		Object.defineProperty( err, key, desc );
	}
	return err;
} // end FUNCTION copy()


// EXPORTS //

module.exports = copy;
