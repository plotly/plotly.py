/**
 * https://en.wikipedia.org/?title=YCgCo
 *
 * @module  color-space/ycgco
 */
'use strict'

var rgb = require('./rgb');

var ycgco = module.exports = {
	name: 'ycgco',
	min: [0, -0.5, -0.5],
	max: [1, 0.5, 0.5],
	channel: ['Y','Cg','Co'],
	alias: ['YCgCo']
};


/**
 * YCgCo to RGB
 * transform through analog form
 *
 * @param {Array} ycgco RGB values
 *
 * @return {Array} YCgCo values
 */
ycgco.rgb = function (arr) {
	var y = arr[0], cg = arr[1], co = arr[2];

	var tmp = y - cg;

	return [
		(tmp + co)*255,
		(y + cg)*255,
		(tmp - co)*255
	];
};


/**
 * RGB to YCgCo
 * transform through analog form
 *
 * @param {Array} ycgco YCgCo values
 *
 * @return {Array} RGB values
 */
rgb.ycgco = function(arr) {
	var r = arr[0]/255, g = arr[1]/255, b = arr[2]/255;

	return [
		0.25*r + 0.5*g + 0.25*b,
		-0.25*r + 0.5*g - 0.25*b,
		0.5*r - 0.5*b
	];
};
