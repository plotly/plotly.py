/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var d3 = require('d3');

var Registry = require('../../registry');
var Plots = require('../../plots/plots');

var Lib = require('../../lib');
var Drawing = require('../drawing');
var Color = require('../color');
var Titles = require('../titles');

var Cartesian = require('../../plots/cartesian');
var axisIDs = require('../../plots/cartesian/axis_ids');

var dragElement = require('../dragelement');
var setCursor = require('../../lib/setcursor');

var constants = require('./constants');

module.exports = function(gd) {
    var fullLayout = gd._fullLayout;
    var rangeSliderData = fullLayout._rangeSliderData;
    for(var i = 0; i < rangeSliderData.length; i++) {
        var opts = rangeSliderData[i][constants.name];
        // fullLayout._uid may not exist when we call makeData
        opts._clipId = opts._id + '-' + fullLayout._uid;
    }

    /*
     * <g container />
     *  <rect bg />
     *  < .... range plot />
     *  <rect mask-min />
     *  <rect mask-max />
     *  <rect slidebox />
     *  <g grabber-min />
     *      <rect handle-min />
     *      <rect grabare-min />
     *  <g grabber-max />
     *      <rect handle-max />
     *      <rect grabare-max />
     *
     *  ...
     */

    function keyFunction(axisOpts) {
        return axisOpts._name;
    }

    var rangeSliders = fullLayout._infolayer
        .selectAll('g.' + constants.containerClassName)
        .data(rangeSliderData, keyFunction);

    // remove exiting sliders and their corresponding clip paths
    rangeSliders.exit().each(function(axisOpts) {
        var opts = axisOpts[constants.name];
        fullLayout._topdefs.select('#' + opts._clipId).remove();
    }).remove();

    // return early if no range slider is visible
    if(rangeSliderData.length === 0) return;

    rangeSliders.enter().append('g')
        .classed(constants.containerClassName, true)
        .attr('pointer-events', 'all');

    // for all present range sliders
    rangeSliders.each(function(axisOpts) {
        var rangeSlider = d3.select(this);
        var opts = axisOpts[constants.name];
        var oppAxisOpts = fullLayout[axisIDs.id2name(axisOpts.anchor)];
        var oppAxisRangeOpts = opts[axisIDs.id2name(axisOpts.anchor)];

        // update range
        // Expand slider range to the axis range
        if(opts.range) {
            var rng = Lib.simpleMap(opts.range, axisOpts.r2l);
            var axRng = Lib.simpleMap(axisOpts.range, axisOpts.r2l);
            var newRng;

            if(axRng[0] < axRng[1]) {
                newRng = [
                    Math.min(rng[0], axRng[0]),
                    Math.max(rng[1], axRng[1])
                ];
            } else {
                newRng = [
                    Math.max(rng[0], axRng[0]),
                    Math.min(rng[1], axRng[1])
                ];
            }

            opts.range = opts._input.range = Lib.simpleMap(newRng, axisOpts.l2r);
        }

        axisOpts.cleanRange('rangeslider.range');

        // update range slider dimensions

        var margin = fullLayout.margin;
        var graphSize = fullLayout._size;
        var domain = axisOpts.domain;
        var tickHeight = opts._tickHeight;

        var oppBottom = opts._oppBottom;

        opts._width = graphSize.w * (domain[1] - domain[0]);

        var x = Math.round(margin.l + (graphSize.w * domain[0]));

        var y = Math.round(
            graphSize.t + graphSize.h * (1 - oppBottom) +
            tickHeight +
            opts._offsetShift + constants.extraPad
        );

        rangeSlider.attr('transform', 'translate(' + x + ',' + y + ')');

        // update data <--> pixel coordinate conversion methods

        var range0 = axisOpts.r2l(opts.range[0]);
        var range1 = axisOpts.r2l(opts.range[1]);
        var dist = range1 - range0;

        opts.p2d = function(v) {
            return (v / opts._width) * dist + range0;
        };

        opts.d2p = function(v) {
            return (v - range0) / dist * opts._width;
        };

        opts._rl = [range0, range1];

        if(oppAxisRangeOpts.rangemode !== 'match') {
            var range0OppAxis = oppAxisOpts.r2l(oppAxisRangeOpts.range[0]);
            var range1OppAxis = oppAxisOpts.r2l(oppAxisRangeOpts.range[1]);
            var distOppAxis = range1OppAxis - range0OppAxis;

            opts.d2pOppAxis = function(v) {
                return (v - range0OppAxis) / distOppAxis * opts._height;
            };
        }

        // update inner nodes

        rangeSlider
            .call(drawBg, gd, axisOpts, opts)
            .call(addClipPath, gd, axisOpts, opts)
            .call(drawRangePlot, gd, axisOpts, opts)
            .call(drawMasks, gd, axisOpts, opts, oppAxisRangeOpts)
            .call(drawSlideBox, gd, axisOpts, opts)
            .call(drawGrabbers, gd, axisOpts, opts);

        // setup drag element
        setupDragElement(rangeSlider, gd, axisOpts, opts);

        // update current range
        setPixelRange(rangeSlider, gd, axisOpts, opts, oppAxisOpts, oppAxisRangeOpts);

        // title goes next to range slider instead of tick labels, so
        // just take it over and draw it from here
        if(axisOpts.side === 'bottom') {
            Titles.draw(gd, axisOpts._id + 'title', {
                propContainer: axisOpts,
                propName: axisOpts._name + '.title',
                placeholder: fullLayout._dfltTitle.x,
                attributes: {
                    x: axisOpts._offset + axisOpts._length / 2,
                    y: y + opts._height + opts._offsetShift + 10 + 1.5 * axisOpts.title.font.size,
                    'text-anchor': 'middle'
                }
            });
        }
    });
};

