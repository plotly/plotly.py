// @flow

import assert from 'assert';

import extend from '../util/extend';

import type {StylePropertySpecification} from '../style-spec';

export default convertFunction;

function convertFunction(parameters: PropertyValueSpecification<any>, propertySpec: StylePropertySpecification) {
    let expression;

    parameters = extend({}, parameters);
    let defaultExpression;
    if (typeof parameters.default !== 'undefined') {
        defaultExpression = convertValue(parameters.default, propertySpec);
    } else {
        defaultExpression = convertValue(propertySpec.default, propertySpec);
        if (defaultExpression === null) {
            defaultExpression = ['error', 'No default property value available.'];
        }
    }

    if (parameters.stops) {
        const zoomAndFeatureDependent = parameters.stops && typeof parameters.stops[0][0] === 'object';
        const featureDependent = zoomAndFeatureDependent || parameters.property !== undefined;
        const zoomDependent = zoomAndFeatureDependent || !featureDependent;

        const stops = parameters.stops.map((stop) => {
            if (!featureDependent && propertySpec.tokens && typeof stop[1] === 'string') {
                return [stop[0], convertTokenString(stop[1])];

            }
            return [stop[0], convertValue(stop[1], propertySpec)];
        });

        if (parameters.colorSpace && parameters.colorSpace !== 'rgb') {
            throw new Error('Unimplemented');
        }

        if (zoomAndFeatureDependent) {
            expression = convertZoomAndPropertyFunction(parameters, propertySpec, stops, defaultExpression);
        } else if (zoomDependent) {
            expression = convertZoomFunction(parameters, propertySpec, stops);
        } else {
            expression = convertPropertyFunction(parameters, propertySpec, stops, defaultExpression);
        }
    } else {
        // identity function
        expression = convertIdentityFunction(parameters, propertySpec, defaultExpression);
    }

    return expression;
}

function convertIdentityFunction(parameters, propertySpec, defaultExpression) {
    const get = ['get', parameters.property];

    if (propertySpec.type === 'color') {
        return parameters.default === undefined ? get : ['to-color', get, parameters.default];
    } else if (propertySpec.type === 'array' && typeof propertySpec.length === 'number') {
        return ['array', propertySpec.value, propertySpec.length, get];
    } else if (propertySpec.type === 'array') {
        return ['array', propertySpec.value, get];
    } else if (propertySpec.type === 'enum') {
        return [
            'let',
            'property_value', ['string', get],
            [
                'match',
                ['var', 'property_value'],
                Object.keys(propertySpec.values), ['var', 'property_value'],
                defaultExpression
            ]
        ];
    } else {
        return parameters.default === undefined ? get : [propertySpec.type, get, parameters.default];
    }
}

function convertValue(value, spec) {
    if (typeof value === 'undefined' || value === null) return null;
    if (spec.type === 'color') {
        return value;
    } else if (spec.type === 'array') {
        return ['literal', value];
    } else {
        return value;
    }
}

function convertZoomAndPropertyFunction(parameters, propertySpec, stops, defaultExpression) {
    const featureFunctionParameters = {};
    const featureFunctionStops = {};
    const zoomStops = [];
    for (let s = 0; s < stops.length; s++) {
        const stop = stops[s];
        const zoom = stop[0].zoom;
        if (featureFunctionParameters[zoom] === undefined) {
            featureFunctionParameters[zoom] = {
                zoom: zoom,
                type: parameters.type,
                property: parameters.property,
                default: parameters.default,
            };
            featureFunctionStops[zoom] = [];
            zoomStops.push(zoom);
        }
        featureFunctionStops[zoom].push([stop[0].value, stop[1]]);
    }

    // the interpolation type for the zoom dimension of a zoom-and-property
    // function is determined directly from the style property specification
    // for which it's being used: linear for interpolatable properties, step
    // otherwise.
    const functionType = getFunctionType({}, propertySpec);
    if (functionType === 'exponential') {
        const expression = ['interpolate', ['linear'], ['zoom']];

        for (const z of zoomStops) {
            const output = convertPropertyFunction(featureFunctionParameters[z], propertySpec, featureFunctionStops[z], defaultExpression);
            appendStopPair(expression, z, output, false);
        }

        return expression;
    } else {
        const expression = ['step', ['zoom']];

        for (const z of zoomStops) {
            const output = convertPropertyFunction(featureFunctionParameters[z], propertySpec, featureFunctionStops[z], defaultExpression);
            appendStopPair(expression, z, output, true);
        }

        fixupDegenerateStepCurve(expression);

        return expression;
    }
}

