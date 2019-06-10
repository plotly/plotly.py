'use strict'

require('enable-mobile')
const createErrors = require('./')
const panZoom = require('pan-zoom')
const fps = require('fps-indicator')({css:`padding: 1.4rem`})
const random = require('gauss-random')
const rgba = require('color-rgba')
const nanoraf = require('nanoraf')
const palettes = require('nice-color-palettes')
const regl = require('regl')({extensions: 'angle_instanced_arrays'})


let N = 1e3
let ratio = window.innerWidth / window.innerHeight
let range = [ -10 * ratio, -10, 10 * ratio, 10 ]
let colors = palettes[ Math.floor(Math.random() * palettes.length) ]


var positions = new Float64Array(2 * N)
var errors = new Float32Array(4 * N)
for(var i=0; i<2*N; ++i) {
	positions[i] = random() //i * 4 / N
	errors[i*2] = Math.random() / 2 //1
	errors[i*2+1] = Math.random() / 2 //1
}

let drawErrors = createErrors(regl, {
	positions: positions,
	errors: errors,

	// positions: [0,0, 10,10, -10,-10],
	// errors: [0,0,0,0, 0,0,0,0, 0,0,0,0],

	capSize: 10,
	lineWidth: 1,

	color: Array(N).fill(0).map(() => colors[Math.floor(Math.random() * colors.length)]),
	// color: 'rgba(0, 0, 127, 1)',

	range: range
})

drawErrors()


//interactions
let prev = null
var frame = nanoraf(drawErrors)

let cnv = document.body.querySelectorAll('canvas')[1]

panZoom(cnv, e => {
	let w = cnv.offsetWidth
	let h = cnv.offsetHeight

	let rx = e.x / w
	let ry = e.y / h

	let xrange = range[2] - range[0],
		yrange = range[3] - range[1]

	if (e.dz) {
		let dz = e.dz / w
		range[0] -= rx * xrange * dz
		range[2] += (1 - rx) * xrange * dz

		range[1] -= (1 - ry) * yrange * dz
		range[3] += ry * yrange * dz
	}

	range[0] -= xrange * e.dx / w
	range[2] -= xrange * e.dx / w
	range[1] += yrange * e.dy / h
	range[3] += yrange * e.dy / h

	let state = {range: range}
	frame(state, prev)
	prev = state
})


window.addEventListener('resize', () => {
	drawErrors()
})
