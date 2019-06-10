/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/


'use strict';

var isPlainObject = require('../lib/is_plain_object');
var noop = require('../lib/noop');
var Loggers = require('../lib/loggers');
var sorterAsc = require('../lib/search').sorterAsc;
var Registry = require('../registry');


exports.containerArrayMatch = require('./container_array_match');

var isAddVal = exports.isAddVal = function isAddVal(val) {
    return val === 'add' || isPlainObject(val);
};

var isRemoveVal = exports.isRemoveVal = function isRemoveVal(val) {
    return val === null || val === 'remove';
};

/*
 * applyContainerArrayChanges: for managing arrays of layout components in relayout
 * handles them all with a consistent interface.
 *
 * Here are the supported actions -> relayout calls -> edits we get here
 * (as prepared in _relayout):
 *
 * add an empty obj -> {'annotations[2]': 'add'} -> {2: {'': 'add'}}
 * add a specific obj -> {'annotations[2]': {attrs}} -> {2: {'': {attrs}}}
 * delete an obj -> {'annotations[2]': 'remove'} -> {2: {'': 'remove'}}
 *               -> {'annotations[2]': null} -> {2: {'': null}}
 * delete the whole array -> {'annotations': 'remove'} -> {'': {'': 'remove'}}
 *                        -> {'annotations': null} -> {'': {'': null}}
 * edit an object -> {'annotations[2].text': 'boo'} -> {2: {'text': 'boo'}}
 *
 * You can combine many edits to different objects. Objects are added and edited
 * in ascending order, then removed in descending order.
 * For example, starting with [a, b, c], if you want to:
 * - replace b with d:
 *   {'annotations[1]': d, 'annotations[2]': null} (b is item 2 after adding d)
 * - add a new item d between a and b, and edit b:
 *    {'annotations[1]': d, 'annotations[2].x': newX} (b is item 2 after adding d)
 * - delete b and edit c:
 *    {'annotations[1]': null, 'annotations[2].x': newX} (c is edited before b is removed)
 *
 * You CANNOT combine adding/deleting an item at index `i` with edits to the same index `i`
 * You CANNOT combine replacing/deleting the whole array with anything else (for the same array).
 *
 * @param {HTMLDivElement} gd
 *  the DOM element of the graph container div
 * @param {Lib.nestedProperty} componentType: the array we are editing
 * @param {Object} edits
 *  the changes to make; keys are indices to edit, values are themselves objects:
 *  {attr: newValue} of changes to make to that index (with add/remove behavior
 *  in special values of the empty attr)
 * @param {Object} flags
 *  the flags for which actions we're going to perform to display these (and
 *  any other) changes. If we're already `recalc`ing, we don't need to redraw
 *  individual items
 * @param {function} _nestedProperty
 *  a (possibly modified for gui edits) nestedProperty constructor
 *  The modified version takes a 3rd argument, for a prefix to the attribute
 *  string necessary for storing GUI edits
 *
 * @returns {bool} `true` if it managed to complete drawing of the changes
 *  `false` would mean the parent should replot.
 */
