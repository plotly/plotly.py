/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var cleanTicks = require('./clean_ticks');

module.exports = function handleTickValueDefaults(containerIn, containerOut, coerce, axType) {
    var tickmode;

    if(containerIn.tickmode === 'array' &&
            (axType === 'log' || axType === 'date')) {
        tickmode = containerOut.tickmode = 'auto';
    } else {
        var tickmodeDefault = Array.isArray(containerIn.tickvals) ? 'array' :
            containerIn.dtick ? 'linear' :
            'auto';
        tickmode = coerce('tickmode', tickmodeDefault);
    }

    if(tickmode === 'auto') coerce('nticks');
    else if(tickmode === 'linear') {
        // dtick is usually a positive number, but there are some
        // special strings available for log or date axes
        // tick0 also has special logic
        var dtick = containerOut.dtick = cleanTicks.dtick(
            containerIn.dtick, axType);
        containerOut.tick0 = cleanTicks.tick0(
            containerIn.tick0, axType, containerOut.calendar, dtick);
    } else if(axType !== 'multicategory') {
        var tickvals = coerce('tickvals');
        if(tickvals === undefined) containerOut.tickmode = 'auto';
        else coerce('ticktext');
    }
};
