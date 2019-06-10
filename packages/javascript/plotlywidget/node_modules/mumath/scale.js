/**
 * Get step out of the set
 *
 * @module mumath/step
 */
'use strict';

var lg = require('./log10');

module.exports = function (minStep, srcSteps) {
	var power = Math.floor(lg(minStep));

	var order = Math.pow(10, power);
	var steps = srcSteps.map(v => v*order);
	order = Math.pow(10, power+1);
	steps = steps.concat(srcSteps.map(v => v*order));

	//find closest scale
	var step = 0;
	for (var i = 0; i < steps.length; i++) {
		step = steps[i];
		if (step >= minStep) break;
	}

	return step;
};
