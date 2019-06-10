'use strict';

// MODULES //

var isArray = require( 'validate.io-array' );
var isBuffer = require( 'validate.io-buffer' );
var typeName = require( 'type-name' );
var regex = require( 'utils-regex-from-string' );
var copyError = require( 'utils-copy-error' );
var indexOf = require( 'utils-indexof' );
var objectKeys = require( 'object-keys' );
var typedArrays = require( './typedarrays.js' );


// FUNCTIONS //

/**
* FUNCTION: cloneInstance( val )
*	Clones a class instance.
*
*	WARNING: this should only be used for simple cases. Any instances with privileged access to variables (e.g., within closures) cannot be cloned. This approach should be considered fragile.
*
*	NOTE: the function is greedy, disregarding the notion of a 'level'. Instead, the function deep copies all properties, as we assume the concept of 'level' applies only to the class instance reference but not to its internal state. This prevents, in theory, two instances from sharing state.
*
* @private
* @param {Object} val - class instance
* @returns {Object} new instance
*/
function cloneInstance( val ) {
	var cache = [];
	var refs = [];
	var names;
	var name;
	var desc;
	var tmp;
	var ref;
	var i;

	ref = Object.create( Object.getPrototypeOf( val ) );
	cache.push( val );
	refs.push( ref );

	names = Object.getOwnPropertyNames( val );
	for ( i = 0; i < names.length; i++ ) {
		name = names[ i ];
		desc = Object.getOwnPropertyDescriptor( val, name );
		if ( desc.hasOwnProperty( 'value' ) ) {
			tmp = ( isArray( val[name] ) ) ? [] : {};
			desc.value = deepCopy( val[name], tmp, cache, refs, -1 );
		}
		Object.defineProperty( ref, name, desc );
	}
	if ( !Object.isExtensible( val ) ) {
		Object.preventExtensions( ref );
	}
	if ( Object.isSealed( val ) ) {
		Object.seal( ref );
	}
	if ( Object.isFrozen( val ) ) {
		Object.freeze( ref );
	}
	return ref;
} // end FUNCTION cloneInstance()


// DEEP COPY //

/**
* FUNCTION: deepCopy( val, copy, cache, refs, level )
*	Recursively performs a deep copy of an input object.
*
* @private
* @param {Array|Object} val - value to copy
* @param {Array|Object} copy - copy
* @param {Array} cache - an array of visited objects
* @param {Array} refs - an array of object references
* @param {Number} level - copy depth
* @returns {*} deep copy
*/
function deepCopy( val, copy, cache, refs, level ) {
	var parent;
	var keys;
	var name;
	var desc;
	var ctor;
	var key;
	var ref;
	var x;
	var i;
	var j;

	level = level - 1;

	// Primitives and functions...
	if (
		typeof val !== 'object' ||
		val === null
	) {
		return val;
	}
	if ( isBuffer( val ) ) {
		return new Buffer( val );
	}
	if ( val instanceof Error ) {
		return copyError( val );
	}
	// Objects...
	name = typeName( val );

	if ( name === 'Date' ) {
		return new Date( +val );
	}
	if ( name === 'RegExp' ) {
		return regex( val.toString() );
	}
	if ( name === 'Set' ) {
		return new Set( val );
	}
	if ( name === 'Map' ) {
		return new Map( val );
	}
	if (
		name === 'String' ||
		name === 'Boolean' ||
		name === 'Number'
	) {
		// Return an equivalent primitive!
		return val.valueOf();
	}
	ctor = typedArrays[ name ];
	if ( ctor ) {
		return ctor( val );
	}
	// Class instances...
	if (
		name !== 'Array' &&
		name !== 'Object'
	) {
		// Cloning requires ES5 or higher...
		if ( typeof Object.freeze === 'function' ) {
			return cloneInstance( val );
		}
		return {};
	}
	// Arrays and plain objects...
	keys = objectKeys( val );
	if ( level > 0 ) {
		parent = name;
		for ( j = 0; j < keys.length; j++ ) {
			key = keys[ j ];
			x = val[ key ];

			// Primitive, Buffer, special class instance...
			name = typeName( x );
			if (
				typeof x !== 'object' ||
				x === null ||
				(
					name !== 'Array' &&
					name !== 'Object'
				) ||
				isBuffer( x )
			) {
				if ( parent === 'Object' ) {
					desc = Object.getOwnPropertyDescriptor( val, key );
					if ( desc.hasOwnProperty( 'value' ) ) {
						desc.value = deepCopy( x );
					}
					Object.defineProperty( copy, key, desc );
				} else {
					copy[ key ] = deepCopy( x );
				}
				continue;
			}
			// Circular reference...
			i = indexOf( cache, x );
			if ( i !== -1 ) {
				copy[ key ] = refs[ i ];
				continue;
			}
			// Plain array or object...
			ref = ( isArray(x) ) ? [] : {};
			cache.push( x );
			refs.push( ref );
			if ( parent === 'Array' ) {
				copy[ key ] = deepCopy( x, ref, cache, refs, level );
			} else {
				desc = Object.getOwnPropertyDescriptor( val, key );
				if ( desc.hasOwnProperty( 'value' ) ) {
					desc.value = deepCopy( x, ref, cache, refs, level );
				}
				Object.defineProperty( copy, key, desc );
			}
		}
	} else {
		if ( name === 'Array' ) {
			for ( j = 0; j < keys.length; j++ ) {
				key = keys[ j ];
				copy[ key ] = val[ key ];
			}
		} else {
			for ( j = 0; j < keys.length; j++ ) {
				key = keys[ j ];
				desc = Object.getOwnPropertyDescriptor( val, key );
				Object.defineProperty( copy, key, desc );
			}
		}
	}
	if ( !Object.isExtensible( val ) ) {
		Object.preventExtensions( copy );
	}
	if ( Object.isSealed( val ) ) {
		Object.seal( copy );
	}
	if ( Object.isFrozen( val ) ) {
		Object.freeze( copy );
	}
	return copy;
} // end FUNCTION deepCopy()


// EXPORTS //

module.exports = deepCopy;
