/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

/*
 * Fill in a 1D array via linear interpolation. This *is* the basis, so we
 * don't have to scale this by some basis as we do for the 2D version. That
 * makes this much simpler. Just loop over it and do the best we can to fill
 * the array.
 */
module.exports = function smoothFillArray(data) {
    var i, i0, i1;
    var n = data.length;

    for(i = 0; i < n; i++) {
        if(data[i] !== undefined) {
            i0 = i;
            break;
        }
    }

    for(i = n - 1; i >= 0; i--) {
        if(data[i] !== undefined) {
            i1 = i;
            break;
        }
    }

    if(i0 === undefined) {
        // Fill with zeros and return early;
        for(i = 0; i < n; i++) {
            data[i] = 0;
        }

        return data;
    } else if(i0 === i1) {
        // Only one data point so can't extrapolate. Fill with it and return early:
        for(i = 0; i < n; i++) {
            data[i] = data[i0];
        }

        return data;
    }

    var iA = i0;
    var iB;
    var m, b, dA, dB;

    // Fill in interior data. When we land on an undefined point,
    // look ahead until the next defined point and then fill in linearly:
    for(i = i0; i < i1; i++) {
        if(data[i] === undefined) {
            iA = iB = i;
            while(iB < i1 && data[iB] === undefined) iB++;

            dA = data[iA - 1];
            dB = data[iB];

            // Lots of variables, but it's just mx + b:
            m = (dB - dA) / (iB - iA + 1);
            b = dA + (1 - iA) * m;

            // Note that this *does* increment the outer loop counter. Worried a linter
            // might complain, but it's the whole point in this case:
            for(i = iA; i < iB; i++) {
                data[i] = m * i + b;
            }

            i = iA = iB;
        }
    }

    // Fill in up to the first data point:
    if(i0 > 0) {
        m = data[i0 + 1] - data[i0];
        b = data[i0];
        for(i = 0; i < i0; i++) {
            data[i] = m * (i - i0) + b;
        }
    }

    // Fill in after the last data point:
    if(i1 < n - 1) {
        m = data[i1] - data[i1 - 1];
        b = data[i1];
        for(i = i1 + 1; i < n; i++) {
            data[i] = m * (i - i1) + b;
        }
    }

    return data;
};
