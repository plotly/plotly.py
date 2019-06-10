import Node from '../Node.js';
import CompileError from '../../utils/CompileError.js';
import removeTrailingComma from '../../utils/removeTrailingComma.js';

export default class FunctionExpression extends Node {
	initialise(transforms) {
		if (this.generator && transforms.generator) {
			CompileError.missingTransform("generators", "generator", this);
		}
		if (this.async && transforms.asyncAwait) {
			CompileError.missingTransform("async functions", "asyncAwait", this);
		}

		this.body.createScope();

		if (this.id) {
			// function expression IDs belong to the child scope...
			this.body.scope.addDeclaration(this.id, 'function');
		}

		super.initialise(transforms);

		const parent = this.parent;
		let methodName;

		if (
			transforms.conciseMethodProperty &&
			parent.type === 'Property' &&
			parent.kind === 'init' &&
			parent.method &&
			parent.key.type === 'Identifier'
		) {
			// object literal concise method
			methodName = parent.key.name;
		} else if (
			transforms.classes &&
			parent.type === 'MethodDefinition' &&
			parent.kind === 'method' &&
			parent.key.type === 'Identifier'
		) {
			// method definition in a class
			methodName = parent.key.name;
		} else if (this.id && this.id.type === 'Identifier') {
			// naked function expression
			methodName = this.id.alias || this.id.name;
		}

		if (methodName) {
			for (const param of this.params) {
				if (param.type === 'Identifier' && methodName === param.name) {
					// workaround for Safari 9/WebKit bug:
					// https://gitlab.com/Rich-Harris/buble/issues/154
					// change parameter name when same as method name

					const scope = this.body.scope;
					const declaration = scope.declarations[methodName];

					const alias = scope.createIdentifier(methodName);
					param.alias = alias;

					for (const identifier of declaration.instances) {
						identifier.alias = alias;
					}

					break;
				}
			}
		}
	}

	transpile(code, transforms) {
		super.transpile(code, transforms);
		if (transforms.trailingFunctionCommas && this.params.length) {
			removeTrailingComma(code, this.params[this.params.length - 1].end);
		}
	}
}
