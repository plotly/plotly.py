/**
 * Whether element is between left & right including
 *
 * @param {number} a
 * @param {number} left
 * @param {number} right
 *
 * @return {Boolean}
 */
'use strict';
module.exports = function(a, left, right){
	if (left > right) {
		var tmp = left;
		left = right;
		right = tmp;
	}
	if (a <= right && a >= left) return true;
	return false;
};
