'use strict';

// MODULES //

var isString = require( 'validate.io-string-primitive' ),
	RE = require( 'regex-regex' );


// REGEX //

/**
* FUNCTION: regex( str )
*	Parses a regular expression string and returns a new regular expression.
*
* @param {String} str - regular expression string
* @returns {RegExp|Null} regular expression or null
*/
function regex( str ) {
	if ( !isString( str ) ) {
		throw new TypeError( 'invalid input argument. Must provide a regular expression string. Value: `' + str + '`.' );
	}
	// Capture the regular expression pattern and any flags:
	str = RE.exec( str );

	// Create a new regular expression:
	return ( str ) ? new RegExp( str[1], str[2] ) : null;
} // end FUNCTION regex()


// EXPORTS //

module.exports = regex;
