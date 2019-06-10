/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var handleAxisDefaults = require('./axis_defaults');
var Template = require('../../plot_api/plot_template');

module.exports = function handleABDefaults(traceIn, traceOut, fullLayout, coerce, dfltColor) {
    var a = coerce('a');

    if(!a) {
        coerce('da');
        coerce('a0');
    }

    var b = coerce('b');

    if(!b) {
        coerce('db');
        coerce('b0');
    }

    mimickAxisDefaults(traceIn, traceOut, fullLayout, dfltColor);
};

function mimickAxisDefaults(traceIn, traceOut, fullLayout, dfltColor) {
    var axesList = ['aaxis', 'baxis'];

    axesList.forEach(function(axName) {
        var axLetter = axName.charAt(0);
        var axIn = traceIn[axName] || {};
        var axOut = Template.newContainer(traceOut, axName);

        var defaultOptions = {
            tickfont: 'x',
            id: axLetter + 'axis',
            letter: axLetter,
            font: traceOut.font,
            name: axName,
            data: traceIn[axLetter],
            calendar: traceOut.calendar,
            dfltColor: dfltColor,
            bgColor: fullLayout.paper_bgcolor,
            fullLayout: fullLayout
        };

        handleAxisDefaults(axIn, axOut, defaultOptions);
        axOut._categories = axOut._categories || [];

        // so we don't have to repeat autotype unnecessarily,
        // copy an autotype back to traceIn
        if(!traceIn[axName] && axIn.type !== '-') {
            traceIn[axName] = {type: axIn.type};
        }
    });
}
