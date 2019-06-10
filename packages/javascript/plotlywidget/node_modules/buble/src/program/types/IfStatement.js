import Node from '../Node.js';

export default class IfStatement extends Node {
	initialise(transforms) {
		super.initialise(transforms);
	}

	transpile(code, transforms) {
		if (
			this.consequent.type !== 'BlockStatement' ||
			(this.consequent.type === 'BlockStatement' && this.consequent.synthetic)
		) {
			code.appendLeft(this.consequent.start, '{ ');
			code.prependRight(this.consequent.end, ' }');
		}

		if (
			this.alternate &&
			this.alternate.type !== 'IfStatement' &&
			(this.alternate.type !== 'BlockStatement' ||
				(this.alternate.type === 'BlockStatement' && this.alternate.synthetic))
		) {
			code.appendLeft(this.alternate.start, '{ ');
			code.prependRight(this.alternate.end, ' }');
		}

		super.transpile(code, transforms);
	}
}
