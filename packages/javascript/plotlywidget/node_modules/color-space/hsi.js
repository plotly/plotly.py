/**
 * http://www.cse.usf.edu/~mshreve/rgb-to-hsi
 * http://web.archive.org/web/20130124054245/http://web2.clarkson.edu/class/image_process/RGB_to_HSI.pdf
 *
 * @module color-space/hsl
 */
'use strict'

var rgb = require('./rgb');

var loop = require('mumath/mod');
var clamp = require('mumath/clamp');


var hsi = module.exports = {
	name: 'hsi',
	min: [0,0,0],
	max: [360,100,255],
	channel: ['hue', 'saturation', 'intensity'],
	alias: ['HSI']
};


/**
 * HSI to RGB
 *
 * @param {Array} hsi Channel values
 *
 * @return {Array} RGB channel values
 */
hsi.rgb = function (hsi) {
	var h = loop(hsi[0], 0, 360) * Math.PI / 180;
	var s = clamp(hsi[1], 0, 100) / 100;
	var i = clamp(hsi[2], 0, 255) / 255;

	var pi3 = Math.PI / 3;

	var r, g, b;
	if (h < (2 * pi3) ) {
		b = i * ( 1 - s );
		r = i * (1 + ( s * Math.cos(h) / Math.cos(pi3 - h) ));
		g = i * (1 + ( s * ( 1 - Math.cos(h) / Math.cos(pi3 - h) )));
	}
	else if (h < (4 * pi3) ) {
		h = h - 2 * pi3;
		r = i * ( 1 - s );
		g = i * (1 + ( s * Math.cos(h) / Math.cos(pi3 - h) ));
		b = i * (1 + ( s * ( 1 - Math.cos(h) / Math.cos(pi3 - h) )));
	}
	else {
		h = h - 4 * pi3;
		g = i * ( 1 - s );
		b = i * (1 + ( s * Math.cos(h) / Math.cos(pi3 - h) ));
		r = i * (1 + ( s * ( 1 - Math.cos(h) / Math.cos(pi3 - h) )));
	}

	return [r * 255, g * 255, b * 255];
};


/**
 * RGB to HSI
 *
 * @param {Array} rgb Channel values
 *
 * @return {Array} HSI channel values
 */
rgb.hsi = function (rgb) {
	var sum = rgb[0] + rgb[1] + rgb[2];

	var r = rgb[0] / sum;
	var g = rgb[1] / sum;
	var b = rgb[2] / sum;

	var h = Math.acos(
		( 0.5 * ((r - g) + (r - b)) ) /
		Math.sqrt( (r - g)*(r - g) + (r - b)*(g - b) )
	);
	if (b > g) {
		h = 2 * Math.PI - h;
	}

	var s = 1 - 3 * Math.min(r, g, b);

	var i = sum / 3;

	return [h * 180 / Math.PI, s * 100, i];
};
