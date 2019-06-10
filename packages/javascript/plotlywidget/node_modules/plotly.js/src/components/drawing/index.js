/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/


'use strict';

var d3 = require('d3');
var isNumeric = require('fast-isnumeric');
var tinycolor = require('tinycolor2');

var Registry = require('../../registry');
var Color = require('../color');
var Colorscale = require('../colorscale');
var Lib = require('../../lib');
var svgTextUtils = require('../../lib/svg_text_utils');

var xmlnsNamespaces = require('../../constants/xmlns_namespaces');
var alignment = require('../../constants/alignment');
var LINE_SPACING = alignment.LINE_SPACING;
var DESELECTDIM = require('../../constants/interactions').DESELECTDIM;

var subTypes = require('../../traces/scatter/subtypes');
var makeBubbleSizeFn = require('../../traces/scatter/make_bubble_size_func');

var drawing = module.exports = {};

// -----------------------------------------------------
// styling functions for plot elements
// -----------------------------------------------------

drawing.font = function(s, family, size, color) {
    // also allow the form font(s, {family, size, color})
    if(Lib.isPlainObject(family)) {
        color = family.color;
        size = family.size;
        family = family.family;
    }
    if(family) s.style('font-family', family);
    if(size + 1) s.style('font-size', size + 'px');
    if(color) s.call(Color.fill, color);
};

/*
 * Positioning helpers
 * Note: do not use `setPosition` with <text> nodes modified by
 * `svgTextUtils.convertToTspans`. Use `svgTextUtils.positionText`
 * instead, so that <tspan.line> elements get updated to match.
 */
drawing.setPosition = function(s, x, y) { s.attr('x', x).attr('y', y); };
drawing.setSize = function(s, w, h) { s.attr('width', w).attr('height', h); };
drawing.setRect = function(s, x, y, w, h) {
    s.call(drawing.setPosition, x, y).call(drawing.setSize, w, h);
};

/** Translate node
 *
 * @param {object} d : calcdata point item
 * @param {sel} sel : d3 selction of node to translate
 * @param {object} xa : corresponding full xaxis object
 * @param {object} ya : corresponding full yaxis object
 *
 * @return {boolean} :
 *  true if selection got translated
 *  false if selection could not get translated
 */
drawing.translatePoint = function(d, sel, xa, ya) {
    var x = xa.c2p(d.x);
    var y = ya.c2p(d.y);

    if(isNumeric(x) && isNumeric(y) && sel.node()) {
        // for multiline text this works better
        if(sel.node().nodeName === 'text') {
            sel.attr('x', x).attr('y', y);
        } else {
            sel.attr('transform', 'translate(' + x + ',' + y + ')');
        }
    } else {
        return false;
    }

    return true;
};

drawing.translatePoints = function(s, xa, ya) {
    s.each(function(d) {
        var sel = d3.select(this);
        drawing.translatePoint(d, sel, xa, ya);
    });
};

drawing.hideOutsideRangePoint = function(d, sel, xa, ya, xcalendar, ycalendar) {
    sel.attr(
        'display',
        (xa.isPtWithinRange(d, xcalendar) && ya.isPtWithinRange(d, ycalendar)) ? null : 'none'
    );
};

drawing.hideOutsideRangePoints = function(traceGroups, subplot) {
    if(!subplot._hasClipOnAxisFalse) return;

    var xa = subplot.xaxis;
    var ya = subplot.yaxis;

    traceGroups.each(function(d) {
        var trace = d[0].trace;
        var xcalendar = trace.xcalendar;
        var ycalendar = trace.ycalendar;
        var selector = Registry.traceIs(trace, 'bar-like') ? '.bartext' : '.point,.textpoint';

        traceGroups.selectAll(selector).each(function(d) {
            drawing.hideOutsideRangePoint(d, d3.select(this), xa, ya, xcalendar, ycalendar);
        });
    });
};

drawing.crispRound = function(gd, lineWidth, dflt) {
    // for lines that disable antialiasing we want to
    // make sure the width is an integer, and at least 1 if it's nonzero

    if(!lineWidth || !isNumeric(lineWidth)) return dflt || 0;

    // but not for static plots - these don't get antialiased anyway.
    if(gd._context.staticPlot) return lineWidth;

    if(lineWidth < 1) return 1;
    return Math.round(lineWidth);
};

drawing.singleLineStyle = function(d, s, lw, lc, ld) {
    s.style('fill', 'none');
    var line = (((d || [])[0] || {}).trace || {}).line || {};
    var lw1 = lw || line.width || 0;
    var dash = ld || line.dash || '';

    Color.stroke(s, lc || line.color);
    drawing.dashLine(s, dash, lw1);
};

