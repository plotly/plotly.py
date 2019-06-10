import Node from '../Node.js';
import CompileError from '../../utils/CompileError.js';
import rewritePattern from 'regexpu-core';

const nonAsciiLsOrPs = /[\u2028-\u2029]/g;

export default class Literal extends Node {
	initialise() {
		if (typeof this.value === 'string') {
			this.program.indentExclusionElements.push(this);
		}
	}

	transpile(code, transforms) {
		if (transforms.numericLiteral) {
			if (this.raw.match(/^0[bo]/i)) {
				code.overwrite(this.start, this.end, String(this.value), {
					storeName: true,
					contentOnly: true
				});
			}
		}

		if (this.regex) {
			const { pattern, flags } = this.regex;

			if (transforms.stickyRegExp && /y/.test(flags))
				CompileError.missingTransform('the regular expression sticky flag', 'stickyRegExp', this);
			if (transforms.unicodeRegExp && /u/.test(flags)) {
				code.overwrite(
					this.start,
					this.end,
					`/${rewritePattern(pattern, flags)}/${flags.replace('u', '')}`,
					{
						contentOnly: true
					}
				);
			}
		} else if (typeof this.value === "string" && this.value.match(nonAsciiLsOrPs)) {
			code.overwrite(
				this.start,
				this.end,
				this.raw.replace(nonAsciiLsOrPs, m => m == '\u2028' ? '\\u2028' : '\\u2029'),
				{
					contentOnly: true
				}
			);
		}
	}
}
