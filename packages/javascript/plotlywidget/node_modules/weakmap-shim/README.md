# weakmap-shim

<!--
    [![build status][1]][2]
    [![NPM version][3]][4]
    [![Coverage Status][5]][6]
    [![gemnasium Dependency Status][7]][8]
    [![Davis Dependency status][9]][10]
-->

<!-- [![browser support][11]][12] -->

A minimal weakmap shim

## Example

```js
var weakMap = require("weakmap-shim")

var map = weakMap()
var key = {}

map.set(key, 'some value')
var v = map.get(key) // 'some value'
```

## create-store Example

```js
var createStore = require('weakmap-shim/create-store')

var store = createStore()
var key = {}

var value = store(key)

// `value` is weakly bound to `key`. `value` is a plain object
value.foo = 'bar'

var value2 = store(key)

var v = value2.foo; // 'bar'
var bool = value === value2; // true
```

## Motivation

Benvie has an excellent [weakmap](https://github.com/Benvie/WeakMap)
  module that's far more robust. However it contains quite a bit
  of loc.

 - `weakmap` : 7451 bytes
 - `weakmap-shim` : 2106 bytes
 - `weakmap-shim/create-store` : 1311 bytes

This module is only worthwhile if you want to add a weakmap to 
  a small module (10 - 30 loc) and dont want to bloat it with
  a heavier weakmap

## Installation

`npm install weakmap-shim`

## Contributors

 - Raynos

## MIT Licenced

  [1]: https://secure.travis-ci.org/Raynos/weakmap-shim.png
  [2]: https://travis-ci.org/Raynos/weakmap-shim
  [3]: https://badge.fury.io/js/weakmap-shim.png
  [4]: https://badge.fury.io/js/weakmap-shim
  [5]: https://coveralls.io/repos/Raynos/weakmap-shim/badge.png
  [6]: https://coveralls.io/r/Raynos/weakmap-shim
  [7]: https://gemnasium.com/Raynos/weakmap-shim.png
  [8]: https://gemnasium.com/Raynos/weakmap-shim
  [9]: https://david-dm.org/Raynos/weakmap-shim.png
  [10]: https://david-dm.org/Raynos/weakmap-shim
  [11]: https://ci.testling.com/Raynos/weakmap-shim.png
  [12]: https://ci.testling.com/Raynos/weakmap-shim