drawing.lineGroupStyle = function(s, lw, lc, ld) {
    s.style('fill', 'none')
    .each(function(d) {
        var line = (((d || [])[0] || {}).trace || {}).line || {};
        var lw1 = lw || line.width || 0;
        var dash = ld || line.dash || '';

        d3.select(this)
            .call(Color.stroke, lc || line.color)
            .call(drawing.dashLine, dash, lw1);
    });
};

drawing.dashLine = function(s, dash, lineWidth) {
    lineWidth = +lineWidth || 0;

    dash = drawing.dashStyle(dash, lineWidth);

    s.style({
        'stroke-dasharray': dash,
        'stroke-width': lineWidth + 'px'
    });
};

drawing.dashStyle = function(dash, lineWidth) {
    lineWidth = +lineWidth || 1;
    var dlw = Math.max(lineWidth, 3);

    if(dash === 'solid') dash = '';
    else if(dash === 'dot') dash = dlw + 'px,' + dlw + 'px';
    else if(dash === 'dash') dash = (3 * dlw) + 'px,' + (3 * dlw) + 'px';
    else if(dash === 'longdash') dash = (5 * dlw) + 'px,' + (5 * dlw) + 'px';
    else if(dash === 'dashdot') {
        dash = (3 * dlw) + 'px,' + dlw + 'px,' + dlw + 'px,' + dlw + 'px';
    } else if(dash === 'longdashdot') {
        dash = (5 * dlw) + 'px,' + (2 * dlw) + 'px,' + dlw + 'px,' + (2 * dlw) + 'px';
    }
    // otherwise user wrote the dasharray themselves - leave it be

    return dash;
};

// Same as fillGroupStyle, except in this case the selection may be a transition
drawing.singleFillStyle = function(sel) {
    var node = d3.select(sel.node());
    var data = node.data();
    var fillcolor = (((data[0] || [])[0] || {}).trace || {}).fillcolor;
    if(fillcolor) {
        sel.call(Color.fill, fillcolor);
    }
};

drawing.fillGroupStyle = function(s) {
    s.style('stroke-width', 0)
    .each(function(d) {
        var shape = d3.select(this);
        // N.B. 'd' won't be a calcdata item when
        // fill !== 'none' on a segment-less and marker-less trace
        if(d[0].trace) {
            shape.call(Color.fill, d[0].trace.fillcolor);
        }
    });
};

var SYMBOLDEFS = require('./symbol_defs');

drawing.symbolNames = [];
drawing.symbolFuncs = [];
drawing.symbolNeedLines = {};
drawing.symbolNoDot = {};
drawing.symbolNoFill = {};
drawing.symbolList = [];

Object.keys(SYMBOLDEFS).forEach(function(k) {
    var symDef = SYMBOLDEFS[k];
    drawing.symbolList = drawing.symbolList.concat(
        [symDef.n, k, symDef.n + 100, k + '-open']);
    drawing.symbolNames[symDef.n] = k;
    drawing.symbolFuncs[symDef.n] = symDef.f;
    if(symDef.needLine) {
        drawing.symbolNeedLines[symDef.n] = true;
    }
    if(symDef.noDot) {
        drawing.symbolNoDot[symDef.n] = true;
    } else {
        drawing.symbolList = drawing.symbolList.concat(
            [symDef.n + 200, k + '-dot', symDef.n + 300, k + '-open-dot']);
    }
    if(symDef.noFill) {
        drawing.symbolNoFill[symDef.n] = true;
    }
});

var MAXSYMBOL = drawing.symbolNames.length;
// add a dot in the middle of the symbol
var DOTPATH = 'M0,0.5L0.5,0L0,-0.5L-0.5,0Z';

drawing.symbolNumber = function(v) {
    if(typeof v === 'string') {
        var vbase = 0;
        if(v.indexOf('-open') > 0) {
            vbase = 100;
            v = v.replace('-open', '');
        }
        if(v.indexOf('-dot') > 0) {
            vbase += 200;
            v = v.replace('-dot', '');
        }
        v = drawing.symbolNames.indexOf(v);
        if(v >= 0) { v += vbase; }
    }
    if((v % 100 >= MAXSYMBOL) || v >= 400) { return 0; }
    return Math.floor(Math.max(v, 0));
};

function makePointPath(symbolNumber, r) {
    var base = symbolNumber % 100;
    return drawing.symbolFuncs[base](r) + (symbolNumber >= 200 ? DOTPATH : '');
}

var HORZGRADIENT = {x1: 1, x2: 0, y1: 0, y2: 0};
var VERTGRADIENT = {x1: 0, x2: 0, y1: 1, y2: 0};
var stopFormatter = d3.format('~.1f');
var gradientInfo = {
    radial: {node: 'radialGradient'},
    radialreversed: {node: 'radialGradient', reversed: true},
    horizontal: {node: 'linearGradient', attrs: HORZGRADIENT},
    horizontalreversed: {node: 'linearGradient', attrs: HORZGRADIENT, reversed: true},
    vertical: {node: 'linearGradient', attrs: VERTGRADIENT},
    verticalreversed: {node: 'linearGradient', attrs: VERTGRADIENT, reversed: true}
};

