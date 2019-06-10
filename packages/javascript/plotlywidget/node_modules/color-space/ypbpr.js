/**
 * https://en.wikipedia.org/?title=YPbPr
 *
 * YPbPr is analog form of YCbCr
 * hence limits are [0..1]
 *
 * Default conversion is ITU-R BT.709
 *
 * @module  color-space/ypbpr
 */
'use strict'

var rgb = require('./rgb');

var ypbpr = module.exports = {
	name: 'ypbpr',
	min: [0,-0.5,-0.5],
	max: [1, 0.5, 0.5],
	channel: ['Y','Pb','Pr'],
	alias: ['YPbPr', 'Y/PB/PR', 'YPRPB', 'PRPBY', 'PBPRY', 'Y/Pb/Pr', 'YPrPb', 'PrPbY', 'PbPrY', 'Y/R-Y/B-Y', 'Y(R-Y)(B-Y)', 'R-Y', 'B-Y']
};


/**
 * YPbPr to RGB
 *
 * @param {Array} ypbpr RGB values
 *
 * @return {Array} YPbPr values
 */
ypbpr.rgb = function(ypbpr, kb, kr) {
	var y = ypbpr[0], pb = ypbpr[1], pr = ypbpr[2];

	//default conversion is ITU-R BT.709
	kb = kb || 0.0722;
	kr = kr || 0.2126;

	var r = y + 2 * pr * (1 - kr);
	var b = y + 2 * pb * (1 - kb);
	var g = (y - kr * r - kb * b) / (1 - kr - kb);

	return [r*255,g*255,b*255];
};


/**
 * RGB to YPbPr
 *
 * @param {Array} ypbpr YPbPr values
 *
 * @return {Array} RGB values
 */
rgb.ypbpr = function(rgb, kb, kr) {
	var r = rgb[0]/255, g = rgb[1]/255, b = rgb[2]/255;

	//ITU-R BT.709
	kb = kb || 0.0722;
	kr = kr || 0.2126;

	var y = kr*r + (1 - kr - kb)*g + kb*b;
	var pb = 0.5 * (b - y) / (1 - kb);
	var pr = 0.5 * (r - y) / (1 - kr);

	return [y, pb, pr];
};
