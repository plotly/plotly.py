/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var isNumeric = require('fast-isnumeric');
var tinycolor = require('tinycolor2');

var baseTraceAttrs = require('../plots/attributes');
var colorscales = require('../components/colorscale/scales');
var DESELECTDIM = require('../constants/interactions').DESELECTDIM;

var nestedProperty = require('./nested_property');
var counterRegex = require('./regex').counter;
var modHalf = require('./mod').modHalf;
var isArrayOrTypedArray = require('./array').isArrayOrTypedArray;

exports.valObjectMeta = {
    data_array: {
        // You can use *dflt=[] to force said array to exist though.
        description: [
            'An {array} of data.',
            'The value MUST be an {array}, or we ignore it.',
            'Note that typed arrays (e.g. Float32Array) are supported.'
        ].join(' '),
        requiredOpts: [],
        otherOpts: ['dflt'],
        coerceFunction: function(v, propOut, dflt) {
            // TODO maybe `v: {type: 'float32', vals: [/* ... */]}` also
            if(isArrayOrTypedArray(v)) propOut.set(v);
            else if(dflt !== undefined) propOut.set(dflt);
        }
    },
    enumerated: {
        description: [
            'Enumerated value type. The available values are listed',
            'in `values`.'
        ].join(' '),
        requiredOpts: ['values'],
        otherOpts: ['dflt', 'coerceNumber', 'arrayOk'],
        coerceFunction: function(v, propOut, dflt, opts) {
            if(opts.coerceNumber) v = +v;
            if(opts.values.indexOf(v) === -1) propOut.set(dflt);
            else propOut.set(v);
        },
        validateFunction: function(v, opts) {
            if(opts.coerceNumber) v = +v;

            var values = opts.values;
            for(var i = 0; i < values.length; i++) {
                var k = String(values[i]);

                if((k.charAt(0) === '/' && k.charAt(k.length - 1) === '/')) {
                    var regex = new RegExp(k.substr(1, k.length - 2));
                    if(regex.test(v)) return true;
                } else if(v === values[i]) return true;
            }
            return false;
        }
    },
    'boolean': {
        description: 'A boolean (true/false) value.',
        requiredOpts: [],
        otherOpts: ['dflt'],
        coerceFunction: function(v, propOut, dflt) {
            if(v === true || v === false) propOut.set(v);
            else propOut.set(dflt);
        }
    },
    number: {
        description: [
            'A number or a numeric value',
            '(e.g. a number inside a string).',
            'When applicable, values greater (less) than `max` (`min`)',
            'are coerced to the `dflt`.'
        ].join(' '),
        requiredOpts: [],
        otherOpts: ['dflt', 'min', 'max', 'arrayOk'],
        coerceFunction: function(v, propOut, dflt, opts) {
            if(!isNumeric(v) ||
                    (opts.min !== undefined && v < opts.min) ||
                    (opts.max !== undefined && v > opts.max)) {
                propOut.set(dflt);
            } else propOut.set(+v);
        }
    },
    integer: {
        description: [
            'An integer or an integer inside a string.',
            'When applicable, values greater (less) than `max` (`min`)',
            'are coerced to the `dflt`.'
        ].join(' '),
        requiredOpts: [],
        otherOpts: ['dflt', 'min', 'max', 'arrayOk'],
        coerceFunction: function(v, propOut, dflt, opts) {
            if(v % 1 || !isNumeric(v) ||
                    (opts.min !== undefined && v < opts.min) ||
                    (opts.max !== undefined && v > opts.max)) {
                propOut.set(dflt);
            } else propOut.set(+v);
        }
    },
    string: {
        description: [
            'A string value.',
            'Numbers are converted to strings except for attributes with',
            '`strict` set to true.'
        ].join(' '),
        requiredOpts: [],
        // TODO 'values shouldn't be in there (edge case: 'dash' in Scatter)
        otherOpts: ['dflt', 'noBlank', 'strict', 'arrayOk', 'values'],
        coerceFunction: function(v, propOut, dflt, opts) {
            if(typeof v !== 'string') {
                var okToCoerce = (typeof v === 'number');

                if(opts.strict === true || !okToCoerce) propOut.set(dflt);
                else propOut.set(String(v));
            } else if(opts.noBlank && !v) propOut.set(dflt);
            else propOut.set(v);
        }
    },
    color: {
        description: [
            'A string describing color.',
            'Supported formats:',
            '- hex (e.g. \'#d3d3d3\')',
            '- rgb (e.g. \'rgb(255, 0, 0)\')',
            '- rgba (e.g. \'rgb(255, 0, 0, 0.5)\')',
            '- hsl (e.g. \'hsl(0, 100%, 50%)\')',
            '- hsv (e.g. \'hsv(0, 100%, 100%)\')',
            '- named colors (full list: http://www.w3.org/TR/css3-color/#svg-color)'
        ].join(' '),
        requiredOpts: [],
        otherOpts: ['dflt', 'arrayOk'],
        coerceFunction: function(v, propOut, dflt) {
            if(tinycolor(v).isValid()) propOut.set(v);
            else propOut.set(dflt);
        }
    },
    colorlist: {
        description: [
            'A list of colors.',
            'Must be an {array} containing valid colors.',
        ].join(' '),
        requiredOpts: [],
        otherOpts: ['dflt'],
        coerceFunction: function(v, propOut, dflt) {
            function isColor(color) {
                return tinycolor(color).isValid();
            }
            if(!Array.isArray(v) || !v.length) propOut.set(dflt);
            else if(v.every(isColor)) propOut.set(v);
            else propOut.set(dflt);
        }
    },
    colorscale: {
        description: [
            'A Plotly colorscale either picked by a name:',
            '(any of', Object.keys(colorscales.scales).join(', '), ')',
            'customized as an {array} of 2-element {arrays} where',
            'the first element is the normalized color level value',
            '(starting at *0* and ending at *1*),',
            'and the second item is a valid color string.'
        ].join(' '),
        requiredOpts: [],
        otherOpts: ['dflt'],
        coerceFunction: function(v, propOut, dflt) {
            propOut.set(colorscales.get(v, dflt));
        }
    },
    angle: {
        description: [
            'A number (in degree) between -180 and 180.'
        ].join(' '),
        requiredOpts: [],
        otherOpts: ['dflt'],
        coerceFunction: function(v, propOut, dflt) {
            if(v === 'auto') propOut.set('auto');
            else if(!isNumeric(v)) propOut.set(dflt);
            else propOut.set(modHalf(+v, 360));
        }
    },
    subplotid: {
        description: [
            'An id string of a subplot type (given by dflt), optionally',
            'followed by an integer >1. e.g. if dflt=\'geo\', we can have',
            '\'geo\', \'geo2\', \'geo3\', ...'
        ].join(' '),
        requiredOpts: ['dflt'],
        otherOpts: ['regex'],
        coerceFunction: function(v, propOut, dflt, opts) {
            var regex = opts.regex || counterRegex(dflt);
            if(typeof v === 'string' && regex.test(v)) {
                propOut.set(v);
                return;
            }
            propOut.set(dflt);
        },
        validateFunction: function(v, opts) {
            var dflt = opts.dflt;

            if(v === dflt) return true;
            if(typeof v !== 'string') return false;
            if(counterRegex(dflt).test(v)) return true;

            return false;
        }
    },
    flaglist: {
        description: [
            'A string representing a combination of flags',
            '(order does not matter here).',
            'Combine any of the available `flags` with *+*.',
            '(e.g. (\'lines+markers\')).',
            'Values in `extras` cannot be combined.'
        ].join(' '),
        requiredOpts: ['flags'],
        otherOpts: ['dflt', 'extras', 'arrayOk'],
        coerceFunction: function(v, propOut, dflt, opts) {
            if(typeof v !== 'string') {
                propOut.set(dflt);
                return;
            }
            if((opts.extras || []).indexOf(v) !== -1) {
                propOut.set(v);
                return;
            }
            var vParts = v.split('+');
            var i = 0;
            while(i < vParts.length) {
                var vi = vParts[i];
                if(opts.flags.indexOf(vi) === -1 || vParts.indexOf(vi) < i) {
                    vParts.splice(i, 1);
                } else i++;
            }
            if(!vParts.length) propOut.set(dflt);
            else propOut.set(vParts.join('+'));
        }
    },
    any: {
        description: 'Any type.',
        requiredOpts: [],
        otherOpts: ['dflt', 'values', 'arrayOk'],
        coerceFunction: function(v, propOut, dflt) {
            if(v === undefined) propOut.set(dflt);
            else propOut.set(v);
        }
    },
    info_array: {
        description: [
            'An {array} of plot information.'
        ].join(' '),
        requiredOpts: ['items'],
        // set `dimensions=2` for a 2D array or '1-2' for either
        // `items` may be a single object instead of an array, in which case
        // `freeLength` must be true.
        // if `dimensions='1-2'` and items is a 1D array, then the value can
        // either be a matching 1D array or an array of such matching 1D arrays
        otherOpts: ['dflt', 'freeLength', 'dimensions'],
        coerceFunction: function(v, propOut, dflt, opts) {
            // simplified coerce function just for array items
            function coercePart(v, opts, dflt) {
                var out;
                var propPart = {set: function(v) { out = v; }};

                if(dflt === undefined) dflt = opts.dflt;

                exports.valObjectMeta[opts.valType].coerceFunction(v, propPart, dflt, opts);

                return out;
            }

            var twoD = opts.dimensions === 2 || (opts.dimensions === '1-2' && Array.isArray(v) && Array.isArray(v[0]));

            if(!Array.isArray(v)) {
                propOut.set(dflt);
                return;
            }

            var items = opts.items;
            var vOut = [];
            var arrayItems = Array.isArray(items);
            var arrayItems2D = arrayItems && twoD && Array.isArray(items[0]);
            var innerItemsOnly = twoD && arrayItems && !arrayItems2D;
            var len = (arrayItems && !innerItemsOnly) ? items.length : v.length;

            var i, j, row, item, len2, vNew;

            dflt = Array.isArray(dflt) ? dflt : [];

            if(twoD) {
                for(i = 0; i < len; i++) {
                    vOut[i] = [];
                    row = Array.isArray(v[i]) ? v[i] : [];
                    if(innerItemsOnly) len2 = items.length;
                    else if(arrayItems) len2 = items[i].length;
                    else len2 = row.length;

                    for(j = 0; j < len2; j++) {
                        if(innerItemsOnly) item = items[j];
                        else if(arrayItems) item = items[i][j];
                        else item = items;

                        vNew = coercePart(row[j], item, (dflt[i] || [])[j]);
                        if(vNew !== undefined) vOut[i][j] = vNew;
                    }
                }
            } else {
                for(i = 0; i < len; i++) {
                    vNew = coercePart(v[i], arrayItems ? items[i] : items, dflt[i]);
                    if(vNew !== undefined) vOut[i] = vNew;
                }
            }

            propOut.set(vOut);
        },
        validateFunction: function(v, opts) {
            if(!Array.isArray(v)) return false;

            var items = opts.items;
            var arrayItems = Array.isArray(items);
            var twoD = opts.dimensions === 2;

            // when free length is off, input and declared lengths must match
            if(!opts.freeLength && v.length !== items.length) return false;

            // valid when all input items are valid
            for(var i = 0; i < v.length; i++) {
                if(twoD) {
                    if(!Array.isArray(v[i]) || (!opts.freeLength && v[i].length !== items[i].length)) {
                        return false;
                    }
                    for(var j = 0; j < v[i].length; j++) {
                        if(!validate(v[i][j], arrayItems ? items[i][j] : items)) {
                            return false;
                        }
                    }
                } else if(!validate(v[i], arrayItems ? items[i] : items)) return false;
            }

            return true;
        }
    }
};

