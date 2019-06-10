[![NPM version](https://badge.fury.io/js/json-parser.svg)](http://badge.fury.io/js/json-parser)
[![Build Status](https://travis-ci.org/kaelzhang/node-json-parser.svg?branch=master)](https://travis-ci.org/kaelzhang/node-json-parser)
<!-- [![Dependency Status](https://david-dm.org/kaelzhang/node-json-parser.svg)](https://david-dm.org/kaelzhang/node-json-parser) -->

# json-parser

JSON parser to parse JSON object and MAINTAIN comments.

This is a very low level module. For most situations, recommend to use [`comment-json`](https://www.npmjs.org/package/comment-json) instead.

## Install

```sh
$ npm install json-parser --save
```

## Usage

```js
parser(text, [reviver=null,] [remove_comments=false])
```

- text `String` The string to parse as JSON. See the [JSON](http://json.org/) object for a description of JSON syntax.
- reviver `function()|null` Default to `null`. It acts the same as the second parameter of [`JSON.parse`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/parse). If a function, prescribes how the value originally produced by parsing is transformed, before being returned.
- remove_comments `Boolean` If true, the parsed JSON Object won't contain comments

Returns the `Object` corresponding to the given JSON text.

content

```js
/**
 blah
 */
// comment at top
{
  // comment for a
  /* block comment */
  "a": 1 // comment at right
}
// comment at bottom
```

```js
var parser = require('json-parser');
var object = parser.parse(content);
console.log(object);
```

And the result will be:

```js
{
  // Comments at the top of the file
  '//^': ['/**\n blah\n */', '// comment at top'],

  // Comments at the bottom of the file
  '//$': ['// comment at bottom'],

  // Comment for a property is the value of `'// <prop>'`
  '// a': [
    ['// comment for a', '/* block comment */'],
    ['// comment at right']
  ],

  // The real value
  a: 1
}
```

```js
var object_no_comments = parser.parse(content, null, true);
console.log(object_no_comments)
```

And the result will be:

```js
{
  a: 1
}
```

## License

MIT
