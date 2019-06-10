# is-string-blank

The fast way to check if a JS string is blank?

### Install

```
npm install is-string-blank
```

### API

```js
var isStringBlank = require('is-string-blank');

isStringBlank(/* any JS object */);
```

### Why?

In [plotly](https://plot.ly/)'s javascript graphing library
[plotly.js](https://plot.ly/javascript/) blank strings should be identified to be ignored e.g. by webgl. 
`is-string-blank` is significantly simplified and sped up

### Author

Alex Johnson | https://github.com/alexcjohnson

### License

Copyright (c) 2015 Alex Johnson Released under the MIT license.