function setupDragElement(rangeSlider, gd, axisOpts, opts) {
    var slideBox = rangeSlider.select('rect.' + constants.slideBoxClassName).node();
    var grabAreaMin = rangeSlider.select('rect.' + constants.grabAreaMinClassName).node();
    var grabAreaMax = rangeSlider.select('rect.' + constants.grabAreaMaxClassName).node();

    rangeSlider.on('mousedown', function() {
        var event = d3.event;
        var target = event.target;
        var startX = event.clientX;
        var offsetX = startX - rangeSlider.node().getBoundingClientRect().left;
        var minVal = opts.d2p(axisOpts._rl[0]);
        var maxVal = opts.d2p(axisOpts._rl[1]);

        var dragCover = dragElement.coverSlip();

        dragCover.addEventListener('mousemove', mouseMove);
        dragCover.addEventListener('mouseup', mouseUp);

        function mouseMove(e) {
            var delta = +e.clientX - startX;
            var pixelMin, pixelMax, cursor;

            switch(target) {
                case slideBox:
                    cursor = 'ew-resize';
                    pixelMin = minVal + delta;
                    pixelMax = maxVal + delta;
                    break;

                case grabAreaMin:
                    cursor = 'col-resize';
                    pixelMin = minVal + delta;
                    pixelMax = maxVal;
                    break;

                case grabAreaMax:
                    cursor = 'col-resize';
                    pixelMin = minVal;
                    pixelMax = maxVal + delta;
                    break;

                default:
                    cursor = 'ew-resize';
                    pixelMin = offsetX;
                    pixelMax = offsetX + delta;
                    break;
            }

            if(pixelMax < pixelMin) {
                var tmp = pixelMax;
                pixelMax = pixelMin;
                pixelMin = tmp;
            }

            opts._pixelMin = pixelMin;
            opts._pixelMax = pixelMax;

            setCursor(d3.select(dragCover), cursor);
            setDataRange(rangeSlider, gd, axisOpts, opts);
        }

        function mouseUp() {
            dragCover.removeEventListener('mousemove', mouseMove);
            dragCover.removeEventListener('mouseup', mouseUp);
            Lib.removeElement(dragCover);
        }
    });
}

function setDataRange(rangeSlider, gd, axisOpts, opts) {
    function clamp(v) {
        return axisOpts.l2r(Lib.constrain(v, opts._rl[0], opts._rl[1]));
    }

    var dataMin = clamp(opts.p2d(opts._pixelMin));
    var dataMax = clamp(opts.p2d(opts._pixelMax));

    window.requestAnimationFrame(function() {
        Registry.call('_guiRelayout', gd, axisOpts._name + '.range', [dataMin, dataMax]);
    });
}

