import Node from '../Node.js';

export default class TemplateLiteral extends Node {
	transpile(code, transforms) {
		super.transpile(code, transforms);

		if (
			transforms.templateString &&
			this.parent.type !== 'TaggedTemplateExpression'
		) {
			const ordered = this.expressions
				.concat(this.quasis)
				.sort((a, b) => a.start - b.start || a.end - b.end)
				.filter((node, i) => {
					// include all expressions
					if (node.type !== 'TemplateElement') return true;

					// include all non-empty strings
					if (node.value.raw) return true;

					// exclude all empty strings not at the head
					return !i;
				});

			// special case – we may be able to skip the first element,
			// if it's the empty string, but only if the second and
			// third elements aren't both expressions (since they maybe
			// be numeric, and `1 + 2 + '3' === '33'`)
			if (ordered.length >= 3) {
				const [first, , third] = ordered;
				if (
					first.type === 'TemplateElement' &&
					first.value.raw === '' &&
					third.type === 'TemplateElement'
				) {
					ordered.shift();
				}
			}

			const parenthesise =
				(this.quasis.length !== 1 || this.expressions.length !== 0) &&
				this.parent.type !== 'TemplateLiteral' &&
				this.parent.type !== 'AssignmentExpression' &&
				this.parent.type !== 'AssignmentPattern' &&
				this.parent.type !== 'VariableDeclarator' &&
				(this.parent.type !== 'BinaryExpression' ||
					this.parent.operator !== '+');

			if (parenthesise) code.appendRight(this.start, '(');

			let lastIndex = this.start;

			ordered.forEach((node, i) => {
				let prefix = i === 0 ? (parenthesise ? '(' : '') : ' + ';

				if (node.type === 'TemplateElement') {
					code.overwrite(
						lastIndex,
						node.end,
						prefix + JSON.stringify(node.value.cooked)
					);
				} else {
					const parenthesise = node.type !== 'Identifier'; // TODO other cases where it's safe

					if (parenthesise) prefix += '(';

					code.remove(lastIndex, node.start);

					if (prefix) code.prependRight(node.start, prefix);
					if (parenthesise) code.appendLeft(node.end, ')');
				}

				lastIndex = node.end;
			});

			if (parenthesise) code.appendLeft(lastIndex, ')');
			code.overwrite(lastIndex, this.end, "", { contentOnly: true });
		}
	}
}
