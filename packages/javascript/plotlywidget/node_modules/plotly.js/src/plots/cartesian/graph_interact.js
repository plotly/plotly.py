/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/


'use strict';

var d3 = require('d3');

var Fx = require('../../components/fx');
var dragElement = require('../../components/dragelement');
var setCursor = require('../../lib/setcursor');

var makeDragBox = require('./dragbox').makeDragBox;
var DRAGGERSIZE = require('./constants').DRAGGERSIZE;

exports.initInteractions = function initInteractions(gd) {
    var fullLayout = gd._fullLayout;

    if(gd._context.staticPlot) {
        // this sweeps up more than just cartesian drag elements...
        d3.select(gd).selectAll('.drag').remove();
        return;
    }

    if(!fullLayout._has('cartesian') && !fullLayout._has('splom')) return;

    var subplots = Object.keys(fullLayout._plots || {}).sort(function(a, b) {
        // sort overlays last, then by x axis number, then y axis number
        if((fullLayout._plots[a].mainplot && true) ===
            (fullLayout._plots[b].mainplot && true)) {
            var aParts = a.split('y');
            var bParts = b.split('y');
            return (aParts[0] === bParts[0]) ?
                (Number(aParts[1] || 1) - Number(bParts[1] || 1)) :
                (Number(aParts[0] || 1) - Number(bParts[0] || 1));
        }
        return fullLayout._plots[a].mainplot ? 1 : -1;
    });

    subplots.forEach(function(subplot) {
        var plotinfo = fullLayout._plots[subplot];
        var xa = plotinfo.xaxis;
        var ya = plotinfo.yaxis;

        // main and corner draggers need not be repeated for
        // overlaid subplots - these draggers drag them all
        if(!plotinfo.mainplot) {
            // main dragger goes over the grids and data, so we use its
            // mousemove events for all data hover effects
            var maindrag = makeDragBox(gd, plotinfo, xa._offset, ya._offset,
                xa._length, ya._length, 'ns', 'ew');

            maindrag.onmousemove = function(evt) {
                // This is on `gd._fullLayout`, *not* fullLayout because the reference
                // changes by the time this is called again.
                gd._fullLayout._rehover = function() {
                    if(gd._fullLayout._hoversubplot === subplot) {
                        Fx.hover(gd, evt, subplot);
                    }
                };

                Fx.hover(gd, evt, subplot);

                // Note that we have *not* used the cached fullLayout variable here
                // since that may be outdated when this is called as a callback later on
                gd._fullLayout._lasthover = maindrag;
                gd._fullLayout._hoversubplot = subplot;
            };

            /*
             * IMPORTANT:
             * We must check for the presence of the drag cover here.
             * If we don't, a 'mouseout' event is triggered on the
             * maindrag before each 'click' event, which has the effect
             * of clearing the hoverdata; thus, cancelling the click event.
             */
            maindrag.onmouseout = function(evt) {
                if(gd._dragging) return;

                // When the mouse leaves this maindrag, unset the hovered subplot.
                // This may cause problems if it leaves the subplot directly *onto*
                // another subplot, but that's a tiny corner case at the moment.
                gd._fullLayout._hoversubplot = null;

                dragElement.unhover(gd, evt);
            };

            // corner draggers
            if(gd._context.showAxisDragHandles) {
                makeDragBox(gd, plotinfo, xa._offset - DRAGGERSIZE, ya._offset - DRAGGERSIZE,
                    DRAGGERSIZE, DRAGGERSIZE, 'n', 'w');
                makeDragBox(gd, plotinfo, xa._offset + xa._length, ya._offset - DRAGGERSIZE,
                    DRAGGERSIZE, DRAGGERSIZE, 'n', 'e');
                makeDragBox(gd, plotinfo, xa._offset - DRAGGERSIZE, ya._offset + ya._length,
                    DRAGGERSIZE, DRAGGERSIZE, 's', 'w');
                makeDragBox(gd, plotinfo, xa._offset + xa._length, ya._offset + ya._length,
                    DRAGGERSIZE, DRAGGERSIZE, 's', 'e');
            }
        }
        if(gd._context.showAxisDragHandles) {
            // x axis draggers - if you have overlaid plots,
            // these drag each axis separately
            if(subplot === xa._mainSubplot) {
                // the y position of the main x axis line
                var y0 = xa._mainLinePosition;
                if(xa.side === 'top') y0 -= DRAGGERSIZE;
                makeDragBox(gd, plotinfo, xa._offset + xa._length * 0.1, y0,
                    xa._length * 0.8, DRAGGERSIZE, '', 'ew');
                makeDragBox(gd, plotinfo, xa._offset, y0,
                    xa._length * 0.1, DRAGGERSIZE, '', 'w');
                makeDragBox(gd, plotinfo, xa._offset + xa._length * 0.9, y0,
                    xa._length * 0.1, DRAGGERSIZE, '', 'e');
            }
            // y axis draggers
            if(subplot === ya._mainSubplot) {
                // the x position of the main y axis line
                var x0 = ya._mainLinePosition;
                if(ya.side !== 'right') x0 -= DRAGGERSIZE;
                makeDragBox(gd, plotinfo, x0, ya._offset + ya._length * 0.1,
                    DRAGGERSIZE, ya._length * 0.8, 'ns', '');
                makeDragBox(gd, plotinfo, x0, ya._offset + ya._length * 0.9,
                    DRAGGERSIZE, ya._length * 0.1, 's', '');
                makeDragBox(gd, plotinfo, x0, ya._offset,
                    DRAGGERSIZE, ya._length * 0.1, 'n', '');
            }
        }
    });

    // In case you mousemove over some hovertext, send it to Fx.hover too
    // we do this so that we can put the hover text in front of everything,
    // but still be able to interact with everything as if it isn't there
    var hoverLayer = fullLayout._hoverlayer.node();

    hoverLayer.onmousemove = function(evt) {
        evt.target = gd._fullLayout._lasthover;
        Fx.hover(gd, evt, fullLayout._hoversubplot);
    };

    hoverLayer.onclick = function(evt) {
        evt.target = gd._fullLayout._lasthover;
        Fx.click(gd, evt);
    };

    // also delegate mousedowns... TODO: does this actually work?
    hoverLayer.onmousedown = function(evt) {
        gd._fullLayout._lasthover.onmousedown(evt);
    };

    exports.updateFx(gd);
};

// Minimal set of update needed on 'modebar' edits.
// We only need to update the <g .draglayer> cursor style.
//
// Note that changing the axis configuration and/or the fixedrange attribute
// should trigger a full initInteractions.
exports.updateFx = function(gd) {
    var fullLayout = gd._fullLayout;
    var cursor = fullLayout.dragmode === 'pan' ? 'move' : 'crosshair';
    setCursor(fullLayout._draggers, cursor);
};
