'use strict'

const parseRect = require('./')
const assert = require('assert')

var res = {x: 10, y: 20, width: 90, height: 80}
assert.deepEqual(parseRect('10 20 100 100'), res)
assert.deepEqual(parseRect(10, 20, 100, 100), res)
assert.deepEqual(parseRect([10, 20, 100, 100]), res)
assert.deepEqual(parseRect({ x: 10, y: 20, width: 90, height: 80 }), res)
assert.deepEqual(parseRect({ x: 10, y: 20, w: 90, h: 80 }), res)
assert.deepEqual(parseRect({ l: 10, t: 20, r: 100, b: 100 }), res)
assert.deepEqual(parseRect({ left: 10, top: 20, right: 100, bottom: 100 }), res)

var res = {x: 0, y: 0, width: 90, height: 80}
assert.deepEqual(parseRect({ width: 90, height: 80 }), res)

assert.deepEqual(parseRect([10, 20]), {width: 10, height: 20, x: 0, y: 0})
assert.deepEqual(parseRect(10), {width: 10, height: 10, x: 0, y: 0})
assert.deepEqual(parseRect([10]), {width: 10, height: 10, x: 0, y: 0})
