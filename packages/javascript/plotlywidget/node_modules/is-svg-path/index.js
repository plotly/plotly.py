'use strict'

module.exports = function isPath(str) {
	if (typeof str !== 'string') return false

	str = str.trim()

	// https://www.w3.org/TR/SVG/paths.html#PathDataBNF
	if (/^[mzlhvcsqta]\s*[-+.0-9][^mlhvzcsqta]+/i.test(str) && /[\dz]$/i.test(str) && str.length > 4) return true

	return false
}
