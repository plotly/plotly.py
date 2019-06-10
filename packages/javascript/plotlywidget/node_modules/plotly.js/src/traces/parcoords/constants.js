/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';


module.exports = {
    maxDimensionCount: 60, // this cannot be increased without WebGL code refactoring
    overdrag: 45,
    verticalPadding: 2, // otherwise, horizontal lines on top or bottom are of lower width
    tickDistance: 50,
    canvasPixelRatio: 1,
    blockLineCount: 5000,
    layers: ['contextLineLayer', 'focusLineLayer', 'pickLineLayer'],
    axisTitleOffset: 28,
    axisExtentOffset: 10,
    bar: {
        width: 4, // Visible width of the filter bar
        captureWidth: 10, // Mouse-sensitive width for interaction (Fitts law)
        fillColor: 'magenta', // Color of the filter bar fill
        fillOpacity: 1, // Filter bar fill opacity
        snapDuration: 150, // tween duration in ms for brush snap for ordinal axes
        snapRatio: 0.25, // ratio of bar extension relative to the distance between two adjacent ordinal values
        snapClose: 0.01, // fraction of inter-value distance to snap to the closer one, even if you're not over it
        strokeColor: 'white', // Color of the filter bar side lines
        strokeOpacity: 1, // Filter bar side stroke opacity
        strokeWidth: 1, // Filter bar side stroke width in pixels
        handleHeight: 8, // Height of the filter bar vertical resize areas on top and bottom
        handleOpacity: 1, // Opacity of the filter bar vertical resize areas on top and bottom
        handleOverlap: 0 // A larger than 0 value causes overlaps with the filter bar, represented as pixels
    },
    cn: {
        axisExtentText: 'axis-extent-text',
        parcoordsLineLayers: 'parcoords-line-layers',
        parcoordsLineLayer: 'parcoords-lines',
        parcoords: 'parcoords',
        parcoordsControlView: 'parcoords-control-view',
        yAxis: 'y-axis',
        axisOverlays: 'axis-overlays',
        axis: 'axis',
        axisHeading: 'axis-heading',
        axisTitle: 'axis-title',
        axisExtent: 'axis-extent',
        axisExtentTop: 'axis-extent-top',
        axisExtentTopText: 'axis-extent-top-text',
        axisExtentBottom: 'axis-extent-bottom',
        axisExtentBottomText: 'axis-extent-bottom-text',
        axisBrush: 'axis-brush'
    },
    id: {
        filterBarPattern: 'filter-bar-pattern'

    }
};