/**
 * Ensures that container[attribute] has a valid value.
 *
 * attributes[attribute] is an object with possible keys:
 * - valType: data_array, enumerated, boolean, ... as in valObjectMeta
 * - values: (enumerated only) array of allowed vals
 * - min, max: (number, integer only) inclusive bounds on allowed vals
 *      either or both may be omitted
 * - dflt: if attribute is invalid or missing, use this default
 *      if dflt is provided as an argument to lib.coerce it takes precedence
 *      as a convenience, returns the value it finally set
 */
exports.coerce = function(containerIn, containerOut, attributes, attribute, dflt) {
    var opts = nestedProperty(attributes, attribute).get();
    var propIn = nestedProperty(containerIn, attribute);
    var propOut = nestedProperty(containerOut, attribute);
    var v = propIn.get();

    var template = containerOut._template;
    if(v === undefined && template) {
        v = nestedProperty(template, attribute).get();
        // already used the template value, so short-circuit the second check
        template = 0;
    }

    if(dflt === undefined) dflt = opts.dflt;

    /**
     * arrayOk: value MAY be an array, then we do no value checking
     * at this point, because it can be more complicated than the
     * individual form (eg. some array vals can be numbers, even if the
     * single values must be color strings)
     */
    if(opts.arrayOk && isArrayOrTypedArray(v)) {
        propOut.set(v);
        return v;
    }

    var coerceFunction = exports.valObjectMeta[opts.valType].coerceFunction;
    coerceFunction(v, propOut, dflt, opts);

    var out = propOut.get();
    // in case v was provided but invalid, try the template again so it still
    // overrides the regular default
    if(template && out === dflt && !validate(v, opts)) {
        v = nestedProperty(template, attribute).get();
        coerceFunction(v, propOut, dflt, opts);
        out = propOut.get();
    }
    return out;
};

