/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/


'use strict';

var Lib = require('../lib');
var Template = require('../plot_api/plot_template');
var handleDomainDefaults = require('./domain').defaults;


/**
 * Find and supply defaults to all subplots of a given type
 * This handles subplots that are contained within one container - so
 * gl3d, geo, ternary... but not 2d axes which have separate x and y axes
 * finds subplots, coerces their `domain` attributes, then calls the
 * given handleDefaults function to fill in everything else.
 *
 * layoutIn: the complete user-supplied input layout
 * layoutOut: the complete finished layout
 * fullData: the finished data array, used only to find subplots
 * opts: {
 *  type: subplot type string
 *  attributes: subplot attributes object
 *  partition: 'x' or 'y', which direction to divide domain space by default
 *      (default 'x', ie side-by-side subplots)
 *      TODO: this option is only here because 3D and geo made opposite
 *      choices in this regard previously and I didn't want to change it.
 *      Instead we should do:
 *      - something consistent
 *      - something more square (4 cuts 2x2, 5/6 cuts 2x3, etc.)
 *      - something that includes all subplot types in one arrangement,
 *        now that we can have them together!
 *  handleDefaults: function of (subplotLayoutIn, subplotLayoutOut, coerce, opts)
 *      this opts object is passed through to handleDefaults, so attach any
 *      additional items needed by this function here as well
 * }
 */
module.exports = function handleSubplotDefaults(layoutIn, layoutOut, fullData, opts) {
    var subplotType = opts.type;
    var subplotAttributes = opts.attributes;
    var handleDefaults = opts.handleDefaults;
    var partition = opts.partition || 'x';

    var ids = layoutOut._subplots[subplotType];
    var idsLength = ids.length;

    var baseId = idsLength && ids[0].replace(/\d+$/, '');

    var subplotLayoutIn, subplotLayoutOut;

    function coerce(attr, dflt) {
        return Lib.coerce(subplotLayoutIn, subplotLayoutOut, subplotAttributes, attr, dflt);
    }

    for(var i = 0; i < idsLength; i++) {
        var id = ids[i];

        // ternary traces get a layout ternary for free!
        if(layoutIn[id]) subplotLayoutIn = layoutIn[id];
        else subplotLayoutIn = layoutIn[id] = {};

        subplotLayoutOut = Template.newContainer(layoutOut, id, baseId);

        // All subplot containers get a `uirevision` inheriting from the base.
        // Currently all subplots containers have some user interaction
        // attributes, but if we ever add one that doesn't, we would need an
        // option to skip this step.
        coerce('uirevision', layoutOut.uirevision);

        var dfltDomains = {};
        dfltDomains[partition] = [i / idsLength, (i + 1) / idsLength];
        handleDomainDefaults(subplotLayoutOut, layoutOut, coerce, dfltDomains);

        opts.id = id;
        handleDefaults(subplotLayoutIn, subplotLayoutOut, coerce, opts);
    }
};
