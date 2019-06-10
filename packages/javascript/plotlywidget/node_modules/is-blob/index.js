'use strict';

module.exports = input => {
	if (typeof Blob === 'undefined') {
		return false;
	}

	return input instanceof Blob || Object.prototype.toString.call(input) === '[object Blob]';
};
