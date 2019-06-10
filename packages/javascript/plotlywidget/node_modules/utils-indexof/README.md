indexOf
===
[![NPM version][npm-image]][npm-url] [![Build Status][build-image]][build-url] [![Coverage Status][coverage-image]][coverage-url] [![Dependencies][dependencies-image]][dependencies-url]

> Returns the first index at which a given element can be found.


## Installation

``` bash
$ npm install utils-indexof
```


## Usage

``` javascript
var indexOf = require( 'utils-indexof' );
```

#### indexOf( arr, searchElement[, fromIndex] )

Returns the first index at which a given element can be found.

``` javascript
var arr = [ 4, 3, 2, 1 ];

var idx = indexOf( arr, 3 );
// returns 1
```

If a `searchElement` is __not__ present in an input `array`, the `function` returns `-1`.

``` javascript
var arr = [ 4, 3, 2, 1 ];

var idx = indexOf( arr, 5 );
// returns -1
```

By default, the implementation searches an input `array` beginning from the first element. To start searching from a different element, specify a `fromIndex`.

``` javascript
var arr = [ 1, 2, 3, 4, 5, 2, 6 ];

var idx = indexOf( arr, 2, 3 );
// returns 5
```

If a `fromIndex` exceeds the input `array` length, the `function` returns `-1`.

``` javascript
var arr = [ 1, 2, 3, 4, 2, 5 ];

var idx = indexOf( arr, 2, 10 );
// returns -1
```

If a `fromIndex` is less than `0`, the starting index is determined relative to the last index (with the last index being equivalent to `fromIndex = -1`).

``` javascript
var arr = [ 1, 2, 3, 4, 5, 2, 6, 2 ];

var idx = indexOf( arr, 2, -4 );
// returns 5

idx = indexOf( arr, 2, -1 );
// returns 7
```

If `fromIndex` is less than `0` __and__ its absolute value exceeds the input `array` length, the `function` searches the entire input `array`.

``` javascript
var arr = [ 1, 2, 3, 4, 5, 2, 6 ];

var idx = indexOf( arr, 2, -10 );
// returns 1
```

The first argument is not limited to `arrays`, but may be any [array-like][validate.io-array-like] `object`.

``` javascript
var str = 'bebop';

var idx = indexOf( str, 'o' );
// returns 3
```


## Notes

* 	Search is performed using __strict equality__ comparison. Thus,
	
	``` javascript
	var arr = [ 1, [1,2,3], 3 ];

	var idx = indexOf( arr, [1,2,3] );
	// returns -1
	```

*	This implementation is __not__ [ECMAScript Standard][ecma-262] compliant. Notably, the [standard][ecma-262] specifies that an `array` be searched by calling `hasOwnProperty` (thus, for most cases, incurring a performance penalty), and the [standard][ecma-262] does __not__ accommodate a `searchElement` equal to `NaN`. In this implementation, the following is possible:

	``` javascript
	// Locate the first element which is NaN...
	var arr = [ 1, NaN, 2, NaN ];

	var idx = indexOf( arr, NaN );
	// returns 1

	// Prototype properties may be searched as well...
	function Obj() {
		this[ 0 ] = 'beep';
		this[ 1 ] = 'boop';
		this[ 2 ] = 'woot';
		this[ 3 ] = 'bap';
		this.length = 4;
		return this;
	}
	Obj.prototype[ 2 ] = 'bop';

	var obj = new Obj();
	
	idx = indexOf( obj, 'bop' );
	// returns -1

	delete obj[ 2 ];

	idx = indexOf( obj, 'bop' );
	// returns 2
	```


## Examples

``` javascript
var indexOf = require( 'utils-indexof' );

var arr;
var obj;
var str;
var idx;
var i;

// Arrays...
arr = new Array( 10 );
for ( i = 0; i < arr.length; i++ ) {
	arr[ i ] = i * 10;
}
idx = indexOf( arr, 40 );

console.log( idx );
// returns 4


// Array-like objects...
obj = {
	'0': 'beep',
	'1': 'boop',
	'2': 'bap',
	'3': 'bop',
	'length': 4
};

idx = indexOf( obj, 'bap' );

console.log( idx );
// returns 2


// Strings...
str = 'beepboopbop';

idx = indexOf( str, 'o' );

console.log( idx );
// returns 5
```

To run the example code from the top-level application directory,

``` bash
$ node ./examples/index.js
```


---
## Tests

### Unit

This repository uses [tape][tape] for unit tests. To run the tests, execute the following command in the top-level application directory:

``` bash
$ make test
```

All new feature development should have corresponding unit tests to validate correct functionality.


### Test Coverage

This repository uses [Istanbul][istanbul] as its code coverage tool. To generate a test coverage report, execute the following command in the top-level application directory:

``` bash
$ make test-cov
```

Istanbul creates a `./reports/coverage` directory. To access an HTML version of the report,

``` bash
$ make view-cov
```


### Browser Support

This repository uses [Testling][testling] for browser testing. To run the tests in a (headless) local web browser, execute the following command in the top-level application directory:

``` bash
$ make test-browsers
```

To view the tests in a local web browser,

``` bash
$ make view-browser-tests
```

<!-- [![browser support][browsers-image]][browsers-url] -->


---
## License

[MIT license](http://opensource.org/licenses/MIT).


## Copyright

Copyright &copy; 2016. Athan Reines.


[npm-image]: http://img.shields.io/npm/v/utils-indexof.svg
[npm-url]: https://npmjs.org/package/utils-indexof

[build-image]: http://img.shields.io/travis/kgryte/utils-indexof/master.svg
[build-url]: https://travis-ci.org/kgryte/utils-indexof

[coverage-image]: https://img.shields.io/codecov/c/github/kgryte/utils-indexof/master.svg
[coverage-url]: https://codecov.io/github/kgryte/utils-indexof?branch=master

[dependencies-image]: http://img.shields.io/david/kgryte/utils-indexof.svg
[dependencies-url]: https://david-dm.org/kgryte/utils-indexof

[dev-dependencies-image]: http://img.shields.io/david/dev/kgryte/utils-indexof.svg
[dev-dependencies-url]: https://david-dm.org/dev/kgryte/utils-indexof

[github-issues-image]: http://img.shields.io/github/issues/kgryte/utils-indexof.svg
[github-issues-url]: https://github.com/kgryte/utils-indexof/issues

[tape]: https://github.com/substack/tape
[istanbul]: https://github.com/gotwarlost/istanbul
[testling]: https://ci.testling.com

[ecma-262]: http://www.ecma-international.org/ecma-262/6.0/#sec-array.prototype.indexof
[validate.io-array-like]: https://github.com/validate.io/array-like
