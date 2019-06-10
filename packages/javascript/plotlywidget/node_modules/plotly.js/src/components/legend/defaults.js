/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var Registry = require('../../registry');
var Lib = require('../../lib');
var Template = require('../../plot_api/plot_template');

var attributes = require('./attributes');
var basePlotLayoutAttributes = require('../../plots/layout_attributes');
var helpers = require('./helpers');


module.exports = function legendDefaults(layoutIn, layoutOut, fullData) {
    var containerIn = layoutIn.legend || {};

    var legendTraceCount = 0;
    var legendReallyHasATrace = false;
    var defaultOrder = 'normal';

    var defaultX, defaultY, defaultXAnchor, defaultYAnchor;

    for(var i = 0; i < fullData.length; i++) {
        var trace = fullData[i];

        if(!trace.visible) continue;

        // Note that we explicitly count any trace that is either shown or
        // *would* be shown by default, toward the two traces you need to
        // ensure the legend is shown by default, because this can still help
        // disambiguate.
        if(trace.showlegend || trace._dfltShowLegend) {
            legendTraceCount++;
            if(trace.showlegend) {
                legendReallyHasATrace = true;
                // Always show the legend by default if there's a pie,
                // or if there's only one trace but it's explicitly shown
                if(Registry.traceIs(trace, 'pie-like') ||
                    trace._input.showlegend === true
                ) {
                    legendTraceCount++;
                }
            }
        }

        if((Registry.traceIs(trace, 'bar') && layoutOut.barmode === 'stack') ||
                ['tonextx', 'tonexty'].indexOf(trace.fill) !== -1) {
            defaultOrder = helpers.isGrouped({traceorder: defaultOrder}) ?
                'grouped+reversed' : 'reversed';
        }

        if(trace.legendgroup !== undefined && trace.legendgroup !== '') {
            defaultOrder = helpers.isReversed({traceorder: defaultOrder}) ?
                'reversed+grouped' : 'grouped';
        }
    }

    var showLegend = Lib.coerce(layoutIn, layoutOut,
        basePlotLayoutAttributes, 'showlegend',
        legendReallyHasATrace && legendTraceCount > 1);

    if(showLegend === false && !containerIn.uirevision) return;

    var containerOut = Template.newContainer(layoutOut, 'legend');

    function coerce(attr, dflt) {
        return Lib.coerce(containerIn, containerOut, attributes, attr, dflt);
    }

    coerce('uirevision', layoutOut.uirevision);

    if(showLegend === false) return;

    coerce('bgcolor', layoutOut.paper_bgcolor);
    coerce('bordercolor');
    coerce('borderwidth');
    Lib.coerceFont(coerce, 'font', layoutOut.font);

    coerce('orientation');
    if(containerOut.orientation === 'h') {
        var xaxis = layoutIn.xaxis;
        if(Registry.getComponentMethod('rangeslider', 'isVisible')(xaxis)) {
            defaultX = 0;
            defaultXAnchor = 'left';
            defaultY = 1.1;
            defaultYAnchor = 'bottom';
        } else {
            defaultX = 0;
            defaultXAnchor = 'left';
            defaultY = -0.1;
            defaultYAnchor = 'top';
        }
    }

    coerce('traceorder', defaultOrder);
    if(helpers.isGrouped(layoutOut.legend)) coerce('tracegroupgap');

    coerce('itemsizing');

    coerce('itemclick');
    coerce('itemdoubleclick');

    coerce('x', defaultX);
    coerce('xanchor', defaultXAnchor);
    coerce('y', defaultY);
    coerce('yanchor', defaultYAnchor);
    coerce('valign');
    Lib.noneOrAll(containerIn, containerOut, ['x', 'y']);
};
