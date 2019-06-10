// @flow

import { toString, ValueType, BooleanType, CollatorType } from '../types';

import type { Expression } from '../expression';
import type EvaluationContext from '../evaluation_context';
import type ParsingContext from '../parsing_context';
import type { Type } from '../types';

function isComparableType(type: Type) {
    return type.kind === 'string' ||
        type.kind === 'number' ||
        type.kind === 'boolean' ||
        type.kind === 'null';
}

/**
 * Special form for ==, !=, implementing the following signatures:
 * - (T1: Comparable, T2: Comparable) => boolean { T1 == T2 }
 * - (Comparable, value) => boolean
 * - (value, Comparable) => boolean
 *
 * Where Comparable = string | number | boolean | null.
 *
 * Evaluation semantics for the value cases are equivalent to Javascript's
 * strict equality (===/!==) -- i.e., when the value argument's type doesn't
 * match that of the Comparable argument, == evaluates to false, != to true.
 *
 * @private
 */
function makeComparison(op: string, negate: boolean) {
    return class Comparison implements Expression {
        type: Type;
        lhs: Expression;
        rhs: Expression;
        collator: Expression | null;

        constructor(lhs: Expression, rhs: Expression, collator: Expression | null) {
            this.type = BooleanType;
            this.lhs = lhs;
            this.rhs = rhs;
            this.collator = collator;
        }

        static parse(args: Array<mixed>, context: ParsingContext): ?Expression {
            if (args.length !== 3 && args.length !== 4)
                return context.error(`Expected two or three arguments.`);

            const lhs = context.parse(args[1], 1, ValueType);
            if (!lhs) return null;
            const rhs = context.parse(args[2], 2, ValueType);
            if (!rhs) return null;

            if (!isComparableType(lhs.type) && !isComparableType(rhs.type)) {
                return context.error(`Expected at least one argument to be a string, number, boolean, or null, but found (${toString(lhs.type)}, ${toString(rhs.type)}) instead.`);
            }

            if (lhs.type.kind !== rhs.type.kind && lhs.type.kind !== 'value' && rhs.type.kind !== 'value') {
                return context.error(`Cannot compare ${toString(lhs.type)} and ${toString(rhs.type)}.`);
            }

            let collator = null;
            if (args.length === 4) {
                if (lhs.type.kind !== 'string' && rhs.type.kind !== 'string') {
                    return context.error(`Cannot use collator to compare non-string types.`);
                }
                collator = context.parse(args[3], 3, CollatorType);
                if (!collator) return null;
            }

            return new Comparison(lhs, rhs, collator);
        }

        evaluate(ctx: EvaluationContext) {
            const equal = this.collator ?
                this.collator.evaluate(ctx).compare(this.lhs.evaluate(ctx), this.rhs.evaluate(ctx)) === 0 :
                this.lhs.evaluate(ctx) === this.rhs.evaluate(ctx);

            return negate ? !equal : equal;
        }

        eachChild(fn: (Expression) => void) {
            fn(this.lhs);
            fn(this.rhs);
            if (this.collator) {
                fn(this.collator);
            }
        }

        possibleOutputs() {
            return [true, false];
        }

        serialize() {
            const serialized = [op];
            this.eachChild(child => { serialized.push(child.serialize()); });
            return serialized;
        }
    };
}

export const Equals = makeComparison('==', false);
export const NotEquals = makeComparison('!=', true);
