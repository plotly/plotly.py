array-like
===
[![NPM version][npm-image]][npm-url] [![Build Status][travis-image]][travis-url] [![Coverage Status][coveralls-image]][coveralls-url] [![Dependencies][dependencies-image]][dependencies-url]

> Validates if a value is array-like.


## Installation

``` bash
$ npm install validate.io-array-like
```

For use in the browser, use [browserify](https://github.com/substack/node-browserify).


## Usage

``` javascript
var isArrayLike = require( 'validate.io-array-like' );
```

#### isArrayLike( value )

Validates if a value is [`array`-like](http://www.2ality.com/2013/05/quirk-array-like-objects.html).

``` javascript
var bool;

bool = isArrayLike( [] );
// returns true

bool = isArrayLike( {'length':10} );
// returns true
```


## Examples

``` javascript
var isArrayLike = require( 'validate.io-array-like' );

console.log( isArrayLike( {'length':10} ) );
// returns true

console.log( isArrayLike( [] ) );
// returns true

console.log( isArrayLike( 'beep' ) );
// returns true

console.log( (function test(){
	return isArrayLike( arguments );
})() );
// returns true

console.log( isArrayLike( null ) );
// returns false

console.log( isArrayLike( undefined ) );
// returns false

console.log( isArrayLike( 5 ) );
// returns false

console.log( isArrayLike( true ) );
// returns false

console.log( isArrayLike( {} ) );
// returns false

console.log( isArrayLike( function(){} ) );
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

Copyright &copy; 2015-2016. Athan Reines.


[npm-image]: http://img.shields.io/npm/v/validate.io-array-like.svg
[npm-url]: https://npmjs.org/package/validate.io-array-like

[travis-image]: http://img.shields.io/travis/validate-io/array-like/master.svg
[travis-url]: https://travis-ci.org/validate-io/array-like

[coveralls-image]: https://img.shields.io/coveralls/validate-io/array-like/master.svg
[coveralls-url]: https://coveralls.io/r/validate-io/array-like?branch=master

[dependencies-image]: http://img.shields.io/david/validate-io/array-like.svg
[dependencies-url]: https://david-dm.org/validate-io/array-like

[dev-dependencies-image]: http://img.shields.io/david/dev/validate-io/array-like.svg
[dev-dependencies-url]: https://david-dm.org/dev/validate-io/array-like

[github-issues-image]: http://img.shields.io/github/issues/validate-io/array-like.svg
[github-issues-url]: https://github.com/validate-io/array-like/issues
