/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var d3 = require('d3');
var Drawing = require('../drawing');
var Axes = require('../../plots/cartesian/axes');
var xmlnsNamespaces = require('../../constants/xmlns_namespaces');

module.exports = function draw(gd) {
    var fullLayout = gd._fullLayout;
    var imageDataAbove = [];
    var imageDataSubplot = {};
    var imageDataBelow = [];
    var subplot;
    var i;

    // Sort into top, subplot, and bottom layers
    for(i = 0; i < fullLayout.images.length; i++) {
        var img = fullLayout.images[i];

        if(img.visible) {
            if(img.layer === 'below' && img.xref !== 'paper' && img.yref !== 'paper') {
                subplot = img.xref + img.yref;

                var plotinfo = fullLayout._plots[subplot];

                if(!plotinfo) {
                    // Fall back to _imageLowerLayer in case the requested subplot doesn't exist.
                    // This can happen if you reference the image to an x / y axis combination
                    // that doesn't have any data on it (and layer is below)
                    imageDataBelow.push(img);
                    continue;
                }

                if(plotinfo.mainplot) {
                    subplot = plotinfo.mainplot.id;
                }

                if(!imageDataSubplot[subplot]) {
                    imageDataSubplot[subplot] = [];
                }
                imageDataSubplot[subplot].push(img);
            } else if(img.layer === 'above') {
                imageDataAbove.push(img);
            } else {
                imageDataBelow.push(img);
            }
        }
    }


    var anchors = {
        x: {
            left: { sizing: 'xMin', offset: 0 },
            center: { sizing: 'xMid', offset: -1 / 2 },
            right: { sizing: 'xMax', offset: -1 }
        },
        y: {
            top: { sizing: 'YMin', offset: 0 },
            middle: { sizing: 'YMid', offset: -1 / 2 },
            bottom: { sizing: 'YMax', offset: -1 }
        }
    };


    // Images must be converted to dataURL's for exporting.
    function setImage(d) {
        var thisImage = d3.select(this);

        if(this.img && this.img.src === d.source) {
            return;
        }

        thisImage.attr('xmlns', xmlnsNamespaces.svg);

        var imagePromise = new Promise(function(resolve) {
            var img = new Image();
            this.img = img;

            // If not set, a `tainted canvas` error is thrown
            img.setAttribute('crossOrigin', 'anonymous');
            img.onerror = errorHandler;
            img.onload = function() {
                var canvas = document.createElement('canvas');
                canvas.width = this.width;
                canvas.height = this.height;

                var ctx = canvas.getContext('2d');
                ctx.drawImage(this, 0, 0);

                var dataURL = canvas.toDataURL('image/png');

                thisImage.attr('xlink:href', dataURL);

                // resolve promise in onload handler instead of on 'load' to support IE11
                // see https://github.com/plotly/plotly.js/issues/1685
                // for more details
                resolve();
            };


            thisImage.on('error', errorHandler);

            img.src = d.source;

            function errorHandler() {
                thisImage.remove();
                resolve();
            }
        }.bind(this));

        gd._promises.push(imagePromise);
    }

    function applyAttributes(d) {
        var thisImage = d3.select(this);

        // Axes if specified
        var xa = Axes.getFromId(gd, d.xref);
        var ya = Axes.getFromId(gd, d.yref);

        var size = fullLayout._size;
        var width = xa ? Math.abs(xa.l2p(d.sizex) - xa.l2p(0)) : d.sizex * size.w;
        var height = ya ? Math.abs(ya.l2p(d.sizey) - ya.l2p(0)) : d.sizey * size.h;

        // Offsets for anchor positioning
        var xOffset = width * anchors.x[d.xanchor].offset;
        var yOffset = height * anchors.y[d.yanchor].offset;

        var sizing = anchors.x[d.xanchor].sizing + anchors.y[d.yanchor].sizing;

        // Final positions
        var xPos = (xa ? xa.r2p(d.x) + xa._offset : d.x * size.w + size.l) + xOffset;
        var yPos = (ya ? ya.r2p(d.y) + ya._offset : size.h - d.y * size.h + size.t) + yOffset;

        // Construct the proper aspectRatio attribute
        switch(d.sizing) {
            case 'fill':
                sizing += ' slice';
                break;

            case 'stretch':
                sizing = 'none';
                break;
        }

        thisImage.attr({
            x: xPos,
            y: yPos,
            width: width,
            height: height,
            preserveAspectRatio: sizing,
            opacity: d.opacity
        });


        // Set proper clipping on images
        var xId = xa ? xa._id : '';
        var yId = ya ? ya._id : '';
        var clipAxes = xId + yId;

        Drawing.setClipUrl(
            thisImage,
            clipAxes ? ('clip' + fullLayout._uid + clipAxes) : null,
            gd
        );
    }

    var imagesBelow = fullLayout._imageLowerLayer.selectAll('image')
        .data(imageDataBelow);
    var imagesAbove = fullLayout._imageUpperLayer.selectAll('image')
        .data(imageDataAbove);

    imagesBelow.enter().append('image');
    imagesAbove.enter().append('image');

    imagesBelow.exit().remove();
    imagesAbove.exit().remove();

    imagesBelow.each(function(d) {
        setImage.bind(this)(d);
        applyAttributes.bind(this)(d);
    });
    imagesAbove.each(function(d) {
        setImage.bind(this)(d);
        applyAttributes.bind(this)(d);
    });

    var allSubplots = Object.keys(fullLayout._plots);
    for(i = 0; i < allSubplots.length; i++) {
        subplot = allSubplots[i];
        var subplotObj = fullLayout._plots[subplot];

        // filter out overlaid plots (which havd their images on the main plot)
        // and gl2d plots (which don't support below images, at least not yet)
        if(!subplotObj.imagelayer) continue;

        var imagesOnSubplot = subplotObj.imagelayer.selectAll('image')
            // even if there are no images on this subplot, we need to run
            // enter and exit in case there were previously
            .data(imageDataSubplot[subplot] || []);

        imagesOnSubplot.enter().append('image');
        imagesOnSubplot.exit().remove();

        imagesOnSubplot.each(function(d) {
            setImage.bind(this)(d);
            applyAttributes.bind(this)(d);
        });
    }
};
