import Node from '../Node.js';
import CompileError from '../../utils/CompileError.js';
import { loopStatement } from '../../utils/patterns.js';

export default class ContinueStatement extends Node {
	transpile(code) {
		const loop = this.findNearest(loopStatement);
		if (loop.shouldRewriteAsFunction) {
			if (this.label)
				throw new CompileError(
					'Labels are not currently supported in a loop with locally-scoped variables',
					this
				);
			code.overwrite(this.start, this.start + 8, 'return');
		}
	}
}
