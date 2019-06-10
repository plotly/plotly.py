# to-array-buffer [![unstable](https://img.shields.io/badge/stability-unstable-orange.svg)](http://github.com/badges/stability-badges) [![Build Status](https://img.shields.io/travis/dy/to-array-buffer.svg)](https://travis-ci.org/dy/to-array-buffer)

Turn any binary data container into an _ArrayBuffer_ in sync way. Detected containers:

* Buffer
* TypedArray
* ArrayBufferView
* ArrayBuffer
* data-uri string
* base64 string
* plain string
* Array
* Array of Arrays
* Number (creates new ArrayBuffer of the defined length in bytes)
* etc.

It also handles some custom data types, like `ImageData`, `AudioBuffer` etc., but in general it returns `null` for objects not looking like binary data containers. Note also that it does not handle _Blob_ and _File_, since they require async API.

[![npm install to-array-buffer](https://nodei.co/npm/to-array-buffer.png?mini=true)](https://npmjs.org/package/to-array-buffer/)

```js
var toArrayBuffer = require('to-array-buffer')
var context = require('audio-context')

// Get array buffer from any object
ab = toArrayBuffer(new Buffer(100))
ab = toArrayBuffer(new Float32Array(12))
ab = toArrayBuffer(dataURIstr)
ab = toArrayBuffer(base64str)
ab = toArrayBuffer(ndarray)
ab = toArrayBuffer([[0, 1, 0], [1, 0, 1]])
```

### Related

* [to-arraybuffer](https://www.npmjs.com/package/to-arraybuffer) − convert Buffer to ArrayBuffer, fast implementation.
* [data-uri-to-buffer](https://npmjs.org/package/data-uri-to-buffer) − advanced data-uri decoder.
* [save-file](https://github.com/dy/save-file) — save any input data to file in node/browser.
* [buffer-to-arraybuffer](https://npmjs.org/package/buffer-to-arraybuffer) — convert surely known Buffer datatype to ArrayBuffer.

© Dmitry Yv 2018. MIT Licensed.
