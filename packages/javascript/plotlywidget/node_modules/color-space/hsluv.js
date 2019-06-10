/**
 * A uniform wrapper for hsluv.
 * // http://www.hsluv.org/
 *
 * @module color-space/hsluv
 */
'use strict'

var xyz = require('./xyz');
var lchuv = require('./lchuv');
var _hsluv = require('hsluv');


module.exports = {
	name: 'hsluv',
	min: [0,0,0],
	max: [360,100,100],
	channel: ['hue', 'saturation', 'lightness'],
	alias: ['HSLuv', 'HuSL'],

	lchuv: _hsluv.hsluvToLch,

	xyz: function(arg){
		return lchuv.xyz(_hsluv.hsluvToLch(arg));
	},

	//a shorter way to convert to hpluv
	hpluv: function(arg){
		return _hsluv.lchToHpluv( _hsluv.hsluvToLch(arg));
	}
};

//extend lchuv, xyz
lchuv.hsluv = _hsluv.lchToHsluv;
xyz.hsluv = function(arg){
	return _hsluv.lchToHsluv(xyz.lchuv(arg));
};
