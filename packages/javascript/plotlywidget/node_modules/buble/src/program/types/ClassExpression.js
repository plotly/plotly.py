import Node from '../Node.js';

export default class ClassExpression extends Node {
	initialise(transforms) {
		this.name = (this.id
			? this.id.name
			: this.parent.type === 'VariableDeclarator'
				? this.parent.id.name
				: this.parent.type !== 'AssignmentExpression'
					? null
					: this.parent.left.type === 'Identifier'
						? this.parent.left.name
						: this.parent.left.type === 'MemberExpression'
							? this.parent.left.property.name
							: null) || this.findScope(true).createIdentifier('anonymous');

		super.initialise(transforms);
	}

	transpile(code, transforms) {
		if (transforms.classes) {
			const superName =
				this.superClass && (this.superClass.name || 'superclass');

			const i0 = this.getIndentation();
			const i1 = i0 + code.getIndentString();

			if (this.superClass) {
				code.remove(this.start, this.superClass.start);
				code.remove(this.superClass.end, this.body.start);
				code.appendRight(this.start, `/*@__PURE__*/(function (${superName}) {\n${i1}`);
			} else {
				code.overwrite(this.start, this.body.start, `/*@__PURE__*/(function () {\n${i1}`);
			}

			this.body.transpile(code, transforms, true, superName);

			let superClass = '';
			if (this.superClass) {
				superClass = code.slice(this.superClass.start, this.superClass.end);
				code.remove(this.superClass.start, this.superClass.end);
			}
			code.appendLeft(this.end, `\n\n${i1}return ${this.name};\n${i0}}(${superClass}))`);
		} else {
			this.body.transpile(code, transforms, false);
		}
	}
}
