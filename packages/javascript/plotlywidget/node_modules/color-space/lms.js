/**
 * A responsivity of cones color space.
 * Used for CAT - chromatic adaptation transform.
 *
 * http://en.wikipedia.org/wiki/LMS_color_space
 * http://www.mathworks.com/matlabcentral/fileexchange/28790-colorspace-transformations
 *
 * @todo xyz -> lms
 * @todo  tests
 *
 * @module color-space/lms
 */
'use strict'

var xyz = require('./xyz');

var lms = module.exports = {
	name: 'lms',
	min: [0,0,0],
	max: [100,100,100],
	channel: ['long', 'medium', 'short'],


	//transform matrices
	matrix: {
		HPE: [
			0.38971, 0.68898,-0.07868,
		   -0.22981, 1.18340, 0.04641,
			0.00000, 0.00000, 1.00000],
		VONKRIES: [
			0.4002, 0.7076, -0.0808,
		   -0.2263, 1.1653,  0.0457,
			0.00000,0.00000, 0.9182],
		BFD: [
			0.8951, 0.2664,-0.1614,
		   -0.7502, 1.7135,	0.0367,
			0.0389,-0.0686, 1.0296],
		CAT97: [
			0.8562, 0.3372,-0.1934,
		   -0.8360, 1.8327, 0.0033,
			0.0357,-0.00469,1.0112],
		CAT00: [
			0.7982, 0.3389,-0.1371,
		   -0.5918, 1.5512, 0.0406,
			0.0008, 0.0239, 0.9753],
		CAT02: [
			0.7328, 0.4296,-0.1624,
		   -0.7036, 1.6975, 0.0061,
			0.0030, 0.0136, 0.9834]
	}
};


lms.xyz = function(arg, matrix){
	var l = arg[0], m = arg[1], s = arg[2];

	if (!matrix) {
		matrix = [
			1.096123820835514, -0.278869000218287, +0.182745179382773,
			0.454369041975359, + 0.473533154307412, +0.072097803717229,
			-0.009627608738429, -0.005698031216113, +1.015325639954543
		];
	}

	return [
		l * matrix[0] + m * matrix[1] + s * matrix[2],
		l * matrix[3] + m * matrix[4] + s * matrix[5],
		l * matrix[6] + m * matrix[7] + s * matrix[8]
	];
};

xyz.lms = function(arg, matrix) {
		var x = arg[0], y = arg[1], z = arg[2];

		if (!matrix) {
			matrix = lms.matrix.CAT02
		}

		return [
			x * matrix[0] + y * matrix[1] + z * matrix[2],
			x * matrix[3] + y * matrix[4] + z * matrix[5],
			x * matrix[6] + y * matrix[7] + z * matrix[8]
		];
};
