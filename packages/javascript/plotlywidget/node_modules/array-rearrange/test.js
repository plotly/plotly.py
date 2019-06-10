'use strict'

var reorder = require('./')
var range = require('array-range')
var assert = require('assert')



assert.deepEqual(reorder([4,3,2,1], [3,2,1,0]), [1,2,3,4])
assert.deepEqual(reorder([4,4, 3,3, 2,2, 1,1], [3,2,1,0], 2), [1,1, 2,2, 3,3, 4,4])
assert.deepEqual(reorder([4,4, 3,3, 2,2, 1,1], [3,2,1,0]), [1,1, 2,2, 3,3, 4,4])
assert.deepEqual(reorder([0,0,1,1,2,2,3,3,4,4,5,5,6,6,7,7], [0,1,4,2,5,6,3,7]), [0,0,1,1,4,4,2,2,5,5,6,6,3,3,7,7])

assert.deepEqual(reorder([0,1,2], [2,0,1]), [2,0,1])

assert.deepEqual(reorder(['A','B','C','D'], [3,0,2,1]), ['D','A','C','B'])


// perf
let N = 1e6
let a = Array.from({length: N}, Math.random)
let idx = Array.from({length: N}, (v, i) => (N - i - 1))

console.time(1)
reorder(a, idx.slice())
console.timeEnd(1)

let _a = new Float64Array(a)
console.time(2)
let b = new Float64Array(N)
for (let i = 0; i < N; i++) {
	b[i] = a[idx[i]]
}
_a.set(b)
console.timeEnd(2)
