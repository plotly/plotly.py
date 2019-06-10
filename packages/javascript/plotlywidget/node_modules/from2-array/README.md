from2-array
===========

[![NPM](https://nodei.co/npm/from2-array.png?global=true)](https://nodei.co/npm/from2-array/)

[![Travis](http://img.shields.io/travis/binocarlos/from2-array.svg?style=flat)](https://travis-ci.org/binocarlos/from2-array)

Create a [from2](https://github.com/hughsk/from2) stream based on an array of source values

Useful when you want to create a Readable stream with some values you already have in an array

## example

```js
var from = require('from2-array')
var through = require('through2')

from.obj([{
  name:'a'
},{
  name:'b'
},{
  name:'c'
}]).pipe(through.obj(function(chunk, enc, cb){
	console.log('found: ' + chunk.name)
	cb()
}))

```

## license

MIT