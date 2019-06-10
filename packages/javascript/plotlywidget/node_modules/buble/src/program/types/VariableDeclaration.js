import Node from '../Node.js';
import destructure from '../../utils/destructure.js';
import { loopStatement } from '../../utils/patterns.js';

export default class VariableDeclaration extends Node {
	initialise(transforms) {
		this.scope = this.findScope(this.kind === 'var');
		this.declarations.forEach(declarator => declarator.initialise(transforms));
	}

	transpile(code, transforms) {
		const i0 = this.getIndentation();
		let kind = this.kind;

		if (transforms.letConst && kind !== 'var') {
			kind = 'var';
			code.overwrite(this.start, this.start + this.kind.length, kind, {
				contentOnly: true,
				storeName: true
			});
		}

		if (transforms.destructuring && this.parent.type !== 'ForOfStatement' && this.parent.type !== 'ForInStatement') {
			let c = this.start;
			let lastDeclaratorIsPattern;

			this.declarations.forEach((declarator, i) => {
				declarator.transpile(code, transforms);

				if (declarator.id.type === 'Identifier') {
					if (i > 0 && this.declarations[i - 1].id.type !== 'Identifier') {
						code.overwrite(c, declarator.id.start, `var `);
					}
				} else {
					const inline = loopStatement.test(this.parent.type);

					if (i === 0) {
						code.remove(c, declarator.id.start);
					} else {
						code.overwrite(c, declarator.id.start, `;\n${i0}`);
					}

					const simple =
						declarator.init.type === 'Identifier' && !declarator.init.rewritten;

					const name = simple
						? (declarator.init.alias || declarator.init.name)
						: declarator.findScope(true).createIdentifier('ref');

					c = declarator.start;

					const statementGenerators = [];

					if (simple) {
						code.remove(declarator.id.end, declarator.end);
					} else {
						statementGenerators.push((start, prefix, suffix) => {
							code.prependRight(declarator.id.end, `var ${name}`);
							code.appendLeft(declarator.init.end, `${suffix}`);
							code.move(declarator.id.end, declarator.end, start);
						});
					}

					const scope = declarator.findScope(false);
					destructure(
						code,
						id => scope.createIdentifier(id),
						({ name }) => scope.resolveName(name),
						declarator.id,
						name,
						inline,
						statementGenerators
					);

					const prefix = inline ? 'var ' : '';
					let suffix = inline ? `, ` : `;\n${i0}`;
					statementGenerators.forEach((fn, j) => {
						if (
							i === this.declarations.length - 1 &&
							j === statementGenerators.length - 1
						) {
							suffix = inline ? '' : ';';
						}

						fn(declarator.start, j === 0 ? prefix : '', suffix);
					});
				}

				c = declarator.end;
				lastDeclaratorIsPattern = declarator.id.type !== 'Identifier';
			});

			if (lastDeclaratorIsPattern && this.end > c) {
				code.overwrite(c, this.end, '', { contentOnly: true });
			}
		} else {
			this.declarations.forEach(declarator => {
				declarator.transpile(code, transforms);
			});
		}
	}
}
