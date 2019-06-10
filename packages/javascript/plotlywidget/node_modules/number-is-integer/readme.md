# number-is-integer [![Build Status](https://travis-ci.org/sindresorhus/number-is-integer.svg?branch=master)](https://travis-ci.org/sindresorhus/number-is-integer)

> ES2015 [`Number.isInteger()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/isInteger) [ponyfill](https://ponyfill.com)


## Install

```
$ npm install --save number-is-integer
```


## Usage

```js
var numberIsInteger = require('number-is-integer');

numberIsInteger(1);
//=> true

numberIsInteger(1.5);
//=> false
```


## Related

- [is-safe-integer](https://github.com/sindresorhus/is-safe-integer) - ES2015 `Number.isSafeInteger()` ponyfill
- [number-is-float](https://github.com/sindresorhus/number-is-float) - Check if something is a float


## License

MIT © [Sindre Sorhus](http://sindresorhus.com)
