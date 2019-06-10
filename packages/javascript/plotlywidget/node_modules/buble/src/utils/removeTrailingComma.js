export default function removeTrailingComma(code, c) {
	while (code.original[c] !== ')') {
		if (code.original[c] === ',') {
			code.remove(c, c + 1);
			return;
		}

		if (code.original[c] === '/') {
			c = code.original.indexOf(code.original[c + 1] === '/' ? '\n' : '*/', c) + 1;
		}
		c += 1;
	}
}
