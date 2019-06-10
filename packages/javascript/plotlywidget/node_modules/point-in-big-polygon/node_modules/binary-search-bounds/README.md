binary-search-bounds
====================
Binary search on arrays.  Also works if the inputs are 1D [ndarrays](https://github.com/mikolalysenko/ndarray).

## Install
```
npm install binary-search-bounds
```

## API

```javascript
var bounds = require("binary-search-bounds")
```

### `bounds.lt(array, y[, cmp, lo, hi])`
Returns the index of the last item in the array `<` y

### `bounds.le(array, y[, cmp, lo, hi])`
Returns the index of the last item in the array `<=` y

### `bounds.gt(array, y[, cmp, lo, hi])`
Returns the index of the first item in the array `>` y

### `bounds.ge(array, y[, cmp, lo, hi])`
Returns the index of the first item in the array `>=` y

### `bounds.eq(array, y[, cmp, lo, hi])`
Returns an index of some item in the array `== y`.

### Notes

The following comments apply to the above methods:

* `array` can be either an array or an [`ndarray`](https://github.com/mikolalysenko/ndarray)
* `cmp` is a comparison function, just like what you would pass to `Array.sort()`
* `y` will always be the second argument passed to `cmp`, so you can ignore it if you are just binary searching on a predicate.
* Assumes the array is sorted as would be the case if you called `Array.sort(cmp)` on it
* If no comparison is passed, assume array is sorted in ascending order (note this is different than the semantics of Array.sort() which converts all entries to strings if you don't pass an argument)
* `lo` gives a lower bound on the array index to search.  If not specified defaults to 0.
* `hi` gives an upper bound on the array index to search.  If not specified defaults to `array.length-1`
* Bouth bounds are inclusive.
* `bounds.le` and `bounds.lt` will return `lo - 1` if no element is found that `==y`
* `bounds.ge` and `bounds.gt` will return `hi + 1` if no element is found that `==y`
* `bounds.eq` will return `-1` if no element matching `y` is found.
* `bounds.eq` will return the first found item with the given index.  It can be a little faster than the other methods if you just want to find some random match and do not care where it is.

## Credits
(c) 2013 Mikola Lysenko. MIT License