/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var hasColorscale = require('../../components/colorscale/helpers').hasColorscale;
var colorscaleCalc = require('../../components/colorscale/calc');
var arraysToCalcdata = require('../bar/arrays_to_calcdata');
var setGroupPositions = require('../bar/cross_trace_calc').setGroupPositions;
var calcSelection = require('../scatter/calc_selection');
var traceIs = require('../../registry').traceIs;
var extendFlat = require('../../lib').extendFlat;

function calc(gd, trace) {
    var fullLayout = gd._fullLayout;
    var subplotId = trace.subplot;
    var radialAxis = fullLayout[subplotId].radialaxis;
    var angularAxis = fullLayout[subplotId].angularaxis;
    var rArray = radialAxis.makeCalcdata(trace, 'r');
    var thetaArray = angularAxis.makeCalcdata(trace, 'theta');
    var len = trace._length;
    var cd = new Array(len);

    // 'size' axis variables
    var sArray = rArray;
    // 'pos' axis variables
    var pArray = thetaArray;

    for(var i = 0; i < len; i++) {
        cd[i] = {p: pArray[i], s: sArray[i]};
    }

    // convert width and offset in 'c' coordinate,
    // set 'c' value(s) in trace._width and trace._offset,
    // to make Bar.crossTraceCalc "just work"
    function d2c(attr) {
        var val = trace[attr];
        if(val !== undefined) {
            trace['_' + attr] = Array.isArray(val) ?
                angularAxis.makeCalcdata(trace, attr) :
                angularAxis.d2c(val, trace.thetaunit);
        }
    }

    if(angularAxis.type === 'linear') {
        d2c('width');
        d2c('offset');
    }

    if(hasColorscale(trace, 'marker')) {
        colorscaleCalc(gd, trace, {
            vals: trace.marker.color,
            containerStr: 'marker',
            cLetter: 'c'
        });
    }
    if(hasColorscale(trace, 'marker.line')) {
        colorscaleCalc(gd, trace, {
            vals: trace.marker.line.color,
            containerStr: 'marker.line',
            cLetter: 'c'
        });
    }

    arraysToCalcdata(cd, trace);
    calcSelection(cd, trace);

    return cd;
}

function crossTraceCalc(gd, polarLayout, subplotId) {
    var calcdata = gd.calcdata;
    var barPolarCd = [];

    for(var i = 0; i < calcdata.length; i++) {
        var cdi = calcdata[i];
        var trace = cdi[0].trace;

        if(trace.visible === true && traceIs(trace, 'bar') &&
            trace.subplot === subplotId
        ) {
            barPolarCd.push(cdi);
        }
    }

    // to make _extremes is filled in correctly so that
    // polar._subplot.radialAxis can get auotrange'd
    // TODO clean up!
    // I think we want to call getAutorange on polar.radialaxis
    // NOT on polar._subplot.radialAxis
    var rAxis = extendFlat({}, polarLayout.radialaxis, {_id: 'x'});
    var aAxis = polarLayout.angularaxis;

    setGroupPositions(gd, aAxis, rAxis, barPolarCd, {
        mode: polarLayout.barmode,
        norm: polarLayout.barnorm,
        gap: polarLayout.bargap,
        groupgap: polarLayout.bargroupgap
    });
}

module.exports = {
    calc: calc,
    crossTraceCalc: crossTraceCalc
};