/**
 * Variation on coerce
 *
 * Uses coerce to get attribute value if user input is valid,
 * returns attribute default if user input it not valid or
 * returns false if there is no user input.
 */
exports.coerce2 = function(containerIn, containerOut, attributes, attribute, dflt) {
    var propIn = nestedProperty(containerIn, attribute);
    var propOut = exports.coerce(containerIn, containerOut, attributes, attribute, dflt);
    var valIn = propIn.get();

    return (valIn !== undefined && valIn !== null) ? propOut : false;
};

/*
 * Shortcut to coerce the three font attributes
 *
 * 'coerce' is a lib.coerce wrapper with implied first three arguments
 */
exports.coerceFont = function(coerce, attr, dfltObj) {
    var out = {};

    dfltObj = dfltObj || {};

    out.family = coerce(attr + '.family', dfltObj.family);
    out.size = coerce(attr + '.size', dfltObj.size);
    out.color = coerce(attr + '.color', dfltObj.color);

    return out;
};

/** Coerce shortcut for 'hoverinfo'
 * handling 1-vs-multi-trace dflt logic
 *
 * @param {object} traceIn : user trace object
 * @param {object} traceOut : full trace object (requires _module ref)
 * @param {object} layoutOut : full layout object (require _dataLength ref)
 * @return {any} : the coerced value
 */
