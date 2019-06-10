/**
 * https://en.wikipedia.org/wiki/CIE_1964_color_space
 *
 * Very similar to LUV, but w and v are calculated a bit differently.
 *
 * @module  color-space/uvw
 */
'use strict'

var ucs = require('./ucs');
var xyz = require('./xyz');

var uvw = module.exports = {
	name: 'uvw',
	min: [-134, -140, 0],
	max: [224, 122, 100],
	channel: ['U','V','W'],
	alias: ['UVW', 'cieuvw', 'cie1964']
};


/**
 * UVW to XYZ
 */
uvw.xyz = function (arg, i, o) {
	var _u, _v, w, u, v, x, y, z, xn, yn, zn, un, vn;
	u = arg[0], v = arg[1], w = arg[2];

	if (w === 0) return [0,0,0];

	//get illuminant/observer
	i = i || 'D65';
	o = o || 2;

	xn = xyz.whitepoint[o][i][0];
	yn = xyz.whitepoint[o][i][1];
	zn = xyz.whitepoint[o][i][2];

	un = (4 * xn) / (xn + (15 * yn) + (3 * zn));
	vn = (6 * yn) / (xn + (15 * yn) + (3 * zn));

	y = Math.pow((w + 17) / 25, 3);

	_u = u / (13 * w) + un || 0;
	_v = v / (13 * w) + vn || 0;

	x = (6 / 4) * y * _u / _v;
	z = y * (2 / _v - 0.5 * _u / _v - 5);

	return [x, y, z];
};


/**
 * XYZ to UVW
 *
 * @return {Array} An UVW array
 */
xyz.uvw = function (arr, i, o) {
	var x = arr[0], y = arr[1], z = arr[2], xn, yn, zn, un, vn;

	//find out normal source u v
	i = i || 'D65';
	o = o || 2;

	xn = xyz.whitepoint[o][i][0];
	yn = xyz.whitepoint[o][i][1];
	zn = xyz.whitepoint[o][i][2];

	un = (4 * xn) / (xn + (15 * yn) + (3 * zn));
	vn = (6 * yn) / (xn + (15 * yn) + (3 * zn));

	var _u = 4 * x / (x + 15 * y + 3 * z) || 0;
	var _v = 6 * y / (x + 15 * y + 3 * z) || 0;

	//calc values
	var w = 25 * Math.pow(y, 1/3) - 17;
	var u = 13 * w * (_u - un);
	var v = 13 * w * (_v - vn);

	return [u, v, w];
};



/**
 * UVW to UCS
 *
 * @param {Array} uvw UCS values
 *
 * @return {Array} UVW values
 */
uvw.ucs = function(uvw) {
	//find chromacity variables
};


/**
 * UCS to UVW
 *
 * @param {Array} uvw UVW values
 *
 * @return {Array} UCS values
 */
ucs.uvw = function(ucs) {
	// //find chromacity variables
	// var u = U / (U + V + W);
	// var v = V / (U + V + W);

	// //find 1964 UVW
	// w = 25 * Math.pow(y, 1/3) - 17;
	// u = 13 * w * (u - un);
	// v = 13 * w * (v - vn);
};
