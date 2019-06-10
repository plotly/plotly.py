/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var Lib = require('../lib');
var Plots = require('../plots/plots');
var PlotSchema = require('./plot_schema');
var dfltConfig = require('./plot_config').dfltConfig;

var isPlainObject = Lib.isPlainObject;
var isArray = Array.isArray;
var isArrayOrTypedArray = Lib.isArrayOrTypedArray;

/**
 * Validate a data array and layout object.
 *
 * @param {array} data
 * @param {object} layout
 *
 * @return {array} array of error objects each containing:
 *  - {string} code
 *      error code ('object', 'array', 'schema', 'unused', 'invisible' or 'value')
 *  - {string} container
 *      container where the error occurs ('data' or 'layout')
 *  - {number} trace
 *      trace index of the 'data' container where the error occurs
 *  - {array} path
 *      nested path to the key that causes the error
 *  - {string} astr
 *      attribute string variant of 'path' compatible with Plotly.restyle and
 *      Plotly.relayout.
 *  - {string} msg
 *      error message (shown in console in logger config argument is enable)
 */
module.exports = function validate(data, layout) {
    var schema = PlotSchema.get();
    var errorList = [];
    var gd = {_context: Lib.extendFlat({}, dfltConfig)};

    var dataIn, layoutIn;

    if(isArray(data)) {
        gd.data = Lib.extendDeep([], data);
        dataIn = data;
    } else {
        gd.data = [];
        dataIn = [];
        errorList.push(format('array', 'data'));
    }

    if(isPlainObject(layout)) {
        gd.layout = Lib.extendDeep({}, layout);
        layoutIn = layout;
    } else {
        gd.layout = {};
        layoutIn = {};
        if(arguments.length > 1) {
            errorList.push(format('object', 'layout'));
        }
    }

    // N.B. dataIn and layoutIn are in general not the same as
    // gd.data and gd.layout after supplyDefaults as some attributes
    // in gd.data and gd.layout (still) get mutated during this step.

    Plots.supplyDefaults(gd);

    var dataOut = gd._fullData;
    var len = dataIn.length;

    for(var i = 0; i < len; i++) {
        var traceIn = dataIn[i];
        var base = ['data', i];

        if(!isPlainObject(traceIn)) {
            errorList.push(format('object', base));
            continue;
        }

        var traceOut = dataOut[i];
        var traceType = traceOut.type;
        var traceSchema = schema.traces[traceType].attributes;

        // PlotSchema does something fancy with trace 'type', reset it here
        // to make the trace schema compatible with Lib.validate.
        traceSchema.type = {
            valType: 'enumerated',
            values: [traceType]
        };

        if(traceOut.visible === false && traceIn.visible !== false) {
            errorList.push(format('invisible', base));
        }

        crawl(traceIn, traceOut, traceSchema, errorList, base);

        var transformsIn = traceIn.transforms;
        var transformsOut = traceOut.transforms;

        if(transformsIn) {
            if(!isArray(transformsIn)) {
                errorList.push(format('array', base, ['transforms']));
            }

            base.push('transforms');

            for(var j = 0; j < transformsIn.length; j++) {
                var path = ['transforms', j];
                var transformType = transformsIn[j].type;

                if(!isPlainObject(transformsIn[j])) {
                    errorList.push(format('object', base, path));
                    continue;
                }

                var transformSchema = schema.transforms[transformType] ?
                    schema.transforms[transformType].attributes :
                    {};

                // add 'type' to transform schema to validate the transform type
                transformSchema.type = {
                    valType: 'enumerated',
                    values: Object.keys(schema.transforms)
                };

                crawl(transformsIn[j], transformsOut[j], transformSchema, errorList, base, path);
            }
        }
    }

    var layoutOut = gd._fullLayout;
    var layoutSchema = fillLayoutSchema(schema, dataOut);

    crawl(layoutIn, layoutOut, layoutSchema, errorList, 'layout');

    // return undefined if no validation errors were found
    return (errorList.length === 0) ? void(0) : errorList;
};

