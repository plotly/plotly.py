import Node from '../Node.js';
import deindent from '../../utils/deindent.js';

export default class ClassDeclaration extends Node {
	initialise(transforms) {
		if (this.id) {
			this.name = this.id.name;
			this.findScope(true).addDeclaration(this.id, 'class');
		} else {
			this.name = this.findScope(true).createIdentifier("defaultExport");
		}

		super.initialise(transforms);
	}

	transpile(code, transforms) {
		if (transforms.classes) {
			if (!this.superClass) deindent(this.body, code);

			const superName =
				this.superClass && (this.superClass.name || 'superclass');

			const i0 = this.getIndentation();
			const i1 = i0 + code.getIndentString();

			// if this is an export default statement, we have to move the export to
			// after the declaration, because `export default var Foo = ...` is illegal
			const isExportDefaultDeclaration = this.parent.type === 'ExportDefaultDeclaration';

			if (isExportDefaultDeclaration) {
				code.remove(this.parent.start, this.start);
			}

			let c = this.start;
			if (this.id) {
				code.overwrite(c, this.id.start, 'var ');
				c = this.id.end;
			} else {
				code.prependLeft(c, `var ${this.name}`);
			}

			if (this.superClass) {
				if (this.superClass.end === this.body.start) {
					code.remove(c, this.superClass.start);
					code.appendLeft(c, ` = /*@__PURE__*/(function (${superName}) {\n${i1}`);
				} else {
					code.overwrite(c, this.superClass.start, ' = ');
					code.overwrite(
						this.superClass.end,
						this.body.start,
						`/*@__PURE__*/(function (${superName}) {\n${i1}`
					);
				}
			} else {
				if (c === this.body.start) {
					code.appendLeft(c, ' = ');
				} else {
					code.overwrite(c, this.body.start, ' = ');
				}
			}

			this.body.transpile(code, transforms, !!this.superClass, superName);

			const syntheticDefaultExport =
				isExportDefaultDeclaration
					? `\n\n${i0}export default ${this.name};`
					: '';
			if (this.superClass) {
				code.appendLeft(this.end, `\n\n${i1}return ${this.name};\n${i0}}(`);
				code.move(this.superClass.start, this.superClass.end, this.end);
				code.prependRight(this.end, `));${syntheticDefaultExport}`);
			} else if (syntheticDefaultExport) {
				code.prependRight(this.end, syntheticDefaultExport);
			}
		} else {
			this.body.transpile(code, transforms, false, null);
		}
	}
}
