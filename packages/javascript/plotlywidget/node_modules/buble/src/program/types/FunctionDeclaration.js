import Node from '../Node.js';
import CompileError from '../../utils/CompileError.js';
import removeTrailingComma from '../../utils/removeTrailingComma.js';

export default class FunctionDeclaration extends Node {
	initialise(transforms) {
		if (this.generator && transforms.generator) {
			CompileError.missingTransform("generators", "generator", this);
		}
		if (this.async && transforms.asyncAwait) {
			CompileError.missingTransform("async functions", "asyncAwait", this);
		}

		this.body.createScope();

		if (this.id) {
			this.findScope(true).addDeclaration(this.id, 'function');
		}
		super.initialise(transforms);
	}

	transpile(code, transforms) {
		super.transpile(code, transforms);
		if (transforms.trailingFunctionCommas && this.params.length) {
			removeTrailingComma(code, this.params[this.params.length - 1].end);
		}
	}
}
