/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/


'use strict';

var Lib = require('../lib');
var isPlainObject = Lib.isPlainObject;
var PlotSchema = require('./plot_schema');
var Plots = require('../plots/plots');
var plotAttributes = require('../plots/attributes');
var Template = require('./plot_template');
var dfltConfig = require('./plot_config').dfltConfig;

/**
 * Plotly.makeTemplate: create a template off an existing figure to reuse
 * style attributes on other figures.
 *
 * Note: separated from the rest of templates because otherwise we get circular
 * references due to PlotSchema.
 *
 * @param {object|DOM element|string} figure: The figure to base the template on
 *     should contain a trace array `figure.data`
 *     and a layout object `figure.layout`
 * @returns {object} template: the extracted template - can then be used as
 *     `layout.template` in another figure.
 */
exports.makeTemplate = function(figure) {
    figure = Lib.isPlainObject(figure) ? figure : Lib.getGraphDiv(figure);
    figure = Lib.extendDeep({_context: dfltConfig}, {data: figure.data, layout: figure.layout});
    Plots.supplyDefaults(figure);
    var data = figure.data || [];
    var layout = figure.layout || {};
    // copy over a few items to help follow the schema
    layout._basePlotModules = figure._fullLayout._basePlotModules;
    layout._modules = figure._fullLayout._modules;

    var template = {
        data: {},
        layout: {}
    };

    /*
     * Note: we do NOT validate template values, we just take what's in the
     * user inputs data and layout, not the validated values in fullData and
     * fullLayout. Even if we were to validate here, there's no guarantee that
     * these values would still be valid when applied to a new figure, which
     * may contain different trace modes, different axes, etc. So it's
     * important that when applying a template we still validate the template
     * values, rather than just using them as defaults.
     */

    data.forEach(function(trace) {
        // TODO: What if no style info is extracted for this trace. We may
        // not want an empty object as the null value.
        // TODO: allow transforms to contribute to templates?
        // as it stands they are ignored, which may be for the best...

        var traceTemplate = {};
        walkStyleKeys(trace, traceTemplate, getTraceInfo.bind(null, trace));

        var traceType = Lib.coerce(trace, {}, plotAttributes, 'type');
        var typeTemplates = template.data[traceType];
        if(!typeTemplates) typeTemplates = template.data[traceType] = [];
        typeTemplates.push(traceTemplate);
    });

    walkStyleKeys(layout, template.layout, getLayoutInfo.bind(null, layout));

    /*
     * Compose the new template with an existing one to the same effect
     *
     * NOTE: there's a possibility of slightly different behavior: if the plot
     * has an invalid value and the old template has a valid value for the same
     * attribute, the plot will use the old template value but this routine
     * will pull the invalid value (resulting in the original default).
     * In the general case it's not possible to solve this with a single value,
     * since valid options can be context-dependent. It could be solved with
     * a *list* of values, but that would be huge complexity for little gain.
     */
    delete template.layout.template;
    var oldTemplate = layout.template;
    if(isPlainObject(oldTemplate)) {
        var oldLayoutTemplate = oldTemplate.layout;

        var i, traceType, oldTypeTemplates, oldTypeLen, typeTemplates, typeLen;

        if(isPlainObject(oldLayoutTemplate)) {
            mergeTemplates(oldLayoutTemplate, template.layout);
        }
        var oldDataTemplate = oldTemplate.data;
        if(isPlainObject(oldDataTemplate)) {
            for(traceType in template.data) {
                oldTypeTemplates = oldDataTemplate[traceType];
                if(Array.isArray(oldTypeTemplates)) {
                    typeTemplates = template.data[traceType];
                    typeLen = typeTemplates.length;
                    oldTypeLen = oldTypeTemplates.length;
                    for(i = 0; i < typeLen; i++) {
                        mergeTemplates(oldTypeTemplates[i % oldTypeLen], typeTemplates[i]);
                    }
                    for(i = typeLen; i < oldTypeLen; i++) {
                        typeTemplates.push(Lib.extendDeep({}, oldTypeTemplates[i]));
                    }
                }
            }
            for(traceType in oldDataTemplate) {
                if(!(traceType in template.data)) {
                    template.data[traceType] = Lib.extendDeep([], oldDataTemplate[traceType]);
                }
            }
        }
    }

    return template;
};

