'use strict';
module.exports = typeof navigator !== 'undefined' &&
	(/MSIE/.test(navigator.userAgent) || /Trident\//.test(navigator.appVersion));
