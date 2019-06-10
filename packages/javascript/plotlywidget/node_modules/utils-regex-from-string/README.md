RegExp
===
[![NPM version][npm-image]][npm-url] [![Build Status][travis-image]][travis-url] [![Coverage Status][codecov-image]][codecov-url] [![Dependencies][dependencies-image]][dependencies-url]

> Parses a [regular expression](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions) string and returns a new [regular expression](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions).


## Installation

``` bash
$ npm install utils-regex-from-string
```


## Usage

``` javascript
var regex = require( 'utils-regex-from-string' );
```

#### regex( str )

Parses a [regular expression](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions) `string` and returns a new [regular expression](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions).

``` javascript
var re = regex( '/beep/' )
// returns /beep/
```

__Note__: provided `strings` must be properly __escaped__.

``` javascript
// Unescaped:
re = regex( '/\w+/' );
// returns /w+/

// Escaped:
re = regex( '/\\w+/' );
// returns /\w+/
```


## Examples

``` javascript
var regex = require( 'utils-regex-from-string' );

console.log( regex( '/beep/' ) );
// returns /beep/

console.log( regex( '/[A-Z]*/' ) );
// returns /[A-Z]*/

console.log( regex( '/\\\\\\\//ig' ) );
// returns /\\\//ig

console.log( regex( '/[A-Z]{0,}/' ) );
// returns /[A-Z]{0,}/

console.log( regex( '/^boop$/' ) );
// returns /^boop$/

console.log( regex( '/(?:.*)/' ) );
// returns /(?:.*)/

console.log( regex( '/(?:beep|boop)/' ) );
// returns /(?:beep|boop)/

console.log( regex( '/\\w+/' ) );
// returns /\w+/
```

To run the example code from the top-level application directory,

``` bash
$ node ./examples/index.js
```


## Tests

### Unit

Unit tests use the [Mocha](http://mochajs.org/) test framework with [Chai](http://chaijs.com) assertions. To run the tests, execute the following command in the top-level application directory:

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


[npm-image]: http://img.shields.io/npm/v/utils-regex-from-string.svg
[npm-url]: https://npmjs.org/package/utils-regex-from-string

[travis-image]: http://img.shields.io/travis/kgryte/utils-regex-from-string/master.svg
[travis-url]: https://travis-ci.org/kgryte/utils-regex-from-string

[codecov-image]: https://img.shields.io/codecov/c/github/kgryte/utils-regex-from-string/master.svg
[codecov-url]: https://codecov.io/github/kgryte/utils-regex-from-string?branch=master

[dependencies-image]: http://img.shields.io/david/kgryte/utils-regex-from-string.svg
[dependencies-url]: https://david-dm.org/kgryte/utils-regex-from-string

[dev-dependencies-image]: http://img.shields.io/david/dev/kgryte/utils-regex-from-string.svg
[dev-dependencies-url]: https://david-dm.org/dev/kgryte/utils-regex-from-string

[github-issues-image]: http://img.shields.io/github/issues/kgryte/utils-regex-from-string.svg
[github-issues-url]: https://github.com/kgryte/utils-regex-from-string/issues
