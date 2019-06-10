# is-svg-path [![build](https://travis-ci.org/dfcreative/is-svg-path.svg?branch=master)](https://travis-ci.org/dfcreative/is-svg-path)

Test if a string is an SVG path.

[![npm install is-svg-path](https://nodei.co/npm/is-svg-path.png?mini=true)](https://npmjs.org/package/is-svg-path/)

```js
const isPath = require('is-svg-path')

isPath('M0 0L10 20 20 0Z') //true
isPath('M00Z') //false
isPath('xyz') //false
```

It does not validate path data nor covers edge cases like `'H0'` etc., but rather detects path in real world.
