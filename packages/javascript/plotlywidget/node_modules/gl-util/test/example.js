'use strict'

const {program, attribute, uniform, context, texture} = require('../')
const assert = require('assert')

document.body.style.margin = 0

let gl = context({
	attributes: {preserveDrawingBuffer: false}
})

let attrs = gl.getContextAttributes();
assert.equal(false, attrs.preserveDrawingBuffer);

let p1 = program(gl, `
	precision mediump float;

	attribute vec2 position;

	void main() {
		gl_Position = vec4(position * 2. - 1., 0., 1.);
	}
`, `
	precision mediump float;

	uniform vec4 color;

	void main () {
		gl_FragColor = color;
	}
`);

let p2 = program(gl, `
	precision mediump float;

	attribute vec3 position;

	void main() {
		gl_Position = vec4(position * 2. - 1., 1.);
	}
`, `
	precision mediump float;

	uniform vec3 color;

	void main () {
		gl_FragColor = vec4(color, 1.);
	}
` )

let p3 = program(gl, `
	precision mediump float;

	attribute vec2 position;

	void main() {
		gl_Position = vec4(position * 2. - 1., 0., 1.);
	}
`, `
	precision mediump float;

	uniform sampler2D color;
	uniform vec4 viewport;
	uniform float x;

	void main () {
		vec2 coord = (gl_FragCoord.xy - viewport.xy) / viewport.zw;
		gl_FragColor = texture2D(color, coord);
	}
`)

program(gl, p1)
attribute(gl, 'position', {data: [0,0,1,0,0,1]});
uniform(gl, 'color', [1, .2, 0, 1.]);

gl.drawArrays(gl.TRIANGLES, 0, 3);

setTimeout(() => {
	program(gl, p2);
	attribute(gl, 'position', {data: [0,0,0,.5,0,0,0,.5,0]});
	uniform(gl, 'color', [.8, .9, 0])
	gl.drawArrays(gl.TRIANGLES, 0, 3);

	setTimeout(() => {
		program(gl, p3);
		uniform(gl, 'x', 1);
		attribute(gl, 'position', {data: [0,0,1,0,0,1]});
		texture(gl, 'color', './texture.gif');
		uniform(gl, 'viewport', [0,0,gl.drawingBufferWidth, gl.drawingBufferHeight]);
		setTimeout(() => {
			gl.drawArrays(gl.TRIANGLES, 0, 3);
		}, 100)
	}, 500)
}, 500);
