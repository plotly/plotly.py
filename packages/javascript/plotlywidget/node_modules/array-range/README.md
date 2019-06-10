# array-range

[![stable](http://badges.github.io/stability-badges/dist/stable.svg)](http://github.com/badges/stability-badges)

Tiny module to create a new dense array with the specified range. 

```js
var range = require('array-range')
range(3)       // -> [ 0, 1, 2 ]
range(1, 4)    // -> [ 1, 2, 3 ]
```

Mainly useful for functional programming. ES6 examples:  

```js
var array = require('array-range')

array(5).map( x => x*x )
// -> [ 0, 1, 4, 9, 16 ]

array(2, 10).filter( x => x%2===0 )
// -> [ 2, 4, 6, 8 ]
```

It can also be useful for creating a fixed size dense array. Cleaner than `apply` and does not create an intermediate array:  

```js
array(5)

//vs.

Array.apply(null, new Array(5))
```

## Usage

[![NPM](https://nodei.co/npm/array-range.png)](https://nodei.co/npm/array-range/)

#### `array(start, end)`

Creates a new dense array with a length of `end-start` elements. `start` is inclusive, `end` is exclusive. Negative values also work, e.g. `range(-10, 10)`

#### `array(len)`

Creates a new dense array with `len` number of elements, from zero to `len-1`. 

If `len` is unspecified, it defaults to zero (empty array). 

## License

MIT, see [LICENSE.md](http://github.com/mattdesl/array-range/blob/master/LICENSE.md) for details.
