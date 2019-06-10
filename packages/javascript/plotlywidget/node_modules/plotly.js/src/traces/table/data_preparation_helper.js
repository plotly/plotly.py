/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var c = require('./constants');
var extendFlat = require('../../lib/extend').extendFlat;
var isNumeric = require('fast-isnumeric');

// pure functions, don't alter but passes on `gd` and parts of `trace` without deep copying
module.exports = function calc(gd, trace) {
    var cellsValues = squareStringMatrix(trace.cells.values);
    var slicer = function(a) {
        return a.slice(trace.header.values.length, a.length);
    };
    var headerValuesIn = squareStringMatrix(trace.header.values);
    if(headerValuesIn.length && !headerValuesIn[0].length) {
        headerValuesIn[0] = [''];
        headerValuesIn = squareStringMatrix(headerValuesIn);
    }
    var headerValues = headerValuesIn
        .concat(slicer(cellsValues).map(function() {
            return emptyStrings((headerValuesIn[0] || ['']).length);
        }));

    var domain = trace.domain;
    var groupWidth = Math.floor(gd._fullLayout._size.w * (domain.x[1] - domain.x[0]));
    var groupHeight = Math.floor(gd._fullLayout._size.h * (domain.y[1] - domain.y[0]));
    var headerRowHeights = trace.header.values.length ?
        headerValues[0].map(function() { return trace.header.height; }) :
        [c.emptyHeaderHeight];
    var rowHeights = cellsValues.length ? cellsValues[0].map(function() { return trace.cells.height; }) : [];
    var headerHeight = headerRowHeights.reduce(sum, 0);
    var scrollHeight = groupHeight - headerHeight;
    var minimumFillHeight = scrollHeight + c.uplift;
    var anchorToRowBlock = makeAnchorToRowBlock(rowHeights, minimumFillHeight);
    var anchorToHeaderRowBlock = makeAnchorToRowBlock(headerRowHeights, headerHeight);
    var headerRowBlocks = makeRowBlock(anchorToHeaderRowBlock, []);
    var rowBlocks = makeRowBlock(anchorToRowBlock, headerRowBlocks);
    var uniqueKeys = {};
    var columnOrder = trace._fullInput.columnorder.concat(slicer(cellsValues.map(function(d, i) {return i;})));
    var columnWidths = headerValues.map(function(d, i) {
        var value = Array.isArray(trace.columnwidth) ?
            trace.columnwidth[Math.min(i, trace.columnwidth.length - 1)] :
            trace.columnwidth;
        return isNumeric(value) ? Number(value) : 1;
    });
    var totalColumnWidths = columnWidths.reduce(sum, 0);

    // fit columns in the available vertical space as there's no vertical scrolling now
    columnWidths = columnWidths.map(function(d) { return d / totalColumnWidths * groupWidth; });

    var maxLineWidth = Math.max(arrayMax(trace.header.line.width), arrayMax(trace.cells.line.width));

    var calcdata = {
        // include staticPlot in the key so if it changes we delete and redraw
        key: trace.uid + gd._context.staticPlot,
        translateX: domain.x[0] * gd._fullLayout._size.w,
        translateY: gd._fullLayout._size.h * (1 - domain.y[1]),
        size: gd._fullLayout._size,
        width: groupWidth,
        maxLineWidth: maxLineWidth,
        height: groupHeight,
        columnOrder: columnOrder, // will be mutated on column move, todo use in callback
        groupHeight: groupHeight,
        rowBlocks: rowBlocks,
        headerRowBlocks: headerRowBlocks,
        scrollY: 0, // will be mutated on scroll
        cells: extendFlat({}, trace.cells, {values: cellsValues}),
        headerCells: extendFlat({}, trace.header, {values: headerValues}),
        gdColumns: headerValues.map(function(d) {return d[0];}),
        gdColumnsOriginalOrder: headerValues.map(function(d) {return d[0];}),
        prevPages: [0, 0],
        scrollbarState: {scrollbarScrollInProgress: false},
        columns: headerValues.map(function(label, i) {
            var foundKey = uniqueKeys[label];
            uniqueKeys[label] = (foundKey || 0) + 1;
            var key = label + '__' + uniqueKeys[label];
            return {
                key: key,
                label: label,
                specIndex: i,
                xIndex: columnOrder[i],
                xScale: xScale,
                x: undefined, // initialized below
                calcdata: undefined, // initialized below
                columnWidth: columnWidths[i]
            };
        })
    };

    calcdata.columns.forEach(function(col) {
        col.calcdata = calcdata;
        col.x = xScale(col);
    });

    return calcdata;
};

function arrayMax(maybeArray) {
    if(Array.isArray(maybeArray)) {
        var max = 0;
        for(var i = 0; i < maybeArray.length; i++) {
            max = Math.max(max, arrayMax(maybeArray[i]));
        }
        return max;
    }
    return maybeArray;
}

function sum(a, b) { return a + b; }

// fill matrix in place to equal lengths
// and ensure it's uniformly 2D
function squareStringMatrix(matrixIn) {
    var matrix = matrixIn.slice();
    var minLen = Infinity;
    var maxLen = 0;
    var i;
    for(i = 0; i < matrix.length; i++) {
        if(!Array.isArray(matrix[i])) matrix[i] = [matrix[i]];
        minLen = Math.min(minLen, matrix[i].length);
        maxLen = Math.max(maxLen, matrix[i].length);
    }

    if(minLen !== maxLen) {
        for(i = 0; i < matrix.length; i++) {
            var padLen = maxLen - matrix[i].length;
            if(padLen) matrix[i] = matrix[i].concat(emptyStrings(padLen));
        }
    }
    return matrix;
}

function emptyStrings(len) {
    var padArray = new Array(len);
    for(var j = 0; j < len; j++) padArray[j] = '';
    return padArray;
}

function xScale(d) {
    return d.calcdata.columns.reduce(function(prev, next) {
        return next.xIndex < d.xIndex ? prev + next.columnWidth : prev;
    }, 0);
}

function makeRowBlock(anchorToRowBlock, auxiliary) {
    var blockAnchorKeys = Object.keys(anchorToRowBlock);
    return blockAnchorKeys.map(function(k) {return extendFlat({}, anchorToRowBlock[k], {auxiliaryBlocks: auxiliary});});
}

function makeAnchorToRowBlock(rowHeights, minimumFillHeight) {
    var anchorToRowBlock = {};
    var currentRowHeight;
    var currentAnchor = 0;
    var currentBlockHeight = 0;
    var currentBlock = makeIdentity();
    var currentFirstRowIndex = 0;
    var blockCounter = 0;
    for(var i = 0; i < rowHeights.length; i++) {
        currentRowHeight = rowHeights[i];
        currentBlock.rows.push({
            rowIndex: i,
            rowHeight: currentRowHeight
        });
        currentBlockHeight += currentRowHeight;
        if(currentBlockHeight >= minimumFillHeight || i === rowHeights.length - 1) {
            anchorToRowBlock[currentAnchor] = currentBlock;
            currentBlock.key = blockCounter++;
            currentBlock.firstRowIndex = currentFirstRowIndex;
            currentBlock.lastRowIndex = i;
            currentBlock = makeIdentity();
            currentAnchor += currentBlockHeight;
            currentFirstRowIndex = i + 1;
            currentBlockHeight = 0;
        }
    }

    return anchorToRowBlock;
}

function makeIdentity() {
    return {
        firstRowIndex: null,
        lastRowIndex: null,
        rows: []
    };
}
