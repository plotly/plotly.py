import Node from '../Node.js';
import CompileError from '../../utils/CompileError.js';

export default class Import extends Node {
	initialise(transforms) {
		if (transforms.moduleImport) {
			CompileError.missingTransform("dynamic import expressions", "moduleImport", this);
		}
		super.initialise(transforms);
	}
}
