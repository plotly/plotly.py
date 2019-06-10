'use strict'

var isBrowser = require('is-browser')
var hasHover

if (typeof global.matchMedia === 'function') {
	hasHover = !global.matchMedia('(hover: none)').matches
}
else {
	hasHover = isBrowser
}

module.exports = hasHover
