/**
 * https://en.wikipedia.org/wiki/CIE_1960_color_space
 *
 * Obsolete color space
 *
 * @module  color-space/ucs
 */
'use strict'

var xyz = require('./xyz');

var ucs = module.exports = {
	name: 'ucs',
	min: [0,0,0],
	max: [100, 100, 100],
	channel: ['U','V','W'],
	alias: ['UCS', 'cie1960']
};


/**
 * UCS to XYZ
 *
 * @param {Array} ucs XYZ values
 *
 * @return {Array} UCS values
 */
ucs.xyz = function(ucs) {
	var u = ucs[0],
		v = ucs[1],
		w = ucs[2];

	return [
		1.5 * u,
		v,
		1.5 * u - 3 * v + 2 * w
	];
};


/**
 * XYZ to UCS
 *
 * @param {Array} ucs UCS values
 *
 * @return {Array} XYZ values
 */
xyz.ucs = function(xyz) {
	var x = xyz[0],
		y = xyz[1],
		z = xyz[2];

	return [
		x * 2/3,
		y,
		0.5 * (-x + 3*y + z)
	];
};
