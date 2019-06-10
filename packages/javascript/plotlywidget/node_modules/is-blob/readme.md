# is-blob [![Build Status](https://travis-ci.org/sindresorhus/is-blob.svg?branch=master)](https://travis-ci.org/sindresorhus/is-blob)

> Check if a value is a [Blob](https://developer.mozilla.org/en/docs/Web/API/Blob) - File-like object of immutable, raw data

*`Blob` is only available in the browser. In Node.js it always returns `false`.*


## Install

```
$ npm install is-blob
```


## Usage

```js
const isBlob = require('is-blob');

isBlob(new Blob(['<h1>Unicorns</h1>'], {type: 'text/html'}));
//=> true
```


## License

MIT © [Sindre Sorhus](https://sindresorhus.com)
