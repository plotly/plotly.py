// @flow

import assert from 'assert';

import {
    ObjectType,
    ValueType,
    StringType,
    NumberType,
    BooleanType,
    checkSubtype,
    toString
} from '../types';
import RuntimeError from '../runtime_error';
import { typeOf } from '../values';

import type { Expression } from '../expression';
import type ParsingContext from '../parsing_context';
import type EvaluationContext from '../evaluation_context';
import type { Type } from '../types';

const types = {
    string: StringType,
    number: NumberType,
    boolean: BooleanType,
    object: ObjectType
};

class Assertion implements Expression {
    type: Type;
    args: Array<Expression>;

    constructor(type: Type, args: Array<Expression>) {
        this.type = type;
        this.args = args;
    }

    static parse(args: Array<mixed>, context: ParsingContext): ?Expression {
        if (args.length < 2)
            return context.error(`Expected at least one argument.`);

        const name: string = (args[0]: any);
        assert(types[name], name);

        const type = types[name];

        const parsed = [];
        for (let i = 1; i < args.length; i++) {
            const input = context.parse(args[i], i, ValueType);
            if (!input) return null;
            parsed.push(input);
        }

        return new Assertion(type, parsed);
    }

    evaluate(ctx: EvaluationContext) {
        for (let i = 0; i < this.args.length; i++) {
            const value = this.args[i].evaluate(ctx);
            const error = checkSubtype(this.type, typeOf(value));
            if (!error) {
                return value;
            } else if (i === this.args.length - 1) {
                throw new RuntimeError(`Expected value to be of type ${toString(this.type)}, but found ${toString(typeOf(value))} instead.`);
            }
        }

        assert(false);
        return null;
    }

    eachChild(fn: (Expression) => void) {
        this.args.forEach(fn);
    }

    possibleOutputs() {
        return [].concat(...this.args.map((arg) => arg.possibleOutputs()));
    }

    serialize() {
        return [this.type.kind].concat(this.args.map(arg => arg.serialize()));
    }
}

export default Assertion;
