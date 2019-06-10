# is-base64

> Predicate that returns true if base64 string.

# Install

```bash
npm install is-base64
```

# Usage

```javascript
var isBase64 = require('is-base64');

var string = 'iVBORw0KGgoAAAAN ... kSuQmCC';
var stringWithMime = 'data:image/png;base64,iVBORw0KGgoAAAA ... AAElFTkSuQmCC';

console.log(isBase64(string)); // true
console.log(isBase64(stringWithMime)); // false
console.log(isBase64(stringWithMime, {mime: true})); // true
console.log(isBase64('1342234')); // false
console.log(isBase64('afQ$%rfew')); // false
console.log(isBase64('dfasdfr342')); // false
console.log(isBase64('uuLMhh==')); // true
console.log(isBase64('uuLMhh')); // false
console.log(isBase64('uuLMhh', {paddingRequired: false})); // true
console.log(isBase64('')); // true
console.log(isBase64('', {allowBlank: false})); // false
```

# API

## isBase64(string, options)

- {string} string - string to check if is valid base64 string

- {object} [options]
    - [options.paddingRequired=true] {boolean} - check for padding
    - [options.mime=false] {boolean} - returns true for valid strings with mime
    - [options.allowBlank=true] {boolean} - returns true for empty string

# License

MIT