function mergeTemplates(oldTemplate, newTemplate) {
    // we don't care about speed here, just make sure we have a totally
    // distinct object from the previous template
    oldTemplate = Lib.extendDeep({}, oldTemplate);

    // sort keys so we always get annotationdefaults before annotations etc
    // so arrayTemplater will work right
    var oldKeys = Object.keys(oldTemplate).sort();
    var i, j;

    function mergeOne(oldVal, newVal, key) {
        if(isPlainObject(newVal) && isPlainObject(oldVal)) {
            mergeTemplates(oldVal, newVal);
        } else if(Array.isArray(newVal) && Array.isArray(oldVal)) {
            // Note: omitted `inclusionAttr` from arrayTemplater here,
            // it's irrelevant as we only want the resulting `_template`.
            var templater = Template.arrayTemplater({_template: oldTemplate}, key);
            for(j = 0; j < newVal.length; j++) {
                var item = newVal[j];
                var oldItem = templater.newItem(item)._template;
                if(oldItem) mergeTemplates(oldItem, item);
            }
            var defaultItems = templater.defaultItems();
            for(j = 0; j < defaultItems.length; j++) newVal.push(defaultItems[j]._template);

            // templateitemname only applies to receiving plots
            for(j = 0; j < newVal.length; j++) delete newVal[j].templateitemname;
        }
    }

    for(i = 0; i < oldKeys.length; i++) {
        var key = oldKeys[i];
        var oldVal = oldTemplate[key];
        if(key in newTemplate) {
            mergeOne(oldVal, newTemplate[key], key);
        } else newTemplate[key] = oldVal;

        // if this is a base key from the old template (eg xaxis), look for
        // extended keys (eg xaxis2) in the new template to merge into
        if(getBaseKey(key) === key) {
            for(var key2 in newTemplate) {
                var baseKey2 = getBaseKey(key2);
                if(key2 !== baseKey2 && baseKey2 === key && !(key2 in oldTemplate)) {
                    mergeOne(oldVal, newTemplate[key2], key);
                }
            }
        }
    }
}

function getBaseKey(key) {
    return key.replace(/[0-9]+$/, '');
}

function walkStyleKeys(parent, templateOut, getAttributeInfo, path, basePath) {
    var pathAttr = basePath && getAttributeInfo(basePath);
    for(var key in parent) {
        var child = parent[key];
        var nextPath = getNextPath(parent, key, path);
        var nextBasePath = getNextPath(parent, key, basePath);
        var attr = getAttributeInfo(nextBasePath);
        if(!attr) {
            var baseKey = getBaseKey(key);
            if(baseKey !== key) {
                nextBasePath = getNextPath(parent, baseKey, basePath);
                attr = getAttributeInfo(nextBasePath);
            }
        }

        // we'll get an attr if path starts with a valid part, then has an
        // invalid ending. Make sure we got all the way to the end.
        if(pathAttr && (pathAttr === attr)) continue;

        if(!attr || attr._noTemplating ||
            attr.valType === 'data_array' ||
            (attr.arrayOk && Array.isArray(child))
        ) {
            continue;
        }

        if(!attr.valType && isPlainObject(child)) {
            walkStyleKeys(child, templateOut, getAttributeInfo, nextPath, nextBasePath);
        } else if(attr._isLinkedToArray && Array.isArray(child)) {
            var dfltDone = false;
            var namedIndex = 0;
            var usedNames = {};
            for(var i = 0; i < child.length; i++) {
                var item = child[i];
                if(isPlainObject(item)) {
                    var name = item.name;
                    if(name) {
                        if(!usedNames[name]) {
                            // named array items: allow all attributes except data arrays
                            walkStyleKeys(item, templateOut, getAttributeInfo,
                                getNextPath(child, namedIndex, nextPath),
                                getNextPath(child, namedIndex, nextBasePath));
                            namedIndex++;
                            usedNames[name] = 1;
                        }
                    } else if(!dfltDone) {
                        var dfltKey = Template.arrayDefaultKey(key);
                        var dfltPath = getNextPath(parent, dfltKey, path);

                        // getAttributeInfo will fail if we try to use dfltKey directly.
                        // Instead put this item into the next array element, then
                        // pull it out and move it to dfltKey.
                        var pathInArray = getNextPath(child, namedIndex, nextPath);
                        walkStyleKeys(item, templateOut, getAttributeInfo, pathInArray,
                            getNextPath(child, namedIndex, nextBasePath));
                        var itemPropInArray = Lib.nestedProperty(templateOut, pathInArray);
                        var dfltProp = Lib.nestedProperty(templateOut, dfltPath);
                        dfltProp.set(itemPropInArray.get());
                        itemPropInArray.set(null);

                        dfltDone = true;
                    }
                }
            }
        } else {
            var templateProp = Lib.nestedProperty(templateOut, nextPath);
            templateProp.set(child);
        }
    }
}

