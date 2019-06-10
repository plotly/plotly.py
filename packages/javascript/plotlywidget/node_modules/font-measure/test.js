'use strict'

let m = require('./')
let a = require('assert')


let fix = {
	top:0,
	bottom:1.125,
	lineHeight:1.125,
	alphabetic:0.890625,
	baseline:0.890625,
	middle:0.546875,
	median:0.546875,
	hanging:0.171875,
	ideographic:1.109375,
	upper:0.1875,
	capHeight:0.703125,
	lower:0.375,
	xHeight:0.515625,
	tittle:0.1875,
	ascent:0.1875,
	descent:1.09375,
	overshoot:0.015625
}

let res = m('sans-serif', {fontSize: 64})
a.deepEqual(m('sans-serif', {fontSize: 64}), fix)
a.deepEqual(m('sans-serif', {fontSize: 64, fontWeight: '700', fontStyle: 'italic'}), fix)
a.equal(m('sans-serif', {fontSize: 64, origin: 'baseline'}).baseline, 0)
