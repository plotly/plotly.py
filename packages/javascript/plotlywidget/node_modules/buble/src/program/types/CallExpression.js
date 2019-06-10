import Node from '../Node.js';
import spread, { isArguments, inlineSpreads, needsParentheses } from '../../utils/spread.js';
import removeTrailingComma from '../../utils/removeTrailingComma.js';

export default class CallExpression extends Node {
	initialise(transforms) {
		if (transforms.spreadRest && this.arguments.length > 1) {
			const lexicalBoundary = this.findLexicalBoundary();

			let i = this.arguments.length;
			while (i--) {
				const arg = this.arguments[i];
				if (arg.type === 'SpreadElement' && isArguments(arg.argument)) {
					this.argumentsArrayAlias = lexicalBoundary.getArgumentsArrayAlias();
				}
			}
		}

		super.initialise(transforms);
	}

	transpile(code, transforms) {
		if (transforms.spreadRest && this.arguments.length) {
			inlineSpreads(code, this, this.arguments);
			// this.arguments.length may have changed, must retest.
		}

		if (transforms.spreadRest && this.arguments.length) {
			let hasSpreadElements = false;
			let context;

			const firstArgument = this.arguments[0];

			if (this.arguments.length === 1) {
				if (firstArgument.type === 'SpreadElement') {
					code.remove(firstArgument.start, firstArgument.argument.start);
					hasSpreadElements = true;
				}
			} else {
				hasSpreadElements = spread(
					code,
					this.arguments,
					firstArgument.start,
					this.argumentsArrayAlias
				);
			}

			if (hasSpreadElements) {
				// we need to handle super() and super.method() differently
				// due to its instance
				let _super = null;
				if (this.callee.type === 'Super') {
					_super = this.callee;
				} else if (
					this.callee.type === 'MemberExpression' &&
					this.callee.object.type === 'Super'
				) {
					_super = this.callee.object;
				}

				if (!_super && this.callee.type === 'MemberExpression') {
					if (this.callee.object.type === 'Identifier') {
						context = this.callee.object.name;
					} else {
						context = this.findScope(true).createDeclaration('ref');
						const callExpression = this.callee.object;
						code.prependRight(callExpression.start, `(${context} = `);
						code.appendLeft(callExpression.end, `)`);
					}
				} else {
					context = 'void 0';
				}

				code.appendLeft(this.callee.end, '.apply');

				if (_super) {
					_super.noCall = true; // bit hacky...

					if (this.arguments.length > 1) {
						if (firstArgument.type === 'SpreadElement') {
							if (needsParentheses(firstArgument.argument)) {
								code.prependRight(firstArgument.start, `( `);
							}
						} else {
							code.prependRight(firstArgument.start, `[ `);
						}

						code.appendLeft(
							this.arguments[this.arguments.length - 1].end,
							' )'
						);
					}
				} else if (this.arguments.length === 1) {
					code.prependRight(firstArgument.start, `${context}, `);
				} else {
					if (firstArgument.type === 'SpreadElement') {
						if (needsParentheses(firstArgument.argument)) {
							code.appendLeft(firstArgument.start, `${context}, ( `);
						} else {
							code.appendLeft(firstArgument.start, `${context}, `);
						}
					} else {
						code.appendLeft(firstArgument.start, `${context}, [ `);
					}

					code.appendLeft(this.arguments[this.arguments.length - 1].end, ' )');
				}
			}
		}

		if (transforms.trailingFunctionCommas && this.arguments.length) {
			removeTrailingComma(code, this.arguments[this.arguments.length - 1].end);
		}

		super.transpile(code, transforms);
	}
}