/**
 * gradient: create and apply a gradient fill
 *
 * @param {object} sel: d3 selection to apply this gradient to
 *     You can use `selection.call(Drawing.gradient, ...)`
 * @param {DOM element} gd: the graph div `sel` is part of
 * @param {string} gradientID: a unique (within this plot) identifier
 *     for this gradient, so that we don't create unnecessary definitions
 * @param {string} type: 'radial', 'horizontal', or 'vertical', optionally with
 *     'reversed' at the end. Normally radial goes center to edge,
 *     horizontal goes right to left, and vertical goes bottom to top
 * @param {array} colorscale: as in attribute values, [[fraction, color], ...]
 * @param {string} prop: the property to apply to, 'fill' or 'stroke'
 */
drawing.gradient = function(sel, gd, gradientID, type, colorscale, prop) {
    var len = colorscale.length;
    var info = gradientInfo[type];
    var colorStops = new Array(len);
    for(var i = 0; i < len; i++) {
        if(info.reversed) {
            colorStops[len - 1 - i] = [stopFormatter((1 - colorscale[i][0]) * 100), colorscale[i][1]];
        } else {
            colorStops[i] = [stopFormatter(colorscale[i][0] * 100), colorscale[i][1]];
        }
    }

    var fullID = 'g' + gd._fullLayout._uid + '-' + gradientID;

    var gradient = gd._fullLayout._defs.select('.gradients')
        .selectAll('#' + fullID)
        .data([type + colorStops.join(';')], Lib.identity);

    gradient.exit().remove();

    gradient.enter()
        .append(info.node)
        .each(function() {
            var el = d3.select(this);
            if(info.attrs) el.attr(info.attrs);

            el.attr('id', fullID);

            var stops = el.selectAll('stop')
                .data(colorStops);
            stops.exit().remove();
            stops.enter().append('stop');

            stops.each(function(d) {
                var tc = tinycolor(d[1]);
                d3.select(this).attr({
                    offset: d[0] + '%',
                    'stop-color': Color.tinyRGB(tc),
                    'stop-opacity': tc.getAlpha()
                });
            });
        });

    sel.style(prop, getFullUrl(fullID, gd))
        .style(prop + '-opacity', null);
};

/*
 * Make the gradients container and clear out any previous gradients.
 * We never collect all the gradients we need in one place,
 * so we can't ever remove gradients that have stopped being useful,
 * except all at once before a full redraw.
 * The upside of this is arbitrary points can share gradient defs
 */
drawing.initGradients = function(gd) {
    var gradientsGroup = Lib.ensureSingle(gd._fullLayout._defs, 'g', 'gradients');
    gradientsGroup.selectAll('linearGradient,radialGradient').remove();
};


drawing.pointStyle = function(s, trace, gd) {
    if(!s.size()) return;

    var fns = drawing.makePointStyleFns(trace);

    s.each(function(d) {
        drawing.singlePointStyle(d, d3.select(this), trace, fns, gd);
    });
};

