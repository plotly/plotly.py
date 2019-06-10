'use strict'

var unquote = require('unquote')
var globalKeywords = require('css-global-keywords')
var systemFontKeywords = require('css-system-font-keywords')
var fontWeightKeywords = require('css-font-weight-keywords')
var fontStyleKeywords = require('css-font-style-keywords')
var fontStretchKeywords = require('css-font-stretch-keywords')
var splitBy = require('string-split-by')
var isSize = require('./lib/util').isSize


module.exports = parseFont


var cache = parseFont.cache = {}


function parseFont (value) {
	if (typeof value !== 'string') throw new Error('Font argument must be a string.')

	if (cache[value]) return cache[value]

	if (value === '') {
		throw new Error('Cannot parse an empty string.')
	}

	if (systemFontKeywords.indexOf(value) !== -1) {
		return cache[value] = {system: value}
	}

	var font = {
		style: 'normal',
		variant: 'normal',
		weight: 'normal',
		stretch: 'normal',
		lineHeight: 'normal',
		size: '1rem',
		family: ['serif']
	}

	var tokens = splitBy(value, /\s+/)
	var token

	while (token = tokens.shift()) {
		if (globalKeywords.indexOf(token) !== -1) {
			['style', 'variant', 'weight', 'stretch'].forEach(function(prop) {
				font[prop] = token
			})

			return cache[value] = font
		}

		if (fontStyleKeywords.indexOf(token) !== -1) {
			font.style = token
			continue
		}

		if (token === 'normal' || token === 'small-caps') {
			font.variant = token
			continue
		}

		if (fontStretchKeywords.indexOf(token) !== -1) {
			font.stretch = token
			continue
		}

		if (fontWeightKeywords.indexOf(token) !== -1) {
			font.weight = token
			continue
		}


		if (isSize(token)) {
			var parts = splitBy(token, '/')
			font.size = parts[0]
			if (parts[1] != null) {
				font.lineHeight = parseLineHeight(parts[1])
			}
			else if (tokens[0] === '/') {
				tokens.shift()
				font.lineHeight = parseLineHeight(tokens.shift())
 			}

			if (!tokens.length) {
				throw new Error('Missing required font-family.')
			}
			font.family = splitBy(tokens.join(' '), /\s*,\s*/).map(unquote)

			return cache[value] = font
		}

		throw new Error('Unknown or unsupported font token: ' + token)
	}

	throw new Error('Missing required font-size.')
}


function parseLineHeight(value) {
	var parsed = parseFloat(value)
	if (parsed.toString() === value) {
		return parsed
	}
	return value
}
