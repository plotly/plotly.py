/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

module.exports = function selectPoints(searchInfo, selectionTester) {
    var cd = searchInfo.cd;
    var selection = [];
    var fullData = cd[0].trace;

    var nodes = fullData._sankey.graph.nodes;

    for(var i = 0; i < nodes.length; i++) {
        var node = nodes[i];
        if(node.partOfGroup) continue; // Those are invisible

        // Position of node's centroid
        var pos = [(node.x0 + node.x1) / 2, (node.y0 + node.y1) / 2];

        // Swap x and y if trace is vertical
        if(fullData.orientation === 'v') pos.reverse();

        if(selectionTester && selectionTester.contains(pos, false, i, searchInfo)) {
            selection.push({
                pointNumber: node.pointNumber
                // TODO: add eventData
            });
        }
    }
    return selection;
};