drawing.singlePointStyle = function(d, sel, trace, fns, gd) {
    var marker = trace.marker;
    var markerLine = marker.line;

    sel.style('opacity',
        fns.selectedOpacityFn ? fns.selectedOpacityFn(d) :
            (d.mo === undefined ? marker.opacity : d.mo)
    );

    if(fns.ms2mrc) {
        var r;

        // handle multi-trace graph edit case
        if(d.ms === 'various' || marker.size === 'various') {
            r = 3;
        } else {
            r = fns.ms2mrc(d.ms);
        }

        // store the calculated size so hover can use it
        d.mrc = r;

        if(fns.selectedSizeFn) {
            r = d.mrc = fns.selectedSizeFn(d);
        }

        // turn the symbol into a sanitized number
        var x = drawing.symbolNumber(d.mx || marker.symbol) || 0;

        // save if this marker is open
        // because that impacts how to handle colors
        d.om = x % 200 >= 100;

        sel.attr('d', makePointPath(x, r));
    }

    var perPointGradient = false;
    var fillColor, lineColor, lineWidth;

    // 'so' is suspected outliers, for box plots
    if(d.so) {
        lineWidth = markerLine.outlierwidth;
        lineColor = markerLine.outliercolor;
        fillColor = marker.outliercolor;
    } else {
        var markerLineWidth = (markerLine || {}).width;

        lineWidth = (
            d.mlw + 1 ||
            markerLineWidth + 1 ||
            // TODO: we need the latter for legends... can we get rid of it?
            (d.trace ? (d.trace.marker.line || {}).width : 0) + 1
        ) - 1 || 0;

        if('mlc' in d) lineColor = d.mlcc = fns.lineScale(d.mlc);
        // weird case: array wasn't long enough to apply to every point
        else if(Lib.isArrayOrTypedArray(markerLine.color)) lineColor = Color.defaultLine;
        else lineColor = markerLine.color;

        if(Lib.isArrayOrTypedArray(marker.color)) {
            fillColor = Color.defaultLine;
            perPointGradient = true;
        }

        if('mc' in d) {
            fillColor = d.mcc = fns.markerScale(d.mc);
        } else {
            fillColor = marker.color || 'rgba(0,0,0,0)';
        }

        if(fns.selectedColorFn) {
            fillColor = fns.selectedColorFn(d);
        }
    }

    if(d.om) {
        // open markers can't have zero linewidth, default to 1px,
        // and use fill color as stroke color
        sel.call(Color.stroke, fillColor)
            .style({
                'stroke-width': (lineWidth || 1) + 'px',
                fill: 'none'
            });
    } else {
        sel.style('stroke-width', lineWidth + 'px');

        var markerGradient = marker.gradient;

        var gradientType = d.mgt;
        if(gradientType) perPointGradient = true;
        else gradientType = markerGradient && markerGradient.type;

        // for legend - arrays will propagate through here, but we don't need
        // to treat it as per-point.
        if(Array.isArray(gradientType)) {
            gradientType = gradientType[0];
            if(!gradientInfo[gradientType]) gradientType = 0;
        }

        if(gradientType && gradientType !== 'none') {
            var gradientColor = d.mgc;
            if(gradientColor) perPointGradient = true;
            else gradientColor = markerGradient.color;

            var gradientID = trace.uid;
            if(perPointGradient) gradientID += '-' + d.i;

            drawing.gradient(sel, gd, gradientID, gradientType,
                [[0, gradientColor], [1, fillColor]], 'fill');
        } else {
            Color.fill(sel, fillColor);
        }

        if(lineWidth) {
            Color.stroke(sel, lineColor);
        }
    }
};

drawing.makePointStyleFns = function(trace) {
    var out = {};
    var marker = trace.marker;

    // allow array marker and marker line colors to be
    // scaled by given max and min to colorscales
    out.markerScale = drawing.tryColorscale(marker, '');
    out.lineScale = drawing.tryColorscale(marker, 'line');

    if(Registry.traceIs(trace, 'symbols')) {
        out.ms2mrc = subTypes.isBubble(trace) ?
            makeBubbleSizeFn(trace) :
            function() { return (marker.size || 6) / 2; };
    }

    if(trace.selectedpoints) {
        Lib.extendFlat(out, drawing.makeSelectedPointStyleFns(trace));
    }

    return out;
};

drawing.makeSelectedPointStyleFns = function(trace) {
    var out = {};

    var selectedAttrs = trace.selected || {};
    var unselectedAttrs = trace.unselected || {};

    var marker = trace.marker || {};
    var selectedMarker = selectedAttrs.marker || {};
    var unselectedMarker = unselectedAttrs.marker || {};

    var mo = marker.opacity;
    var smo = selectedMarker.opacity;
    var usmo = unselectedMarker.opacity;
    var smoIsDefined = smo !== undefined;
    var usmoIsDefined = usmo !== undefined;

    if(Lib.isArrayOrTypedArray(mo) || smoIsDefined || usmoIsDefined) {
        out.selectedOpacityFn = function(d) {
            var base = d.mo === undefined ? marker.opacity : d.mo;

            if(d.selected) {
                return smoIsDefined ? smo : base;
            } else {
                return usmoIsDefined ? usmo : DESELECTDIM * base;
            }
        };
    }

    var mc = marker.color;
    var smc = selectedMarker.color;
    var usmc = unselectedMarker.color;

    if(smc || usmc) {
        out.selectedColorFn = function(d) {
            var base = d.mcc || mc;

            if(d.selected) {
                return smc || base;
            } else {
                return usmc || base;
            }
        };
    }

    var ms = marker.size;
    var sms = selectedMarker.size;
    var usms = unselectedMarker.size;
    var smsIsDefined = sms !== undefined;
    var usmsIsDefined = usms !== undefined;

    if(Registry.traceIs(trace, 'symbols') && (smsIsDefined || usmsIsDefined)) {
        out.selectedSizeFn = function(d) {
            var base = d.mrc || ms / 2;

            if(d.selected) {
                return smsIsDefined ? sms / 2 : base;
            } else {
                return usmsIsDefined ? usms / 2 : base;
            }
        };
    }

    return out;
};

drawing.makeSelectedTextStyleFns = function(trace) {
    var out = {};

    var selectedAttrs = trace.selected || {};
    var unselectedAttrs = trace.unselected || {};

    var textFont = trace.textfont || {};
    var selectedTextFont = selectedAttrs.textfont || {};
    var unselectedTextFont = unselectedAttrs.textfont || {};

    var tc = textFont.color;
    var stc = selectedTextFont.color;
    var utc = unselectedTextFont.color;

    out.selectedTextColorFn = function(d) {
        var base = d.tc || tc;

        if(d.selected) {
            return stc || base;
        } else {
            if(utc) return utc;
            else return stc ? base : Color.addOpacity(base, DESELECTDIM);
        }
    };

    return out;
};

