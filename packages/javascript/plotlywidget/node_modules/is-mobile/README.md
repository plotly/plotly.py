
# is-mobile

Check if mobile browser, based on useragent string.

[![Build Status](https://travis-ci.org/juliangruber/is-mobile.svg?branch=master)](https://travis-ci.org/juliangruber/is-mobile)

## Example

```js
var mobile = require('is-mobile');

console.log(mobile());
// => false
```

## API

### mobile({ [ua], [tablet] })

Returns true if a mobile browser is being used.

If you don't specify `opts.ua` it will use `navigator.userAgent`.

To add support for tablets, set `tablet: true`.

`opts.ua` can also be an instance of a [node.js http request](http://nodejs.org/api/http.html#http_http_incomingmessage), in which
case it will reader the user agent header.

Example:

```js
var http = require('http');
var mobile = require('is-mobile');

var server = http.createServer(function (req, res) {
  res.end(mobile(req));
});

server.listen(8000);
```

## Installation

With [npm](https://npmjs.org) do:

```bash
npm install is-mobile
```

Bundle for the browser with
[browserify](https://github.com/substack/node-browserify).

## Kudos

Taken from [detectmobilebrowsers.com](http://detectmobilebrowsers.com/).

## License

(MIT)

Copyright (c) 2013 Julian Gruber &lt;julian@juliangruber.com&gt;

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
