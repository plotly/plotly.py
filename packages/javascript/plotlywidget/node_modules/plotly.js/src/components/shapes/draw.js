/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/


'use strict';

var Registry = require('../../registry');
var Lib = require('../../lib');
var Axes = require('../../plots/cartesian/axes');
var Color = require('../color');
var Drawing = require('../drawing');
var arrayEditor = require('../../plot_api/plot_template').arrayEditor;

var dragElement = require('../dragelement');
var setCursor = require('../../lib/setcursor');

var constants = require('./constants');
var helpers = require('./helpers');


// Shapes are stored in gd.layout.shapes, an array of objects
// index can point to one item in this array,
//  or non-numeric to simply add a new one
//  or -1 to modify all existing
// opt can be the full options object, or one key (to be set to value)
//  or undefined to simply redraw
// if opt is blank, val can be 'add' or a full options object to add a new
//  annotation at that point in the array, or 'remove' to delete this one

module.exports = {
    draw: draw,
    drawOne: drawOne
};

function draw(gd) {
    var fullLayout = gd._fullLayout;

    // Remove previous shapes before drawing new in shapes in fullLayout.shapes
    fullLayout._shapeUpperLayer.selectAll('path').remove();
    fullLayout._shapeLowerLayer.selectAll('path').remove();

    for(var k in fullLayout._plots) {
        var shapelayer = fullLayout._plots[k].shapelayer;
        if(shapelayer) shapelayer.selectAll('path').remove();
    }

    for(var i = 0; i < fullLayout.shapes.length; i++) {
        if(fullLayout.shapes[i].visible) {
            drawOne(gd, i);
        }
    }

    // may need to resurrect this if we put text (LaTeX) in shapes
    // return Plots.previousPromises(gd);
}

function drawOne(gd, index) {
    // remove the existing shape if there is one.
    // because indices can change, we need to look in all shape layers
    gd._fullLayout._paperdiv
        .selectAll('.shapelayer [data-index="' + index + '"]')
        .remove();

    var options = gd._fullLayout.shapes[index] || {};

    // this shape is gone - quit now after deleting it
    // TODO: use d3 idioms instead of deleting and redrawing every time
    if(!options._input || options.visible === false) return;

    if(options.layer !== 'below') {
        drawShape(gd._fullLayout._shapeUpperLayer);
    } else if(options.xref === 'paper' || options.yref === 'paper') {
        drawShape(gd._fullLayout._shapeLowerLayer);
    } else {
        var plotinfo = gd._fullLayout._plots[options.xref + options.yref];
        if(plotinfo) {
            var mainPlot = plotinfo.mainplotinfo || plotinfo;
            drawShape(mainPlot.shapelayer);
        } else {
            // Fall back to _shapeLowerLayer in case the requested subplot doesn't exist.
            // This can happen if you reference the shape to an x / y axis combination
            // that doesn't have any data on it (and layer is below)
            drawShape(gd._fullLayout._shapeLowerLayer);
        }
    }

    function drawShape(shapeLayer) {
        var attrs = {
            'data-index': index,
            'fill-rule': 'evenodd',
            d: getPathString(gd, options)
        };
        var lineColor = options.line.width ? options.line.color : 'rgba(0,0,0,0)';

        var path = shapeLayer.append('path')
            .attr(attrs)
            .style('opacity', options.opacity)
            .call(Color.stroke, lineColor)
            .call(Color.fill, options.fillcolor)
            .call(Drawing.dashLine, options.line.dash, options.line.width);

        setClipPath(path, gd, options);

        if(gd._context.edits.shapePosition) setupDragElement(gd, path, options, index, shapeLayer);
    }
}

function setClipPath(shapePath, gd, shapeOptions) {
    // note that for layer="below" the clipAxes can be different from the
    // subplot we're drawing this in. This could cause problems if the shape
    // spans two subplots. See https://github.com/plotly/plotly.js/issues/1452
    var clipAxes = (shapeOptions.xref + shapeOptions.yref).replace(/paper/g, '');

    Drawing.setClipUrl(
        shapePath,
        clipAxes ? 'clip' + gd._fullLayout._uid + clipAxes : null,
        gd
    );
}

