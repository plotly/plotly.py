'use strict'

var Scatter = require('./scatter')
var extend = require('object-assign')

module.exports = function (regl, options) {
	var scatter = new Scatter(regl, options)

	var render = scatter.render.bind(scatter)

	// expose API
	extend(render, {
		render: render,
		update: scatter.update.bind(scatter),
		draw: scatter.draw.bind(scatter),
		destroy: scatter.destroy.bind(scatter),
		regl: scatter.regl,
		gl: scatter.gl,
		canvas: scatter.gl.canvas,
		groups: scatter.groups,
		markers: scatter.markerCache,
		palette: scatter.palette
	})

	return render
}
