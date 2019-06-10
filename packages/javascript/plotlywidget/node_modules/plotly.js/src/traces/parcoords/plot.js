/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var parcoords = require('./parcoords');
var prepareRegl = require('../../lib/prepare_regl');

module.exports = function plot(gd, cdparcoords) {
    var fullLayout = gd._fullLayout;
    var svg = fullLayout._toppaper;
    var root = fullLayout._paperdiv;
    var container = fullLayout._glcontainer;

    var success = prepareRegl(gd);
    if(!success) return;

    var gdDimensions = {};
    var gdDimensionsOriginalOrder = {};
    var fullIndices = {};
    var inputIndices = {};

    var size = fullLayout._size;

    cdparcoords.forEach(function(d, i) {
        var trace = d[0].trace;
        fullIndices[i] = trace.index;
        var iIn = inputIndices[i] = trace._fullInput.index;
        gdDimensions[i] = gd.data[iIn].dimensions;
        gdDimensionsOriginalOrder[i] = gd.data[iIn].dimensions.slice();
    });

    var filterChanged = function(i, originalDimensionIndex, newRanges) {
        // Have updated `constraintrange` data on `gd.data` and raise `Plotly.restyle` event
        // without having to incur heavy UI blocking due to an actual `Plotly.restyle` call

        var gdDimension = gdDimensionsOriginalOrder[i][originalDimensionIndex];
        var newConstraints = newRanges.map(function(r) { return r.slice(); });

        // Store constraint range in preGUI
        // This one doesn't work if it's stored in pieces in _storeDirectGUIEdit
        // because it's an array of variable dimensionality. So store the whole
        // thing at once manually.
        var aStr = 'dimensions[' + originalDimensionIndex + '].constraintrange';
        var preGUI = fullLayout._tracePreGUI[gd._fullData[fullIndices[i]]._fullInput.uid];
        if(preGUI[aStr] === undefined) {
            var initialVal = gdDimension.constraintrange;
            preGUI[aStr] = initialVal || null;
        }

        var fullDimension = gd._fullData[fullIndices[i]].dimensions[originalDimensionIndex];

        if(!newConstraints.length) {
            delete gdDimension.constraintrange;
            delete fullDimension.constraintrange;
            newConstraints = null;
        } else {
            if(newConstraints.length === 1) newConstraints = newConstraints[0];
            gdDimension.constraintrange = newConstraints;
            fullDimension.constraintrange = newConstraints.slice();
            // wrap in another array for restyle event data
            newConstraints = [newConstraints];
        }

        var restyleData = {};
        restyleData[aStr] = newConstraints;
        gd.emit('plotly_restyle', [restyleData, [inputIndices[i]]]);
    };

    var hover = function(eventData) {
        gd.emit('plotly_hover', eventData);
    };

    var unhover = function(eventData) {
        gd.emit('plotly_unhover', eventData);
    };

    var axesMoved = function(i, visibleIndices) {
        // Have updated order data on `gd.data` and raise `Plotly.restyle` event
        // without having to incur heavy UI blocking due to an actual `Plotly.restyle` call

        function visible(dimension) {return !('visible' in dimension) || dimension.visible;}

        function newIdx(visibleIndices, orig, dim) {
            var origIndex = orig.indexOf(dim);
            var currentIndex = visibleIndices.indexOf(origIndex);
            if(currentIndex === -1) {
                // invisible dimensions initially go to the end
                currentIndex += orig.length;
            }
            return currentIndex;
        }

        function sorter(orig) {
            return function sorter(d1, d2) {
                var i1 = newIdx(visibleIndices, orig, d1);
                var i2 = newIdx(visibleIndices, orig, d2);
                return i1 - i2;
            };
        }

        // drag&drop sorting of the visible dimensions
        var orig = sorter(gdDimensionsOriginalOrder[i].filter(visible));
        gdDimensions[i].sort(orig);

        // invisible dimensions are not interpreted in the context of drag&drop sorting as an invisible dimension
        // cannot be dragged; they're interspersed into their original positions by this subsequent merging step
        gdDimensionsOriginalOrder[i].filter(function(d) {return !visible(d);})
             .sort(function(d) {
                 // subsequent splicing to be done left to right, otherwise indices may be incorrect
                 return gdDimensionsOriginalOrder[i].indexOf(d);
             })
            .forEach(function(d) {
                gdDimensions[i].splice(gdDimensions[i].indexOf(d), 1); // remove from the end
                gdDimensions[i].splice(gdDimensionsOriginalOrder[i].indexOf(d), 0, d); // insert at original index
            });

        // TODO: we can't really store this part of the interaction state
        // directly as below, since it incudes data arrays. If we want to
        // persist column order we may have to do something special for this
        // case to just store the order itself.
        // Registry.call('_storeDirectGUIEdit',
        //     gd.data[inputIndices[i]],
        //     fullLayout._tracePreGUI[gd._fullData[fullIndices[i]]._fullInput.uid],
        //     {dimensions: gdDimensions[i]}
        // );

        gd.emit('plotly_restyle', [{dimensions: [gdDimensions[i]]}, [inputIndices[i]]]);
    };

    parcoords(
        root,
        svg,
        container,
        cdparcoords,
        {
            width: size.w,
            height: size.h,
            margin: {
                t: size.t,
                r: size.r,
                b: size.b,
                l: size.l
            }
        },
        {
            filterChanged: filterChanged,
            hover: hover,
            unhover: unhover,
            axesMoved: axesMoved
        });
};
