/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/


'use strict';

var colorscaleDefaults = require('../../components/colorscale/defaults');
var handleLabelDefaults = require('./label_defaults');


module.exports = function handleStyleDefaults(traceIn, traceOut, coerce, layout, opts) {
    var coloring = coerce('contours.coloring');

    var showLines;
    var lineColor = '';
    if(coloring === 'fill') showLines = coerce('contours.showlines');

    if(showLines !== false) {
        if(coloring !== 'lines') lineColor = coerce('line.color', '#000');
        coerce('line.width', 0.5);
        coerce('line.dash');
    }

    if(coloring !== 'none') {
        // plots/plots always coerces showlegend to true, but in this case
        // we default to false and (by default) show a colorbar instead
        if(traceIn.showlegend !== true) traceOut.showlegend = false;
        traceOut._dfltShowLegend = false;

        colorscaleDefaults(
            traceIn, traceOut, layout, coerce, {prefix: '', cLetter: 'z'}
        );
    }

    coerce('line.smoothing');

    handleLabelDefaults(coerce, layout, lineColor, opts);
};
