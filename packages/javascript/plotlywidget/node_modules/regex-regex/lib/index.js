'use strict';

var re = /^\/((?:\\\/|[^\/])+)\/([imgy]*)$/;
/*
	Matches parts of a regular expression string.

	/^\/
		-	match a string that begins with a /
	()
		-	capture
	(?:)+
		-	capture, but do not remember, a group of characters which occur 1 or more times
	\\\/
		-	match the literal \/
	|
		-	OR
	[^\/]
		-	anything which is not the literal \/
	\/
		-	match the literal /
	([imgy]*)
		-	capture any characters matching `imgy` occurring 0 or more times
	$/
		-	string end
*/


// EXPORTS //

module.exports = re;
