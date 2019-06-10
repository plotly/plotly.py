Number Primitive
===
[![NPM version][npm-image]][npm-url] [![Build Status][travis-image]][travis-url] [![Coverage Status][coveralls-image]][coveralls-url] [![Dependencies][dependencies-image]][dependencies-url]

> Validates if a value is a number primitive.


## Installation

``` bash
$ npm install validate.io-number-primitive
```

For use in the browser, use [browserify](https://github.com/substack/node-browserify).


## Usage

``` javascript
var isNumber = require( 'validate.io-number-primitive' );
```

#### isNumber( value )

Validates if a `value` is a `number` primitive, excluding `NaN`.

``` javascript
var value = Math.PI;

var bool = isNumber( value );
// returns true
```


## Examples

``` javascript
var isNumber = require( 'validate.io-number-primitive' );

console.log( isNumber( Math.PI ) );
// returns true

console.log( isNumber( NaN ) );
// returns false

console.log( isNumber( new Number( 5 ) ) );
// returns false

console.log( isNumber( '5' ) );
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


[npm-image]: http://img.shields.io/npm/v/validate.io-number-primitive.svg
[npm-url]: https://npmjs.org/package/validate.io-number-primitive

[travis-image]: http://img.shields.io/travis/validate-io/number-primitive/master.svg
[travis-url]: https://travis-ci.org/validate-io/number-primitive

[coveralls-image]: https://img.shields.io/coveralls/validate-io/number-primitive/master.svg
[coveralls-url]: https://coveralls.io/r/validate-io/number-primitive?branch=master

[dependencies-image]: http://img.shields.io/david/validate-io/number-primitive.svg
[dependencies-url]: https://david-dm.org/validate-io/number-primitive

[dev-dependencies-image]: http://img.shields.io/david/dev/validate-io/number-primitive.svg
[dev-dependencies-url]: https://david-dm.org/dev/validate-io/number-primitive

[github-issues-image]: http://img.shields.io/github/issues/validate-io/number-primitive.svg
[github-issues-url]: https://github.com/validate-io/number-primitive/issues
