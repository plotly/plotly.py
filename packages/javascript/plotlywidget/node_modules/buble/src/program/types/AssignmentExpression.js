import Node from '../Node.js';
import checkConst from '../../utils/checkConst.js';
import destructure from '../../utils/destructure.js';

export default class AssignmentExpression extends Node {
	initialise(transforms) {
		if (this.left.type === 'Identifier') {
			const declaration = this.findScope(false).findDeclaration(this.left.name);
			// special case – https://gitlab.com/Rich-Harris/buble/issues/11
			const statement = declaration && declaration.node.ancestor(3);
			if (
				statement &&
				statement.type === 'ForStatement' &&
				statement.body.contains(this)
			) {
				statement.reassigned[this.left.name] = true;
			}
		}

		super.initialise(transforms);
	}

	transpile(code, transforms) {
		if (this.left.type === 'Identifier') {
			// Do this check after everything has been initialized to find
			// shadowing declarations after this expression
			checkConst(this.left, this.findScope(false));
		}

		if (this.operator === '**=' && transforms.exponentiation) {
			this.transpileExponentiation(code, transforms);
		} else if (/Pattern/.test(this.left.type) && transforms.destructuring) {
			this.transpileDestructuring(code);
		}

		super.transpile(code, transforms);
	}

	transpileDestructuring(code) {
		const writeScope = this.findScope(true);
		const lookupScope = this.findScope(false);
		const assign = writeScope.createDeclaration('assign');
		code.appendRight(this.left.end, `(${assign}`);

		code.appendLeft(this.right.end, ', ');
		const statementGenerators = [];
		destructure(
			code,
			id => writeScope.createDeclaration(id),
			node => {
				const name = lookupScope.resolveName(node.name);
				checkConst(node, lookupScope);
				return name;
			},
			this.left,
			assign,
			true,
			statementGenerators
		);

		let suffix = ', ';
		statementGenerators.forEach((fn, j) => {
			if (j === statementGenerators.length - 1) {
				suffix = '';
			}

			fn(this.end, '', suffix);
		});

		if (this.unparenthesizedParent().type === 'ExpressionStatement') {
			// no rvalue needed for expression statement
			code.prependRight(this.end, `)`);
		} else {
			// destructuring is part of an expression - need an rvalue
			code.appendRight(this.end, `, ${assign})`);
		}
	}

	transpileExponentiation(code) {
		const scope = this.findScope(false);

		// first, the easy part – `**=` -> `=`
		let charIndex = this.left.end;
		while (code.original[charIndex] !== '*') charIndex += 1;
		code.remove(charIndex, charIndex + 2);

		// how we do the next part depends on a number of factors – whether
		// this is a top-level statement, and whether we're updating a
		// simple or complex reference
		let base;

		const left = this.left.unparenthesize();

		if (left.type === 'Identifier') {
			base = scope.resolveName(left.name);
		} else if (left.type === 'MemberExpression') {
			let object;
			let needsObjectVar = false;
			let property;
			let needsPropertyVar = false;

			const statement = this.findNearest(/(?:Statement|Declaration)$/);
			const i0 = statement.getIndentation();

			if (left.property.type === 'Identifier') {
				property = left.computed
					? scope.resolveName(left.property.name)
					: left.property.name;
			} else {
				property = scope.createDeclaration('property');
				needsPropertyVar = true;
			}

			if (left.object.type === 'Identifier') {
				object = scope.resolveName(left.object.name);
			} else {
				object = scope.createDeclaration('object');
				needsObjectVar = true;
			}

			if (left.start === statement.start) {
				if (needsObjectVar && needsPropertyVar) {
					code.prependRight(statement.start, `${object} = `);
					code.overwrite(
						left.object.end,
						left.property.start,
						`;\n${i0}${property} = `
					);
					code.overwrite(
						left.property.end,
						left.end,
						`;\n${i0}${object}[${property}]`
					);
				} else if (needsObjectVar) {
					code.prependRight(statement.start, `${object} = `);
					code.appendLeft(left.object.end, `;\n${i0}`);
					code.appendLeft(left.object.end, object);
				} else if (needsPropertyVar) {
					code.prependRight(left.property.start, `${property} = `);
					code.appendLeft(left.property.end, `;\n${i0}`);
					code.move(left.property.start, left.property.end, this.start);

					code.appendLeft(left.object.end, `[${property}]`);
					code.remove(left.object.end, left.property.start);
					code.remove(left.property.end, left.end);
				}
			} else {
				if (needsObjectVar && needsPropertyVar) {
					code.prependRight(left.start, `( ${object} = `);
					code.overwrite(
						left.object.end,
						left.property.start,
						`, ${property} = `
					);
					code.overwrite(
						left.property.end,
						left.end,
						`, ${object}[${property}]`
					);
				} else if (needsObjectVar) {
					code.prependRight(left.start, `( ${object} = `);
					code.appendLeft(left.object.end, `, ${object}`);
				} else if (needsPropertyVar) {
					code.prependRight(left.property.start, `( ${property} = `);
					code.appendLeft(left.property.end, `, `);
					code.move(left.property.start, left.property.end, left.start);

					code.overwrite(left.object.end, left.property.start, `[${property}]`);
					code.remove(left.property.end, left.end);
				}

				if (needsPropertyVar) {
					code.appendLeft(this.end, ` )`);
				}
			}

			base =
				object +
				(left.computed || needsPropertyVar ? `[${property}]` : `.${property}`);
		}

		code.prependRight(this.right.start, `Math.pow( ${base}, `);
		code.appendLeft(this.right.end, ` )`);
	}
}
