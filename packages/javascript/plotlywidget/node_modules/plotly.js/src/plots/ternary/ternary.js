/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/


'use strict';

var d3 = require('d3');
var tinycolor = require('tinycolor2');

var Registry = require('../../registry');
var Lib = require('../../lib');
var _ = Lib._;
var Color = require('../../components/color');
var Drawing = require('../../components/drawing');
var setConvert = require('../cartesian/set_convert');
var extendFlat = require('../../lib/extend').extendFlat;
var Plots = require('../plots');
var Axes = require('../cartesian/axes');
var dragElement = require('../../components/dragelement');
var Fx = require('../../components/fx');
var Titles = require('../../components/titles');
var prepSelect = require('../cartesian/select').prepSelect;
var selectOnClick = require('../cartesian/select').selectOnClick;
var clearSelect = require('../cartesian/select').clearSelect;
var constants = require('../cartesian/constants');

function Ternary(options, fullLayout) {
    this.id = options.id;
    this.graphDiv = options.graphDiv;
    this.init(fullLayout);
    this.makeFramework(fullLayout);

    // unfortunately, we have to keep track of some axis tick settings
    // as ternary subplots do not implement the 'ticks' editType
    this.aTickLayout = null;
    this.bTickLayout = null;
    this.cTickLayout = null;
}

module.exports = Ternary;

var proto = Ternary.prototype;

proto.init = function(fullLayout) {
    this.container = fullLayout._ternarylayer;
    this.defs = fullLayout._defs;
    this.layoutId = fullLayout._uid;
    this.traceHash = {};
    this.layers = {};
};

proto.plot = function(ternaryCalcData, fullLayout) {
    var _this = this;
    var ternaryLayout = fullLayout[_this.id];
    var graphSize = fullLayout._size;

    _this._hasClipOnAxisFalse = false;
    for(var i = 0; i < ternaryCalcData.length; i++) {
        var trace = ternaryCalcData[i][0].trace;

        if(trace.cliponaxis === false) {
            _this._hasClipOnAxisFalse = true;
            break;
        }
    }

    _this.updateLayers(ternaryLayout);
    _this.adjustLayout(ternaryLayout, graphSize);
    Plots.generalUpdatePerTraceModule(_this.graphDiv, _this, ternaryCalcData, ternaryLayout);
    _this.layers.plotbg.select('path').call(Color.fill, ternaryLayout.bgcolor);
};

proto.makeFramework = function(fullLayout) {
    var _this = this;
    var gd = _this.graphDiv;
    var ternaryLayout = fullLayout[_this.id];

    var clipId = _this.clipId = 'clip' + _this.layoutId + _this.id;
    var clipIdRelative = _this.clipIdRelative = 'clip-relative' + _this.layoutId + _this.id;

    // clippath for this ternary subplot
    _this.clipDef = Lib.ensureSingleById(fullLayout._clips, 'clipPath', clipId, function(s) {
        s.append('path').attr('d', 'M0,0Z');
    });

    // 'relative' clippath (i.e. no translation) for this ternary subplot
    _this.clipDefRelative = Lib.ensureSingleById(fullLayout._clips, 'clipPath', clipIdRelative, function(s) {
        s.append('path').attr('d', 'M0,0Z');
    });

    // container for everything in this ternary subplot
    _this.plotContainer = Lib.ensureSingle(_this.container, 'g', _this.id);
    _this.updateLayers(ternaryLayout);

    Drawing.setClipUrl(_this.layers.backplot, clipId, gd);
    Drawing.setClipUrl(_this.layers.grids, clipId, gd);
};

