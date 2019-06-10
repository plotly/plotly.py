import Node from '../Node.js';
import CompileError from '../../utils/CompileError.js';

export default class ExportDefaultDeclaration extends Node {
	initialise(transforms) {
		if (transforms.moduleExport)
			CompileError.missingTransform("export", "moduleExport", this);
		super.initialise(transforms);
	}
}
