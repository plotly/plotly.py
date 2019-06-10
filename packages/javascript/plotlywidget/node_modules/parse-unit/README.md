# parse-unit

[![stable](http://badges.github.io/stability-badges/dist/stable.svg)](http://github.com/badges/stability-badges)

Parses a number and unit string, eg `"20px"` into `[20, "px"]`. 

```js
var unit = require('parse-unit')

//prints [50, "gold"]
console.log( unit("50 gold") ) 
```

## Usage

[![NPM](https://nodei.co/npm/parse-unit.png)](https://nodei.co/npm/parse-unit/)

#### `parse(str[, out])`

Parses the string and its unit, returning an array containing the number and unit, separated. 

```
"-20 foo" => [-20, "foo"]
"5.5%" => [5.5, "%"]
5 => [5, ""]
"5" => [5, ""]
```

This will create a new array unless you specify an array to `out`, which allows you to re-use arrays. 

## License

MIT, see [LICENSE.md](http://github.com/mattdesl/parse-unit/blob/master/LICENSE.md) for details.
