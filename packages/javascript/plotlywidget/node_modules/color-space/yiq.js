/**
 * YIQ https://en.wikipedia.org/?title=YIQ
 *
 * @module  color-space/yiq
 */
'use strict'

var rgb = require('./rgb');

var yiq = module.exports = {
	name: 'yiq',
	min: [0,-0.5957,-0.5226],
	max: [1, 0.5957, 0.5226],
	channel: ['Y','I','Q'],
	alias: ['YIQ']
};

yiq.rgb = function(yiq) {
	var y = yiq[0],
		i = yiq[1],
		q = yiq[2],
		r, g, b;

	r = (y * 1) + (i *  0.956) + (q * 0.621);
	g = (y * 1) + (i * -0.272) + (q * -0.647);
	b = (y * 1) + (i * -1.108) + (q * 1.705);

	r = Math.min(Math.max(0, r), 1);
	g = Math.min(Math.max(0, g), 1);
	b = Math.min(Math.max(0, b), 1);

	return [r * 255, g * 255, b * 255];
};


//extend rgb
rgb.yiq = function(rgb) {
	var r = rgb[0] / 255,
		g = rgb[1] / 255,
		b = rgb[2] / 255;


	var y = (r * 0.299) + (g * 0.587) + (b * 0.114);
	var i = 0, q = 0;
	if (r !== g || g !== b) {
		i = (r * 0.596) + (g * -0.275) + (b * -0.321);
		q = (r * 0.212) + (g * -0.528) + (b * 0.311);
	}
	return [y, i, q];
};
