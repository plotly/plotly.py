'use strict'

var paren = require('parenthesis')

module.exports = function splitBy (string, separator, o) {
	if (string == null) throw Error('First argument should be a string')
	if (separator == null) throw Error('Separator should be a string or a RegExp')

	if (!o) o = {}
	else if (typeof o === 'string' || Array.isArray(o)) {
		o = {ignore: o}
	}

	if (o.escape == null) o.escape = true
	if (o.ignore == null) o.ignore = ['[]', '()', '{}', '<>', '""', "''", '``', '“”', '«»']
	else {
		if (typeof o.ignore === 'string') {o.ignore = [o.ignore]}

		o.ignore = o.ignore.map(function (pair) {
			// '"' → '""'
			if (pair.length === 1) pair = pair + pair
			return pair
		})
	}

	var tokens = paren.parse(string, {flat: true, brackets: o.ignore})
	var str = tokens[0]

	var parts = str.split(separator)

	// join parts separated by escape
	if (o.escape) {
		var cleanParts = []
		for (var i = 0; i < parts.length; i++) {
			var prev = parts[i]
			var part = parts[i + 1]

			if (prev[prev.length - 1] === '\\' && prev[prev.length - 2] !== '\\') {
				cleanParts.push(prev + separator + part)
				i++
			}
			else {
				cleanParts.push(prev)
			}
		}
		parts = cleanParts
	}

	// open parens pack & apply unquotes, if any
	for (var i = 0; i < parts.length; i++) {
		tokens[0] = parts[i]
		parts[i] = paren.stringify(tokens, {flat: true})
	}

	return parts
}
