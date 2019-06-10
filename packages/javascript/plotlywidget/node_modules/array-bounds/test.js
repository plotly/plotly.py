'use strict'

const bounds = require('./')
const assert = require('assert')

let a = [-Infinity, -1, 0, 1, Infinity]
assert.deepEqual(bounds(a), [-Infinity, Infinity])

let b = [0, .5, 1]
assert.deepEqual(bounds(b), [0, 1])

let c = [0, 50, 100]
assert.deepEqual(bounds(c), [0, 100])

let d = [0, 0, .1, .2, 1, 2]
assert.deepEqual(bounds(d, 2), [0, 0, 1, 2])

let e = [-1, -2, -3, 0, 0, 0, 3, 2, 1]
assert.deepEqual(bounds(e, 3), [-1, -2, -3, 3, 2, 1])
