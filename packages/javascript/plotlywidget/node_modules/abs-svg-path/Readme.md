
# abs-svg-path

  redefine an svg path with absolute coordinates

## Installation

_With [packin](//github.com/jkroso/packin) or [component](//github.com/component/component)_

    $ packin add jkroso/abs-svg-path

then in your app:

```js
var abs = require('abs-svg-path')
```

## API

### abs(path)

  redefine `path` with absolute coordinates

```js
abs([['l',10,20],['l',30,40]]) // => [['L',10,20],['L',40,60]]
abs([
  ['q', 1,2, 33,44],
  ['L', 50,60],
  ['c', 1,2, 3,4, 33,44]
]) // => [['Q',1,2,33,44],['L', 50, 60],['C',51,62, 53,64, 83,104]]
```

## Running the tests

Just run `make test`