function convertPropertyFunction(parameters, propertySpec, stops, defaultExpression) {
    const type = getFunctionType(parameters, propertySpec);

    const inputType = typeof stops[0][0];
    assert(
        inputType === 'string' ||
        inputType === 'number' ||
        inputType === 'boolean'
    );

    let input = [inputType, ['get', parameters.property]];

    let expression;
    let isStep = false;
    if (type === 'categorical' && inputType === 'boolean') {
        assert(parameters.stops.length > 0 && parameters.stops.length <= 2);
        if (parameters.stops[0][0] === false) {
            input = ['!', input];
        }
        expression = [ 'case', input, parameters.stops[0][1] ];
        if (parameters.stops.length > 1) {
            expression.push(parameters.stops[1][1]);
        } else {
            expression.push(defaultExpression);
        }
        return expression;
    } else if (type === 'categorical') {
        expression = ['match', input];
    } else if (type === 'interval') {
        expression = ['step', input];
        isStep = true;
    } else if (type === 'exponential') {
        const base = parameters.base !== undefined ? parameters.base : 1;
        expression = ['interpolate', ['exponential', base], input];
    } else {
        throw new Error(`Unknown property function type ${type}`);
    }

    for (const stop of stops) {
        appendStopPair(expression, stop[0], stop[1], isStep);
    }

    if (expression[0] === 'match') {
        expression.push(defaultExpression);
    }

    fixupDegenerateStepCurve(expression);

    return expression;
}

function convertZoomFunction(parameters, propertySpec, stops, input = ['zoom']) {
    const type = getFunctionType(parameters, propertySpec);
    let expression;
    let isStep = false;
    if (type === 'interval') {
        expression = ['step', input];
        isStep = true;
    } else if (type === 'exponential') {
        const base = parameters.base !== undefined ? parameters.base : 1;
        expression = ['interpolate', ['exponential', base], input];
    } else {
        throw new Error(`Unknown zoom function type "${type}"`);
    }

    for (const stop of stops) {
        appendStopPair(expression, stop[0], stop[1], isStep);
    }

    fixupDegenerateStepCurve(expression);

    return expression;
}

function fixupDegenerateStepCurve(expression) {
    // degenerate step curve (i.e. a constant function): add a noop stop
    if (expression[0] === 'step' && expression.length === 3) {
        expression.push(0);
        expression.push(expression[3]);
    }
}

function appendStopPair(curve, input, output, isStep) {
    // Skip duplicate stop values. They were not validated for functions, but they are for expressions.
    // https://github.com/mapbox/mapbox-gl-js/issues/4107
    if (curve.length > 3 && input === curve[curve.length - 2]) {
        return;
    }
    // step curves don't get the first input value, as it is redundant.
    if (!(isStep && curve.length === 2)) {
        curve.push(input);
    }
    curve.push(output);
}

function getFunctionType(parameters, propertySpec) {
    if (parameters.type) {
        return parameters.type;
    } else if (propertySpec.function) {
        return propertySpec.function === 'interpolated' ? 'exponential' : 'interval';
    } else {
        return 'exponential';
    }
}

// "String with {name} token" => ["concat", "String with ", ["get", "name"], " token"]
function convertTokenString(s) {
    const result = ['concat'];
    const re = /{([^{}]+)}/g;
    let pos = 0;
    let match;
    while ((match = re.exec(s)) !== null) {
        const literal = s.slice(pos, re.lastIndex - match[0].length);
        pos = re.lastIndex;
        if (literal.length > 0) result.push(literal);
        result.push(['to-string', ['get', match[1]]]);
    }

    if (result.length === 1) {
        return s;
    }

    if (pos < s.length) {
        result.push(s.slice(pos));
    } else if (result.length === 2) {
        return result[1];
    }

    return result;
}

