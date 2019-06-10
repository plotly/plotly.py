/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var isNumeric = require('fast-isnumeric');

var Lib = require('../../lib');
var extractOpts = require('./helpers').extractOpts;

module.exports = function calc(gd, trace, opts) {
    var fullLayout = gd._fullLayout;
    var vals = opts.vals;
    var containerStr = opts.containerStr;

    var container = containerStr ?
        Lib.nestedProperty(trace, containerStr).get() :
        trace;

    var cOpts = extractOpts(container);
    var auto = cOpts.auto !== false;
    var min = cOpts.min;
    var max = cOpts.max;
    var mid = cOpts.mid;

    var minVal = function() { return Lib.aggNums(Math.min, null, vals); };
    var maxVal = function() { return Lib.aggNums(Math.max, null, vals); };

    if(min === undefined) {
        min = minVal();
    } else if(auto) {
        if(container._colorAx && isNumeric(min)) {
            min = Math.min(min, minVal());
        } else {
            min = minVal();
        }
    }

    if(max === undefined) {
        max = maxVal();
    } else if(auto) {
        if(container._colorAx && isNumeric(max)) {
            max = Math.max(max, maxVal());
        } else {
            max = maxVal();
        }
    }

    if(auto && mid !== undefined) {
        if(max - mid > mid - min) {
            min = mid - (max - mid);
        } else if(max - mid < mid - min) {
            max = mid + (mid - min);
        }
    }

    if(min === max) {
        min -= 0.5;
        max += 0.5;
    }

    cOpts._sync('min', min);
    cOpts._sync('max', max);

    if(cOpts.autocolorscale) {
        var scl;
        if(min * max < 0) scl = fullLayout.colorscale.diverging;
        else if(min >= 0) scl = fullLayout.colorscale.sequential;
        else scl = fullLayout.colorscale.sequentialminus;
        cOpts._sync('colorscale', scl);
    }
};
