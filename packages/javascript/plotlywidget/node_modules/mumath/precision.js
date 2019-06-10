/**
 * @module  mumath/precision
 *
 * Get precision from float:
 *
 * @example
 * 1.1 → 1, 1234 → 0, .1234 → 4
 *
 * @param {number} n
 *
 * @return {number} decimap places
 */
'use strict';

var almost = require('almost-equal');
var norm = require('./normalize');

module.exports = function (n, eps) {
	n = norm(n);

	var str = n + '';

	//1e-10 etc
	var e = str.indexOf('e-');
	if (e >= 0) return parseInt(str.substring(e+2));

	//imperfect ints, like 3.0000000000000004 or 1.9999999999999998
	var remainder = Math.abs(n % 1);
	var remStr = remainder + '';

	if (almost(remainder, 1, eps) || almost(remainder, 0, eps)) return 0;

	//usual floats like .0123
	var d = remStr.indexOf('.') + 1;

	if (d) return remStr.length - d;

	//regular inte
	return 0;
};
