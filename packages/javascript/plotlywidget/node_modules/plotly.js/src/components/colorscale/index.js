/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var scales = require('./scales');
var helpers = require('./helpers');

module.exports = {
    moduleType: 'component',
    name: 'colorscale',

    attributes: require('./attributes'),
    layoutAttributes: require('./layout_attributes'),

    supplyLayoutDefaults: require('./layout_defaults'),
    handleDefaults: require('./defaults'),
    crossTraceDefaults: require('./cross_trace_defaults'),

    calc: require('./calc'),

    // ./scales.js is required in lib/coerce.js ;
    // it needs to be a seperate module to avoid circular a dependency
    scales: scales.scales,
    defaultScale: scales.defaultScale,
    getScale: scales.get,
    isValidScale: scales.isValid,

    hasColorscale: helpers.hasColorscale,
    extractOpts: helpers.extractOpts,
    extractScale: helpers.extractScale,
    flipScale: helpers.flipScale,
    makeColorScaleFunc: helpers.makeColorScaleFunc,
    makeColorScaleFuncFromTrace: helpers.makeColorScaleFuncFromTrace
};
