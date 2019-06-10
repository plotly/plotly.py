dims
===
[![NPM version][npm-image]][npm-url] [![Build Status][travis-image]][travis-url] [![Coverage Status][coveralls-image]][coveralls-url] [![Dependencies][dependencies-image]][dependencies-url]

> Computes dimensions for arrays and matrices.


## Installation

``` bash
$ npm install compute-dims
```

For use in the browser, use [browserify](https://github.com/substack/node-browserify).


## Usage


``` javascript
var dims = require( 'compute-dims' );
```

#### dims( x[, max] )

Computes dimensions of `x`. `x` may be either an [`array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array) (including nested `arrays`) or a [`matrix`](https://github.com/dstructs/matrix).

``` javascript
var matrix = require( 'dstructs-matrix' ),
	data,
	d;

data = [ 1, 2 ];
d = dims( data );
// returns [2]

data = [ [1,2], [1,2] ];
d = dims( data );
// returns [2,2]

data = matrix( [1,2,3,4], [2,2] )
d = dims( data );
// returns [2,2]
```

If an `array` element has a dimension inconsistent with other elements, the function returns `null`.

``` javascript
data = [ [1,2], [1] ];
d = dims( data );
// returns null
```

To limit the number of dimensions returned, set the `max` option.

``` javascript
data = [ [[1,2], [3,4]] ]; // 1x2x2
d = dims( data, 2 );
// returns [1,2]

data = [ [[1,2], [3,4,5,6,7,8]] ];
d = dims( data );
// returns null

d = dims( data, 2 );
// returns [1,2]

data = matrix( [1,2,3,4], [2,2] );
d = dims( data, 1 );
// returns [2]
```


## Examples

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

Copyright &copy; 2014-2015. The [Compute.io](https://github.com/compute-io) Authors.

[npm-image]: http://img.shields.io/npm/v/compute-dims.svg
[npm-url]: https://npmjs.org/package/compute-dims

[travis-image]: http://img.shields.io/travis/compute-io/dims/master.svg
[travis-url]: https://travis-ci.org/compute-io/dims

[coveralls-image]: https://img.shields.io/coveralls/compute-io/dims/master.svg
[coveralls-url]: https://coveralls.io/r/compute-io/dims?branch=master

[dependencies-image]: http://img.shields.io/david/compute-io/dims.svg
[dependencies-url]: https://david-dm.org/compute-io/dims

[dev-dependencies-image]: http://img.shields.io/david/dev/compute-io/dims.svg
[dev-dependencies-url]: https://david-dm.org/dev/compute-io/dims

[github-issues-image]: http://img.shields.io/github/issues/compute-io/dims.svg
[github-issues-url]: https://github.com/compute-io/dims/issues
