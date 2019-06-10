# add-line-numbers

[![stable](http://badges.github.io/stability-badges/dist/stable.svg)](http://github.com/badges/stability-badges)

Adds line numbers to a source string, padding left and starting at the given offset.

## Example

#### example.js

```js
var addLineNumbers = require('add-line-numbers')
var stdin = require('get-stdin')

stdin(function (body) {
  var src = addLineNumbers(body.toString())
  process.stdout.write(src + '\n')
})
```

Now run the following in bash:

```sh
node example.js < some-file.js
```

Resulting output:

```js
 1: var addLineNumbers = require('./')
 2: var test = require('tape')
 3: 
 4: test('adds line numbers to a source string', function (t) {
 5:   t.equal(addLineNumbers([
 6:     'one',
 7:     'is second'
 8:   ].join('\r\n')), '1: one\n2: is second', 'return carriage')
 9: 
10:   t.equal(addLineNumbers([
11:     'one',
12:     'is second'
13:   ].join('\n'), 0), '0: one\n1: is second', 'start offset')
14: 
...
```

## Usage

[![NPM](https://nodei.co/npm/add-line-numbers.png)](https://www.npmjs.com/package/add-line-numbers)

#### `str = addLineNumbers(str, start, delimiter)`

Adds a number to the start of each line in the `str` text. 

- `start` (Number) number to start counting at, defaults to 1
- `delimiter` (String) joins the number and line, defaults to `": "`

Returns the transformed string.

## License

MIT, see [LICENSE.md](http://github.com/Jam3/add-line-numbers/blob/master/LICENSE.md) for details.
