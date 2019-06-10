/**
 * OSA-UCS
 *
 * @module  color-space/osa-ucs
 */
'use strict'

var xyz = require('./xyz');


var osaucs = {
	name: 'osaucs',
	alias: ['OSA-UCS'],
	channel: ['L', 'j', 'g'],
	min: [-10, -6, -10],
	max: [8, 12, 6]
};


/**
 * There’s no analytical solution to this
 */
osaucs.xyz = function (arg) {
	var x, y, z;

	throw 'Unimplemented';
	//http://www.researchgate.net/publication/259253763_Comparison_of_the_performance_of_inverse_transformation_methods_from_OSA-UCS_to_CIEXYZ

	return [x, y, z];
};


/**
 * Transform to xyz osaucs
 *
 * @param {Array} arg Input xyz array
 *
 * @return {Array} Ljg array
 */
xyz.osaucs = function (arg) {
	var X = arg[0], Y = arg[1], Z = arg[2];

	var x = X / (X + Y + Z);
	var y = Y / (X + Y + Z);

	//FIXME: there might be a typo, wiki states 1.8103 as a constant value
	var K = 4.4934*x*x + 4.3034*y*y - 4.276*x*y - 1.3744*x - 2.56439*y + 1.8103;
	var Y0 = K*Y;

	var L_ = 5.9*(Math.pow(Y0, 1/3) - 2/3 + 0.042*Math.pow(Math.max(Y0, 30) - 30, 1/3));
	var L = (L_ - 14.3993) / Math.sqrt(2);

	var C = L_ / (5.9 * (Math.pow(Y0, 1/3) - 2/3));

	var R = 0.7790*X + 0.4194*Y - 0.1648*Z;
	var G = -0.4493*X + 1.3265*Y + 0.0927*Z;
	var B = -0.1149*X + 0.3394*Y + 0.7170*Z;

	R = Math.pow(R, 1/3) || 0;
	G = Math.pow(G, 1/3) || 0;
	B = Math.pow(B, 1/3) || 0;

	var a = -13.7*R + 17.7*G - 4*B;
	var b = 1.7*R + 8*G - 9.7*B;

	var g = C*a;
	var j = C*b;

	//polar form
	// var p = Math.sqrt(j*j + g*g);
	// var phi = Math.atan2(j, g);

	return [L, j, g];
};


module.exports = osaucs;
