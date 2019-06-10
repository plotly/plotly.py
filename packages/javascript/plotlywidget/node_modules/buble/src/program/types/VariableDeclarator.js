import Node from '../Node.js';

export default class VariableDeclarator extends Node {
	initialise(transforms) {
		let kind = this.parent.kind;
		if (kind === 'let' && this.parent.parent.type === 'ForStatement') {
			kind = 'for.let'; // special case...
		}

		this.parent.scope.addDeclaration(this.id, kind);
		super.initialise(transforms);
	}

	transpile(code, transforms) {
		if (!this.init && transforms.letConst && this.parent.kind !== 'var') {
			const inLoop = this.findNearest(
				/Function|^For(In|Of)?Statement|^(?:Do)?WhileStatement/
			);
			if (
				inLoop &&
				!/Function/.test(inLoop.type) &&
				!this.isLeftDeclaratorOfLoop()
			) {
				code.appendLeft(this.id.end, ' = (void 0)');
			}
		}

		if (this.id) this.id.transpile(code, transforms);
		if (this.init) this.init.transpile(code, transforms);
	}

	isLeftDeclaratorOfLoop() {
		return (
			this.parent &&
			this.parent.type === 'VariableDeclaration' &&
			this.parent.parent &&
			(this.parent.parent.type === 'ForInStatement' ||
				this.parent.parent.type === 'ForOfStatement') &&
			this.parent.parent.left &&
			this.parent.parent.left.declarations[0] === this
		);
	}
}
