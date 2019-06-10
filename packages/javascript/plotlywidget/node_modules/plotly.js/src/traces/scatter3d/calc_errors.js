/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var Registry = require('../../registry');

function calculateAxisErrors(data, params, scaleFactor, axis) {
    if(!params || !params.visible) return null;

    var computeError = Registry.getComponentMethod('errorbars', 'makeComputeError')(params);
    var result = new Array(data.length);

    for(var i = 0; i < data.length; i++) {
        var errors = computeError(+data[i], i);

        if(axis.type === 'log') {
            var point = axis.c2l(data[i]);
            var min = data[i] - errors[0];
            var max = data[i] + errors[1];

            result[i] = [
                (axis.c2l(min, true) - point) * scaleFactor,
                (axis.c2l(max, true) - point) * scaleFactor
            ];

            // Keep track of the lower error bound which isn't negative!
            if(min > 0) {
                var lower = axis.c2l(min);
                if(!axis._lowerLogErrorBound) axis._lowerLogErrorBound = lower;
                axis._lowerErrorBound = Math.min(axis._lowerLogErrorBound, lower);
            }
        } else {
            result[i] = [
                -errors[0] * scaleFactor,
                errors[1] * scaleFactor
            ];
        }
    }

    return result;
}

function dataLength(array) {
    for(var i = 0; i < array.length; i++) {
        if(array[i]) return array[i].length;
    }
    return 0;
}

function calculateErrors(data, scaleFactor, sceneLayout) {
    var errors = [
        calculateAxisErrors(data.x, data.error_x, scaleFactor[0], sceneLayout.xaxis),
        calculateAxisErrors(data.y, data.error_y, scaleFactor[1], sceneLayout.yaxis),
        calculateAxisErrors(data.z, data.error_z, scaleFactor[2], sceneLayout.zaxis)
    ];

    var n = dataLength(errors);
    if(n === 0) return null;

    var errorBounds = new Array(n);

    for(var i = 0; i < n; i++) {
        var bound = [[0, 0, 0], [0, 0, 0]];

        for(var j = 0; j < 3; j++) {
            if(errors[j]) {
                for(var k = 0; k < 2; k++) {
                    bound[k][j] = errors[j][i][k];
                }
            }
        }

        errorBounds[i] = bound;
    }

    return errorBounds;
}

module.exports = calculateErrors;
