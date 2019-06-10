// @flow

import { toString, array, ValueType, StringType, NumberType, BooleanType, checkSubtype } from '../types';

import { typeOf } from '../values';
import RuntimeError from '../runtime_error';

import type { Expression } from '../expression';
import type ParsingContext from '../parsing_context';
import type EvaluationContext from '../evaluation_context';
import type { ArrayType } from '../types';

const types = {
    string: StringType,
    number: NumberType,
    boolean: BooleanType
};

class ArrayAssertion implements Expression {
    type: ArrayType;
    input: Expression;

    constructor(type: ArrayType, input: Expression) {
        this.type = type;
        this.input = input;
    }

    static parse(args: Array<mixed>, context: ParsingContext): ?Expression {
        if (args.length < 2 || args.length > 4)
            return context.error(`Expected 1, 2, or 3 arguments, but found ${args.length - 1} instead.`);

        let itemType;
        let N;
        if (args.length > 2) {
            const type = args[1];
            if (typeof type !== 'string' || !(type in types))
                return context.error('The item type argument of "array" must be one of string, number, boolean', 1);
            itemType = types[type];
        } else {
            itemType = ValueType;
        }

        if (args.length > 3) {
            if (
                typeof args[2] !== 'number' ||
                args[2] < 0 ||
                args[2] !== Math.floor(args[2])
            ) {
                return context.error('The length argument to "array" must be a positive integer literal', 2);
            }
            N = args[2];
        }

        const type = array(itemType, N);

        const input = context.parse(args[args.length - 1], args.length - 1, ValueType);
        if (!input) return null;

        return new ArrayAssertion(type, input);
    }

    evaluate(ctx: EvaluationContext) {
        const value = this.input.evaluate(ctx);
        const error = checkSubtype(this.type, typeOf(value));
        if (error) {
            throw new RuntimeError(`Expected value to be of type ${toString(this.type)}, but found ${toString(typeOf(value))} instead.`);
        }
        return value;
    }

    eachChild(fn: (Expression) => void) {
        fn(this.input);
    }

    possibleOutputs() {
        return this.input.possibleOutputs();
    }

    serialize() {
        const serialized = ["array"];
        const itemType = this.type.itemType;
        if (itemType.kind === 'string' ||
            itemType.kind === 'number' ||
            itemType.kind === 'boolean') {
            serialized.push(itemType.kind);
            const N = this.type.N;
            if (typeof N === 'number') {
                serialized.push(N);
            }
        }
        serialized.push(this.input.serialize());
        return serialized;
    }
}

export default ArrayAssertion;