proto.updateLayers = function(ternaryLayout) {
    var _this = this;
    var layers = _this.layers;

    // inside that container, we have one container for the data, and
    // one each for the three axes around it.

    var plotLayers = ['draglayer', 'plotbg', 'backplot', 'grids'];

    if(ternaryLayout.aaxis.layer === 'below traces') {
        plotLayers.push('aaxis', 'aline');
    }
    if(ternaryLayout.baxis.layer === 'below traces') {
        plotLayers.push('baxis', 'bline');
    }
    if(ternaryLayout.caxis.layer === 'below traces') {
        plotLayers.push('caxis', 'cline');
    }

    plotLayers.push('frontplot');

    if(ternaryLayout.aaxis.layer === 'above traces') {
        plotLayers.push('aaxis', 'aline');
    }
    if(ternaryLayout.baxis.layer === 'above traces') {
        plotLayers.push('baxis', 'bline');
    }
    if(ternaryLayout.caxis.layer === 'above traces') {
        plotLayers.push('caxis', 'cline');
    }

    var toplevel = _this.plotContainer.selectAll('g.toplevel')
        .data(plotLayers, String);

    var grids = ['agrid', 'bgrid', 'cgrid'];

    toplevel.enter().append('g')
        .attr('class', function(d) { return 'toplevel ' + d; })
        .each(function(d) {
            var s = d3.select(this);
            layers[d] = s;

            // containers for different trace types.
            // NOTE - this is different from cartesian, where all traces
            // are in front of grids. Here I'm putting maps behind the grids
            // so the grids will always be visible if they're requested.
            // Perhaps we want that for cartesian too?
            if(d === 'frontplot') {
                s.append('g').classed('scatterlayer', true);
            } else if(d === 'backplot') {
                s.append('g').classed('maplayer', true);
            } else if(d === 'plotbg') {
                s.append('path').attr('d', 'M0,0Z');
            } else if(d === 'aline' || d === 'bline' || d === 'cline') {
                s.append('path');
            } else if(d === 'grids') {
                grids.forEach(function(d) {
                    layers[d] = s.append('g').classed('grid ' + d, true);
                });
            }
        });

    toplevel.order();
};

var whRatio = Math.sqrt(4 / 3);

