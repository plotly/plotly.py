/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var Registry = require('../../registry');
var isArrayOrTypedArray = require('../../lib').isArrayOrTypedArray;

module.exports = function makeBoundArray(trace, arrayIn, v0In, dvIn, numbricks, ax) {
    var arrayOut = [];
    var isContour = Registry.traceIs(trace, 'contour');
    var isHist = Registry.traceIs(trace, 'histogram');
    var isGL2D = Registry.traceIs(trace, 'gl2d');
    var v0;
    var dv;
    var i;

    var isArrayOfTwoItemsOrMore = isArrayOrTypedArray(arrayIn) && arrayIn.length > 1;

    if(isArrayOfTwoItemsOrMore && !isHist && (ax.type !== 'category')) {
        var len = arrayIn.length;

        // given vals are brick centers
        // hopefully length === numbricks, but use this method even if too few are supplied
        // and extend it linearly based on the last two points
        if(len <= numbricks) {
            // contour plots only want the centers
            if(isContour || isGL2D) arrayOut = arrayIn.slice(0, numbricks);
            else if(numbricks === 1) {
                arrayOut = [arrayIn[0] - 0.5, arrayIn[0] + 0.5];
            } else {
                arrayOut = [1.5 * arrayIn[0] - 0.5 * arrayIn[1]];

                for(i = 1; i < len; i++) {
                    arrayOut.push((arrayIn[i - 1] + arrayIn[i]) * 0.5);
                }

                arrayOut.push(1.5 * arrayIn[len - 1] - 0.5 * arrayIn[len - 2]);
            }

            if(len < numbricks) {
                var lastPt = arrayOut[arrayOut.length - 1];
                var delta = lastPt - arrayOut[arrayOut.length - 2];

                for(i = len; i < numbricks; i++) {
                    lastPt += delta;
                    arrayOut.push(lastPt);
                }
            }
        } else {
            // hopefully length === numbricks+1, but do something regardless:
            // given vals are brick boundaries
            return isContour ?
                arrayIn.slice(0, numbricks) :  // we must be strict for contours
                arrayIn.slice(0, numbricks + 1);
        }
    } else {
        var calendar = trace[ax._id.charAt(0) + 'calendar'];

        if(isHist) {
            v0 = ax.r2c(v0In, 0, calendar);
        } else {
            if(isArrayOrTypedArray(arrayIn) && arrayIn.length === 1) {
                v0 = arrayIn[0];
            } else if(v0In === undefined) {
                v0 = 0;
            } else {
                var fn = ax.type === 'log' ? ax.d2c : ax.r2c;
                v0 = fn(v0In, 0, calendar);
            }
        }

        dv = dvIn || 1;

        for(i = (isContour || isGL2D) ? 0 : -0.5; i < numbricks; i++) {
            arrayOut.push(v0 + dv * i);
        }
    }

    return arrayOut;
};
