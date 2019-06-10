/**
 * @module  string-to-arraybuffer
 */

'use strict'

var atob = require('atob-lite')
var isBase64 = require('is-base64')

module.exports = function stringToArrayBuffer (arg) {
	if (typeof arg !== 'string') throw Error('Argument should be a string')

	//valid data uri
	if (/^data\:/i.test(arg)) return decode(arg)

	//base64
	if (isBase64(arg)) arg = atob(arg)

	return str2ab(arg)
}

function str2ab (str) {
	var array = new Uint8Array(str.length);
	for(var i = 0; i < str.length; i++) {
		array[i] = str.charCodeAt(i);
	}
	return array.buffer
}

function decode(uri) {
	// strip newlines
	uri = uri.replace(/\r?\n/g, '');

	// split the URI up into the "metadata" and the "data" portions
	var firstComma = uri.indexOf(',');
	if (-1 === firstComma || firstComma <= 4) throw new TypeError('malformed data-URI');

	// remove the "data:" scheme and parse the metadata
	var meta = uri.substring(5, firstComma).split(';');

	var base64 = false;
	var charset = 'US-ASCII';
	for (var i = 0; i < meta.length; i++) {
		if ('base64' == meta[i]) {
			base64 = true;
		} else if (0 == meta[i].indexOf('charset=')) {
			charset = meta[i].substring(8);
		}
	}

	// get the encoded data portion and decode URI-encoded chars
	var data = unescape(uri.substring(firstComma + 1));

	if (base64) data = atob(data)

	var abuf = str2ab(data)

	abuf.type = meta[0] || 'text/plain'
	abuf.charset = charset

	return abuf
}