function setPixelRange(rangeSlider, gd, axisOpts, opts, oppAxisOpts, oppAxisRangeOpts) {
    var hw2 = constants.handleWidth / 2;

    function clamp(v) {
        return Lib.constrain(v, 0, opts._width);
    }

    function clampOppAxis(v) {
        return Lib.constrain(v, 0, opts._height);
    }

    function clampHandle(v) {
        return Lib.constrain(v, -hw2, opts._width + hw2);
    }

    var pixelMin = clamp(opts.d2p(axisOpts._rl[0]));
    var pixelMax = clamp(opts.d2p(axisOpts._rl[1]));

    rangeSlider.select('rect.' + constants.slideBoxClassName)
        .attr('x', pixelMin)
        .attr('width', pixelMax - pixelMin);

    rangeSlider.select('rect.' + constants.maskMinClassName)
        .attr('width', pixelMin);

    rangeSlider.select('rect.' + constants.maskMaxClassName)
        .attr('x', pixelMax)
        .attr('width', opts._width - pixelMax);

    if(oppAxisRangeOpts.rangemode !== 'match') {
        var pixelMinOppAxis = opts._height - clampOppAxis(opts.d2pOppAxis(oppAxisOpts._rl[1]));
        var pixelMaxOppAxis = opts._height - clampOppAxis(opts.d2pOppAxis(oppAxisOpts._rl[0]));

        rangeSlider.select('rect.' + constants.maskMinOppAxisClassName)
            .attr('x', pixelMin)
            .attr('height', pixelMinOppAxis)
            .attr('width', pixelMax - pixelMin);

        rangeSlider.select('rect.' + constants.maskMaxOppAxisClassName)
            .attr('x', pixelMin)
            .attr('y', pixelMaxOppAxis)
            .attr('height', opts._height - pixelMaxOppAxis)
            .attr('width', pixelMax - pixelMin);

        rangeSlider.select('rect.' + constants.slideBoxClassName)
            .attr('y', pixelMinOppAxis)
            .attr('height', pixelMaxOppAxis - pixelMinOppAxis);
    }

    // add offset for crispier corners
    // https://github.com/plotly/plotly.js/pull/1409
    var offset = 0.5;

    var xMin = Math.round(clampHandle(pixelMin - hw2)) - offset;
    var xMax = Math.round(clampHandle(pixelMax - hw2)) + offset;

    rangeSlider.select('g.' + constants.grabberMinClassName)
        .attr('transform', 'translate(' + xMin + ',' + offset + ')');

    rangeSlider.select('g.' + constants.grabberMaxClassName)
        .attr('transform', 'translate(' + xMax + ',' + offset + ')');
}

function drawBg(rangeSlider, gd, axisOpts, opts) {
    var bg = Lib.ensureSingle(rangeSlider, 'rect', constants.bgClassName, function(s) {
        s.attr({
            x: 0,
            y: 0,
            'shape-rendering': 'crispEdges'
        });
    });

    var borderCorrect = (opts.borderwidth % 2) === 0 ?
        opts.borderwidth :
        opts.borderwidth - 1;

    var offsetShift = -opts._offsetShift;
    var lw = Drawing.crispRound(gd, opts.borderwidth);

    bg.attr({
        width: opts._width + borderCorrect,
        height: opts._height + borderCorrect,
        transform: 'translate(' + offsetShift + ',' + offsetShift + ')',
        fill: opts.bgcolor,
        stroke: opts.bordercolor,
        'stroke-width': lw
    });
}

function addClipPath(rangeSlider, gd, axisOpts, opts) {
    var fullLayout = gd._fullLayout;

    var clipPath = Lib.ensureSingleById(fullLayout._topdefs, 'clipPath', opts._clipId, function(s) {
        s.append('rect').attr({ x: 0, y: 0 });
    });

    clipPath.select('rect').attr({
        width: opts._width,
        height: opts._height
    });
}

function drawRangePlot(rangeSlider, gd, axisOpts, opts) {
    var calcData = gd.calcdata;

    var rangePlots = rangeSlider.selectAll('g.' + constants.rangePlotClassName)
        .data(axisOpts._subplotsWith, Lib.identity);

    rangePlots.enter().append('g')
        .attr('class', function(id) { return constants.rangePlotClassName + ' ' + id; })
        .call(Drawing.setClipUrl, opts._clipId, gd);

    rangePlots.order();

    rangePlots.exit().remove();

    var mainplotinfo;

    rangePlots.each(function(id, i) {
        var plotgroup = d3.select(this);
        var isMainPlot = (i === 0);

        var oppAxisOpts = axisIDs.getFromId(gd, id, 'y');
        var oppAxisName = oppAxisOpts._name;
        var oppAxisRangeOpts = opts[oppAxisName];

        var mockFigure = {
            data: [],
            layout: {
                xaxis: {
                    type: axisOpts.type,
                    domain: [0, 1],
                    range: opts.range.slice(),
                    calendar: axisOpts.calendar
                },
                width: opts._width,
                height: opts._height,
                margin: { t: 0, b: 0, l: 0, r: 0 }
            },
            _context: gd._context
        };

        mockFigure.layout[oppAxisName] = {
            type: oppAxisOpts.type,
            domain: [0, 1],
            range: oppAxisRangeOpts.rangemode !== 'match' ? oppAxisRangeOpts.range.slice() : oppAxisOpts.range.slice(),
            calendar: oppAxisOpts.calendar
        };

        Plots.supplyDefaults(mockFigure);

        var xa = mockFigure._fullLayout.xaxis;
        var ya = mockFigure._fullLayout[oppAxisName];

        xa.clearCalc();
        xa.setScale();
        ya.clearCalc();
        ya.setScale();

        var plotinfo = {
            id: id,
            plotgroup: plotgroup,
            xaxis: xa,
            yaxis: ya,
            isRangePlot: true
        };

        if(isMainPlot) mainplotinfo = plotinfo;
        else {
            plotinfo.mainplot = 'xy';
            plotinfo.mainplotinfo = mainplotinfo;
        }

        Cartesian.rangePlot(gd, plotinfo, filterRangePlotCalcData(calcData, id));
    });
}

