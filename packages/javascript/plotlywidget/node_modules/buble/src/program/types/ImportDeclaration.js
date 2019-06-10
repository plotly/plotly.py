import Node from '../Node.js';
import CompileError from '../../utils/CompileError.js';

export default class ImportDeclaration extends Node {
	initialise(transforms) {
		if (transforms.moduleImport)
			CompileError.missingTransform("import", "moduleImport", this);
		super.initialise(transforms);
	}
}
