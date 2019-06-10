import Node from '../Node.js';
import CompileError from '../../utils/CompileError.js';

export default class ObjectExpression extends Node {
	transpile(code, transforms) {
		super.transpile(code, transforms);

		let firstPropertyStart = this.start + 1;
		let spreadPropertyCount = 0;
		let computedPropertyCount = 0;
		let firstSpreadProperty = null;
		let firstComputedProperty = null;

		for (let i = 0; i < this.properties.length; ++i) {
			const prop = this.properties[i];
			if (prop.type === 'SpreadElement') {
				// First see if we can inline the spread, to save needing objectAssign.
				const argument = prop.argument;
				if (
					argument.type === 'ObjectExpression' || (
						argument.type === 'Literal' &&
						typeof argument.value !== 'string'
					)
				) {
					if (argument.type === 'ObjectExpression' && argument.properties.length > 0) {
						// Strip the `...{` and the `}` with a possible trailing comma before it,
						// leaving just the possible trailing comma after it.
						code.remove(prop.start, argument.properties[0].start);
						code.remove(argument.properties[argument.properties.length - 1].end, prop.end);
						this.properties.splice(i, 1, ...argument.properties);
						i--;
					} else {
						// An empty object, boolean, null, undefined, number or regexp (but NOT
						// string) will spread to nothing, so just remove the element altogether,
						// including a possible trailing comma.
						code.remove(prop.start, i === this.properties.length - 1
							? prop.end
							: this.properties[i + 1].start);
						this.properties.splice(i, 1);
						i--;
					}
				} else {
					spreadPropertyCount += 1;
					if (firstSpreadProperty === null) firstSpreadProperty = i;
				}
			} else if (prop.computed && transforms.computedProperty) {
				computedPropertyCount += 1;
				if (firstComputedProperty === null) firstComputedProperty = i;
			}
		}

		if (spreadPropertyCount && !transforms.objectRestSpread && !(computedPropertyCount && transforms.computedProperty)) {
			spreadPropertyCount = 0;
			firstSpreadProperty = null;
		} else if (spreadPropertyCount) {
			if (!this.program.options.objectAssign) {
				throw new CompileError(
					"Object spread operator requires specified objectAssign option with 'Object.assign' or polyfill helper.",
					this
				);
			}
			let i = this.properties.length;
			while (i--) {
				const prop = this.properties[i];

				// enclose run of non-spread properties in curlies
				if (prop.type === 'Property' && !computedPropertyCount) {
					const lastProp = this.properties[i - 1];
					const nextProp = this.properties[i + 1];

					if (!lastProp || lastProp.type !== 'Property') {
						code.prependRight(prop.start, '{');
					}

					if (!nextProp || nextProp.type !== 'Property') {
						code.appendLeft(prop.end, '}');
					}
				}

				// Remove ellipsis on spread property
				if (prop.type === 'SpreadElement') {
					code.remove(prop.start, prop.argument.start);
					code.remove(prop.argument.end, prop.end);
				}
			}

			// wrap the whole thing in Object.assign
			firstPropertyStart = this.properties[0].start;
			if (!computedPropertyCount) {
				code.overwrite(
					this.start,
					firstPropertyStart,
					`${this.program.options.objectAssign}({}, `
				);
				code.overwrite(
					this.properties[this.properties.length - 1].end,
					this.end,
					')'
				);
			} else if (this.properties[0].type === 'SpreadElement') {
				code.overwrite(
					this.start,
					firstPropertyStart,
					`${this.program.options.objectAssign}({}, `
				);
				code.remove(this.end - 1, this.end);
				code.appendRight(this.end, ')');
			} else {
				code.prependLeft(this.start, `${this.program.options.objectAssign}(`);
				code.appendRight(this.end, ')');
			}
		}

		if (computedPropertyCount && transforms.computedProperty) {
			const i0 = this.getIndentation();

			let isSimpleAssignment;
			let name;

			if (
				this.parent.type === 'VariableDeclarator' &&
				this.parent.parent.declarations.length === 1 &&
				this.parent.id.type === 'Identifier'
			) {
				isSimpleAssignment = true;
				name = this.parent.id.alias || this.parent.id.name; // TODO is this right?
			} else if (
				this.parent.type === 'AssignmentExpression' &&
				this.parent.parent.type === 'ExpressionStatement' &&
				this.parent.left.type === 'Identifier'
			) {
				isSimpleAssignment = true;
				name = this.parent.left.alias || this.parent.left.name; // TODO is this right?
			} else if (
				this.parent.type === 'AssignmentPattern' &&
				this.parent.left.type === 'Identifier'
			) {
				isSimpleAssignment = true;
				name = this.parent.left.alias || this.parent.left.name; // TODO is this right?
			}

			if (spreadPropertyCount) isSimpleAssignment = false;

			// handle block scoping
			name = this.findScope(false).resolveName(name);

			const start = firstPropertyStart;
			const end = this.end;

			if (isSimpleAssignment) {
				// ???
			} else {
				if (
					firstSpreadProperty === null ||
					firstComputedProperty < firstSpreadProperty
				) {
					name = this.findScope(true).createDeclaration('obj');

					code.prependRight(this.start, `( ${name} = `);
				} else name = null; // We don't actually need this variable
			}

			const len = this.properties.length;
			let lastComputedProp;
			let sawNonComputedProperty = false;
			let isFirst = true;

			for (let i = 0; i < len; i += 1) {
				const prop = this.properties[i];
				let moveStart = i > 0 ? this.properties[i - 1].end : start;

				if (
					prop.type === 'Property' &&
					(prop.computed || (lastComputedProp && !spreadPropertyCount))
				) {
					if (i === 0) moveStart = this.start + 1; // Trim leading whitespace
					lastComputedProp = prop;

					if (!name) {
						name = this.findScope(true).createDeclaration('obj');

						const propId = name + (prop.computed ? '' : '.');
						code.appendRight(prop.start, `( ${name} = {}, ${propId}`);
					} else {
						const propId =
							(isSimpleAssignment ? `;\n${i0}${name}` : `, ${name}`) +
							(prop.key.type === 'Literal' || prop.computed ? '' : '.');

						if (moveStart < prop.start) {
							code.overwrite(moveStart, prop.start, propId);
						} else {
							code.prependRight(prop.start, propId);
						}
					}

					let c = prop.key.end;
					if (prop.computed) {
						while (code.original[c] !== ']') c += 1;
						c += 1;
					}
					if (prop.key.type === 'Literal' && !prop.computed) {
						code.overwrite(
							prop.start,
							prop.key.end + 1,
							'[' + code.slice(prop.start, prop.key.end) + '] = '
						);
					} else if (prop.shorthand || (prop.method && !prop.computed && transforms.conciseMethodProperty)) {
						// Replace : with = if Property::transpile inserted the :
						code.overwrite(
							prop.key.start,
							prop.key.end,
							code.slice(prop.key.start, prop.key.end).replace(/:/, ' =')
						);
					} else {
						if (prop.value.start > c) code.remove(c, prop.value.start);
						code.prependLeft(c, ' = ');
					}

					// This duplicates behavior from Property::transpile which is disabled
					// for computed properties or if conciseMethodProperty is false
					if (prop.method && (prop.computed || !transforms.conciseMethodProperty)) {
						if (prop.value.generator) code.remove(prop.start, prop.key.start);
						code.prependRight(prop.value.start, `function${prop.value.generator ? '*' : ''} `);
					}
				} else if (prop.type === 'SpreadElement') {
					if (name && i > 0) {
						if (!lastComputedProp) {
							lastComputedProp = this.properties[i - 1];
						}
						code.appendLeft(lastComputedProp.end, `, ${name} )`);

						lastComputedProp = null;
						name = null;
					}
				} else {
					if (!isFirst && spreadPropertyCount) {
						// We are in an Object.assign context, so we need to wrap regular properties
						code.prependRight(prop.start, '{');
						code.appendLeft(prop.end, '}');
					}
					sawNonComputedProperty = true;
				}
				if (isFirst && (prop.type === 'SpreadElement' || prop.computed)) {
					let beginEnd = sawNonComputedProperty
						? this.properties[this.properties.length - 1].end
						: this.end - 1;
					// Trim trailing comma because it can easily become a leading comma which is illegal
					if (code.original[beginEnd] == ',') ++beginEnd;
					const closing = code.slice(beginEnd, end);
					code.prependLeft(moveStart, closing);
					code.remove(beginEnd, end);
					isFirst = false;
				}

				// Clean up some extranous whitespace
				let c = prop.end;
				if (i < len - 1 && !sawNonComputedProperty) {
					while (code.original[c] !== ',') c += 1;
				} else if (i == len - 1) c = this.end;
				if (prop.end != c) code.overwrite(prop.end, c, '', {contentOnly: true});
			}

			if (!isSimpleAssignment && name) {
				code.appendLeft(lastComputedProp.end, `, ${name} )`);
			}
		}
	}
}
