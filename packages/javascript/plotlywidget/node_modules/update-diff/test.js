'use strict'

let updateDiff = require('./')

let assert = require('assert')

assert.deepEqual(updateDiff({}, {
	a: '100.1',
	b: undefined,
	c: null,
	d: 1,
	e: ['foo'],
	f: 'bar'
}, {
	a: parseFloat,
	b: true,
	c: false,
	e: x => x[0],
	d: f => f
}), {
	a: 100.1,
	b: undefined,
	d: 1,
	e: 'foo'
})

