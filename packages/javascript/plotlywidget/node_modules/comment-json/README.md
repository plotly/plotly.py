[![NPM version](https://badge.fury.io/js/comment-json.svg)](http://badge.fury.io/js/comment-json)
[![Build Status](https://travis-ci.org/kaelzhang/node-comment-json.svg?branch=master)](https://travis-ci.org/kaelzhang/node-comment-json)
[![Dependency Status](https://david-dm.org/kaelzhang/node-comment-json.svg)](https://david-dm.org/kaelzhang/node-comment-json)

# comment-json

- Parse JSON strings with comments into JavaScript objects.
- stringify the objects into JSON strings with comments if there are.

The usage of `comment-json` is exactly the same as the vanilla [`JSON`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON) object.

## Install

```sh
$ npm install comment-json --save
```

## Usage

package.json:

```json
{
  // package name
  "name": "comment-json"
}
```

```js
var json = require('comment-json');
var fs = require('fs');
var obj = json.parse(fs.readFileSync('package.json').toString());
console.log(obj);
// ->
// {
//   "// name": [["// package name"]],
//   name: "comment-json"
// }

json.stringify(obj, null, 2); 
// Will be the same as package.json,
// which will be very useful if we use a json file to store configurations.
```

## json.parse(string, [reviver=null], [removes_comments=false])

The arguments are the same as the vanilla [`JSON.parse`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/parse), except for `removes_comments`:

- removes_comments `Boolean` If true, the comments won't be maintained, which is often used when we want to get a clean object.

Above all, `json.parse()` is not a parser with 100% accuracy to output an AST which describes every detail of the commented json, including the locations of every comments, whitespaces, etc.

But it DOES work, and could meet most of our requirements to record important informations as fast as possible without making everything too complicated. 

#### Let's jump into a much more integrated case:

code:

```js
/**
 block comment at the top
 */
// comment at the top
{
  // comment for a
  // comment line 2 for a
  /* block comment */
  "a": 1 // comment at right
}
// comment at the bottom
```

```js
var result = json.parse(code);
```

Then the `result` will be:

```js
{
  // Comments at the top of the file
  '//^': [
    '/**\n block comment at the top\n */', 
    '// comment at the top'
  ],

  // Comments at the bottom of the file
  '//$': ['// comment at the bottom'],

  // Comment for a property is the value of `'// <prop>'`
  '// a': [
    // Comments above property `a`
    [
      '// comment for a',
      '// comment line 2 for a',
      '/* block comment */'
    ],
    ['// comment at right']
  ],

  // The real value
  a: 1
}
```

#### If you want to strip comments

```js
json.parse(code, null, true);
// -> {a: 1}
```

**TL;NR**

There are two types of comments:
  - single line comment which starts with `//`
  - block comment which is wrapped by `/*` and `*/`

`//^`, is the array which contains comments at the top. If there are two lines of comments which start with `//`, they will be considered as two comment items in the array.

`//$`, similar to `//^`, is the comments at the bottom.

`// <key>`, is a two-dimensional array contains the comments for a certain property `key`.
  - the first item of the array is an array of the comments above the `key`
  - the second item is the comments at the right side of the `key`


## json.stringify(object, [replacer], [space])

The arguments are the same as the vanilla [`JSON.stringify`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify).

And it does the similar thing as the vanilla one, but also deal with extra properties and convert them into comments.

#### space

If space is not specified, or the space is an empty string, the result of `json.stringify()` will be no comments.

For the case above:

```js
console.log( json.stringify(result) ); // {"a":1}
console.log( json.stringify(result, null, 2) ); // is the same as `code`
```


<!-- ### json.strip(string)

Strips comments from `string`.

### json.clean(object)

Clean comment properties.

```js
var object = {
  "// name": "// package name",
  name: "comment-json"
};
json.clean(object); // {name: "comment-json"}
``` -->

## License

MIT
