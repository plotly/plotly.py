import Node from '../Node.js';
import checkConst from '../../utils/checkConst.js';

export default class UpdateExpression extends Node {
	initialise(transforms) {
		if (this.argument.type === 'Identifier') {
			const declaration = this.findScope(false).findDeclaration(
				this.argument.name
			);
			// special case – https://gitlab.com/Rich-Harris/buble/issues/150
			const statement = declaration && declaration.node.ancestor(3);
			if (
				statement &&
				statement.type === 'ForStatement' &&
				statement.body.contains(this)
			) {
				statement.reassigned[this.argument.name] = true;
			}
		}

		super.initialise(transforms);
	}

	transpile(code, transforms) {
		if (this.argument.type === 'Identifier') {
			// Do this check after everything has been initialized to find
			// shadowing declarations after this expression
			checkConst(this.argument, this.findScope(false));
		}
		super.transpile(code, transforms);
	}
}