proto.adjustLayout = function(ternaryLayout, graphSize) {
    var _this = this;
    var domain = ternaryLayout.domain;
    var xDomainCenter = (domain.x[0] + domain.x[1]) / 2;
    var yDomainCenter = (domain.y[0] + domain.y[1]) / 2;
    var xDomain = domain.x[1] - domain.x[0];
    var yDomain = domain.y[1] - domain.y[0];
    var wmax = xDomain * graphSize.w;
    var hmax = yDomain * graphSize.h;
    var sum = ternaryLayout.sum;
    var amin = ternaryLayout.aaxis.min;
    var bmin = ternaryLayout.baxis.min;
    var cmin = ternaryLayout.caxis.min;

    var x0, y0, w, h, xDomainFinal, yDomainFinal;

    if(wmax > whRatio * hmax) {
        h = hmax;
        w = h * whRatio;
    } else {
        w = wmax;
        h = w / whRatio;
    }

    xDomainFinal = xDomain * w / wmax;
    yDomainFinal = yDomain * h / hmax;

    x0 = graphSize.l + graphSize.w * xDomainCenter - w / 2;
    y0 = graphSize.t + graphSize.h * (1 - yDomainCenter) - h / 2;

    _this.x0 = x0;
    _this.y0 = y0;
    _this.w = w;
    _this.h = h;
    _this.sum = sum;

    // set up the x and y axis objects we'll use to lay out the points
    _this.xaxis = {
        type: 'linear',
        range: [amin + 2 * cmin - sum, sum - amin - 2 * bmin],
        domain: [
            xDomainCenter - xDomainFinal / 2,
            xDomainCenter + xDomainFinal / 2
        ],
        _id: 'x'
    };
    setConvert(_this.xaxis, _this.graphDiv._fullLayout);
    _this.xaxis.setScale();
    _this.xaxis.isPtWithinRange = function(d) {
        return (
            d.a >= _this.aaxis.range[0] &&
            d.a <= _this.aaxis.range[1] &&
            d.b >= _this.baxis.range[1] &&
            d.b <= _this.baxis.range[0] &&
            d.c >= _this.caxis.range[1] &&
            d.c <= _this.caxis.range[0]
        );
    };

    _this.yaxis = {
        type: 'linear',
        range: [amin, sum - bmin - cmin],
        domain: [
            yDomainCenter - yDomainFinal / 2,
            yDomainCenter + yDomainFinal / 2
        ],
        _id: 'y'
    };
    setConvert(_this.yaxis, _this.graphDiv._fullLayout);
    _this.yaxis.setScale();
    _this.yaxis.isPtWithinRange = function() { return true; };

    // set up the modified axes for tick drawing
    var yDomain0 = _this.yaxis.domain[0];

    // aaxis goes up the left side. Set it up as a y axis, but with
    // fictitious angles and domain, but then rotate and translate
    // it into place at the end
    var aaxis = _this.aaxis = extendFlat({}, ternaryLayout.aaxis, {
        range: [amin, sum - bmin - cmin],
        side: 'left',
        // tickangle = 'auto' means 0 anyway for a y axis, need to coerce to 0 here
        // so we can shift by 30.
        tickangle: (+ternaryLayout.aaxis.tickangle || 0) - 30,
        domain: [yDomain0, yDomain0 + yDomainFinal * whRatio],
        anchor: 'free',
        position: 0,
        _id: 'y',
        _length: w
    });
    setConvert(aaxis, _this.graphDiv._fullLayout);
    aaxis.setScale();

    // baxis goes across the bottom (backward). We can set it up as an x axis
    // without any enclosing transformation.
    var baxis = _this.baxis = extendFlat({}, ternaryLayout.baxis, {
        range: [sum - amin - cmin, bmin],
        side: 'bottom',
        domain: _this.xaxis.domain,
        anchor: 'free',
        position: 0,
        _id: 'x',
        _length: w
    });
    setConvert(baxis, _this.graphDiv._fullLayout);
    baxis.setScale();

    // caxis goes down the right side. Set it up as a y axis, with
    // post-transformation similar to aaxis
    var caxis = _this.caxis = extendFlat({}, ternaryLayout.caxis, {
        range: [sum - amin - bmin, cmin],
        side: 'right',
        tickangle: (+ternaryLayout.caxis.tickangle || 0) + 30,
        domain: [yDomain0, yDomain0 + yDomainFinal * whRatio],
        anchor: 'free',
        position: 0,
        _id: 'y',
        _length: w
    });
    setConvert(caxis, _this.graphDiv._fullLayout);
    caxis.setScale();

    var triangleClip = 'M' + x0 + ',' + (y0 + h) + 'h' + w + 'l-' + (w / 2) + ',-' + h + 'Z';
    _this.clipDef.select('path').attr('d', triangleClip);
    _this.layers.plotbg.select('path').attr('d', triangleClip);

    var triangleClipRelative = 'M0,' + h + 'h' + w + 'l-' + (w / 2) + ',-' + h + 'Z';
    _this.clipDefRelative.select('path').attr('d', triangleClipRelative);

    var plotTransform = 'translate(' + x0 + ',' + y0 + ')';
    _this.plotContainer.selectAll('.scatterlayer,.maplayer')
        .attr('transform', plotTransform);

    _this.clipDefRelative.select('path').attr('transform', null);

    // TODO: shift axes to accommodate linewidth*sin(30) tick mark angle

    // TODO: there's probably an easier way to handle these translations/offsets now...
    var bTransform = 'translate(' + (x0 - baxis._offset) + ',' + (y0 + h) + ')';

    _this.layers.baxis.attr('transform', bTransform);
    _this.layers.bgrid.attr('transform', bTransform);

    var aTransform = 'translate(' + (x0 + w / 2) + ',' + y0 +
        ')rotate(30)translate(0,' + -aaxis._offset + ')';
    _this.layers.aaxis.attr('transform', aTransform);
    _this.layers.agrid.attr('transform', aTransform);

    var cTransform = 'translate(' + (x0 + w / 2) + ',' + y0 +
        ')rotate(-30)translate(0,' + -caxis._offset + ')';
    _this.layers.caxis.attr('transform', cTransform);
    _this.layers.cgrid.attr('transform', cTransform);

    _this.drawAxes(true);

    _this.layers.aline.select('path')
        .attr('d', aaxis.showline ?
            'M' + x0 + ',' + (y0 + h) + 'l' + (w / 2) + ',-' + h : 'M0,0')
        .call(Color.stroke, aaxis.linecolor || '#000')
        .style('stroke-width', (aaxis.linewidth || 0) + 'px');
    _this.layers.bline.select('path')
        .attr('d', baxis.showline ?
            'M' + x0 + ',' + (y0 + h) + 'h' + w : 'M0,0')
        .call(Color.stroke, baxis.linecolor || '#000')
        .style('stroke-width', (baxis.linewidth || 0) + 'px');
    _this.layers.cline.select('path')
        .attr('d', caxis.showline ?
            'M' + (x0 + w / 2) + ',' + y0 + 'l' + (w / 2) + ',' + h : 'M0,0')
        .call(Color.stroke, caxis.linecolor || '#000')
        .style('stroke-width', (caxis.linewidth || 0) + 'px');

    if(!_this.graphDiv._context.staticPlot) {
        _this.initInteractions();
    }

    Drawing.setClipUrl(
        _this.layers.frontplot,
        _this._hasClipOnAxisFalse ? null : _this.clipId,
        _this.graphDiv
    );
};

