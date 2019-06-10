/**
 * https://en.wikipedia.org/?title=YCbCr
 *
 * YCbCr is a digital form of YPbPr conversion
 * Thence limits are [16...235], according to the ITU-R BT.709 or ITU-R BT.601
 *
 * @module  color-space/ycbcr
 */
'use strict'

var rgb = require('./rgb');
var ypbpr = require('./ypbpr');

var ycbcr = module.exports = {
	name: 'ycbcr',
	min: [16, 16, 16],
	max: [235, 240, 240],
	channel: ['Y','Cb','Cr'],
	alias: ['YCbCr', 'YCC']
};


/**
 * From analog to digital form.
 * Simple scale to min/max ranges
 *
 * @return {Array} Resulting digitized form
 */
ypbpr.ycbcr = function (ypbpr) {
	var y = ypbpr[0], pb = ypbpr[1], pr = ypbpr[2];

	return [
		16 + 219 * y,
		128 + 224 * pb,
		128 + 224 * pr
	];
}


/**
 * From digital to analog form.
 * Scale to min/max ranges
 */
ycbcr.ypbpr = function (ycbcr) {
	var y = ycbcr[0], cb = ycbcr[1], cr = ycbcr[2];

	return [
		(y - 16) / 219,
		(cb - 128) / 224,
		(cr - 128) / 224
	];
}


/**
 * YCbCr to RGB
 * transform through analog form
 *
 * @param {Array} ycbcr RGB values
 *
 * @return {Array} YCbCr values
 */
ycbcr.rgb = function (arr, kb, kr) {
	return ypbpr.rgb(ycbcr.ypbpr(arr), kb, kr);
};


/**
 * RGB to YCbCr
 * transform through analog form
 *
 * @param {Array} ycbcr YCbCr values
 *
 * @return {Array} RGB values
 */
rgb.ycbcr = function(arr, kb, kr) {
	return ypbpr.ycbcr(rgb.ypbpr(arr, kb, kr));
};
