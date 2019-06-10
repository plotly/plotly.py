matrix-like
===
[![NPM version][npm-image]][npm-url] [![Build Status][travis-image]][travis-url] [![Coverage Status][coveralls-image]][coveralls-url] [![Dependencies][dependencies-image]][dependencies-url]

> Validates if a value is [matrix](https://github.com/dstructs/matrix)-like.


## Installation

``` bash
$ npm install validate.io-matrix-like
```

For use in the browser, use [browserify](https://github.com/substack/node-browserify).


## Usage

``` javascript
var matrixLike = require( 'validate.io-matrix-like' );
```

#### matrixLike( value )

Validates if a value is [matrix](https://github.com/dstructs/matrix)-like.

``` javascript
var mat = {
	'data': new Int8Array( 10 ),
	'shape': [5,2],
	'offset': 0,
	'strides': [2,1],
	'dtype': 'int8',
	'length': 10
};

console.log( matrixLike( mat ) );
// returns true
```


## Examples

``` javascript
var matrixLike = require( 'validate.io-matrix-like' );

var mat = {
	'data': new Int8Array( 10 ),
	'shape': [5,2],
	'offset': 0,
	'strides': [2,1],
	'dtype': 'int8',
	'length': 10
};
console.log( matrixLike( mat ) );
// returns true

console.log( matrixLike( [] ) );
// returns false

console.log( matrixLike( {} ) );
// returns false

console.log( matrixLike( null ) );
// returns false
```

To run the example code from the top-level application directory,

``` bash
$ node ./examples/index.js
```


## Tests

### Unit

Unit tests use the [Mocha](http://mochajs.org) test framework with [Chai](http://chaijs.com) assertions. To run the tests, execute the following command in the top-level application directory:

``` bash
$ make test
```

All new feature development should have corresponding unit tests to validate correct functionality.


### Test Coverage

This repository uses [Istanbul](https://github.com/gotwarlost/istanbul) as its code coverage tool. To generate a test coverage report, execute the following command in the top-level application directory:

``` bash
$ make test-cov
```

Istanbul creates a `./reports/coverage` directory. To access an HTML version of the report,

``` bash
$ make view-cov
```


---
## License

[MIT license](http://opensource.org/licenses/MIT). 


## Copyright

Copyright &copy; 2015. Athan Reines.


[npm-image]: http://img.shields.io/npm/v/validate.io-matrix-like.svg
[npm-url]: https://npmjs.org/package/validate.io-matrix-like

[travis-image]: http://img.shields.io/travis/validate-io/matrix-like/master.svg
[travis-url]: https://travis-ci.org/validate-io/matrix-like

[coveralls-image]: https://img.shields.io/coveralls/validate-io/matrix-like/master.svg
[coveralls-url]: https://coveralls.io/r/validate-io/matrix-like?branch=master

[dependencies-image]: http://img.shields.io/david/validate-io/matrix-like.svg
[dependencies-url]: https://david-dm.org/validate-io/matrix-like

[dev-dependencies-image]: http://img.shields.io/david/dev/validate-io/matrix-like.svg
[dev-dependencies-url]: https://david-dm.org/dev/validate-io/matrix-like

[github-issues-image]: http://img.shields.io/github/issues/validate-io/matrix-like.svg
[github-issues-url]: https://github.com/validate-io/matrix-like/issues
