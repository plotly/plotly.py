import Node from '../Node.js';
import { loopStatement } from '../../utils/patterns.js';

export default class ReturnStatement extends Node {
	initialise(transforms) {
		this.loop = this.findNearest(loopStatement);
		this.nearestFunction = this.findNearest(/Function/);

		if (
			this.loop &&
			(!this.nearestFunction || this.loop.depth > this.nearestFunction.depth)
		) {
			this.loop.canReturn = true;
			this.shouldWrap = true;
		}

		if (this.argument) this.argument.initialise(transforms);
	}

	transpile(code, transforms) {
		const shouldWrap =
			this.shouldWrap && this.loop && this.loop.shouldRewriteAsFunction;

		if (this.argument) {
			if (shouldWrap) code.prependRight(this.argument.start, `{ v: `);
			this.argument.transpile(code, transforms);
			if (shouldWrap) code.appendLeft(this.argument.end, ` }`);
		} else if (shouldWrap) {
			code.appendLeft(this.start + 6, ' {}');
		}
	}
}
