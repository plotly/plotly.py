import Node from '../Node.js';
import CompileError from '../../utils/CompileError.js';
import { loopStatement } from '../../utils/patterns.js';

export default class BreakStatement extends Node {
	initialise() {
		const loop = this.findNearest(loopStatement);
		const switchCase = this.findNearest('SwitchCase');

		if (loop && (!switchCase || loop.depth > switchCase.depth)) {
			loop.canBreak = true;
			this.loop = loop;
		}
	}

	transpile(code) {
		if (this.loop && this.loop.shouldRewriteAsFunction) {
			if (this.label)
				throw new CompileError(
					'Labels are not currently supported in a loop with locally-scoped variables',
					this
				);
			code.overwrite(this.start, this.start + 5, `return 'break'`);
		}
	}
}