function getLayoutInfo(layout, path) {
    return PlotSchema.getLayoutValObject(
        layout, Lib.nestedProperty({}, path).parts
    );
}

function getTraceInfo(trace, path) {
    return PlotSchema.getTraceValObject(
        trace, Lib.nestedProperty({}, path).parts
    );
}

function getNextPath(parent, key, path) {
    var nextPath;
    if(!path) nextPath = key;
    else if(Array.isArray(parent)) nextPath = path + '[' + key + ']';
    else nextPath = path + '.' + key;

    return nextPath;
}

/**
 * validateTemplate: Test for consistency between the given figure and
 * a template, either already included in the figure or given separately.
 * Note that not every issue we identify here is necessarily a problem,
 * it depends on what you're using the template for.
 *
 * @param {object|DOM element} figure: the plot, with {data, layout} members,
 *     to test the template against
 * @param {Optional(object)} template: the template, with its own {data, layout},
 *     to test. If omitted, we will look for a template already attached as the
 *     plot's `layout.template` attribute.
 *
 * @returns {array} array of error objects each containing:
 *  - {string} code
 *      error code ('missing', 'unused', 'reused', 'noLayout', 'noData')
 *  - {string} msg
 *      a full readable description of the issue.
 */
exports.validateTemplate = function(figureIn, template) {
    var figure = Lib.extendDeep({}, {
        _context: dfltConfig,
        data: figureIn.data,
        layout: figureIn.layout
    });
    var layout = figure.layout || {};
    if(!isPlainObject(template)) template = layout.template || {};
    var layoutTemplate = template.layout;
    var dataTemplate = template.data;
    var errorList = [];

    figure.layout = layout;
    figure.layout.template = template;
    Plots.supplyDefaults(figure);

    var fullLayout = figure._fullLayout;
    var fullData = figure._fullData;

    var layoutPaths = {};
    function crawlLayoutForContainers(obj, paths) {
        for(var key in obj) {
            if(key.charAt(0) !== '_' && isPlainObject(obj[key])) {
                var baseKey = getBaseKey(key);
                var nextPaths = [];
                var i;
                for(i = 0; i < paths.length; i++) {
                    nextPaths.push(getNextPath(obj, key, paths[i]));
                    if(baseKey !== key) nextPaths.push(getNextPath(obj, baseKey, paths[i]));
                }
                for(i = 0; i < nextPaths.length; i++) {
                    layoutPaths[nextPaths[i]] = 1;
                }
                crawlLayoutForContainers(obj[key], nextPaths);
            }
        }
    }

    function crawlLayoutTemplateForContainers(obj, path) {
        for(var key in obj) {
            if(key.indexOf('defaults') === -1 && isPlainObject(obj[key])) {
                var nextPath = getNextPath(obj, key, path);
                if(layoutPaths[nextPath]) {
                    crawlLayoutTemplateForContainers(obj[key], nextPath);
                } else {
                    errorList.push({code: 'unused', path: nextPath});
                }
            }
        }
    }

    if(!isPlainObject(layoutTemplate)) {
        errorList.push({code: 'layout'});
    } else {
        crawlLayoutForContainers(fullLayout, ['layout']);
        crawlLayoutTemplateForContainers(layoutTemplate, 'layout');
    }

    if(!isPlainObject(dataTemplate)) {
        errorList.push({code: 'data'});
    } else {
        var typeCount = {};
        var traceType;
        for(var i = 0; i < fullData.length; i++) {
            var fullTrace = fullData[i];
            traceType = fullTrace.type;
            typeCount[traceType] = (typeCount[traceType] || 0) + 1;
            if(!fullTrace._fullInput._template) {
                // this takes care of the case of traceType in the data but not
                // the template
                errorList.push({
                    code: 'missing',
                    index: fullTrace._fullInput.index,
                    traceType: traceType
                });
            }
        }
        for(traceType in dataTemplate) {
            var templateCount = dataTemplate[traceType].length;
            var dataCount = typeCount[traceType] || 0;
            if(templateCount > dataCount) {
                errorList.push({
                    code: 'unused',
                    traceType: traceType,
                    templateCount: templateCount,
                    dataCount: dataCount
                });
            } else if(dataCount > templateCount) {
                errorList.push({
                    code: 'reused',
                    traceType: traceType,
                    templateCount: templateCount,
                    dataCount: dataCount
                });
            }
        }
    }

    // _template: false is when someone tried to modify an array item
    // but there was no template with matching name
    function crawlForMissingTemplates(obj, path) {
        for(var key in obj) {
            if(key.charAt(0) === '_') continue;
            var val = obj[key];
            var nextPath = getNextPath(obj, key, path);
            if(isPlainObject(val)) {
                if(Array.isArray(obj) && val._template === false && val.templateitemname) {
                    errorList.push({
                        code: 'missing',
                        path: nextPath,
                        templateitemname: val.templateitemname
                    });
                }
                crawlForMissingTemplates(val, nextPath);
            } else if(Array.isArray(val) && hasPlainObject(val)) {
                crawlForMissingTemplates(val, nextPath);
            }
        }
    }
    crawlForMissingTemplates({data: fullData, layout: fullLayout}, '');

    if(errorList.length) return errorList.map(format);
};