exports.coerceHoverinfo = function(traceIn, traceOut, layoutOut) {
    var moduleAttrs = traceOut._module.attributes;
    var attrs = moduleAttrs.hoverinfo ? moduleAttrs : baseTraceAttrs;

    var valObj = attrs.hoverinfo;
    var dflt;

    if(layoutOut._dataLength === 1) {
        var flags = valObj.dflt === 'all' ?
            valObj.flags.slice() :
            valObj.dflt.split('+');

        flags.splice(flags.indexOf('name'), 1);
        dflt = flags.join('+');
    }

    return exports.coerce(traceIn, traceOut, attrs, 'hoverinfo', dflt);
};

/** Coerce shortcut for [un]selected.marker.opacity,
 *  which has special default logic, to ensure that it corresponds to the
 *  default selection behavior while allowing to be overtaken by any other
 *  [un]selected attribute.
 *
 *  N.B. This must be called *after* coercing all the other [un]selected attrs,
 *  to give the intended result.
 *
 * @param {object} traceOut : fullData item
 * @param {function} coerce : lib.coerce wrapper with implied first three arguments
 */
exports.coerceSelectionMarkerOpacity = function(traceOut, coerce) {
    if(!traceOut.marker) return;

    var mo = traceOut.marker.opacity;
    // you can still have a `marker` container with no markers if there's text
    if(mo === undefined) return;

    var smoDflt;
    var usmoDflt;

    // Don't give [un]selected.marker.opacity a default value if
    // marker.opacity is an array: handle this during style step.
    //
    // Only give [un]selected.marker.opacity a default value if you don't
    // set any other [un]selected attributes.
    if(!isArrayOrTypedArray(mo) && !traceOut.selected && !traceOut.unselected) {
        smoDflt = mo;
        usmoDflt = DESELECTDIM * mo;
    }

    coerce('selected.marker.opacity', smoDflt);
    coerce('unselected.marker.opacity', usmoDflt);
};

function validate(value, opts) {
    var valObjectDef = exports.valObjectMeta[opts.valType];

    if(opts.arrayOk && isArrayOrTypedArray(value)) return true;

    if(valObjectDef.validateFunction) {
        return valObjectDef.validateFunction(value, opts);
    }

    var failed = {};
    var out = failed;
    var propMock = { set: function(v) { out = v; } };

    // 'failed' just something mutable that won't be === anything else

    valObjectDef.coerceFunction(value, propMock, failed, opts);
    return out !== failed;
}
exports.validate = validate;