proto.drawAxes = function(doTitles) {
    var _this = this;
    var gd = _this.graphDiv;
    var titlesuffix = _this.id.substr(7) + 'title';
    var layers = _this.layers;
    var aaxis = _this.aaxis;
    var baxis = _this.baxis;
    var caxis = _this.caxis;

    _this.drawAx(aaxis);
    _this.drawAx(baxis);
    _this.drawAx(caxis);

    if(doTitles) {
        var apad = Math.max(aaxis.showticklabels ? aaxis.tickfont.size / 2 : 0,
            (caxis.showticklabels ? caxis.tickfont.size * 0.75 : 0) +
            (caxis.ticks === 'outside' ? caxis.ticklen * 0.87 : 0));
        var bpad = (baxis.showticklabels ? baxis.tickfont.size : 0) +
            (baxis.ticks === 'outside' ? baxis.ticklen : 0) + 3;

        layers['a-title'] = Titles.draw(gd, 'a' + titlesuffix, {
            propContainer: aaxis,
            propName: _this.id + '.aaxis.title',
            placeholder: _(gd, 'Click to enter Component A title'),
            attributes: {
                x: _this.x0 + _this.w / 2,
                y: _this.y0 - aaxis.title.font.size / 3 - apad,
                'text-anchor': 'middle'
            }
        });
        layers['b-title'] = Titles.draw(gd, 'b' + titlesuffix, {
            propContainer: baxis,
            propName: _this.id + '.baxis.title',
            placeholder: _(gd, 'Click to enter Component B title'),
            attributes: {
                x: _this.x0 - bpad,
                y: _this.y0 + _this.h + baxis.title.font.size * 0.83 + bpad,
                'text-anchor': 'middle'
            }
        });
        layers['c-title'] = Titles.draw(gd, 'c' + titlesuffix, {
            propContainer: caxis,
            propName: _this.id + '.caxis.title',
            placeholder: _(gd, 'Click to enter Component C title'),
            attributes: {
                x: _this.x0 + _this.w + bpad,
                y: _this.y0 + _this.h + caxis.title.font.size * 0.83 + bpad,
                'text-anchor': 'middle'
            }
        });
    }
};

proto.drawAx = function(ax) {
    var _this = this;
    var gd = _this.graphDiv;
    var axName = ax._name;
    var axLetter = axName.charAt(0);
    var axId = ax._id;
    var axLayer = _this.layers[axName];
    var counterAngle = 30;

    var stashKey = axLetter + 'tickLayout';
    var newTickLayout = strTickLayout(ax);
    if(_this[stashKey] !== newTickLayout) {
        axLayer.selectAll('.' + axId + 'tick').remove();
        _this[stashKey] = newTickLayout;
    }

    ax.setScale();

    var vals = Axes.calcTicks(ax);
    var valsClipped = Axes.clipEnds(ax, vals);
    var transFn = Axes.makeTransFn(ax);
    var tickSign = Axes.getTickSigns(ax)[2];

    var caRad = Lib.deg2rad(counterAngle);
    var pad = tickSign * (ax.linewidth || 1) / 2;
    var len = tickSign * ax.ticklen;
    var w = _this.w;
    var h = _this.h;

    var tickPath = axLetter === 'b' ?
        'M0,' + pad + 'l' + (Math.sin(caRad) * len) + ',' + (Math.cos(caRad) * len) :
        'M' + pad + ',0l' + (Math.cos(caRad) * len) + ',' + (-Math.sin(caRad) * len);

    var gridPath = {
        a: 'M0,0l' + h + ',-' + (w / 2),
        b: 'M0,0l-' + (w / 2) + ',-' + h,
        c: 'M0,0l-' + h + ',' + (w / 2)
    }[axLetter];

    Axes.drawTicks(gd, ax, {
        vals: ax.ticks === 'inside' ? valsClipped : vals,
        layer: axLayer,
        path: tickPath,
        transFn: transFn,
        crisp: false
    });

    Axes.drawGrid(gd, ax, {
        vals: valsClipped,
        layer: _this.layers[axLetter + 'grid'],
        path: gridPath,
        transFn: transFn,
        crisp: false
    });

    Axes.drawLabels(gd, ax, {
        vals: vals,
        layer: axLayer,
        transFn: transFn,
        labelFns: Axes.makeLabelFns(ax, 0, counterAngle)
    });
};

