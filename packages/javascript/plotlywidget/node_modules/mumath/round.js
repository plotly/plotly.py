/**
 * Precision round
 *
 * @param {number} value
 * @param {number} step Minimal discrete to round
 *
 * @return {number}
 *
 * @example
 * toPrecision(213.34, 1) == 213
 * toPrecision(213.34, .1) == 213.3
 * toPrecision(213.34, 10) == 210
 */
'use strict';
var precision = require('./precision');

module.exports = function(value, step) {
	if (step === 0) return value;
	if (!step) return Math.round(value);
	value = Math.round(value / step) * step;
	return parseFloat(value.toFixed(precision(step)));
};
