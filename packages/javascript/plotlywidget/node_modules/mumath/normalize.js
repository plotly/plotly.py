/**
 * Get rid of float remainder
 *
 * @module mumath/normalize
 */
'use strict';

var almost = require('almost-equal');

module.exports = function(value, eps) {
	//ignore ints
	var rem = value%1;
	if (!rem) return value;

	if (eps == null) eps = Number.EPSILON || almost.FLT_EPSILON;

	//pick number’s neighbour, which is way shorter, like 0.4999999999999998 → 0.5
	//O(20)
	var range = 5;
	var len = (rem+'').length;

	for (var i = 1; i < range; i+=.5) {
		var left = rem - eps*i,
			right = rem + eps*i;

		var leftStr = left+'', rightStr = right + '';

		if (len - leftStr.length > 2) return value - eps*i;
		if (len - rightStr.length > 2) return value + eps*i;

		// if (leftStr[2] != rightStr[2])
	}

	return value;
};