function crawl(objIn, objOut, schema, list, base, path) {
    path = path || [];

    var keys = Object.keys(objIn);

    for(var i = 0; i < keys.length; i++) {
        var k = keys[i];

        // transforms are handled separately
        if(k === 'transforms') continue;

        var p = path.slice();
        p.push(k);

        var valIn = objIn[k];
        var valOut = objOut[k];

        var nestedSchema = getNestedSchema(schema, k);
        var isInfoArray = (nestedSchema || {}).valType === 'info_array';
        var isColorscale = (nestedSchema || {}).valType === 'colorscale';
        var items = (nestedSchema || {}).items;

        if(!isInSchema(schema, k)) {
            list.push(format('schema', base, p));
        } else if(isPlainObject(valIn) && isPlainObject(valOut)) {
            crawl(valIn, valOut, nestedSchema, list, base, p);
        } else if(isInfoArray && isArray(valIn)) {
            if(valIn.length > valOut.length) {
                list.push(format('unused', base, p.concat(valOut.length)));
            }
            var len = valOut.length;
            var arrayItems = Array.isArray(items);
            if(arrayItems) len = Math.min(len, items.length);
            var m, n, item, valInPart, valOutPart;
            if(nestedSchema.dimensions === 2) {
                for(n = 0; n < len; n++) {
                    if(isArray(valIn[n])) {
                        if(valIn[n].length > valOut[n].length) {
                            list.push(format('unused', base, p.concat(n, valOut[n].length)));
                        }
                        var len2 = valOut[n].length;
                        for(m = 0; m < (arrayItems ? Math.min(len2, items[n].length) : len2); m++) {
                            item = arrayItems ? items[n][m] : items;
                            valInPart = valIn[n][m];
                            valOutPart = valOut[n][m];
                            if(!Lib.validate(valInPart, item)) {
                                list.push(format('value', base, p.concat(n, m), valInPart));
                            } else if(valOutPart !== valInPart && valOutPart !== +valInPart) {
                                list.push(format('dynamic', base, p.concat(n, m), valInPart, valOutPart));
                            }
                        }
                    } else {
                        list.push(format('array', base, p.concat(n), valIn[n]));
                    }
                }
            } else {
                for(n = 0; n < len; n++) {
                    item = arrayItems ? items[n] : items;
                    valInPart = valIn[n];
                    valOutPart = valOut[n];
                    if(!Lib.validate(valInPart, item)) {
                        list.push(format('value', base, p.concat(n), valInPart));
                    } else if(valOutPart !== valInPart && valOutPart !== +valInPart) {
                        list.push(format('dynamic', base, p.concat(n), valInPart, valOutPart));
                    }
                }
            }
        } else if(nestedSchema.items && !isInfoArray && isArray(valIn)) {
            var _nestedSchema = items[Object.keys(items)[0]];
            var indexList = [];

            var j, _p;

            // loop over valOut items while keeping track of their
            // corresponding input container index (given by _index)
            for(j = 0; j < valOut.length; j++) {
                var _index = valOut[j]._index || j;

                _p = p.slice();
                _p.push(_index);

                if(isPlainObject(valIn[_index]) && isPlainObject(valOut[j])) {
                    indexList.push(_index);
                    var valInj = valIn[_index];
                    var valOutj = valOut[j];
                    if(isPlainObject(valInj) && valInj.visible !== false && valOutj.visible === false) {
                        list.push(format('invisible', base, _p));
                    } else crawl(valInj, valOutj, _nestedSchema, list, base, _p);
                }
            }

            // loop over valIn to determine where it went wrong for some items
            for(j = 0; j < valIn.length; j++) {
                _p = p.slice();
                _p.push(j);

                if(!isPlainObject(valIn[j])) {
                    list.push(format('object', base, _p, valIn[j]));
                } else if(indexList.indexOf(j) === -1) {
                    list.push(format('unused', base, _p));
                }
            }
        } else if(!isPlainObject(valIn) && isPlainObject(valOut)) {
            list.push(format('object', base, p, valIn));
        } else if(!isArrayOrTypedArray(valIn) && isArrayOrTypedArray(valOut) && !isInfoArray && !isColorscale) {
            list.push(format('array', base, p, valIn));
        } else if(!(k in objOut)) {
            list.push(format('unused', base, p, valIn));
        } else if(!Lib.validate(valIn, nestedSchema)) {
            list.push(format('value', base, p, valIn));
        } else if(nestedSchema.valType === 'enumerated' &&
            ((nestedSchema.coerceNumber && valIn !== +valOut) || valIn !== valOut)
        ) {
            list.push(format('dynamic', base, p, valIn, valOut));
        }
    }

    return list;
}

