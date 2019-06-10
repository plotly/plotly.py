/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/


'use strict';

var Lib = require('../../lib');
var Axes = require('../../plots/cartesian/axes');

var draw = require('./draw').draw;


module.exports = function calcAutorange(gd) {
    var fullLayout = gd._fullLayout;
    var annotationList = Lib.filterVisible(fullLayout.annotations);

    if(annotationList.length && gd._fullData.length) {
        return Lib.syncOrAsync([draw, annAutorange], gd);
    }
};

function annAutorange(gd) {
    var fullLayout = gd._fullLayout;

    // find the bounding boxes for each of these annotations'
    // relative to their anchor points
    // use the arrow and the text bg rectangle,
    // as the whole anno may include hidden text in its bbox
    Lib.filterVisible(fullLayout.annotations).forEach(function(ann) {
        var xa = Axes.getFromId(gd, ann.xref);
        var ya = Axes.getFromId(gd, ann.yref);

        ann._extremes = {};
        if(xa) calcAxisExpansion(ann, xa);
        if(ya) calcAxisExpansion(ann, ya);
    });
}

function calcAxisExpansion(ann, ax) {
    var axId = ax._id;
    var letter = axId.charAt(0);
    var pos = ann[letter];
    var apos = ann['a' + letter];
    var ref = ann[letter + 'ref'];
    var aref = ann['a' + letter + 'ref'];
    var padplus = ann['_' + letter + 'padplus'];
    var padminus = ann['_' + letter + 'padminus'];
    var shift = {x: 1, y: -1}[letter] * ann[letter + 'shift'];
    var headSize = 3 * ann.arrowsize * ann.arrowwidth || 0;
    var headPlus = headSize + shift;
    var headMinus = headSize - shift;
    var startHeadSize = 3 * ann.startarrowsize * ann.arrowwidth || 0;
    var startHeadPlus = startHeadSize + shift;
    var startHeadMinus = startHeadSize - shift;
    var extremes;

    if(aref === ref) {
        // expand for the arrowhead (padded by arrowhead)
        var extremeArrowHead = Axes.findExtremes(ax, [ax.r2c(pos)], {
            ppadplus: headPlus,
            ppadminus: headMinus
        });
        // again for the textbox (padded by textbox)
        var extremeText = Axes.findExtremes(ax, [ax.r2c(apos)], {
            ppadplus: Math.max(padplus, startHeadPlus),
            ppadminus: Math.max(padminus, startHeadMinus)
        });
        extremes = {
            min: [extremeArrowHead.min[0], extremeText.min[0]],
            max: [extremeArrowHead.max[0], extremeText.max[0]]
        };
    } else {
        startHeadPlus = apos ? startHeadPlus + apos : startHeadPlus;
        startHeadMinus = apos ? startHeadMinus - apos : startHeadMinus;
        extremes = Axes.findExtremes(ax, [ax.r2c(pos)], {
            ppadplus: Math.max(padplus, headPlus, startHeadPlus),
            ppadminus: Math.max(padminus, headMinus, startHeadMinus)
        });
    }

    ann._extremes[axId] = extremes;
}