exports.applyContainerArrayChanges = function applyContainerArrayChanges(gd, np, edits, flags, _nestedProperty) {
    var componentType = np.astr;
    var supplyComponentDefaults = Registry.getComponentMethod(componentType, 'supplyLayoutDefaults');
    var draw = Registry.getComponentMethod(componentType, 'draw');
    var drawOne = Registry.getComponentMethod(componentType, 'drawOne');
    var replotLater = flags.replot || flags.recalc || (supplyComponentDefaults === noop) || (draw === noop);
    var layout = gd.layout;
    var fullLayout = gd._fullLayout;

    if(edits['']) {
        if(Object.keys(edits).length > 1) {
            Loggers.warn('Full array edits are incompatible with other edits',
                componentType);
        }

        var fullVal = edits[''][''];

        if(isRemoveVal(fullVal)) np.set(null);
        else if(Array.isArray(fullVal)) np.set(fullVal);
        else {
            Loggers.warn('Unrecognized full array edit value', componentType, fullVal);
            return true;
        }

        if(replotLater) return false;

        supplyComponentDefaults(layout, fullLayout);
        draw(gd);
        return true;
    }

    var componentNums = Object.keys(edits).map(Number).sort(sorterAsc);
    var componentArrayIn = np.get();
    var componentArray = componentArrayIn || [];
    // componentArrayFull is used just to keep splices in line between
    // full and input arrays, so private keys can be copied over after
    // redoing supplyDefaults
    // TODO: this assumes componentArray is in gd.layout - which will not be
    // true after we extend this to restyle
    var componentArrayFull = _nestedProperty(fullLayout, componentType).get();

    var deletes = [];
    var firstIndexChange = -1;
    var maxIndex = componentArray.length;
    var i;
    var j;
    var componentNum;
    var objEdits;
    var objKeys;
    var objVal;
    var adding, prefix;

    // first make the add and edit changes
    for(i = 0; i < componentNums.length; i++) {
        componentNum = componentNums[i];
        objEdits = edits[componentNum];
        objKeys = Object.keys(objEdits);
        objVal = objEdits[''],
        adding = isAddVal(objVal);

        if(componentNum < 0 || componentNum > componentArray.length - (adding ? 0 : 1)) {
            Loggers.warn('index out of range', componentType, componentNum);
            continue;
        }

        if(objVal !== undefined) {
            if(objKeys.length > 1) {
                Loggers.warn(
                    'Insertion & removal are incompatible with edits to the same index.',
                    componentType, componentNum);
            }

            if(isRemoveVal(objVal)) {
                deletes.push(componentNum);
            } else if(adding) {
                if(objVal === 'add') objVal = {};
                componentArray.splice(componentNum, 0, objVal);
                if(componentArrayFull) componentArrayFull.splice(componentNum, 0, {});
            } else {
                Loggers.warn('Unrecognized full object edit value',
                    componentType, componentNum, objVal);
            }

            if(firstIndexChange === -1) firstIndexChange = componentNum;
        } else {
            for(j = 0; j < objKeys.length; j++) {
                prefix = componentType + '[' + componentNum + '].';
                _nestedProperty(componentArray[componentNum], objKeys[j], prefix)
                    .set(objEdits[objKeys[j]]);
            }
        }
    }

    // now do deletes
    for(i = deletes.length - 1; i >= 0; i--) {
        componentArray.splice(deletes[i], 1);
        // TODO: this drops private keys that had been stored in componentArrayFull
        // does this have any ill effects?
        if(componentArrayFull) componentArrayFull.splice(deletes[i], 1);
    }

    if(!componentArray.length) np.set(null);
    else if(!componentArrayIn) np.set(componentArray);

    if(replotLater) return false;

    supplyComponentDefaults(layout, fullLayout);

    // finally draw all the components we need to
    // if we added or removed any, redraw all after it
    if(drawOne !== noop) {
        var indicesToDraw;
        if(firstIndexChange === -1) {
            // there's no re-indexing to do, so only redraw components that changed
            indicesToDraw = componentNums;
        } else {
            // in case the component array was shortened, we still need do call
            // drawOne on the latter items so they get properly removed
            maxIndex = Math.max(componentArray.length, maxIndex);
            indicesToDraw = [];
            for(i = 0; i < componentNums.length; i++) {
                componentNum = componentNums[i];
                if(componentNum >= firstIndexChange) break;
                indicesToDraw.push(componentNum);
            }
            for(i = firstIndexChange; i < maxIndex; i++) {
                indicesToDraw.push(i);
            }
        }
        for(i = 0; i < indicesToDraw.length; i++) {
            drawOne(gd, indicesToDraw[i]);
        }
    } else draw(gd);

    return true;
};
