import Node from '../Node.js';
import CompileError from '../../utils/CompileError.js';
import { loopStatement } from '../../utils/patterns.js';

export default class Super extends Node {
	initialise(transforms) {
		if (transforms.classes) {
			this.method = this.findNearest('MethodDefinition');
			if (!this.method)
				throw new CompileError('use of super outside class method', this);

			const parentClass = this.findNearest('ClassBody').parent;
			this.superClassName =
				parentClass.superClass && (parentClass.superClass.name || 'superclass');

			if (!this.superClassName)
				throw new CompileError('super used in base class', this);

			this.isCalled =
				this.parent.type === 'CallExpression' && this === this.parent.callee;

			if (this.method.kind !== 'constructor' && this.isCalled) {
				throw new CompileError(
					'super() not allowed outside class constructor',
					this
				);
			}

			this.isMember = this.parent.type === 'MemberExpression';

			if (!this.isCalled && !this.isMember) {
				throw new CompileError(
					'Unexpected use of `super` (expected `super(...)` or `super.*`)',
					this
				);
			}
		}

		if (transforms.arrow) {
			const lexicalBoundary = this.findLexicalBoundary();
			const arrowFunction = this.findNearest('ArrowFunctionExpression');
			const loop = this.findNearest(loopStatement);

			if (arrowFunction && arrowFunction.depth > lexicalBoundary.depth) {
				this.thisAlias = lexicalBoundary.getThisAlias();
			}

			if (
				loop &&
				loop.body.contains(this) &&
				loop.depth > lexicalBoundary.depth
			) {
				this.thisAlias = lexicalBoundary.getThisAlias();
			}
		}
	}

	transpile(code, transforms) {
		if (transforms.classes) {
			const expression =
				this.isCalled || this.method.static
					? this.superClassName
					: `${this.superClassName}.prototype`;

			code.overwrite(this.start, this.end, expression, {
				storeName: true,
				contentOnly: true
			});

			const callExpression = this.isCalled ? this.parent : this.parent.parent;

			if (callExpression && callExpression.type === 'CallExpression') {
				if (!this.noCall) {
					// special case – `super( ...args )`
					code.appendLeft(callExpression.callee.end, '.call');
				}

				const thisAlias = this.thisAlias || 'this';

				if (callExpression.arguments.length) {
					code.appendLeft(callExpression.arguments[0].start, `${thisAlias}, `);
				} else {
					code.appendLeft(callExpression.end - 1, `${thisAlias}`);
				}
			}
		}
	}
}
