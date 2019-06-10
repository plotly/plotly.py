/**
 * https://en.wikipedia.org/?title=YDbDr
 *
 * @module  color-space/ydbdr
 */
'use strict'

var rgb = require('./rgb');
var yuv = require('./yuv');

var ydbdr = module.exports = {
	name: 'ydbdr',
	min: [0,-1.333,-1.333],
	max: [1, 1.333, 1.333],
	channel: ['Y','Db','Dr'],
	alias: ['YDbDr']
};


/**
 * YDbDr to RGB
 *
 * @param {Array} ydbdr RGB values
 *
 * @return {Array} YDbDr values
 */
ydbdr.rgb = function(ydbdr) {
	var y = ydbdr[0], db = ydbdr[1], dr = ydbdr[2];

	var r = y + 0.000092303716148*db - 0.525912630661865*dr;
	var g = y - 0.129132898890509*db + 0.267899328207599*dr;
	var b = y + 0.664679059978955*db - 0.000079202543533*dr;

	return [r*255, g*255, b*255];
};


/**
 * RGB to YDbDr
 *
 * @param {Array} ydbdr YDbDr values
 *
 * @return {Array} RGB values
 */
rgb.ydbdr = function(rgb) {
	var r = rgb[0]/255, g = rgb[1]/255, b = rgb[2]/255;
	return [
		0.299*r + 0.587*g + 0.114*b,
		-0.450*r - 0.883*g + 1.333*b,
		-1.333*r + 1.116*g + 0.217*b
	];
};


/**
 * To YUV
 */
yuv.ydbdr = function (yuv) {
	return [
		yuv[0], 3.059*yuv[1], -2.169*yuv[2]
	]
};

/**
 * From YUV
 */
ydbdr.yuv = function (ydbdr) {
	return [
		ydbdr[0], ydbdr[1] / 3.059, -ydbdr[2] / 2.169
	]
};