function hasPlainObject(arr) {
    for(var i = 0; i < arr.length; i++) {
        if(isPlainObject(arr[i])) return true;
    }
}

function format(opts) {
    var msg;
    switch(opts.code) {
        case 'data':
            msg = 'The template has no key data.';
            break;
        case 'layout':
            msg = 'The template has no key layout.';
            break;
        case 'missing':
            if(opts.path) {
                msg = 'There are no templates for item ' + opts.path +
                    ' with name ' + opts.templateitemname;
            } else {
                msg = 'There are no templates for trace ' + opts.index +
                    ', of type ' + opts.traceType + '.';
            }
            break;
        case 'unused':
            if(opts.path) {
                msg = 'The template item at ' + opts.path +
                    ' was not used in constructing the plot.';
            } else if(opts.dataCount) {
                msg = 'Some of the templates of type ' + opts.traceType +
                    ' were not used. The template has ' + opts.templateCount +
                    ' traces, the data only has ' + opts.dataCount +
                    ' of this type.';
            } else {
                msg = 'The template has ' + opts.templateCount +
                    ' traces of type ' + opts.traceType +
                    ' but there are none in the data.';
            }
            break;
        case 'reused':
            msg = 'Some of the templates of type ' + opts.traceType +
                ' were used more than once. The template has ' +
                opts.templateCount + ' traces, the data has ' +
                opts.dataCount + ' of this type.';
            break;
    }
    opts.msg = msg;

    return opts;
}
