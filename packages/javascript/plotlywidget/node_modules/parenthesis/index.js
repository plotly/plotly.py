'use strict'

/**
 * @module parenthesis
 */

function parse (str, opts) {
	// pretend non-string parsed per-se
	if (typeof str !== 'string') return [str]

	var res = [str]

	if (typeof opts === 'string' || Array.isArray(opts)) {
		opts = {brackets: opts}
	}
	else if (!opts) opts = {}

	var brackets = opts.brackets ? (Array.isArray(opts.brackets) ? opts.brackets : [opts.brackets]) : ['{}', '[]', '()']

	var escape = opts.escape || '___'

	var flat = !!opts.flat

	brackets.forEach(function (bracket) {
		// create parenthesis regex
		var pRE = new RegExp(['\\', bracket[0], '[^\\', bracket[0], '\\', bracket[1], ']*\\', bracket[1]].join(''))

		var ids = []

		function replaceToken(token, idx, str){
			// save token to res
			var refId = res.push(token.slice(bracket[0].length, -bracket[1].length)) - 1

			ids.push(refId)

			return escape + refId + escape
		}

		res.forEach(function (str, i) {
			var prevStr

			// replace paren tokens till there’s none
			var a = 0
			while (str != prevStr) {
				prevStr = str
				str = str.replace(pRE, replaceToken)
				if (a++ > 10e3) throw Error('References have circular dependency. Please, check them.')
			}

			res[i] = str
		})

		// wrap found refs to brackets
		ids = ids.reverse()
		res = res.map(function (str) {
			ids.forEach(function (id) {
				str = str.replace(new RegExp('(\\' + escape + id + '\\' + escape + ')', 'g'), bracket[0] + '$1' + bracket[1])
			})
			return str
		})
	})

	var re = new RegExp('\\' + escape + '([0-9]+)' + '\\' + escape)

	// transform references to tree
	function nest (str, refs, escape) {
		var res = [], match

		var a = 0
		while (match = re.exec(str)) {
			if (a++ > 10e3) throw Error('Circular references in parenthesis')

			res.push(str.slice(0, match.index))

			res.push(nest(refs[match[1]], refs))

			str = str.slice(match.index + match[0].length)
		}

		res.push(str)

		return res
	}

	return flat ? res : nest(res[0], res)
}

function stringify (arg, opts) {
	if (opts && opts.flat) {
		var escape = opts && opts.escape || '___'

		var str = arg[0], prevStr

		// pretend bad string stringified with no parentheses
		if (!str) return ''


		var re = new RegExp('\\' + escape + '([0-9]+)' + '\\' + escape)

		var a = 0
		while (str != prevStr) {
			if (a++ > 10e3) throw Error('Circular references in ' + arg)
			prevStr = str
			str = str.replace(re, replaceRef)
		}

		return str
	}

	return arg.reduce(function f (prev, curr) {
		if (Array.isArray(curr)) {
			curr = curr.reduce(f, '')
		}
		return prev + curr
	}, '')

	function replaceRef(match, idx){
		if (arg[idx] == null) throw Error('Reference ' + idx + 'is undefined')
		return arg[idx]
	}
}

function parenthesis (arg, opts) {
	if (Array.isArray(arg)) {
		return stringify(arg, opts)
	}
	else {
		return parse(arg, opts)
	}
}

parenthesis.parse = parse
parenthesis.stringify = stringify

module.exports = parenthesis
