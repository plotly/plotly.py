import ArrayExpression from './ArrayExpression.js';
import ArrowFunctionExpression from './ArrowFunctionExpression.js';
import AssignmentExpression from './AssignmentExpression.js';
import AwaitExpression from './AwaitExpression.js';
import BinaryExpression from './BinaryExpression.js';
import BreakStatement from './BreakStatement.js';
import CallExpression from './CallExpression.js';
import ClassBody from './ClassBody.js';
import ClassDeclaration from './ClassDeclaration.js';
import ClassExpression from './ClassExpression.js';
import ContinueStatement from './ContinueStatement.js';
import ExportDefaultDeclaration from './ExportDefaultDeclaration.js';
import ExportNamedDeclaration from './ExportNamedDeclaration.js';
import ForStatement from './ForStatement.js';
import ForInStatement from './ForInStatement.js';
import ForOfStatement from './ForOfStatement.js';
import FunctionDeclaration from './FunctionDeclaration.js';
import FunctionExpression from './FunctionExpression.js';
import Identifier from './Identifier.js';
import IfStatement from './IfStatement.js';
import Import from './Import.js';
import ImportDeclaration from './ImportDeclaration.js';
import ImportDefaultSpecifier from './ImportDefaultSpecifier.js';
import ImportSpecifier from './ImportSpecifier.js';
import JSXAttribute from './JSXAttribute.js';
import JSXClosingElement from './JSXClosingElement.js';
import JSXClosingFragment from './JSXClosingFragment.js';
import JSXElement from './JSXElement.js';
import JSXExpressionContainer from './JSXExpressionContainer.js';
import JSXFragment from './JSXFragment.js';
import JSXOpeningElement from './JSXOpeningElement.js';
import JSXOpeningFragment from './JSXOpeningFragment.js';
import JSXSpreadAttribute from './JSXSpreadAttribute.js';
import Literal from './Literal.js';
import LoopStatement from './shared/LoopStatement.js';
import MemberExpression from './MemberExpression.js';
import NewExpression from './NewExpression.js';
import ObjectExpression from './ObjectExpression.js';
import Property from './Property.js';
import ReturnStatement from './ReturnStatement.js';
import Super from './Super.js';
import TaggedTemplateExpression from './TaggedTemplateExpression.js';
import TemplateElement from './TemplateElement.js';
import TemplateLiteral from './TemplateLiteral.js';
import ThisExpression from './ThisExpression.js';
import UpdateExpression from './UpdateExpression.js';
import VariableDeclaration from './VariableDeclaration.js';
import VariableDeclarator from './VariableDeclarator.js';

export default {
	ArrayExpression,
	ArrowFunctionExpression,
	AssignmentExpression,
	AwaitExpression,
	BinaryExpression,
	BreakStatement,
	CallExpression,
	ClassBody,
	ClassDeclaration,
	ClassExpression,
	ContinueStatement,
	DoWhileStatement: LoopStatement,
	ExportNamedDeclaration,
	ExportDefaultDeclaration,
	ForStatement,
	ForInStatement,
	ForOfStatement,
	FunctionDeclaration,
	FunctionExpression,
	Identifier,
	IfStatement,
	Import,
	ImportDeclaration,
	ImportDefaultSpecifier,
	ImportSpecifier,
	JSXAttribute,
	JSXClosingElement,
	JSXClosingFragment,
	JSXElement,
	JSXExpressionContainer,
	JSXFragment,
	JSXOpeningElement,
	JSXOpeningFragment,
	JSXSpreadAttribute,
	Literal,
	MemberExpression,
	NewExpression,
	ObjectExpression,
	Property,
	ReturnStatement,
	Super,
	TaggedTemplateExpression,
	TemplateElement,
	TemplateLiteral,
	ThisExpression,
	UpdateExpression,
	VariableDeclaration,
	VariableDeclarator,
	WhileStatement: LoopStatement
};