function setupDragElement(gd, shapePath, shapeOptions, index, shapeLayer) {
    var MINWIDTH = 10;
    var MINHEIGHT = 10;

    var xPixelSized = shapeOptions.xsizemode === 'pixel';
    var yPixelSized = shapeOptions.ysizemode === 'pixel';
    var isLine = shapeOptions.type === 'line';
    var isPath = shapeOptions.type === 'path';

    var editHelpers = arrayEditor(gd.layout, 'shapes', shapeOptions);
    var modifyItem = editHelpers.modifyItem;

    var x0, y0, x1, y1, xAnchor, yAnchor;
    var n0, s0, w0, e0, optN, optS, optW, optE;
    var pathIn;

    // setup conversion functions
    var xa = Axes.getFromId(gd, shapeOptions.xref);
    var ya = Axes.getFromId(gd, shapeOptions.yref);
    var x2p = helpers.getDataToPixel(gd, xa);
    var y2p = helpers.getDataToPixel(gd, ya, true);
    var p2x = helpers.getPixelToData(gd, xa);
    var p2y = helpers.getPixelToData(gd, ya, true);

    var sensoryElement = obtainSensoryElement();
    var dragOptions = {
        element: sensoryElement.node(),
        gd: gd,
        prepFn: startDrag,
        doneFn: endDrag,
        clickFn: abortDrag
    };
    var dragMode;

    dragElement.init(dragOptions);

    sensoryElement.node().onmousemove = updateDragMode;

    function obtainSensoryElement() {
        return isLine ? createLineDragHandles() : shapePath;
    }

    function createLineDragHandles() {
        var minSensoryWidth = 10;
        var sensoryWidth = Math.max(shapeOptions.line.width, minSensoryWidth);

        // Helper shapes group
        // Note that by setting the `data-index` attr, it is ensured that
        // the helper group is purged in this modules `draw` function
        var g = shapeLayer.append('g')
          .attr('data-index', index);

        // Helper path for moving
        g.append('path')
          .attr('d', shapePath.attr('d'))
          .style({
              'cursor': 'move',
              'stroke-width': sensoryWidth,
              'stroke-opacity': '0' // ensure not visible
          });

        // Helper circles for resizing
        var circleStyle = {
            'fill-opacity': '0' // ensure not visible
        };
        var circleRadius = sensoryWidth / 2 > minSensoryWidth ? sensoryWidth / 2 : minSensoryWidth;

        g.append('circle')
          .attr({
              'data-line-point': 'start-point',
              'cx': xPixelSized ? x2p(shapeOptions.xanchor) + shapeOptions.x0 : x2p(shapeOptions.x0),
              'cy': yPixelSized ? y2p(shapeOptions.yanchor) - shapeOptions.y0 : y2p(shapeOptions.y0),
              'r': circleRadius
          })
          .style(circleStyle)
          .classed('cursor-grab', true);

        g.append('circle')
          .attr({
              'data-line-point': 'end-point',
              'cx': xPixelSized ? x2p(shapeOptions.xanchor) + shapeOptions.x1 : x2p(shapeOptions.x1),
              'cy': yPixelSized ? y2p(shapeOptions.yanchor) - shapeOptions.y1 : y2p(shapeOptions.y1),
              'r': circleRadius
          })
          .style(circleStyle)
          .classed('cursor-grab', true);

        return g;
    }

    function updateDragMode(evt) {
        if(isLine) {
            if(evt.target.tagName === 'path') {
                dragMode = 'move';
            } else {
                dragMode = evt.target.attributes['data-line-point'].value === 'start-point' ?
                  'resize-over-start-point' : 'resize-over-end-point';
            }
        } else {
            // element might not be on screen at time of setup,
            // so obtain bounding box here
            var dragBBox = dragOptions.element.getBoundingClientRect();

            // choose 'move' or 'resize'
            // based on initial position of cursor within the drag element
            var w = dragBBox.right - dragBBox.left;
            var h = dragBBox.bottom - dragBBox.top;
            var x = evt.clientX - dragBBox.left;
            var y = evt.clientY - dragBBox.top;
            var cursor = (!isPath && w > MINWIDTH && h > MINHEIGHT && !evt.shiftKey) ?
                dragElement.getCursor(x / w, 1 - y / h) :
                'move';

            setCursor(shapePath, cursor);

            // possible values 'move', 'sw', 'w', 'se', 'e', 'ne', 'n', 'nw' and 'w'
            dragMode = cursor.split('-')[0];
        }
    }

    function startDrag(evt) {
        // setup update strings and initial values
        if(xPixelSized) {
            xAnchor = x2p(shapeOptions.xanchor);
        }
        if(yPixelSized) {
            yAnchor = y2p(shapeOptions.yanchor);
        }

        if(shapeOptions.type === 'path') {
            pathIn = shapeOptions.path;
        } else {
            x0 = xPixelSized ? shapeOptions.x0 : x2p(shapeOptions.x0);
            y0 = yPixelSized ? shapeOptions.y0 : y2p(shapeOptions.y0);
            x1 = xPixelSized ? shapeOptions.x1 : x2p(shapeOptions.x1);
            y1 = yPixelSized ? shapeOptions.y1 : y2p(shapeOptions.y1);
        }

        if(x0 < x1) {
            w0 = x0;
            optW = 'x0';
            e0 = x1;
            optE = 'x1';
        } else {
            w0 = x1;
            optW = 'x1';
            e0 = x0;
            optE = 'x0';
        }

        // For fixed size shapes take opposing direction of y-axis into account.
        // Hint: For data sized shapes this is done by the y2p function.
        if((!yPixelSized && y0 < y1) || (yPixelSized && y0 > y1)) {
            n0 = y0;
            optN = 'y0';
            s0 = y1;
            optS = 'y1';
        } else {
            n0 = y1;
            optN = 'y1';
            s0 = y0;
            optS = 'y0';
        }

        // setup dragMode and the corresponding handler
        updateDragMode(evt);
        renderVisualCues(shapeLayer, shapeOptions);
        deactivateClipPathTemporarily(shapePath, shapeOptions, gd);
        dragOptions.moveFn = (dragMode === 'move') ? moveShape : resizeShape;
    }

    function endDrag() {
        setCursor(shapePath);
        removeVisualCues(shapeLayer);

        // Don't rely on clipPath being activated during re-layout
        setClipPath(shapePath, gd, shapeOptions);
        Registry.call('_guiRelayout', gd, editHelpers.getUpdateObj());
    }

    function abortDrag() {
        removeVisualCues(shapeLayer);
    }

    function moveShape(dx, dy) {
        if(shapeOptions.type === 'path') {
            var noOp = function(coord) { return coord; };
            var moveX = noOp;
            var moveY = noOp;

            if(xPixelSized) {
                modifyItem('xanchor', shapeOptions.xanchor = p2x(xAnchor + dx));
            } else {
                moveX = function moveX(x) { return p2x(x2p(x) + dx); };
                if(xa && xa.type === 'date') moveX = helpers.encodeDate(moveX);
            }

            if(yPixelSized) {
                modifyItem('yanchor', shapeOptions.yanchor = p2y(yAnchor + dy));
            } else {
                moveY = function moveY(y) { return p2y(y2p(y) + dy); };
                if(ya && ya.type === 'date') moveY = helpers.encodeDate(moveY);
            }

            modifyItem('path', shapeOptions.path = movePath(pathIn, moveX, moveY));
        } else {
            if(xPixelSized) {
                modifyItem('xanchor', shapeOptions.xanchor = p2x(xAnchor + dx));
            } else {
                modifyItem('x0', shapeOptions.x0 = p2x(x0 + dx));
                modifyItem('x1', shapeOptions.x1 = p2x(x1 + dx));
            }

            if(yPixelSized) {
                modifyItem('yanchor', shapeOptions.yanchor = p2y(yAnchor + dy));
            } else {
                modifyItem('y0', shapeOptions.y0 = p2y(y0 + dy));
                modifyItem('y1', shapeOptions.y1 = p2y(y1 + dy));
            }
        }

        shapePath.attr('d', getPathString(gd, shapeOptions));
        renderVisualCues(shapeLayer, shapeOptions);
    }

    function resizeShape(dx, dy) {
        if(isPath) {
            // TODO: implement path resize, don't forget to update dragMode code
            var noOp = function(coord) { return coord; };
            var moveX = noOp;
            var moveY = noOp;

            if(xPixelSized) {
                modifyItem('xanchor', shapeOptions.xanchor = p2x(xAnchor + dx));
            } else {
                moveX = function moveX(x) { return p2x(x2p(x) + dx); };
                if(xa && xa.type === 'date') moveX = helpers.encodeDate(moveX);
            }

            if(yPixelSized) {
                modifyItem('yanchor', shapeOptions.yanchor = p2y(yAnchor + dy));
            } else {
                moveY = function moveY(y) { return p2y(y2p(y) + dy); };
                if(ya && ya.type === 'date') moveY = helpers.encodeDate(moveY);
            }

            modifyItem('path', shapeOptions.path = movePath(pathIn, moveX, moveY));
        } else if(isLine) {
            if(dragMode === 'resize-over-start-point') {
                var newX0 = x0 + dx;
                var newY0 = yPixelSized ? y0 - dy : y0 + dy;
                modifyItem('x0', shapeOptions.x0 = xPixelSized ? newX0 : p2x(newX0));
                modifyItem('y0', shapeOptions.y0 = yPixelSized ? newY0 : p2y(newY0));
            } else if(dragMode === 'resize-over-end-point') {
                var newX1 = x1 + dx;
                var newY1 = yPixelSized ? y1 - dy : y1 + dy;
                modifyItem('x1', shapeOptions.x1 = xPixelSized ? newX1 : p2x(newX1));
                modifyItem('y1', shapeOptions.y1 = yPixelSized ? newY1 : p2y(newY1));
            }
        } else {
            var newN = (~dragMode.indexOf('n')) ? n0 + dy : n0;
            var newS = (~dragMode.indexOf('s')) ? s0 + dy : s0;
            var newW = (~dragMode.indexOf('w')) ? w0 + dx : w0;
            var newE = (~dragMode.indexOf('e')) ? e0 + dx : e0;

            // Do things in opposing direction for y-axis.
            // Hint: for data-sized shapes the reversal of axis direction is done in p2y.
            if(~dragMode.indexOf('n') && yPixelSized) newN = n0 - dy;
            if(~dragMode.indexOf('s') && yPixelSized) newS = s0 - dy;

            // Update shape eventually. Again, be aware of the
            // opposing direction of the y-axis of fixed size shapes.
            if((!yPixelSized && newS - newN > MINHEIGHT) ||
              (yPixelSized && newN - newS > MINHEIGHT)) {
                modifyItem(optN, shapeOptions[optN] = yPixelSized ? newN : p2y(newN));
                modifyItem(optS, shapeOptions[optS] = yPixelSized ? newS : p2y(newS));
            }
            if(newE - newW > MINWIDTH) {
                modifyItem(optW, shapeOptions[optW] = xPixelSized ? newW : p2x(newW));
                modifyItem(optE, shapeOptions[optE] = xPixelSized ? newE : p2x(newE));
            }
        }

        shapePath.attr('d', getPathString(gd, shapeOptions));
        renderVisualCues(shapeLayer, shapeOptions);
    }

    function renderVisualCues(shapeLayer, shapeOptions) {
        if(xPixelSized || yPixelSized) {
            renderAnchor();
        }

        function renderAnchor() {
            var isNotPath = shapeOptions.type !== 'path';

            // d3 join with dummy data to satisfy d3 data-binding
            var visualCues = shapeLayer.selectAll('.visual-cue').data([0]);

            // Enter
            var strokeWidth = 1;
            visualCues.enter()
              .append('path')
              .attr({
                  'fill': '#fff',
                  'fill-rule': 'evenodd',
                  'stroke': '#000',
                  'stroke-width': strokeWidth
              })
              .classed('visual-cue', true);

            // Update
            var posX = x2p(
              xPixelSized ?
                shapeOptions.xanchor :
                Lib.midRange(
                  isNotPath ?
                    [shapeOptions.x0, shapeOptions.x1] :
                    helpers.extractPathCoords(shapeOptions.path, constants.paramIsX))
            );
            var posY = y2p(
              yPixelSized ?
                shapeOptions.yanchor :
                Lib.midRange(
                  isNotPath ?
                    [shapeOptions.y0, shapeOptions.y1] :
                    helpers.extractPathCoords(shapeOptions.path, constants.paramIsY))
            );

            posX = helpers.roundPositionForSharpStrokeRendering(posX, strokeWidth);
            posY = helpers.roundPositionForSharpStrokeRendering(posY, strokeWidth);

            if(xPixelSized && yPixelSized) {
                var crossPath = 'M' + (posX - 1 - strokeWidth) + ',' + (posY - 1 - strokeWidth) +
                  'h-8v2h8 v8h2v-8 h8v-2h-8 v-8h-2 Z';
                visualCues.attr('d', crossPath);
            } else if(xPixelSized) {
                var vBarPath = 'M' + (posX - 1 - strokeWidth) + ',' + (posY - 9 - strokeWidth) +
                  'v18 h2 v-18 Z';
                visualCues.attr('d', vBarPath);
            } else {
                var hBarPath = 'M' + (posX - 9 - strokeWidth) + ',' + (posY - 1 - strokeWidth) +
                  'h18 v2 h-18 Z';
                visualCues.attr('d', hBarPath);
            }
        }
    }

    function removeVisualCues(shapeLayer) {
        shapeLayer.selectAll('.visual-cue').remove();
    }

    function deactivateClipPathTemporarily(shapePath, shapeOptions, gd) {
        var xref = shapeOptions.xref;
        var yref = shapeOptions.yref;
        var xa = Axes.getFromId(gd, xref);
        var ya = Axes.getFromId(gd, yref);

        var clipAxes = '';
        if(xref !== 'paper' && !xa.autorange) clipAxes += xref;
        if(yref !== 'paper' && !ya.autorange) clipAxes += yref;

        Drawing.setClipUrl(
            shapePath,
            clipAxes ? 'clip' + gd._fullLayout._uid + clipAxes : null,
            gd
        );
    }
}

