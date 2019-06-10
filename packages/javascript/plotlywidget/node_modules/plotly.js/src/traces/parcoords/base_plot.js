/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var d3 = require('d3');
var getModuleCalcData = require('../../plots/get_data').getModuleCalcData;
var parcoordsPlot = require('./plot');
var xmlnsNamespaces = require('../../constants/xmlns_namespaces');

var PARCOORDS = 'parcoords';

exports.name = PARCOORDS;

exports.plot = function(gd) {
    var calcData = getModuleCalcData(gd.calcdata, PARCOORDS)[0];
    if(calcData.length) parcoordsPlot(gd, calcData);
};

exports.clean = function(newFullData, newFullLayout, oldFullData, oldFullLayout) {
    var hadParcoords = (oldFullLayout._has && oldFullLayout._has(PARCOORDS));
    var hasParcoords = (newFullLayout._has && newFullLayout._has(PARCOORDS));

    if(hadParcoords && !hasParcoords) {
        oldFullLayout._paperdiv.selectAll('.parcoords').remove();
        oldFullLayout._glimages.selectAll('*').remove();
    }
};

exports.toSVG = function(gd) {
    var imageRoot = gd._fullLayout._glimages;
    var root = d3.select(gd).selectAll('.svg-container');
    var canvases = root.filter(function(d, i) {return i === root.size() - 1;})
        .selectAll('.gl-canvas-context, .gl-canvas-focus');

    function canvasToImage() {
        var canvas = this;
        var imageData = canvas.toDataURL('image/png');
        var image = imageRoot.append('svg:image');

        image.attr({
            xmlns: xmlnsNamespaces.svg,
            'xlink:href': imageData,
            preserveAspectRatio: 'none',
            x: 0,
            y: 0,
            width: canvas.width,
            height: canvas.height
        });
    }

    canvases.each(canvasToImage);

    // Chrome / Safari bug workaround - browser apparently loses connection to the defined pattern
    // Without the workaround, these browsers 'lose' the filter brush styling (color etc.) after a snapshot
    // on a subsequent interaction.
    // Firefox works fine without this workaround
    window.setTimeout(function() {
        d3.selectAll('#filterBarPattern')
            .attr('id', 'filterBarPattern');
    }, 60);
};
