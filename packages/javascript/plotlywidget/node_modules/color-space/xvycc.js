/**
 * https://en.wikipedia.org/wiki/XvYCC
 *
 * Sony xvYCC is extended YCbCr
 *
 * It uses same transformation as
 * SD: ITU-R BT.601
 * HD: ITU-R BT.709
 *
 * But have extended mins/maxes, which (may) result in negative rgb values
 *
 * https://web.archive.org/web/20130524104850/http://www.sony.net/SonyInfo/technology/technology/theme/xvycc_01.html
 *
 * //TODO: look for a spec (120$) - there are xvYCC ←→ XYZ conversion formulas
 *
 * @module  color-space/xvycc
 */
'use strict'

var rgb = require('./rgb');
var ypbpr = require('./ypbpr');

var xvycc = module.exports = {
	name: 'xvycc',
	min: [0, 0, 0],
	max: [255, 255, 255],
	channel: ['Y','Cb','Cr'],
	alias: ['xvYCC']
};


/**
 * From analog to digital form.
 * Simple scale to min/max ranges
 *
 * @return {Array} Resulting digitized form
 */
ypbpr.xvycc = function (ypbpr) {
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
xvycc.ypbpr = function (xvycc) {
	var y = xvycc[0], cb = xvycc[1], cr = xvycc[2];

	return [
		(y - 16) / 219,
		(cb - 128) / 224,
		(cr - 128) / 224
	];
}


/**
 * xvYCC to RGB
 * transform through analog form
 *
 * @param {Array} xvycc RGB values
 *
 * @return {Array} xvYCC values
 */
xvycc.rgb = function (arr, kb, kr) {
	return ypbpr.rgb(xvycc.ypbpr(arr), kb, kr);
};


/**
 * RGB to xvYCC
 * transform through analog form
 *
 * @param {Array} xvycc xvYCC values
 *
 * @return {Array} RGB values
 */
rgb.xvycc = function(arr, kb, kr) {
	return ypbpr.xvycc(rgb.ypbpr(arr, kb, kr));
};
