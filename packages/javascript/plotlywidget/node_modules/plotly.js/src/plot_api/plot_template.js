/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/


'use strict';

var Lib = require('../lib');
var plotAttributes = require('../plots/attributes');

var TEMPLATEITEMNAME = 'templateitemname';

var templateAttrs = {
    name: {
        valType: 'string',
        role: 'style',
        editType: 'none',
        description: [
            'When used in a template, named items are created in the output figure',
            'in addition to any items the figure already has in this array.',
            'You can modify these items in the output figure by making your own',
            'item with `templateitemname` matching this `name`',
            'alongside your modifications (including `visible: false` or',
            '`enabled: false` to hide it).',
            'Has no effect outside of a template.'
        ].join(' ')
    }
};
templateAttrs[TEMPLATEITEMNAME] = {
    valType: 'string',
    role: 'info',
    editType: 'calc',
    description: [
        'Used to refer to a named item in this array in the template. Named',
        'items from the template will be created even without a matching item',
        'in the input figure, but you can modify one by making an item with',
        '`templateitemname` matching its `name`, alongside your modifications',
        '(including `visible: false` or `enabled: false` to hide it).',
        'If there is no template or no matching item, this item will be',
        'hidden unless you explicitly show it with `visible: true`.'
    ].join(' ')
};

/**
 * templatedArray: decorate an attributes object with templating (and array)
 * properties.
 *
 * @param {string} name: the singular form of the array name. Sets
 *     `_isLinkedToArray` to this, so the schema knows to treat this as an array.
 * @param {object} attrs: the item attributes. Since all callers are expected
 *     to be constructing this object on the spot, we mutate it here for
 *     performance, rather than extending a new object with it.
 *
 * @returns {object}: the decorated `attrs` object
 */
exports.templatedArray = function(name, attrs) {
    attrs._isLinkedToArray = name;
    attrs.name = templateAttrs.name;
    attrs[TEMPLATEITEMNAME] = templateAttrs[TEMPLATEITEMNAME];
    return attrs;
};

/**
 * traceTemplater: logic for matching traces to trace templates
 *
 * @param {object} dataTemplate: collection of {traceType: [{template}, ...]}
 *     ie each type the template applies to contains a list of template objects,
 *     to be provided cyclically to data traces of that type.
 *
 * @returns {object}: {newTrace}, a function:
 *     newTrace(traceIn): that takes the input traceIn, coerces its type, then
 *         uses that type to find the next template to apply. returns the output
 *         traceOut with template attached, ready to continue supplyDefaults.
 */
exports.traceTemplater = function(dataTemplate) {
    var traceCounts = {};
    var traceType, typeTemplates;

    for(traceType in dataTemplate) {
        typeTemplates = dataTemplate[traceType];
        if(Array.isArray(typeTemplates) && typeTemplates.length) {
            traceCounts[traceType] = 0;
        }
    }

    function newTrace(traceIn) {
        traceType = Lib.coerce(traceIn, {}, plotAttributes, 'type');
        var traceOut = {type: traceType, _template: null};
        if(traceType in traceCounts) {
            typeTemplates = dataTemplate[traceType];
            // cycle through traces in the template set for this type
            var typei = traceCounts[traceType] % typeTemplates.length;
            traceCounts[traceType]++;
            traceOut._template = typeTemplates[typei];
        } else {
            // TODO: anything we should do for types missing from the template?
            // try to apply some other type? Or just bail as we do here?
            // Actually I think yes, we should apply other types; would be nice
            // if all scatter* could inherit from each other, and if histogram
            // could inherit from bar, etc... but how to specify this? And do we
            // compose them, or if a type is present require it to be complete?
            // Actually this could apply to layout too - 3D annotations
            // inheriting from 2D, axes of different types inheriting from each
            // other...
        }
        return traceOut;
    }

    return {
        newTrace: newTrace
        // TODO: function to figure out what's left & what didn't work
    };
};

/**
 * newContainer: Create a new sub-container inside `container` and propagate any
 * applicable template to it. If there's no template, still propagates
 * `undefined` so relinkPrivate will not retain an old template!
 *
 * @param {object} container: the outer container, should already have _template
 *     if there *is* a template for this plot
 * @param {string} name: the key of the new container to make
 * @param {string} baseName: if applicable, a base attribute to take the
 *     template from, ie for xaxis3 the base would be xaxis
 *
 * @returns {object}: an object for inclusion _full*, empty except for the
 *     appropriate template piece
 */
exports.newContainer = function(container, name, baseName) {
    var template = container._template;
    var part = template && (template[name] || (baseName && template[baseName]));
    if(!Lib.isPlainObject(part)) part = null;

    var out = container[name] = {_template: part};
    return out;
};

/**
 * arrayTemplater: special logic for templating both defaults and specific items
 * in a container array (annotations etc)
 *
 * @param {object} container: the outer container, should already have _template
 *     if there *is* a template for this plot
 * @param {string} name: the name of the array to template (ie 'annotations')
 *     will be used to find default ('annotationdefaults' object) and specific
 *     ('annotations' array) template specs.
 * @param {string} inclusionAttr: the attribute determining this item's
 *     inclusion in the output, usually 'visible' or 'enabled'
 *
 * @returns {object}: {newItem, defaultItems}, both functions:
 *     newItem(itemIn): create an output item, bare except for the correct
 *         template and name(s), as the base for supplyDefaults
 *     defaultItems(): to be called after all newItem calls, return any
 *         specific template items that have not already beeen included,
 *         also as bare output items ready for supplyDefaults.
 */
