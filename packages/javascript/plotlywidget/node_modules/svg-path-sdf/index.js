'use strict'

var pathBounds = require('svg-path-bounds')
var parsePath = require('parse-svg-path')
var drawPath = require('draw-svg-path')
var isSvgPath = require('is-svg-path')
var bitmapSdf = require('bitmap-sdf')

var canvas = document.createElement('canvas')
var ctx = canvas.getContext('2d')


module.exports = pathSdf


function pathSdf (path, options) {
	if (!isSvgPath(path)) throw Error('Argument should be valid svg path string')

	if (!options) options = {}

	var w, h
	if (options.shape) {
		w = options.shape[0]
		h = options.shape[1]
	}
	else {
		w = canvas.width = options.w || options.width || 200
		h = canvas.height = options.h || options.height || 200
	}
	var size = Math.min(w, h)

	var stroke = options.stroke || 0

	var viewbox = options.viewbox || options.viewBox || pathBounds(path)
	var scale = [w / (viewbox[2] - viewbox[0]), h / (viewbox[3] - viewbox[1])]
	var maxScale = Math.min(scale[0] || 0, scale[1] || 0) / 2

	//clear ctx
	ctx.fillStyle = 'black'
	ctx.fillRect(0, 0, w, h)

	ctx.fillStyle = 'white'

	if (stroke)	{
		if (typeof stroke != 'number') stroke = 1
		if (stroke > 0) {
			ctx.strokeStyle = 'white'
		}
		else {
			ctx.strokeStyle = 'black'
		}

		ctx.lineWidth = Math.abs(stroke)
	}

	ctx.translate(w * .5, h * .5)
	ctx.scale(maxScale, maxScale)

	//if canvas svg paths api is available
	if (isPath2DSupported()) {
		var path2d = new Path2D(path)
		ctx.fill(path2d)
		stroke && ctx.stroke(path2d)
	}
	//fallback to bezier-curves
	else {
		var segments = parsePath(path)
		drawPath(ctx, segments)
		ctx.fill()
		stroke && ctx.stroke()
	}

	ctx.setTransform(1, 0, 0, 1, 0, 0);

	var data = bitmapSdf(ctx, {
		cutoff: options.cutoff != null ? options.cutoff : .5,
		radius: options.radius != null ? options.radius : size * .5
	})

	return data
}

var path2DSupported

function isPath2DSupported () {
	if (path2DSupported != null) return path2DSupported

	var ctx = document.createElement('canvas').getContext('2d')
	ctx.canvas.width = ctx.canvas.height = 1

	if (!window.Path2D) return path2DSupported = false

	var path = new Path2D('M0,0h1v1h-1v-1Z')

	ctx.fillStyle = 'black'
	ctx.fill(path)

	var idata = ctx.getImageData(0,0,1,1)

	return path2DSupported = idata && idata.data && idata.data[3] === 255
}
