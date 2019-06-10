/**
 * YES color space
 * http://www.atlantis-press.com/php/download_paper.php?id=198
 *
 * @module color-space/yes
 */
'use strict'

var rgb = require('./rgb');

var yes = module.exports = {
	name: 'yes',
	min: [0,0,0],
	max: [1,1,1],
	channel: ['luminance', 'e-factor', 's-factor']
};


yes.rgb = function(arg){
	var y = arg[0], e = arg[1], s = arg[2];

	var m = [
		1, 1.431, .126,
		1, -.569, .126,
		1, .431, -1.874
	];

	var r = y * m[0] + e * m[1] + s * m[2],
		g = y * m[3] + e * m[4] + s * m[5],
		b = y * m[6] + e * m[7] + s * m[8];

	return [r*255, g*255, b*255];
};

rgb.yes = function(arg) {
	var r = arg[0] / 255, g = arg[1] / 255, b = arg[2] / 255;

	var m = [
		.253, .684, .063,
		.500, -.50, .0,
		.250, .250, -.5
	];

	return [
		r * m[0] + g * m[1] + b * m[2],
		r * m[3] + g * m[4] + b * m[5],
		r * m[6] + g * m[7] + b * m[8]
	];
};
