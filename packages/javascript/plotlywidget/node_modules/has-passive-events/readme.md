# has-passive-events  [![unstable](https://img.shields.io/badge/stability-unstable-green.svg)](http://github.com/badges/stability-badges) [![Build Status](https://img.shields.io/travis/dfcreative/has-passive-events.svg)](https://travis-ci.org/dfcreative/has-passive-events)

Check if event listener options are available on the current device. [Try it out](http://dfcreative.github.io/has-passive-events/).

[![npm install has-passive-events](https://nodei.co/npm/has-passive-events.png?mini=true)](https://npmjs.org/package/has-passive-events/)

```js
const hasPassive = require('has-passive-events')

hasPassive ? element.addEventListener('wheel', handler, {passive: true}) : element.addEventListener('wheel', handler)
```

If you find edge case, please address [issues](https://github.com/dfcreative/has-passive-events/issues).