drawing.selectedPointStyle = function(s, trace) {
    if(!s.size() || !trace.selectedpoints) return;

    var fns = drawing.makeSelectedPointStyleFns(trace);
    var marker = trace.marker || {};
    var seq = [];

    if(fns.selectedOpacityFn) {
        seq.push(function(pt, d) {
            pt.style('opacity', fns.selectedOpacityFn(d));
        });
    }

    if(fns.selectedColorFn) {
        seq.push(function(pt, d) {
            Color.fill(pt, fns.selectedColorFn(d));
        });
    }

    if(fns.selectedSizeFn) {
        seq.push(function(pt, d) {
            var mx = d.mx || marker.symbol || 0;
            var mrc2 = fns.selectedSizeFn(d);

            pt.attr('d', makePointPath(drawing.symbolNumber(mx), mrc2));

            // save for Drawing.selectedTextStyle
            d.mrc2 = mrc2;
        });
    }

    if(seq.length) {
        s.each(function(d) {
            var pt = d3.select(this);
            for(var i = 0; i < seq.length; i++) {
                seq[i](pt, d);
            }
        });
    }
};

drawing.tryColorscale = function(marker, prefix) {
    var cont = prefix ? Lib.nestedProperty(marker, prefix).get() : marker;

    if(cont) {
        var colorArray = cont.color;
        if((cont.colorscale || cont._colorAx) && Lib.isArrayOrTypedArray(colorArray)) {
            return Colorscale.makeColorScaleFuncFromTrace(cont);
        }
    }
    return Lib.identity;
};

var TEXTOFFSETSIGN = {
    start: 1, end: -1, middle: 0, bottom: 1, top: -1
};

function textPointPosition(s, textPosition, fontSize, markerRadius) {
    var group = d3.select(s.node().parentNode);

    var v = textPosition.indexOf('top') !== -1 ?
        'top' :
        textPosition.indexOf('bottom') !== -1 ? 'bottom' : 'middle';
    var h = textPosition.indexOf('left') !== -1 ?
        'end' :
        textPosition.indexOf('right') !== -1 ? 'start' : 'middle';

    // if markers are shown, offset a little more than
    // the nominal marker size
    // ie 2/1.6 * nominal, bcs some markers are a bit bigger
    var r = markerRadius ? markerRadius / 0.8 + 1 : 0;

    var numLines = (svgTextUtils.lineCount(s) - 1) * LINE_SPACING + 1;
    var dx = TEXTOFFSETSIGN[h] * r;
    var dy = fontSize * 0.75 + TEXTOFFSETSIGN[v] * r +
        (TEXTOFFSETSIGN[v] - 1) * numLines * fontSize / 2;

    // fix the overall text group position
    s.attr('text-anchor', h);
    group.attr('transform', 'translate(' + dx + ',' + dy + ')');
}

function extracTextFontSize(d, trace) {
    var fontSize = d.ts || trace.textfont.size;
    return (isNumeric(fontSize) && fontSize > 0) ? fontSize : 0;
}

// draw text at points
drawing.textPointStyle = function(s, trace, gd) {
    if(!s.size()) return;

    var selectedTextColorFn;

    if(trace.selectedpoints) {
        var fns = drawing.makeSelectedTextStyleFns(trace);
        selectedTextColorFn = fns.selectedTextColorFn;
    }

    s.each(function(d) {
        var p = d3.select(this);
        var text = Lib.extractOption(d, trace, 'tx', 'text');

        if(!text && text !== 0) {
            p.remove();
            return;
        }

        var pos = d.tp || trace.textposition;
        var fontSize = extracTextFontSize(d, trace);
        var fontColor = selectedTextColorFn ?
            selectedTextColorFn(d) :
            (d.tc || trace.textfont.color);

        p.call(drawing.font,
                d.tf || trace.textfont.family,
                fontSize,
                fontColor)
            .text(text)
            .call(svgTextUtils.convertToTspans, gd)
            .call(textPointPosition, pos, fontSize, d.mrc);
    });
};

drawing.selectedTextStyle = function(s, trace) {
    if(!s.size() || !trace.selectedpoints) return;

    var fns = drawing.makeSelectedTextStyleFns(trace);

    s.each(function(d) {
        var tx = d3.select(this);
        var tc = fns.selectedTextColorFn(d);
        var tp = d.tp || trace.textposition;
        var fontSize = extracTextFontSize(d, trace);

        Color.fill(tx, tc);
        textPointPosition(tx, tp, fontSize, d.mrc2 || d.mrc);
    });
};

