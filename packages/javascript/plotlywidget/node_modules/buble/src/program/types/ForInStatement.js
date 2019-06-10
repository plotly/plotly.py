import LoopStatement from './shared/LoopStatement.js';
import destructure from '../../utils/destructure.js';
import extractNames from '../extractNames.js';

export default class ForInStatement extends LoopStatement {
	findScope(functionScope) {
		return functionScope || !this.createdScope
			? this.parent.findScope(functionScope)
			: this.body.scope;
	}

	transpile(code, transforms) {
		const hasDeclaration = this.left.type === 'VariableDeclaration';

		if (this.shouldRewriteAsFunction) {
			// which variables are declared in the init statement?
			const names = hasDeclaration
				? this.left.declarations.map(declarator => extractNames(declarator.id))
				: [];

			this.args = names.map(
				name => (name in this.aliases ? this.aliases[name].outer : name)
			);
			this.params = names.map(
				name => (name in this.aliases ? this.aliases[name].inner : name)
			);
		}

		super.transpile(code, transforms);

		const maybePattern = hasDeclaration ? this.left.declarations[0].id : this.left;
		if (maybePattern.type !== 'Identifier') {
			this.destructurePattern(code, maybePattern, hasDeclaration);
		}
	}

	destructurePattern(code, pattern, isDeclaration) {
		const scope = this.findScope(true);
		const i0 = this.getIndentation();
		const i1 = i0 + code.getIndentString();

		const ref = scope.createIdentifier('ref');

		const bodyStart = this.body.body.length ? this.body.body[0].start : this.body.start + 1;

		code.move(pattern.start, pattern.end, bodyStart);

		code.prependRight(pattern.end, isDeclaration ? ref : `var ${ref}`);

		const statementGenerators = [];
		destructure(
			code,
			id => scope.createIdentifier(id),
			({ name }) => scope.resolveName(name),
			pattern,
			ref,
			false,
			statementGenerators
		);

		let suffix = `;\n${i1}`;
		statementGenerators.forEach((fn, i) => {
			if (i === statementGenerators.length - 1) {
				suffix = `;\n\n${i1}`;
			}

			fn(bodyStart, '', suffix);
		});
	}
}