function strTickLayout(axLayout) {
    return axLayout.ticks + String(axLayout.ticklen) + String(axLayout.showticklabels);
}

// hard coded paths for zoom corners
// uses the same sizing as cartesian, length is MINZOOM/2, width is 3px
var CLEN = constants.MINZOOM / 2 + 0.87;
var BLPATH = 'm-0.87,.5h' + CLEN + 'v3h-' + (CLEN + 5.2) +
    'l' + (CLEN / 2 + 2.6) + ',-' + (CLEN * 0.87 + 4.5) +
    'l2.6,1.5l-' + (CLEN / 2) + ',' + (CLEN * 0.87) + 'Z';
var BRPATH = 'm0.87,.5h-' + CLEN + 'v3h' + (CLEN + 5.2) +
    'l-' + (CLEN / 2 + 2.6) + ',-' + (CLEN * 0.87 + 4.5) +
    'l-2.6,1.5l' + (CLEN / 2) + ',' + (CLEN * 0.87) + 'Z';
var TOPPATH = 'm0,1l' + (CLEN / 2) + ',' + (CLEN * 0.87) +
    'l2.6,-1.5l-' + (CLEN / 2 + 2.6) + ',-' + (CLEN * 0.87 + 4.5) +
    'l-' + (CLEN / 2 + 2.6) + ',' + (CLEN * 0.87 + 4.5) +
    'l2.6,1.5l' + (CLEN / 2) + ',-' + (CLEN * 0.87) + 'Z';
var STARTMARKER = 'm0.5,0.5h5v-2h-5v-5h-2v5h-5v2h5v5h2Z';

// I guess this could be shared with cartesian... but for now it's separate.
var SHOWZOOMOUTTIP = true;