// generalized Catmull-Rom splines, per
// http://www.cemyuksel.com/research/catmullrom_param/catmullrom.pdf
var CatmullRomExp = 0.5;
drawing.smoothopen = function(pts, smoothness) {
    if(pts.length < 3) { return 'M' + pts.join('L');}
    var path = 'M' + pts[0];
    var tangents = [];
    var i;
    for(i = 1; i < pts.length - 1; i++) {
        tangents.push(makeTangent(pts[i - 1], pts[i], pts[i + 1], smoothness));
    }
    path += 'Q' + tangents[0][0] + ' ' + pts[1];
    for(i = 2; i < pts.length - 1; i++) {
        path += 'C' + tangents[i - 2][1] + ' ' + tangents[i - 1][0] + ' ' + pts[i];
    }
    path += 'Q' + tangents[pts.length - 3][1] + ' ' + pts[pts.length - 1];
    return path;
};

drawing.smoothclosed = function(pts, smoothness) {
    if(pts.length < 3) { return 'M' + pts.join('L') + 'Z'; }
    var path = 'M' + pts[0];
    var pLast = pts.length - 1;
    var tangents = [makeTangent(pts[pLast], pts[0], pts[1], smoothness)];
    var i;
    for(i = 1; i < pLast; i++) {
        tangents.push(makeTangent(pts[i - 1], pts[i], pts[i + 1], smoothness));
    }
    tangents.push(
        makeTangent(pts[pLast - 1], pts[pLast], pts[0], smoothness)
    );

    for(i = 1; i <= pLast; i++) {
        path += 'C' + tangents[i - 1][1] + ' ' + tangents[i][0] + ' ' + pts[i];
    }
    path += 'C' + tangents[pLast][1] + ' ' + tangents[0][0] + ' ' + pts[0] + 'Z';
    return path;
};

function makeTangent(prevpt, thispt, nextpt, smoothness) {
    var d1x = prevpt[0] - thispt[0];
    var d1y = prevpt[1] - thispt[1];
    var d2x = nextpt[0] - thispt[0];
    var d2y = nextpt[1] - thispt[1];
    var d1a = Math.pow(d1x * d1x + d1y * d1y, CatmullRomExp / 2);
    var d2a = Math.pow(d2x * d2x + d2y * d2y, CatmullRomExp / 2);
    var numx = (d2a * d2a * d1x - d1a * d1a * d2x) * smoothness;
    var numy = (d2a * d2a * d1y - d1a * d1a * d2y) * smoothness;
    var denom1 = 3 * d2a * (d1a + d2a);
    var denom2 = 3 * d1a * (d1a + d2a);
    return [
        [
            d3.round(thispt[0] + (denom1 && numx / denom1), 2),
            d3.round(thispt[1] + (denom1 && numy / denom1), 2)
        ], [
            d3.round(thispt[0] - (denom2 && numx / denom2), 2),
            d3.round(thispt[1] - (denom2 && numy / denom2), 2)
        ]
    ];
}

// step paths - returns a generator function for paths
// with the given step shape
var STEPPATH = {
    hv: function(p0, p1) {
        return 'H' + d3.round(p1[0], 2) + 'V' + d3.round(p1[1], 2);
    },
    vh: function(p0, p1) {
        return 'V' + d3.round(p1[1], 2) + 'H' + d3.round(p1[0], 2);
    },
    hvh: function(p0, p1) {
        return 'H' + d3.round((p0[0] + p1[0]) / 2, 2) + 'V' +
            d3.round(p1[1], 2) + 'H' + d3.round(p1[0], 2);
    },
    vhv: function(p0, p1) {
        return 'V' + d3.round((p0[1] + p1[1]) / 2, 2) + 'H' +
            d3.round(p1[0], 2) + 'V' + d3.round(p1[1], 2);
    }
};
var STEPLINEAR = function(p0, p1) {
    return 'L' + d3.round(p1[0], 2) + ',' + d3.round(p1[1], 2);
};
drawing.steps = function(shape) {
    var onestep = STEPPATH[shape] || STEPLINEAR;
    return function(pts) {
        var path = 'M' + d3.round(pts[0][0], 2) + ',' + d3.round(pts[0][1], 2);
        for(var i = 1; i < pts.length; i++) {
            path += onestep(pts[i - 1], pts[i]);
        }
        return path;
    };
};

// off-screen svg render testing element, shared by the whole page
// uses the id 'js-plotly-tester' and stores it in drawing.tester
drawing.makeTester = function() {
    var tester = Lib.ensureSingleById(d3.select('body'), 'svg', 'js-plotly-tester', function(s) {
        s.attr(xmlnsNamespaces.svgAttrs)
            .style({
                position: 'absolute',
                left: '-10000px',
                top: '-10000px',
                width: '9000px',
                height: '9000px',
                'z-index': '1'
            });
    });

    // browsers differ on how they describe the bounding rect of
    // the svg if its contents spill over... so make a 1x1px
    // reference point we can measure off of.
    var testref = Lib.ensureSingle(tester, 'path', 'js-reference-point', function(s) {
        s.attr('d', 'M0,0H1V1H0Z')
            .style({
                'stroke-width': 0,
                fill: 'black'
            });
    });

    drawing.tester = tester;
    drawing.testref = testref;
};

