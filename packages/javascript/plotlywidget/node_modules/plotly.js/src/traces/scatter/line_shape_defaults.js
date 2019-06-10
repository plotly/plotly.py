/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/


'use strict';


// common to 'scatter' and 'scatterternary'
module.exports = function handleLineShapeDefaults(traceIn, traceOut, coerce) {
    var shape = coerce('line.shape');
    if(shape === 'spline') coerce('line.smoothing');
};
