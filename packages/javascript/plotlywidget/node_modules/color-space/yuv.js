/**
 * YUV https://en.wikipedia.org/?title=YUV
 *
 * @module  color-space/yuv
 */
'use strict'

var rgb = require('./rgb');

var yuv = module.exports = {
	name: 'yuv',
	min: [0,-0.5,-0.5],
	max: [1, 0.5, 0.5],
	channel: ['Y','U','V'],
	alias: ['YUV', 'EBU'],

};

yuv.rgb = function(yuv) {
	var y = yuv[0],
		u = yuv[1],
		v = yuv[2],
		r, g, b;

	r = (y * 1) + (u *  0) + (v * 1.13983);
	g = (y * 1) + (u * -0.39465) + (v * -0.58060);
	b = (y * 1) + (u * 2.02311) + (v * 0);

	r = Math.min(Math.max(0, r), 1);
	g = Math.min(Math.max(0, g), 1);
	b = Math.min(Math.max(0, b), 1);

	return [r * 255, g * 255, b * 255];
}


//extend rgb
rgb.yuv = function(rgb) {
	var r = rgb[0] / 255,
		g = rgb[1] / 255,
		b = rgb[2] / 255;

	var y = (r * 0.299) + (g * 0.587) + (b * 0.114);
	var u = (r * -0.14713) + (g * -0.28886) + (b * 0.436);
	var v = (r * 0.615) + (g * -0.51499) + (b * -0.10001);

	return [y, u, v];
};