function getPathString(gd, options) {
    var type = options.type;
    var xa = Axes.getFromId(gd, options.xref);
    var ya = Axes.getFromId(gd, options.yref);
    var gs = gd._fullLayout._size;
    var x2r, x2p, y2r, y2p;
    var x0, x1, y0, y1;

    if(xa) {
        x2r = helpers.shapePositionToRange(xa);
        x2p = function(v) { return xa._offset + xa.r2p(x2r(v, true)); };
    } else {
        x2p = function(v) { return gs.l + gs.w * v; };
    }

    if(ya) {
        y2r = helpers.shapePositionToRange(ya);
        y2p = function(v) { return ya._offset + ya.r2p(y2r(v, true)); };
    } else {
        y2p = function(v) { return gs.t + gs.h * (1 - v); };
    }

    if(type === 'path') {
        if(xa && xa.type === 'date') x2p = helpers.decodeDate(x2p);
        if(ya && ya.type === 'date') y2p = helpers.decodeDate(y2p);
        return convertPath(options, x2p, y2p);
    }

    if(options.xsizemode === 'pixel') {
        var xAnchorPos = x2p(options.xanchor);
        x0 = xAnchorPos + options.x0;
        x1 = xAnchorPos + options.x1;
    } else {
        x0 = x2p(options.x0);
        x1 = x2p(options.x1);
    }

    if(options.ysizemode === 'pixel') {
        var yAnchorPos = y2p(options.yanchor);
        y0 = yAnchorPos - options.y0;
        y1 = yAnchorPos - options.y1;
    } else {
        y0 = y2p(options.y0);
        y1 = y2p(options.y1);
    }

    if(type === 'line') return 'M' + x0 + ',' + y0 + 'L' + x1 + ',' + y1;
    if(type === 'rect') return 'M' + x0 + ',' + y0 + 'H' + x1 + 'V' + y1 + 'H' + x0 + 'Z';

    // circle
    var cx = (x0 + x1) / 2;
    var cy = (y0 + y1) / 2;
    var rx = Math.abs(cx - x0);
    var ry = Math.abs(cy - y0);
    var rArc = 'A' + rx + ',' + ry;
    var rightPt = (cx + rx) + ',' + cy;
    var topPt = cx + ',' + (cy - ry);
    return 'M' + rightPt + rArc + ' 0 1,1 ' + topPt +
        rArc + ' 0 0,1 ' + rightPt + 'Z';
}


