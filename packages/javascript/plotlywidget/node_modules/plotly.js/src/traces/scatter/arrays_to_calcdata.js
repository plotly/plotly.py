/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/


'use strict';

var Lib = require('../../lib');


// arrayOk attributes, merge them into calcdata array
module.exports = function arraysToCalcdata(cd, trace) {
    // so each point knows which index it originally came from
    for(var i = 0; i < cd.length; i++) cd[i].i = i;

    Lib.mergeArray(trace.text, cd, 'tx');
    Lib.mergeArray(trace.hovertext, cd, 'htx');
    Lib.mergeArray(trace.customdata, cd, 'data');
    Lib.mergeArray(trace.textposition, cd, 'tp');
    if(trace.textfont) {
        Lib.mergeArray(trace.textfont.size, cd, 'ts');
        Lib.mergeArray(trace.textfont.color, cd, 'tc');
        Lib.mergeArray(trace.textfont.family, cd, 'tf');
    }

    var marker = trace.marker;
    if(marker) {
        Lib.mergeArray(marker.size, cd, 'ms');
        Lib.mergeArray(marker.opacity, cd, 'mo');
        Lib.mergeArray(marker.symbol, cd, 'mx');
        Lib.mergeArray(marker.color, cd, 'mc');

        var markerLine = marker.line;
        if(marker.line) {
            Lib.mergeArray(markerLine.color, cd, 'mlc');
            Lib.mergeArray(markerLine.width, cd, 'mlw');
        }

        var markerGradient = marker.gradient;
        if(markerGradient && markerGradient.type !== 'none') {
            Lib.mergeArray(markerGradient.type, cd, 'mgt');
            Lib.mergeArray(markerGradient.color, cd, 'mgc');
        }
    }
};
