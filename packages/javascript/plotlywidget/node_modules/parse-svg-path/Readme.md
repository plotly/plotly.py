
# parse-svg-path

  A minimal svg path parser. For the delux model see [hughsk/svg-path-parser](//github.com/hughsk/svg-path-parser) or for the streaming model see [nfroidure/SVGPathData](//github.com/nfroidure/SVGPathData).

## Installation

- [packin](//github.com/jkroso/packin): `packin add jkroso/parse-svg-path`
- [component](//github.com/component/component#installing-packages): `component install jkroso/parse-svg-path`
- [npm](//npmjs.org/doc/cli/npm-install.html): `npm install parse-svg-path`

then in your app:

```js
var parse = require('parse-svg-path')
```

## API

### parse(string)

  parse an svg path data string. Generates an Array
  of commands where each command is an Array of the
  form `[command, arg1, arg2, ...]`

```js
parse('m1 2 3 4') // => [['m',1,2],['l',3,4]]
```

## Running the tests

Just run `make` and navigate your browser to the test directory.