function convertPath(options, x2p, y2p) {
    var pathIn = options.path;
    var xSizemode = options.xsizemode;
    var ySizemode = options.ysizemode;
    var xAnchor = options.xanchor;
    var yAnchor = options.yanchor;

    return pathIn.replace(constants.segmentRE, function(segment) {
        var paramNumber = 0;
        var segmentType = segment.charAt(0);
        var xParams = constants.paramIsX[segmentType];
        var yParams = constants.paramIsY[segmentType];
        var nParams = constants.numParams[segmentType];

        var paramString = segment.substr(1).replace(constants.paramRE, function(param) {
            if(xParams[paramNumber]) {
                if(xSizemode === 'pixel') param = x2p(xAnchor) + Number(param);
                else param = x2p(param);
            } else if(yParams[paramNumber]) {
                if(ySizemode === 'pixel') param = y2p(yAnchor) - Number(param);
                else param = y2p(param);
            }
            paramNumber++;

            if(paramNumber > nParams) param = 'X';
            return param;
        });

        if(paramNumber > nParams) {
            paramString = paramString.replace(/[\s,]*X.*/, '');
            Lib.log('Ignoring extra params in segment ' + segment);
        }

        return segmentType + paramString;
    });
}

function movePath(pathIn, moveX, moveY) {
    return pathIn.replace(constants.segmentRE, function(segment) {
        var paramNumber = 0;
        var segmentType = segment.charAt(0);
        var xParams = constants.paramIsX[segmentType];
        var yParams = constants.paramIsY[segmentType];
        var nParams = constants.numParams[segmentType];

        var paramString = segment.substr(1).replace(constants.paramRE, function(param) {
            if(paramNumber >= nParams) return param;

            if(xParams[paramNumber]) param = moveX(param);
            else if(yParams[paramNumber]) param = moveY(param);

            paramNumber++;

            return param;
        });

        return segmentType + paramString;
    });
}