// the 'full' layout schema depends on the traces types presents
function fillLayoutSchema(schema, dataOut) {
    var layoutSchema = schema.layout.layoutAttributes;

    for(var i = 0; i < dataOut.length; i++) {
        var traceOut = dataOut[i];
        var traceSchema = schema.traces[traceOut.type];
        var traceLayoutAttr = traceSchema.layoutAttributes;

        if(traceLayoutAttr) {
            if(traceOut.subplot) {
                Lib.extendFlat(layoutSchema[traceSchema.attributes.subplot.dflt], traceLayoutAttr);
            } else {
                Lib.extendFlat(layoutSchema, traceLayoutAttr);
            }
        }
    }

    return layoutSchema;
}

// validation error codes
var code2msgFunc = {
    object: function(base, astr) {
        var prefix;

        if(base === 'layout' && astr === '') prefix = 'The layout argument';
        else if(base[0] === 'data' && astr === '') {
            prefix = 'Trace ' + base[1] + ' in the data argument';
        } else prefix = inBase(base) + 'key ' + astr;

        return prefix + ' must be linked to an object container';
    },
    array: function(base, astr) {
        var prefix;

        if(base === 'data') prefix = 'The data argument';
        else prefix = inBase(base) + 'key ' + astr;

        return prefix + ' must be linked to an array container';
    },
    schema: function(base, astr) {
        return inBase(base) + 'key ' + astr + ' is not part of the schema';
    },
    unused: function(base, astr, valIn) {
        var target = isPlainObject(valIn) ? 'container' : 'key';

        return inBase(base) + target + ' ' + astr + ' did not get coerced';
    },
    dynamic: function(base, astr, valIn, valOut) {
        return [
            inBase(base) + 'key',
            astr,
            '(set to \'' + valIn + '\')',
            'got reset to',
            '\'' + valOut + '\'',
            'during defaults.'
        ].join(' ');
    },
    invisible: function(base, astr) {
        return (
            astr ? (inBase(base) + 'item ' + astr) : ('Trace ' + base[1])
        ) + ' got defaulted to be not visible';
    },
    value: function(base, astr, valIn) {
        return [
            inBase(base) + 'key ' + astr,
            'is set to an invalid value (' + valIn + ')'
        ].join(' ');
    }
};

function inBase(base) {
    if(isArray(base)) return 'In data trace ' + base[1] + ', ';

    return 'In ' + base + ', ';
}

function format(code, base, path, valIn, valOut) {
    path = path || '';

    var container, trace;

    // container is either 'data' or 'layout
    // trace is the trace index if 'data', null otherwise

    if(isArray(base)) {
        container = base[0];
        trace = base[1];
    } else {
        container = base;
        trace = null;
    }

    var astr = convertPathToAttributeString(path);
    var msg = code2msgFunc[code](base, astr, valIn, valOut);

    // log to console if logger config option is enabled
    Lib.log(msg);

    return {
        code: code,
        container: container,
        trace: trace,
        path: path,
        astr: astr,
        msg: msg
    };
}

function isInSchema(schema, key) {
    var parts = splitKey(key);
    var keyMinusId = parts.keyMinusId;
    var id = parts.id;

    if((keyMinusId in schema) && schema[keyMinusId]._isSubplotObj && id) {
        return true;
    }

    return (key in schema);
}

function getNestedSchema(schema, key) {
    if(key in schema) return schema[key];

    var parts = splitKey(key);

    return schema[parts.keyMinusId];
}

var idRegex = Lib.counterRegex('([a-z]+)');

function splitKey(key) {
    var idMatch = key.match(idRegex);

    return {
        keyMinusId: idMatch && idMatch[1],
        id: idMatch && idMatch[2]
    };
}

function convertPathToAttributeString(path) {
    if(!isArray(path)) return String(path);

    var astr = '';

    for(var i = 0; i < path.length; i++) {
        var p = path[i];

        if(typeof p === 'number') {
            astr = astr.substr(0, astr.length - 1) + '[' + p + ']';
        } else {
            astr += p;
        }

        if(i < path.length - 1) astr += '.';
    }

    return astr;
}
