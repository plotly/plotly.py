/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var extendFlat = require('../../lib/extend').extendFlat;

// pure functions, don't alter but passes on `gd` and parts of `trace` without deep copying

exports.splitToPanels = function(d) {
    var prevPages = [0, 0];
    var headerPanel = extendFlat({}, d, {
        key: 'header',
        type: 'header',
        page: 0,
        prevPages: prevPages,
        currentRepaint: [null, null],
        dragHandle: true,
        values: d.calcdata.headerCells.values[d.specIndex],
        rowBlocks: d.calcdata.headerRowBlocks,
        calcdata: extendFlat({}, d.calcdata, {cells: d.calcdata.headerCells})
    });
    var revolverPanel1 = extendFlat({}, d, {
        key: 'cells1',
        type: 'cells',
        page: 0,
        prevPages: prevPages,
        currentRepaint: [null, null],
        dragHandle: false,
        values: d.calcdata.cells.values[d.specIndex],
        rowBlocks: d.calcdata.rowBlocks
    });
    var revolverPanel2 = extendFlat({}, d, {
        key: 'cells2',
        type: 'cells',
        page: 1,
        prevPages: prevPages,
        currentRepaint: [null, null],
        dragHandle: false,
        values: d.calcdata.cells.values[d.specIndex],
        rowBlocks: d.calcdata.rowBlocks
    });
    // order due to SVG using painter's algo:
    return [revolverPanel1, revolverPanel2, headerPanel];
};

exports.splitToCells = function(d) {
    var fromTo = rowFromTo(d);
    return (d.values || []).slice(fromTo[0], fromTo[1]).map(function(v, i) {
        // By keeping identical key, a DOM node removal, creation and addition is spared, important when visible
        // grid has a lot of elements (quadratic with xcol/ycol count).
        // But it has to be busted when `svgUtil.convertToTspans` is used as it reshapes cell subtrees asynchronously,
        // and by that time the user may have scrolled away, resulting in stale overwrites. The real solution will be
        // to turn `svgUtil.convertToTspans` into a cancelable request, in which case no key busting is needed.
        var buster = (typeof v === 'string') && v.match(/[<$&> ]/) ? '_keybuster_' + Math.random() : '';
        return {
            // keyWithinBlock: /*fromTo[0] + */i, // optimized future version - no busting
            // keyWithinBlock: fromTo[0] + i, // initial always-unoptimized version - janky scrolling with 5+ columns
            keyWithinBlock: i + buster, // current compromise: regular content is very fast; async content is possible
            key: fromTo[0] + i,
            column: d,
            calcdata: d.calcdata,
            page: d.page,
            rowBlocks: d.rowBlocks,
            value: v
        };
    });
};

function rowFromTo(d) {
    var rowBlock = d.rowBlocks[d.page];
    // fixme rowBlock truthiness check is due to ugly hack of placing 2nd panel as d.page = -1
    var rowFrom = rowBlock ? rowBlock.rows[0].rowIndex : 0;
    var rowTo = rowBlock ? rowFrom + rowBlock.rows.length : 0;
    return [rowFrom, rowTo];
}
