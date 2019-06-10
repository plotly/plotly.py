# parenthesis [![Build Status](https://travis-ci.org/dy/parenthesis.svg?branch=master)](https://travis-ci.org/dy/parenthesis)

Parse parentheses from a string, return folded arrays.

[![npm install parenthesis](https://nodei.co/npm/parenthesis.png?mini=true)](https://npmjs.org/package/parenthesis/)


```js
var parse = require('parenthesis')

// Parse into nested format
parse('a(b[c{d}])')
// ['a(', ['b[', ['c{', ['d'], '}'], ']'], ')']

// Parse into flat format with cross-references
parse('a(b[c{d}])', {
	brackets: ['()'],
	escape: '\\',
	flat: true
})
// ['a(\\1)', 'b[c{d}]']


// Stringify nested format
parse.stringify(['a(', ['b[', ['c{', ['d'], '}'], ']'], ')'])
// 'a(b[c{d}])'

// Stringify flat format with cross-references
parse.stringify(['a(\\1)', 'b[c{d}]'], {flat: true, escape: '\\'})
// 'a(b[c{d}])'
```

## API

### tokens = paren.parse(string, brackets|opts?)

Return array with tokens.

Option | Default | Meaning
---|---|---
`brackets` | `['{}', '[]', '()']` | Single brackets string or list of strings to detect brackets. Can be repeating brackets eg. `"" or ''`.
`escape` | `'___'` | Escape prefix for flat references.
`flat` | `false` | Return flat array instead of nested arrays.

### str = paren.stringify(tokens, {flat}?)

Stringify tokens back. Pass `{flat: true}` flag for flat tokens array.

## Related

* [balanced-match](http://npmjs.org/package/balanced-match)


## License

© 2018 Dmitry Yv. MIT License