proto.initInteractions = function() {
    var _this = this;
    var dragger = _this.layers.plotbg.select('path').node();
    var gd = _this.graphDiv;
    var zoomLayer = gd._fullLayout._zoomlayer;

    // use plotbg for the main interactions
    var dragOptions = {
        element: dragger,
        gd: gd,
        plotinfo: {
            id: _this.id,
            xaxis: _this.xaxis,
            yaxis: _this.yaxis
        },
        subplot: _this.id,
        prepFn: function(e, startX, startY) {
            // these aren't available yet when initInteractions
            // is called
            dragOptions.xaxes = [_this.xaxis];
            dragOptions.yaxes = [_this.yaxis];
            var dragModeNow = gd._fullLayout.dragmode;

            if(dragModeNow === 'lasso') dragOptions.minDrag = 1;
            else dragOptions.minDrag = undefined;

            if(dragModeNow === 'zoom') {
                dragOptions.moveFn = zoomMove;
                dragOptions.clickFn = clickZoomPan;
                dragOptions.doneFn = zoomDone;
                zoomPrep(e, startX, startY);
            } else if(dragModeNow === 'pan') {
                dragOptions.moveFn = plotDrag;
                dragOptions.clickFn = clickZoomPan;
                dragOptions.doneFn = dragDone;
                panPrep();
                clearSelect(gd);
            } else if(dragModeNow === 'select' || dragModeNow === 'lasso') {
                prepSelect(e, startX, startY, dragOptions, dragModeNow);
            }
        }
    };

    var x0, y0, mins0, span0, mins, lum, path0, dimmed, zb, corners;

    function makeUpdate(_mins) {
        var attrs = {};
        attrs[_this.id + '.aaxis.min'] = _mins.a;
        attrs[_this.id + '.baxis.min'] = _mins.b;
        attrs[_this.id + '.caxis.min'] = _mins.c;
        return attrs;
    }

    function clickZoomPan(numClicks, evt) {
        var clickMode = gd._fullLayout.clickmode;

        removeZoombox(gd);

        if(numClicks === 2) {
            gd.emit('plotly_doubleclick', null);
            Registry.call('_guiRelayout', gd, makeUpdate({a: 0, b: 0, c: 0}));
        }

        if(clickMode.indexOf('select') > -1 && numClicks === 1) {
            selectOnClick(evt, gd, [_this.xaxis], [_this.yaxis], _this.id, dragOptions);
        }

        if(clickMode.indexOf('event') > -1) {
            Fx.click(gd, evt, _this.id);
        }
    }

    function zoomPrep(e, startX, startY) {
        var dragBBox = dragger.getBoundingClientRect();
        x0 = startX - dragBBox.left;
        y0 = startY - dragBBox.top;
        mins0 = {
            a: _this.aaxis.range[0],
            b: _this.baxis.range[1],
            c: _this.caxis.range[1]
        };
        mins = mins0;
        span0 = _this.aaxis.range[1] - mins0.a;
        lum = tinycolor(_this.graphDiv._fullLayout[_this.id].bgcolor).getLuminance();
        path0 = 'M0,' + _this.h + 'L' + (_this.w / 2) + ', 0L' + _this.w + ',' + _this.h + 'Z';
        dimmed = false;

        zb = zoomLayer.append('path')
            .attr('class', 'zoombox')
            .attr('transform', 'translate(' + _this.x0 + ', ' + _this.y0 + ')')
            .style({
                'fill': lum > 0.2 ? 'rgba(0,0,0,0)' : 'rgba(255,255,255,0)',
                'stroke-width': 0
            })
            .attr('d', path0);

        corners = zoomLayer.append('path')
            .attr('class', 'zoombox-corners')
            .attr('transform', 'translate(' + _this.x0 + ', ' + _this.y0 + ')')
            .style({
                fill: Color.background,
                stroke: Color.defaultLine,
                'stroke-width': 1,
                opacity: 0
            })
            .attr('d', 'M0,0Z');

        clearSelect(gd);
    }

    function getAFrac(x, y) { return 1 - (y / _this.h); }
    function getBFrac(x, y) { return 1 - ((x + (_this.h - y) / Math.sqrt(3)) / _this.w); }
    function getCFrac(x, y) { return ((x - (_this.h - y) / Math.sqrt(3)) / _this.w); }

    function zoomMove(dx0, dy0) {
        var x1 = x0 + dx0;
        var y1 = y0 + dy0;
        var afrac = Math.max(0, Math.min(1, getAFrac(x0, y0), getAFrac(x1, y1)));
        var bfrac = Math.max(0, Math.min(1, getBFrac(x0, y0), getBFrac(x1, y1)));
        var cfrac = Math.max(0, Math.min(1, getCFrac(x0, y0), getCFrac(x1, y1)));
        var xLeft = ((afrac / 2) + cfrac) * _this.w;
        var xRight = (1 - (afrac / 2) - bfrac) * _this.w;
        var xCenter = (xLeft + xRight) / 2;
        var xSpan = xRight - xLeft;
        var yBottom = (1 - afrac) * _this.h;
        var yTop = yBottom - xSpan / whRatio;

        if(xSpan < constants.MINZOOM) {
            mins = mins0;
            zb.attr('d', path0);
            corners.attr('d', 'M0,0Z');
        } else {
            mins = {
                a: mins0.a + afrac * span0,
                b: mins0.b + bfrac * span0,
                c: mins0.c + cfrac * span0
            };
            zb.attr('d', path0 + 'M' + xLeft + ',' + yBottom +
                'H' + xRight + 'L' + xCenter + ',' + yTop +
                'L' + xLeft + ',' + yBottom + 'Z');
            corners.attr('d', 'M' + x0 + ',' + y0 + STARTMARKER +
                'M' + xLeft + ',' + yBottom + BLPATH +
                'M' + xRight + ',' + yBottom + BRPATH +
                'M' + xCenter + ',' + yTop + TOPPATH);
        }

        if(!dimmed) {
            zb.transition()
                .style('fill', lum > 0.2 ? 'rgba(0,0,0,0.4)' :
                    'rgba(255,255,255,0.3)')
                .duration(200);
            corners.transition()
                .style('opacity', 1)
                .duration(200);
            dimmed = true;
        }

        gd.emit('plotly_relayouting', makeUpdate(mins));
    }

    function zoomDone() {
        removeZoombox(gd);

        if(mins === mins0) return;

        Registry.call('_guiRelayout', gd, makeUpdate(mins));

        if(SHOWZOOMOUTTIP && gd.data && gd._context.showTips) {
            Lib.notifier(_(gd, 'Double-click to zoom back out'), 'long');
            SHOWZOOMOUTTIP = false;
        }
    }

    function panPrep() {
        mins0 = {
            a: _this.aaxis.range[0],
            b: _this.baxis.range[1],
            c: _this.caxis.range[1]
        };
        mins = mins0;
    }

    function plotDrag(dx, dy) {
        var dxScaled = dx / _this.xaxis._m;
        var dyScaled = dy / _this.yaxis._m;
        mins = {
            a: mins0.a - dyScaled,
            b: mins0.b + (dxScaled + dyScaled) / 2,
            c: mins0.c - (dxScaled - dyScaled) / 2
        };
        var minsorted = [mins.a, mins.b, mins.c].sort();
        var minindices = {
            a: minsorted.indexOf(mins.a),
            b: minsorted.indexOf(mins.b),
            c: minsorted.indexOf(mins.c)
        };
        if(minsorted[0] < 0) {
            if(minsorted[1] + minsorted[0] / 2 < 0) {
                minsorted[2] += minsorted[0] + minsorted[1];
                minsorted[0] = minsorted[1] = 0;
            } else {
                minsorted[2] += minsorted[0] / 2;
                minsorted[1] += minsorted[0] / 2;
                minsorted[0] = 0;
            }
            mins = {
                a: minsorted[minindices.a],
                b: minsorted[minindices.b],
                c: minsorted[minindices.c]
            };
            dy = (mins0.a - mins.a) * _this.yaxis._m;
            dx = (mins0.c - mins.c - mins0.b + mins.b) * _this.xaxis._m;
        }

        // move the data (translate, don't redraw)
        var plotTransform = 'translate(' + (_this.x0 + dx) + ',' + (_this.y0 + dy) + ')';
        _this.plotContainer.selectAll('.scatterlayer,.maplayer')
            .attr('transform', plotTransform);

        var plotTransform2 = 'translate(' + -dx + ',' + -dy + ')';
        _this.clipDefRelative.select('path').attr('transform', plotTransform2);

        // move the ticks
        _this.aaxis.range = [mins.a, _this.sum - mins.b - mins.c];
        _this.baxis.range = [_this.sum - mins.a - mins.c, mins.b];
        _this.caxis.range = [_this.sum - mins.a - mins.b, mins.c];

        _this.drawAxes(false);

        if(_this._hasClipOnAxisFalse) {
            _this.plotContainer
                .select('.scatterlayer').selectAll('.trace')
                .call(Drawing.hideOutsideRangePoints, _this);
        }

        gd.emit('plotly_relayouting', makeUpdate(mins));
    }

    function dragDone() {
        Registry.call('_guiRelayout', gd, makeUpdate(mins));
    }

    // finally, set up hover and click
    // these event handlers must already be set before dragElement.init
    // so it can stash them and override them.
    dragger.onmousemove = function(evt) {
        Fx.hover(gd, evt, _this.id);
        gd._fullLayout._lasthover = dragger;
        gd._fullLayout._hoversubplot = _this.id;
    };

    dragger.onmouseout = function(evt) {
        if(gd._dragging) return;

        dragElement.unhover(gd, evt);
    };

    dragElement.init(dragOptions);
};

function removeZoombox(gd) {
    d3.select(gd)
        .selectAll('.zoombox,.js-zoombox-backdrop,.js-zoombox-menu,.zoombox-corners')
        .remove();
}