function filterRangePlotCalcData(calcData, subplotId) {
    var out = [];

    for(var i = 0; i < calcData.length; i++) {
        var calcTrace = calcData[i];
        var trace = calcTrace[0].trace;

        if(trace.xaxis + trace.yaxis === subplotId) {
            out.push(calcTrace);
        }
    }

    return out;
}

function drawMasks(rangeSlider, gd, axisOpts, opts, oppAxisRangeOpts) {
    var maskMin = Lib.ensureSingle(rangeSlider, 'rect', constants.maskMinClassName, function(s) {
        s.attr({
            x: 0,
            y: 0,
            'shape-rendering': 'crispEdges'
        });
    });

    maskMin
        .attr('height', opts._height)
        .call(Color.fill, constants.maskColor);

    var maskMax = Lib.ensureSingle(rangeSlider, 'rect', constants.maskMaxClassName, function(s) {
        s.attr({
            y: 0,
            'shape-rendering': 'crispEdges'
        });
    });

    maskMax
        .attr('height', opts._height)
        .call(Color.fill, constants.maskColor);

    // masks used for oppAxis zoom
    if(oppAxisRangeOpts.rangemode !== 'match') {
        var maskMinOppAxis = Lib.ensureSingle(rangeSlider, 'rect', constants.maskMinOppAxisClassName, function(s) {
            s.attr({
                y: 0,
                'shape-rendering': 'crispEdges'
            });
        });

        maskMinOppAxis
            .attr('width', opts._width)
            .call(Color.fill, constants.maskOppAxisColor);

        var maskMaxOppAxis = Lib.ensureSingle(rangeSlider, 'rect', constants.maskMaxOppAxisClassName, function(s) {
            s.attr({
                y: 0,
                'shape-rendering': 'crispEdges'
            });
        });

        maskMaxOppAxis
            .attr('width', opts._width)
            .style('border-top', constants.maskOppBorder)
            .call(Color.fill, constants.maskOppAxisColor);
    }
}

function drawSlideBox(rangeSlider, gd, axisOpts, opts) {
    if(gd._context.staticPlot) return;

    var slideBox = Lib.ensureSingle(rangeSlider, 'rect', constants.slideBoxClassName, function(s) {
        s.attr({
            y: 0,
            cursor: constants.slideBoxCursor,
            'shape-rendering': 'crispEdges'
        });
    });

    slideBox.attr({
        height: opts._height,
        fill: constants.slideBoxFill
    });
}

function drawGrabbers(rangeSlider, gd, axisOpts, opts) {
    // <g grabber />
    var grabberMin = Lib.ensureSingle(rangeSlider, 'g', constants.grabberMinClassName);
    var grabberMax = Lib.ensureSingle(rangeSlider, 'g', constants.grabberMaxClassName);

    // <g handle />
    var handleFixAttrs = {
        x: 0,
        width: constants.handleWidth,
        rx: constants.handleRadius,
        fill: Color.background,
        stroke: Color.defaultLine,
        'stroke-width': constants.handleStrokeWidth,
        'shape-rendering': 'crispEdges'
    };
    var handleDynamicAttrs = {
        y: Math.round(opts._height / 4),
        height: Math.round(opts._height / 2),
    };
    var handleMin = Lib.ensureSingle(grabberMin, 'rect', constants.handleMinClassName, function(s) {
        s.attr(handleFixAttrs);
    });
    handleMin.attr(handleDynamicAttrs);

    var handleMax = Lib.ensureSingle(grabberMax, 'rect', constants.handleMaxClassName, function(s) {
        s.attr(handleFixAttrs);
    });
    handleMax.attr(handleDynamicAttrs);

    // <g grabarea />
    if(gd._context.staticPlot) return;

    var grabAreaFixAttrs = {
        width: constants.grabAreaWidth,
        x: 0,
        y: 0,
        fill: constants.grabAreaFill,
        cursor: constants.grabAreaCursor
    };

    var grabAreaMin = Lib.ensureSingle(grabberMin, 'rect', constants.grabAreaMinClassName, function(s) {
        s.attr(grabAreaFixAttrs);
    });
    grabAreaMin.attr('height', opts._height);

    var grabAreaMax = Lib.ensureSingle(grabberMax, 'rect', constants.grabAreaMaxClassName, function(s) {
        s.attr(grabAreaFixAttrs);
    });
    grabAreaMax.attr('height', opts._height);
}
