/**
 * Composed set of all math utils, wrapped
 *
 * @module  mumath
 */
'use strict';
const wrap = require('./wrap');

module.exports = {
	clamp: wrap(require('./clamp')),
	within: wrap(require('./within')),
	round: wrap(require('./round')),
	precision: wrap(require('./precision')),
	mod: wrap(require('./mod')),
	log10: wrap(require('./log10')),
	len: wrap(require('./len')),
	closest: wrap(require('./closest')),
	order: wrap(require('./order')),
	lerp: wrap(require('./lerp')),
	isMultiple: wrap(require('./is-multiple')),
	normalize: wrap(require('./normalize')),
	scale: wrap(require('./scale')),
	// pretty: wrap(require('./pretty')),
};
