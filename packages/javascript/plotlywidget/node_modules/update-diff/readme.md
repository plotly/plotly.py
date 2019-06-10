# update-diff [![unstable](https://img.shields.io/badge/stability-unstable-green.svg)](http://github.com/badges/stability-badges)

Update object by mapping differences in order. Comes handy for organizing state updating.

[![npm install update-diff](https://nodei.co/npm/update-diff.png?mini=true)](https://npmjs.org/package/update-diff/)

```js
let prop = require('update-diff')

let state = {propA: 0, propB: 1, propC: ['foo'], propD: 'bar'}

updateDiff(state, modifications, [
//initial mapping
{
	propA: value => value,
	propB: true,
	propC: Array.isArray
},
//second-pass mapping
{
	propX: (x, state) => state.propB + x
},
//third-pass mapping
{
	propA: (value, state) => state.propA ? 'a' : 'b'
}
])

// {propB: 1, propC: ['foo']}
```

## Related

* [obj-map-prop](https://github.com/dfcreative/obj-map-prop) − map object properties by a dict
* [map-obj](https://github.com/sindresorhus/map-obj) − map properties by single function
* [filter-obj](https://github.com/sindresorhus/filter-obj) − filter properties by single function


## Credits

© 2017 Dima Yv. MIT License
