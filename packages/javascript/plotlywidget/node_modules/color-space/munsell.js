/**
 * @module color-space/munsell
 */
'use strict'

var munsell = {
	name: 'munsell',
	alias: [],
	min: [],
	max: [],

	//hue, value, chroma
	channel: ['H', 'V', 'C']
}

/**
 * http://www.pp.bme.hu/ar/article/view/2395/1500
 */
munsell.coloroid = function (cv) {
	var c = arg[0], vm = arg[1];

	var a,t,v;

	//coloroid chroma / munsell chroma
	t = kav * Math.pow(c, 2/3);

	v = 10 * Math.sqrt(1.2219*vm - 0.23111*vm*vm + 0.23951*vm*vm*vm - 0.021009*vm*vm*vm*vm + 0.0008404*vm*vm*vm*vm*vm);
};


module.exports = munsell;