/*
 * use our offscreen tester to get a clientRect for an element,
 * in a reference frame where it isn't translated (or transformed) and
 * its anchor point is at (0,0)
 * always returns a copy of the bbox, so the caller can modify it safely
 *
 * @param {SVGElement} node: the element to measure. If possible this should be
 *   a <text> or MathJax <g> element that's already passed through
 *   `convertToTspans` because in that case we can cache the results, but it's
 *   possible to pass in any svg element.
 *
 * @param {boolean} inTester: is this element already in `drawing.tester`?
 *   If you are measuring a dummy element, rather than one you really intend
 *   to use on the plot, making it in `drawing.tester` in the first place
 *   allows us to test faster because it cuts out cloning and appending it.
 *
 * @param {string} hash: for internal use only, if we already know the cache key
 *   for this element beforehand.
 *
 * @return {object}: a plain object containing the width, height, left, right,
 *   top, and bottom of `node`
 */
drawing.savedBBoxes = {};
var savedBBoxesCount = 0;
var maxSavedBBoxes = 10000;

drawing.bBox = function(node, inTester, hash) {
    /*
     * Cache elements we've already measured so we don't have to
     * remeasure the same thing many times
     * We have a few bBox callers though who pass a node larger than
     * a <text> or a MathJax <g>, such as an axis group containing many labels.
     * These will not generate a hash (unless we figure out an appropriate
     * hash key for them) and thus we will not hash them.
     */
    if(!hash) hash = nodeHash(node);
    var out;
    if(hash) {
        out = drawing.savedBBoxes[hash];
        if(out) return Lib.extendFlat({}, out);
    } else if(node.childNodes.length === 1) {
        /*
         * If we have only one child element, which is itself hashable, make
         * a new hash from this element plus its x,y,transform
         * These bounding boxes *include* x,y,transform - mostly for use by
         * callers trying to avoid overlaps (ie titles)
         */
        var innerNode = node.childNodes[0];

        hash = nodeHash(innerNode);
        if(hash) {
            var x = +innerNode.getAttribute('x') || 0;
            var y = +innerNode.getAttribute('y') || 0;
            var transform = innerNode.getAttribute('transform');

            if(!transform) {
                // in this case, just varying x and y, don't bother caching
                // the final bBox because the alteration is quick.
                var innerBB = drawing.bBox(innerNode, false, hash);
                if(x) {
                    innerBB.left += x;
                    innerBB.right += x;
                }
                if(y) {
                    innerBB.top += y;
                    innerBB.bottom += y;
                }
                return innerBB;
            }
            /*
             * else we have a transform - rather than make a complicated
             * (and error-prone and probably slow) transform parser/calculator,
             * just continue on calculating the boundingClientRect of the group
             * and use the new composite hash to cache it.
             * That said, `innerNode.transform.baseVal` is an array of
             * `SVGTransform` objects, that *do* seem to have a nice matrix
             * multiplication interface that we could use to avoid making
             * another getBoundingClientRect call...
             */
            hash += '~' + x + '~' + y + '~' + transform;

            out = drawing.savedBBoxes[hash];
            if(out) return Lib.extendFlat({}, out);
        }
    }
    var testNode, tester;
    if(inTester) {
        testNode = node;
    } else {
        tester = drawing.tester.node();

        // copy the node to test into the tester
        testNode = node.cloneNode(true);
        tester.appendChild(testNode);
    }

    // standardize its position (and newline tspans if any)
    d3.select(testNode)
        .attr('transform', null)
        .call(svgTextUtils.positionText, 0, 0);

    var testRect = testNode.getBoundingClientRect();
    var refRect = drawing.testref
        .node()
        .getBoundingClientRect();

    if(!inTester) tester.removeChild(testNode);

    var bb = {
        height: testRect.height,
        width: testRect.width,
        left: testRect.left - refRect.left,
        top: testRect.top - refRect.top,
        right: testRect.right - refRect.left,
        bottom: testRect.bottom - refRect.top
    };

    // make sure we don't have too many saved boxes,
    // or a long session could overload on memory
    // by saving boxes for long-gone elements
    if(savedBBoxesCount >= maxSavedBBoxes) {
        drawing.savedBBoxes = {};
        savedBBoxesCount = 0;
    }

    // cache this bbox
    if(hash) drawing.savedBBoxes[hash] = bb;
    savedBBoxesCount++;

    return Lib.extendFlat({}, bb);
};

