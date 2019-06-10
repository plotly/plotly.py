'use strict'

var sizes = require('css-font-size-keywords')

module.exports = {
	isSize: function isSize(value) {
		return /^[\d\.]/.test(value)
			|| value.indexOf('/') !== -1
			|| sizes.indexOf(value) !== -1
	}
}
