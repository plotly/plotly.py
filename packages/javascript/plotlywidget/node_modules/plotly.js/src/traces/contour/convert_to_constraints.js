/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var Lib = require('../../lib');

// The contour extraction is great, except it totally fails for constraints because we
// need weird range loops and flipped contours instead of the usual format. This function
// does some weird manipulation of the extracted pathinfo data such that it magically
// draws contours correctly *as* constraints.
module.exports = function(pathinfo, operation) {
    var i, pi0, pi1;

    var op0 = function(arr) { return arr.reverse(); };
    var op1 = function(arr) { return arr; };

    switch(operation) {
        case '=':
        case '<':
            return pathinfo;
        case '>':
            if(pathinfo.length !== 1) {
                Lib.warn('Contour data invalid for the specified inequality operation.');
            }

            // In this case there should be exactly two contour levels in pathinfo. We
            // simply concatenate the info into one pathinfo and flip all of the data
            // in one. This will draw the contour as closed.
            pi0 = pathinfo[0];

            for(i = 0; i < pi0.edgepaths.length; i++) {
                pi0.edgepaths[i] = op0(pi0.edgepaths[i]);
            }

            for(i = 0; i < pi0.paths.length; i++) {
                pi0.paths[i] = op0(pi0.paths[i]);
            }
            return pathinfo;
        case '][':
            var tmp = op0;
            op0 = op1;
            op1 = tmp;
            // It's a nice rule, except this definitely *is* what's intended here.
            /* eslint-disable: no-fallthrough */
        case '[]':
            /* eslint-enable: no-fallthrough */
            if(pathinfo.length !== 2) {
                Lib.warn('Contour data invalid for the specified inequality range operation.');
            }

            // In this case there should be exactly two contour levels in pathinfo. We
            // simply concatenate the info into one pathinfo and flip all of the data
            // in one. This will draw the contour as closed.
            pi0 = copyPathinfo(pathinfo[0]);
            pi1 = copyPathinfo(pathinfo[1]);

            for(i = 0; i < pi0.edgepaths.length; i++) {
                pi0.edgepaths[i] = op0(pi0.edgepaths[i]);
            }

            for(i = 0; i < pi0.paths.length; i++) {
                pi0.paths[i] = op0(pi0.paths[i]);
            }

            while(pi1.edgepaths.length) {
                pi0.edgepaths.push(op1(pi1.edgepaths.shift()));
            }
            while(pi1.paths.length) {
                pi0.paths.push(op1(pi1.paths.shift()));
            }
            return [pi0];
    }
};

function copyPathinfo(pi) {
    return Lib.extendFlat({}, pi, {
        edgepaths: Lib.extendDeep([], pi.edgepaths),
        paths: Lib.extendDeep([], pi.paths)
    });
}
