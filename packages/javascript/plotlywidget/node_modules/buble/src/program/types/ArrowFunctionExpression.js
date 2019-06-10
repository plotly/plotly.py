import Node from '../Node.js';
import CompileError from '../../utils/CompileError.js';
import removeTrailingComma from '../../utils/removeTrailingComma.js';

export default class ArrowFunctionExpression extends Node {
	initialise(transforms) {
		if (this.async && transforms.asyncAwait) {
			CompileError.missingTransform("async arrow functions", "asyncAwait", this);
		}
		this.body.createScope();
		super.initialise(transforms);
	}

	transpile(code, transforms) {
		let openParensPos = this.start;
		for (let end = (this.body || this.params[0]).start - 1; code.original[openParensPos] !== '(' && openParensPos < end;) {
			++openParensPos;
		}
		if (code.original[openParensPos] !== '(') openParensPos = -1;
		const naked = openParensPos === -1;

		if (transforms.arrow || this.needsArguments(transforms)) {
			// remove arrow
			let charIndex = this.body.start;
			while (code.original[charIndex] !== '=') {
				charIndex -= 1;
			}
			code.remove(charIndex, this.body.start);

			super.transpile(code, transforms);

			// wrap naked parameter
			if (naked) {
				code.prependRight(this.params[0].start, '(');
				code.appendLeft(this.params[0].end, ')');
			}

			// standalone expression statement
			const standalone = this.parent && this.parent.type === 'ExpressionStatement';
			let start, text = standalone ? '!' : '';
			if (this.async) text += 'async ';
			text += 'function';
			if (!standalone) text += ' ';
			if (naked) {
				start = this.params[0].start;
			} else {
				start = openParensPos;
			}
			// add function
			if (start > this.start) {
				code.overwrite(this.start, start, text);
			} else {
				code.prependRight(this.start, text);
			}
		} else {
			super.transpile(code, transforms);
		}

		if (transforms.trailingFunctionCommas && this.params.length && !naked) {
			removeTrailingComma(code, this.params[this.params.length - 1].end);
		}
	}

	// Returns whether any transforms that will happen use `arguments`
	needsArguments(transforms) {
		return (
			transforms.spreadRest &&
			this.params.filter(param => param.type === 'RestElement').length > 0
		);
	}
}
