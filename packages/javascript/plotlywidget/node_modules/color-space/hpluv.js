/**
 * A uniform wrapper for hpluv.
 * // http://www.hsluv.org/
 *
 * @module color-space/hpluv
 */
'use strict'

var xyz = require('./xyz');
var lchuv = require('./lchuv');
var _hsluv = require('hsluv');

module.exports = {
	name: 'hpluv',
	min: [0,0,0],
	max: [360,100,100],
	channel: ['hue', 'saturation', 'lightness'],
	alias: ['HPLuv', 'HuSLp'],

	lchuv: _hsluv.hpluvToLch,
	xyz: function(arg){return lchuv.xyz(_hsluv.hpluvToLch(arg));},

	//a shorter way to convert to husl
	hsluv: function(arg){
		return _hsluv.lchToHsluv( _hsluv.hpluvToLch(arg));
	}

};

//extend lchuv, xyz
lchuv.hpluv = _hsluv.lchToHpluv;
xyz.hpluv = function(arg){return _hsluv.lchToHpluv(xyz.lchuv(arg));};
