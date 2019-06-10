/**
 * YcCbcCrc is ITU-R BT.2020
 *
 * @module  color-space/yccbccrc
 */
'use strict'

var rgb = require('./rgb');
var ypbpr = require('./ypbpr');

var yccbccrc = module.exports = {
	name: 'yccbccrc',
	min: [0, -0.5, -0.5],
	max: [1, 0.5, 0.5],
	channel: ['Yc','Cbc','Crc'],
	alias: ['YcCbcCrc']
};


/**
 * YcCbcCrc to RGB
 *
 * @param {Array} yccbccrc RGB values
 *
 * @return {Array} YcCbcCrc values
 */
yccbccrc.rgb = function(yccbccrc) {
	return ypbpr.rgb(yccbccrc, 0.0593, 0.2627);
};


/**
 * RGB to YcCbcCrc
 *
 * @param {Array} yccbccrc YcCbcCrc values
 *
 * @return {Array} RGB values
 */
rgb.yccbccrc = function(arr) {
	return rgb.ypbpr(arr, 0.0593, 0.2627);
};
