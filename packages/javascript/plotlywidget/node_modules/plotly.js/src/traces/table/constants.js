/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

module.exports = {
    cellPad: 8,
    columnExtentOffset: 10,
    columnTitleOffset: 28,
    emptyHeaderHeight: 16,
    latexCheck: /^\$.*\$$/,
    goldenRatio: 1.618,
    lineBreaker: '<br>',
    maxDimensionCount: 60,
    overdrag: 45,
    releaseTransitionDuration: 120,
    releaseTransitionEase: 'cubic-out',
    scrollbarCaptureWidth: 18,
    scrollbarHideDelay: 1000,
    scrollbarHideDuration: 1000,
    scrollbarOffset: 5,
    scrollbarWidth: 8,
    transitionDuration: 100,
    transitionEase: 'cubic-out',
    uplift: 5,
    wrapSpacer: ' ',
    wrapSplitCharacter: ' ',
    cn: {
        // general class names
        table: 'table',
        tableControlView: 'table-control-view',
        scrollBackground: 'scroll-background',
        yColumn: 'y-column',
        columnBlock: 'column-block',
        scrollAreaClip: 'scroll-area-clip',
        scrollAreaClipRect: 'scroll-area-clip-rect',
        columnBoundary: 'column-boundary',
        columnBoundaryClippath: 'column-boundary-clippath',
        columnBoundaryRect: 'column-boundary-rect',
        columnCells: 'column-cells',
        columnCell: 'column-cell',
        cellRect: 'cell-rect',
        cellText: 'cell-text',
        cellTextHolder: 'cell-text-holder',

        // scroll related class names
        scrollbarKit: 'scrollbar-kit',
        scrollbar: 'scrollbar',
        scrollbarSlider: 'scrollbar-slider',
        scrollbarGlyph: 'scrollbar-glyph',
        scrollbarCaptureZone: 'scrollbar-capture-zone'
    }
};
