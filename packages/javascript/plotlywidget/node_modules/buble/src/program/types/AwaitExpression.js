import Node from '../Node.js';
import CompileError from '../../utils/CompileError.js';

export default class AwaitExpression extends Node {
	initialise(transforms) {
		if (transforms.asyncAwait) {
			CompileError.missingTransform("await", "asyncAwait", this);
		}
		super.initialise(transforms);
	}
}
