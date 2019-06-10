/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/


'use strict';

var isNumeric = require('fast-isnumeric');
var isArrayOrTypedArray = require('./array').isArrayOrTypedArray;

/**
 * convert a string s (such as 'xaxis.range[0]')
 * representing a property of nested object into set and get methods
 * also return the string and object so we don't have to keep track of them
 * allows [-1] for an array index, to set a property inside all elements
 * of an array
 * eg if obj = {arr: [{a: 1}, {a: 2}]}
 * you can do p = nestedProperty(obj, 'arr[-1].a')
 * but you cannot set the array itself this way, to do that
 * just set the whole array.
 * eg if obj = {arr: [1, 2, 3]}
 * you can't do nestedProperty(obj, 'arr[-1]').set(5)
 * but you can do nestedProperty(obj, 'arr').set([5, 5, 5])
 */
module.exports = function nestedProperty(container, propStr) {
    if(isNumeric(propStr)) propStr = String(propStr);
    else if(typeof propStr !== 'string' ||
            propStr.substr(propStr.length - 4) === '[-1]') {
        throw 'bad property string';
    }

    var j = 0;
    var propParts = propStr.split('.');
    var indexed;
    var indices;
    var i;

    // check for parts of the nesting hierarchy that are numbers (ie array elements)
    while(j < propParts.length) {
        // look for non-bracket chars, then any number of [##] blocks
        indexed = String(propParts[j]).match(/^([^\[\]]*)((\[\-?[0-9]*\])+)$/);
        if(indexed) {
            if(indexed[1]) propParts[j] = indexed[1];
            // allow propStr to start with bracketed array indices
            else if(j === 0) propParts.splice(0, 1);
            else throw 'bad property string';

            indices = indexed[2]
                .substr(1, indexed[2].length - 2)
                .split('][');

            for(i = 0; i < indices.length; i++) {
                j++;
                propParts.splice(j, 0, Number(indices[i]));
            }
        }
        j++;
    }

    if(typeof container !== 'object') {
        return badContainer(container, propStr, propParts);
    }

    return {
        set: npSet(container, propParts, propStr),
        get: npGet(container, propParts),
        astr: propStr,
        parts: propParts,
        obj: container
    };
};

function npGet(cont, parts) {
    return function() {
        var curCont = cont;
        var curPart;
        var allSame;
        var out;
        var i;
        var j;

        for(i = 0; i < parts.length - 1; i++) {
            curPart = parts[i];
            if(curPart === -1) {
                allSame = true;
                out = [];
                for(j = 0; j < curCont.length; j++) {
                    out[j] = npGet(curCont[j], parts.slice(i + 1))();
                    if(out[j] !== out[0]) allSame = false;
                }
                return allSame ? out[0] : out;
            }
            if(typeof curPart === 'number' && !isArrayOrTypedArray(curCont)) {
                return undefined;
            }
            curCont = curCont[curPart];
            if(typeof curCont !== 'object' || curCont === null) {
                return undefined;
            }
        }

        // only hit this if parts.length === 1
        if(typeof curCont !== 'object' || curCont === null) return undefined;

        out = curCont[parts[i]];
        if(out === null) return undefined;
        return out;
    };
}

/*
 * Can this value be deleted? We can delete `undefined`, and `null` except INSIDE an
 * *args* array.
 *
 * Previously we also deleted some `{}` and `[]`, in order to try and make set/unset
 * a net noop; but this causes far more complication than it's worth, and still had
 * lots of exceptions. See https://github.com/plotly/plotly.js/issues/1410
 *
 * *args* arrays get passed directly to API methods and we should respect null if
 * the user put it there, but otherwise null is deleted as we use it as code
 * in restyle/relayout/update for "delete this value" whereas undefined means
 * "ignore this edit"
 */
var ARGS_PATTERN = /(^|\.)args\[/;
function isDeletable(val, propStr) {
    return (val === undefined) || (val === null && !propStr.match(ARGS_PATTERN));
}

function npSet(cont, parts, propStr) {
    return function(val) {
        var curCont = cont;
        var propPart = '';
        var containerLevels = [[cont, propPart]];
        var toDelete = isDeletable(val, propStr);
        var curPart;
        var i;

        for(i = 0; i < parts.length - 1; i++) {
            curPart = parts[i];

            if(typeof curPart === 'number' && !isArrayOrTypedArray(curCont)) {
                throw 'array index but container is not an array';
            }

            // handle special -1 array index
            if(curPart === -1) {
                toDelete = !setArrayAll(curCont, parts.slice(i + 1), val, propStr);
                if(toDelete) break;
                else return;
            }

            if(!checkNewContainer(curCont, curPart, parts[i + 1], toDelete)) {
                break;
            }

            curCont = curCont[curPart];

            if(typeof curCont !== 'object' || curCont === null) {
                throw 'container is not an object';
            }

            propPart = joinPropStr(propPart, curPart);

            containerLevels.push([curCont, propPart]);
        }

        if(toDelete) {
            if(i === parts.length - 1) {
                delete curCont[parts[i]];

                // The one bit of pruning we still do: drop `undefined` from the end of arrays.
                // In case someone has already unset previous items, continue until we hit a
                // non-undefined value.
                if(Array.isArray(curCont) && +parts[i] === curCont.length - 1) {
                    while(curCont.length && curCont[curCont.length - 1] === undefined) {
                        curCont.pop();
                    }
                }
            }
        } else curCont[parts[i]] = val;
    };
}

function joinPropStr(propStr, newPart) {
    var toAdd = newPart;
    if(isNumeric(newPart)) toAdd = '[' + newPart + ']';
    else if(propStr) toAdd = '.' + newPart;

    return propStr + toAdd;
}

// handle special -1 array index
function setArrayAll(containerArray, innerParts, val, propStr) {
    var arrayVal = isArrayOrTypedArray(val);
    var allSet = true;
    var thisVal = val;
    var thisPropStr = propStr.replace('-1', 0);
    var deleteThis = arrayVal ? false : isDeletable(val, thisPropStr);
    var firstPart = innerParts[0];
    var i;

    for(i = 0; i < containerArray.length; i++) {
        thisPropStr = propStr.replace('-1', i);
        if(arrayVal) {
            thisVal = val[i % val.length];
            deleteThis = isDeletable(thisVal, thisPropStr);
        }
        if(deleteThis) allSet = false;
        if(!checkNewContainer(containerArray, i, firstPart, deleteThis)) {
            continue;
        }
        npSet(containerArray[i], innerParts, propStr.replace('-1', i))(thisVal);
    }
    return allSet;
}

/**
 * make new sub-container as needed.
 * returns false if there's no container and none is needed
 * because we're only deleting an attribute
 */
function checkNewContainer(container, part, nextPart, toDelete) {
    if(container[part] === undefined) {
        if(toDelete) return false;

        if(typeof nextPart === 'number') container[part] = [];
        else container[part] = {};
    }
    return true;
}

function badContainer(container, propStr, propParts) {
    return {
        set: function() { throw 'bad container'; },
        get: function() {},
        astr: propStr,
        parts: propParts,
        obj: container
    };
}
