/**
 * @module color-space/cmy
 */
'use strict'

var rgb = require('./rgb');

var cmy = module.exports = {
	name: 'cmy',
	min: [0,0,0],
	max: [100,100,100],
	channel: ['cyan', 'magenta', 'yellow'],
	alias: ['CMY']
};


/**
 * CMY to RGB
 *
 * @param {Array} cmy Channels
 *
 * @return {Array} RGB channels
 */
cmy.rgb = function(cmy) {
	var c = cmy[0] / 100,
		m = cmy[1] / 100,
		y = cmy[2] / 100;

	return [
		(1 - c) * 255,
		(1 - m) * 255,
		(1 - y) * 255
	];
};


/**
 * RGB to CMY
 *
 * @param {Array} rgb channels
 *
 * @return {Array} CMY channels
 */
rgb.cmy = function(rgb) {
	var r = rgb[0] / 255,
		g = rgb[1] / 255,
		b = rgb[2] / 255;

	return [
		(1-r) * 100 || 0,
		(1-g) * 100 || 0,
		(1-b) * 100 || 0
	];
};
