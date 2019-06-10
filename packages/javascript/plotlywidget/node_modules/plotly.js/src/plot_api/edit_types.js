/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var Lib = require('../lib');
var extendFlat = Lib.extendFlat;
var isPlainObject = Lib.isPlainObject;

var traceOpts = {
    valType: 'flaglist',
    extras: ['none'],
    flags: ['calc', 'clearAxisTypes', 'plot', 'style', 'markerSize', 'colorbars'],
    description: [
        'trace attributes should include an `editType` string matching this flaglist.',
        '*calc* is the most extensive: a full `Plotly.plot` starting by clearing `gd.calcdata`',
        'to force it to be regenerated',
        '*clearAxisTypes* resets the types of the axes this trace is on, because new data could',
        'cause the automatic axis type detection to change. Log type will not be cleared, as that',
        'is never automatically chosen so must have been user-specified.',
        '*plot* calls `Plotly.plot` but without first clearing `gd.calcdata`.',
        '*style* only calls `module.style` (or module.editStyle) for all trace modules and redraws the legend.',
        '*markerSize* is like *style*, but propagate axis-range changes due to scatter `marker.size`',
        '*colorbars* only redraws colorbars.'
    ].join(' ')
};

var layoutOpts = {
    valType: 'flaglist',
    extras: ['none'],
    flags: [
        'calc', 'plot', 'legend', 'ticks', 'axrange',
        'layoutstyle', 'modebar', 'camera', 'arraydraw', 'colorbars'
    ],
    description: [
        'layout attributes should include an `editType` string matching this flaglist.',
        '*calc* is the most extensive: a full `Plotly.plot` starting by clearing `gd.calcdata`',
        'to force it to be regenerated',
        '*plot* calls `Plotly.plot` but without first clearing `gd.calcdata`.',
        '*legend* only redraws the legend.',
        '*ticks* only redraws axis ticks, labels, and gridlines.',
        '*axrange* minimal sequence when updating axis ranges.',
        '*layoutstyle* reapplies global and SVG cartesian axis styles.',
        '*modebar* just updates the modebar.',
        '*camera* just updates the camera settings for gl3d scenes.',
        '*arraydraw* allows component arrays to invoke the redraw routines just for the',
        'component(s) that changed.',
        '*colorbars* only redraws colorbars.'
    ].join(' ')
};

// flags for inside restyle/relayout include a few extras
// that shouldn't be used in attributes, to deal with certain
// combinations and conditionals efficiently
var traceEditTypeFlags = traceOpts.flags.slice()
    .concat(['fullReplot']);

var layoutEditTypeFlags = layoutOpts.flags.slice()
    .concat('layoutReplot');

module.exports = {
    traces: traceOpts,
    layout: layoutOpts,
    /*
     * default (all false) edit flags for restyle (traces)
     * creates a new object each call, so the caller can mutate freely
     */
    traceFlags: function() { return falseObj(traceEditTypeFlags); },

    /*
     * default (all false) edit flags for relayout
     * creates a new object each call, so the caller can mutate freely
     */
    layoutFlags: function() { return falseObj(layoutEditTypeFlags); },

    /*
     * update `flags` with the `editType` values found in `attr`
     */
    update: function(flags, attr) {
        var editType = attr.editType;
        if(editType && editType !== 'none') {
            var editTypeParts = editType.split('+');
            for(var i = 0; i < editTypeParts.length; i++) {
                flags[editTypeParts[i]] = true;
            }
        }
    },

    overrideAll: overrideAll
};

function falseObj(keys) {
    var out = {};
    for(var i = 0; i < keys.length; i++) out[keys[i]] = false;
    return out;
}

/**
 * For attributes that are largely copied from elsewhere into a plot type that doesn't
 * support partial redraws - overrides the editType field of all attributes in the object
 *
 * @param {object} attrs: the attributes to override. Will not be mutated.
 * @param {string} editTypeOverride: the new editType to use
 * @param {'nested'|'from-root'} overrideContainers:
 *   - 'nested' will override editType for nested containers but not the root.
 *   - 'from-root' will also override editType of the root container.
 *   Containers below the absolute top level (trace or layout root) DO need an
 *   editType even if they are not `valObject`s themselves (eg `scatter.marker`)
 *   to handle the case where you edit the whole container.
 *
 * @return {object} a new attributes object with `editType` modified as directed
 */
function overrideAll(attrs, editTypeOverride, overrideContainers) {
    var out = extendFlat({}, attrs);
    for(var key in out) {
        var attr = out[key];
        if(isPlainObject(attr)) {
            out[key] = overrideOne(attr, editTypeOverride, overrideContainers, key);
        }
    }
    if(overrideContainers === 'from-root') out.editType = editTypeOverride;

    return out;
}

function overrideOne(attr, editTypeOverride, overrideContainers, key) {
    if(attr.valType) {
        var out = extendFlat({}, attr);
        out.editType = editTypeOverride;

        if(Array.isArray(attr.items)) {
            out.items = new Array(attr.items.length);
            for(var i = 0; i < attr.items.length; i++) {
                out.items[i] = overrideOne(attr.items[i], editTypeOverride, 'from-root');
            }
        }
        return out;
    } else {
        // don't provide an editType for the _deprecated container
        return overrideAll(attr, editTypeOverride,
            (key.charAt(0) === '_') ? 'nested' : 'from-root');
    }
}