exports.arrayTemplater = function(container, name, inclusionAttr) {
    var template = container._template;
    var defaultsTemplate = template && template[arrayDefaultKey(name)];
    var templateItems = template && template[name];
    if(!Array.isArray(templateItems) || !templateItems.length) {
        templateItems = [];
    }

    var usedNames = {};

    function newItem(itemIn) {
        // include name and templateitemname in the output object for ALL
        // container array items. Note: you could potentially use different
        // name and templateitemname, if you're using one template to make
        // another template. templateitemname would be the name in the original
        // template, and name is the new "subclassed" item name.
        var out = {name: itemIn.name, _input: itemIn};
        var templateItemName = out[TEMPLATEITEMNAME] = itemIn[TEMPLATEITEMNAME];

        // no itemname: use the default template
        if(!validItemName(templateItemName)) {
            out._template = defaultsTemplate;
            return out;
        }

        // look for an item matching this itemname
        // note these do not inherit from the default template, only the item.
        for(var i = 0; i < templateItems.length; i++) {
            var templateItem = templateItems[i];
            if(templateItem.name === templateItemName) {
                // Note: it's OK to use a template item more than once
                // but using it at least once will stop it from generating
                // a default item at the end.
                usedNames[templateItemName] = 1;
                out._template = templateItem;
                return out;
            }
        }

        // Didn't find a matching template item, so since this item is intended
        // to only be modifications it's most likely broken. Hide it unless
        // it's explicitly marked visible - in which case it gets NO template,
        // not even the default.
        out[inclusionAttr] = itemIn[inclusionAttr] || false;
        // special falsy value we can look for in validateTemplate
        out._template = false;
        return out;
    }

    function defaultItems() {
        var out = [];
        for(var i = 0; i < templateItems.length; i++) {
            var templateItem = templateItems[i];
            var name = templateItem.name;
            // only allow named items to be added as defaults,
            // and only allow each name once
            if(validItemName(name) && !usedNames[name]) {
                var outi = {
                    _template: templateItem,
                    name: name,
                    _input: {_templateitemname: name}
                };
                outi[TEMPLATEITEMNAME] = templateItem[TEMPLATEITEMNAME];
                out.push(outi);
                usedNames[name] = 1;
            }
        }
        return out;
    }

    return {
        newItem: newItem,
        defaultItems: defaultItems
    };
};

function validItemName(name) {
    return name && typeof name === 'string';
}

function arrayDefaultKey(name) {
    var lastChar = name.length - 1;
    if(name.charAt(lastChar) !== 's') {
        Lib.warn('bad argument to arrayDefaultKey: ' + name);
    }
    return name.substr(0, name.length - 1) + 'defaults';
}
exports.arrayDefaultKey = arrayDefaultKey;

/**
 * arrayEditor: helper for editing array items that may have come from
 *     template defaults (in which case they will not exist in the input yet)
 *
 * @param {object} parentIn: the input container (eg gd.layout)
 * @param {string} containerStr: the attribute string for the container inside
 *     `parentIn`.
 * @param {object} itemOut: the _full* item (eg gd._fullLayout.annotations[0])
 *     that we'll be editing. Assumed to have been created by `arrayTemplater`.
 *
 * @returns {object}: {modifyBase, modifyItem, getUpdateObj, applyUpdate}, all functions:
 *     modifyBase(attr, value): Add an update that's *not* related to the item.
 *         `attr` is the full attribute string.
 *     modifyItem(attr, value): Add an update to the item. `attr` is just the
 *         portion of the attribute string inside the item.
 *     getUpdateObj(): Get the final constructed update object, to use in
 *         `restyle` or `relayout`. Also resets the update object in case this
 *         update was canceled.
 *     applyUpdate(attr, value): optionally add an update `attr: value`,
 *         then apply it to `parent` which should be the parent of `containerIn`,
 *         ie the object to which `containerStr` is the attribute string.
 */
exports.arrayEditor = function(parentIn, containerStr, itemOut) {
    var lengthIn = (Lib.nestedProperty(parentIn, containerStr).get() || []).length;
    var index = itemOut._index;
    // Check that we are indeed off the end of this container.
    // Otherwise a devious user could put a key `_templateitemname` in their
    // own input and break lots of things.
    var templateItemName = (index >= lengthIn) && (itemOut._input || {})._templateitemname;
    if(templateItemName) index = lengthIn;
    var itemStr = containerStr + '[' + index + ']';

    var update;
    function resetUpdate() {
        update = {};
        if(templateItemName) {
            update[itemStr] = {};
            update[itemStr][TEMPLATEITEMNAME] = templateItemName;
        }
    }
    resetUpdate();

    function modifyBase(attr, value) {
        update[attr] = value;
    }

    function modifyItem(attr, value) {
        if(templateItemName) {
            // we're making a new object: edit that object
            Lib.nestedProperty(update[itemStr], attr).set(value);
        } else {
            // we're editing an existing object: include *just* the edit
            update[itemStr + '.' + attr] = value;
        }
    }

    function getUpdateObj() {
        var updateOut = update;
        resetUpdate();
        return updateOut;
    }

    function applyUpdate(attr, value) {
        if(attr) modifyItem(attr, value);
        var updateToApply = getUpdateObj();
        for(var key in updateToApply) {
            Lib.nestedProperty(parentIn, key).set(updateToApply[key]);
        }
    }

    return {
        modifyBase: modifyBase,
        modifyItem: modifyItem,
        getUpdateObj: getUpdateObj,
        applyUpdate: applyUpdate
    };
};