// capture everything about a node (at least in our usage) that
// impacts its bounding box, given that bBox clears x, y, and transform
function nodeHash(node) {
    var inputText = node.getAttribute('data-unformatted');
    if(inputText === null) return;
    return inputText +
        node.getAttribute('data-math') +
        node.getAttribute('text-anchor') +
        node.getAttribute('style');
}

/**
 * Set clipPath URL in a way that work for all situations.
 *
 * In details, graphs on pages with <base> HTML tags need to prepend
 * the clip path ids with the page's base url EXCEPT during toImage exports.
 *
 * @param {d3 selection} s : node to add clip-path attribute
 * @param {string} localId : local clip-path (w/o base url) id
 * @param {DOM element || object} gd
 * - context._baseUrl {string}
 * - context._exportedPlot {boolean}
 */
drawing.setClipUrl = function(s, localId, gd) {
    s.attr('clip-path', getFullUrl(localId, gd));
};

function getFullUrl(localId, gd) {
    if(!localId) return null;

    var context = gd._context;
    var baseUrl = context._exportedPlot ? '' : (context._baseUrl || '');
    return 'url(\'' + baseUrl + '#' + localId + '\')';
}

drawing.getTranslate = function(element) {
    // Note the separator [^\d] between x and y in this regex
    // We generally use ',' but IE will convert it to ' '
    var re = /.*\btranslate\((-?\d*\.?\d*)[^-\d]*(-?\d*\.?\d*)[^\d].*/;
    var getter = element.attr ? 'attr' : 'getAttribute';
    var transform = element[getter]('transform') || '';

    var translate = transform.replace(re, function(match, p1, p2) {
        return [p1, p2].join(' ');
    })
    .split(' ');

    return {
        x: +translate[0] || 0,
        y: +translate[1] || 0
    };
};

drawing.setTranslate = function(element, x, y) {
    var re = /(\btranslate\(.*?\);?)/;
    var getter = element.attr ? 'attr' : 'getAttribute';
    var setter = element.attr ? 'attr' : 'setAttribute';
    var transform = element[getter]('transform') || '';

    x = x || 0;
    y = y || 0;

    transform = transform.replace(re, '').trim();
    transform += ' translate(' + x + ', ' + y + ')';
    transform = transform.trim();

    element[setter]('transform', transform);

    return transform;
};

drawing.getScale = function(element) {
    var re = /.*\bscale\((\d*\.?\d*)[^\d]*(\d*\.?\d*)[^\d].*/;
    var getter = element.attr ? 'attr' : 'getAttribute';
    var transform = element[getter]('transform') || '';

    var translate = transform.replace(re, function(match, p1, p2) {
        return [p1, p2].join(' ');
    })
    .split(' ');

    return {
        x: +translate[0] || 1,
        y: +translate[1] || 1
    };
};

drawing.setScale = function(element, x, y) {
    var re = /(\bscale\(.*?\);?)/;
    var getter = element.attr ? 'attr' : 'getAttribute';
    var setter = element.attr ? 'attr' : 'setAttribute';
    var transform = element[getter]('transform') || '';

    x = x || 1;
    y = y || 1;

    transform = transform.replace(re, '').trim();
    transform += ' scale(' + x + ', ' + y + ')';
    transform = transform.trim();

    element[setter]('transform', transform);

    return transform;
};

var SCALE_RE = /\s*sc.*/;

drawing.setPointGroupScale = function(selection, xScale, yScale) {
    xScale = xScale || 1;
    yScale = yScale || 1;

    if(!selection) return;

    // The same scale transform for every point:
    var scale = (xScale === 1 && yScale === 1) ?
        '' :
        ' scale(' + xScale + ',' + yScale + ')';

    selection.each(function() {
        var t = (this.getAttribute('transform') || '').replace(SCALE_RE, '');
        t += scale;
        t = t.trim();
        this.setAttribute('transform', t);
    });
};

var TEXT_POINT_LAST_TRANSLATION_RE = /translate\([^)]*\)\s*$/;

drawing.setTextPointsScale = function(selection, xScale, yScale) {
    if(!selection) return;

    selection.each(function() {
        var transforms;
        var el = d3.select(this);
        var text = el.select('text');

        if(!text.node()) return;

        var x = parseFloat(text.attr('x') || 0);
        var y = parseFloat(text.attr('y') || 0);

        var existingTransform = (el.attr('transform') || '').match(TEXT_POINT_LAST_TRANSLATION_RE);

        if(xScale === 1 && yScale === 1) {
            transforms = [];
        } else {
            transforms = [
                'translate(' + x + ',' + y + ')',
                'scale(' + xScale + ',' + yScale + ')',
                'translate(' + (-x) + ',' + (-y) + ')',
            ];
        }

        if(existingTransform) {
            transforms.push(existingTransform);
        }

        el.attr('transform', transforms.join(' '));
    });
};
