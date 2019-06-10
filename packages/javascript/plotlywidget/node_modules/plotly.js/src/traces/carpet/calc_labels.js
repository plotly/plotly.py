/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var Axes = require('../../plots/cartesian/axes');
var extendFlat = require('../../lib/extend').extendFlat;

module.exports = function calcLabels(trace, axis) {
    var i, tobj, prefix, suffix, gridline;

    var labels = axis._labels = [];
    var gridlines = axis._gridlines;

    for(i = 0; i < gridlines.length; i++) {
        gridline = gridlines[i];

        if(['start', 'both'].indexOf(axis.showticklabels) !== -1) {
            tobj = Axes.tickText(axis, gridline.value);

            extendFlat(tobj, {
                prefix: prefix,
                suffix: suffix,
                endAnchor: true,
                xy: gridline.xy(0),
                dxy: gridline.dxy(0, 0),
                axis: gridline.axis,
                length: gridline.crossAxis.length,
                font: gridline.axis.tickfont,
                isFirst: i === 0,
                isLast: i === gridlines.length - 1
            });

            labels.push(tobj);
        }

        if(['end', 'both'].indexOf(axis.showticklabels) !== -1) {
            tobj = Axes.tickText(axis, gridline.value);

            extendFlat(tobj, {
                endAnchor: false,
                xy: gridline.xy(gridline.crossLength - 1),
                dxy: gridline.dxy(gridline.crossLength - 2, 1),
                axis: gridline.axis,
                length: gridline.crossAxis.length,
                font: gridline.axis.tickfont,
                isFirst: i === 0,
                isLast: i === gridlines.length - 1
            });

            labels.push(tobj);
        }
    }
};
