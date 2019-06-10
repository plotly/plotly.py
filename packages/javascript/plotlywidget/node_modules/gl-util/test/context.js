'use strict'

let t = require('tape')
let context = require('../context')
let isBrowser = require('is-browser')
let createGl = require('gl')

t('context over context', t => {
	if (!isBrowser) return t.end()

	let gl = context()

	t.equal(gl, context(gl))

	t.end()
})

t('context container as string', t => {
	if (!isBrowser) return t.end()
	let canvas = document.body.appendChild(document.createElement('canvas'))
	canvas.id = 'canvas'
	let gl = context('#canvas')

	document.body.removeChild(canvas)

	t.end()
})

t('headless', t => {
	let gl = context(createGl(10, 10))

	t.equal(gl, context(gl))

	t.end()
})
