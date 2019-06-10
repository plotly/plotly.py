/**
 * Cubehelix http://astron-soc.in/bulletin/11June/289392011.pdf
 *
 * @module color-space/cubehelix
 */
'use strict'

var rgb = require('./rgb');
var clamp = require('mumath/clamp');


var cubehelix = module.exports = {
	name: 'cubehelix',
	channel: ['fraction'],
	min: [0],
	max: [1]
};


/** Default options for space */
var defaults = cubehelix.defaults = {
	//0..3
	start: 0,
	//-10..10
	rotation: 0.5,
	//0..1+
	hue: 1,
	//0..2
	gamma: 1
};


/**
 * Transform cubehelix level to RGB
 *
 * @param {Number} fraction 0..1 cubehelix level
 * @param {Object} options Mapping options, overrides defaults
 *
 * @return {Array} rgb tuple
 */
cubehelix.rgb = function(fraction, options) {
	options = options || {};

	if (fraction.length) fraction = fraction[0];

	var start = options.start !== undefined ? options.start : defaults.start;
	var rotation = options.rotation !== undefined ? options.rotation : defaults.rotation;
	var gamma = options.gamma !== undefined ? options.gamma : defaults.gamma;
	var hue = options.hue !== undefined ? options.hue : defaults.hue;

	var angle = 2 * Math.PI * (start/3 + 1.0 + rotation * fraction);

	fraction = Math.pow(fraction, gamma);

	var amp = hue * fraction * (1-fraction)/2.0;

	var r = fraction + amp*(-0.14861*Math.cos(angle)+1.78277*Math.sin(angle));
	var g = fraction + amp*(-0.29227*Math.cos(angle)-0.90649*Math.sin(angle));
	var b = fraction + amp*(+1.97294*Math.cos(angle));

	r = clamp(r, 0, 1);
	g = clamp(g, 0, 1);
	b = clamp(b, 0, 1);

	return [r * 255, g * 255, b * 255];
};


/**
 * RGB to cubehelix
 *
 * @param {Array} rgb RGB values
 *
 * @return {Array} cubehelix fraction(s)
 */
rgb.cubehelix = function(rgb) {
	//TODO - there is no backwise conversion yet
};
