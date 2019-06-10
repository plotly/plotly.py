RegExp String
===
[![NPM version][npm-image]][npm-url] [![Build Status][travis-image]][travis-url] [![Coverage Status][codecov-image]][codecov-url] [![Dependencies][dependencies-image]][dependencies-url]

> [Regular expression](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions) to parse a [regular expression](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions) string.


## Installation

``` bash
$ npm install regex-regex
```


## Usage

``` javascript
var re = require( 'regex-regex' );
```

#### re

[Regular expression](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions) to parse a [regular expression](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions) string. 

``` javascript
var bool = re.test( '/^beep$/' );
// returns true

bool = re.test( '' );
// returns false
```

[Regular expression](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions) strings should be escaped.

``` javascript
bool = re.test( '/^\/([^\/]+)\/(.*)$/' );
// returns false

bool = re.test( '/^\\/([^\\/]+)\\/(.*)$/' );
// returns true
```


## Examples

``` javascript
var re = require( 'regex-regex' );

console.log( re.test( '/beep/' ) );
// returns true

console.log( re.test( '/^.*$/ig' ) );
// returns true

console.log( re.test( '/^\\/([^\\/]+)\\/(.*)$/' ) );
// returns true

console.log( re.test( '/^\/([^\/]+)\/(.*)$/' ) );
// returns false

console.log( re.test( '/boop' ) );
// returns false

console.log( re.test( '' ) );
// returns false
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


[npm-image]: http://img.shields.io/npm/v/regex-regex.svg
[npm-url]: https://npmjs.org/package/regex-regex

[travis-image]: http://img.shields.io/travis/kgryte/regex-regex/master.svg
[travis-url]: https://travis-ci.org/kgryte/regex-regex

[codecov-image]: https://img.shields.io/codecov/c/github/kgryte/regex-regex/master.svg
[codecov-url]: https://codecov.io/github/kgryte/regex-regex?branch=master

[dependencies-image]: http://img.shields.io/david/kgryte/regex-regex.svg
[dependencies-url]: https://david-dm.org/kgryte/regex-regex

[dev-dependencies-image]: http://img.shields.io/david/dev/kgryte/regex-regex.svg
[dev-dependencies-url]: https://david-dm.org/dev/kgryte/regex-regex

[github-issues-image]: http://img.shields.io/github/issues/kgryte/regex-regex.svg
[github-issues-url]: https://github.com/kgryte/regex-regex/issues
