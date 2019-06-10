import Node from '../Node.js';
import { loopStatement } from '../../utils/patterns.js';

export default class ThisExpression extends Node {
	initialise(transforms) {
		const lexicalBoundary = this.findLexicalBoundary();

		if (transforms.letConst) {
			// save all loops up to the lexical boundary in case we need
			// to alias them later for block-scoped declarations
			let node = this.findNearest(loopStatement);
			while (node && node.depth > lexicalBoundary.depth) {
				node.thisRefs.push(this);
				node = node.parent.findNearest(loopStatement);
			}
		}

		if (transforms.arrow) {
			const arrowFunction = this.findNearest('ArrowFunctionExpression');

			if (arrowFunction && arrowFunction.depth > lexicalBoundary.depth) {
				this.alias = lexicalBoundary.getThisAlias();
			}
		}
	}

	transpile(code) {
		if (this.alias) {
			code.overwrite(this.start, this.end, this.alias, {
				storeName: true,
				contentOnly: true
			});
		}
	}
}
