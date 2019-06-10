/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

exports.pointsAccessorFunction = function(transforms, opts) {
    var tr;
    var prevIndexToPoints;
    for(var i = 0; i < transforms.length; i++) {
        tr = transforms[i];
        if(tr === opts) break;
        if(!tr._indexToPoints || tr.enabled === false) continue;
        prevIndexToPoints = tr._indexToPoints;
    }
    var originalPointsAccessor = prevIndexToPoints ?
        function(i) {return prevIndexToPoints[i];} :
        function(i) {return [i];};
    return originalPointsAccessor;
};
