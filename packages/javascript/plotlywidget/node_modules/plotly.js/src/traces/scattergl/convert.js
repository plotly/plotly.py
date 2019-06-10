/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var isNumeric = require('fast-isnumeric');
var svgSdf = require('svg-path-sdf');
var rgba = require('color-normalize');

var Registry = require('../../registry');
var Lib = require('../../lib');
var Drawing = require('../../components/drawing');
var AxisIDs = require('../../plots/cartesian/axis_ids');

var formatColor = require('../../lib/gl_format_color').formatColor;
var subTypes = require('../scatter/subtypes');
var makeBubbleSizeFn = require('../scatter/make_bubble_size_func');

var constants = require('./constants');
var DESELECTDIM = require('../../constants/interactions').DESELECTDIM;

var TEXTOFFSETSIGN = {
    start: 1, left: 1, end: -1, right: -1, middle: 0, center: 0, bottom: 1, top: -1
};

function convertStyle(gd, trace) {
    var i;

    var opts = {
        marker: undefined,
        markerSel: undefined,
        markerUnsel: undefined,
        line: undefined,
        fill: undefined,
        errorX: undefined,
        errorY: undefined,
        text: undefined,
        textSel: undefined,
        textUnsel: undefined
    };

    if(trace.visible !== true) return opts;

    if(subTypes.hasText(trace)) {
        opts.text = convertTextStyle(trace);
        opts.textSel = convertTextSelection(trace, trace.selected);
        opts.textUnsel = convertTextSelection(trace, trace.unselected);
    }

    if(subTypes.hasMarkers(trace)) {
        opts.marker = convertMarkerStyle(trace);
        opts.markerSel = convertMarkerSelection(trace, trace.selected);
        opts.markerUnsel = convertMarkerSelection(trace, trace.unselected);

        if(!trace.unselected && Array.isArray(trace.marker.opacity)) {
            var mo = trace.marker.opacity;
            opts.markerUnsel.opacity = new Array(mo.length);
            for(i = 0; i < mo.length; i++) {
                opts.markerUnsel.opacity[i] = DESELECTDIM * mo[i];
            }
        }
    }

    if(subTypes.hasLines(trace)) {
        opts.line = {
            overlay: true,
            thickness: trace.line.width,
            color: trace.line.color,
            opacity: trace.opacity
        };

        var dashes = (constants.DASHES[trace.line.dash] || [1]).slice();
        for(i = 0; i < dashes.length; ++i) {
            dashes[i] *= trace.line.width;
        }
        opts.line.dashes = dashes;
    }

    if(trace.error_x && trace.error_x.visible) {
        opts.errorX = convertErrorBarStyle(trace, trace.error_x);
    }

    if(trace.error_y && trace.error_y.visible) {
        opts.errorY = convertErrorBarStyle(trace, trace.error_y);
    }

    if(!!trace.fill && trace.fill !== 'none') {
        opts.fill = {
            closed: true,
            fill: trace.fillcolor,
            thickness: 0
        };
    }

    return opts;
}

function convertTextStyle(trace) {
    var count = trace._length;
    var textfontIn = trace.textfont;
    var textpositionIn = trace.textposition;
    var textPos = Array.isArray(textpositionIn) ? textpositionIn : [textpositionIn];
    var tfc = textfontIn.color;
    var tfs = textfontIn.size;
    var tff = textfontIn.family;
    var optsOut = {};
    var i;

    optsOut.text = trace.text;
    optsOut.opacity = trace.opacity;
    optsOut.font = {};
    optsOut.align = [];
    optsOut.baseline = [];

    for(i = 0; i < textPos.length; i++) {
        var tp = textPos[i].split(/\s+/);

        switch(tp[1]) {
            case 'left':
                optsOut.align.push('right');
                break;
            case 'right':
                optsOut.align.push('left');
                break;
            default:
                optsOut.align.push(tp[1]);
        }
        switch(tp[0]) {
            case 'top':
                optsOut.baseline.push('bottom');
                break;
            case 'bottom':
                optsOut.baseline.push('top');
                break;
            default:
                optsOut.baseline.push(tp[0]);
        }
    }

    if(Array.isArray(tfc)) {
        optsOut.color = new Array(count);
        for(i = 0; i < count; i++) {
            optsOut.color[i] = tfc[i];
        }
    } else {
        optsOut.color = tfc;
    }

    if(Array.isArray(tfs) || Array.isArray(tff)) {
        // if any textfont param is array - make render a batch
        optsOut.font = new Array(count);
        for(i = 0; i < count; i++) {
            var fonti = optsOut.font[i] = {};

            fonti.size = Array.isArray(tfs) ?
                (isNumeric(tfs[i]) ? tfs[i] : 0) :
                tfs;

            fonti.family = Array.isArray(tff) ? tff[i] : tff;
        }
    } else {
        // if both are single values, make render fast single-value
        optsOut.font = {size: tfs, family: tff};
    }

    return optsOut;
}


function convertMarkerStyle(trace) {
    var count = trace._length;
    var optsIn = trace.marker;
    var optsOut = {};
    var i;

    var multiSymbol = Array.isArray(optsIn.symbol);
    var multiColor = Lib.isArrayOrTypedArray(optsIn.color);
    var multiLineColor = Lib.isArrayOrTypedArray(optsIn.line.color);
    var multiOpacity = Lib.isArrayOrTypedArray(optsIn.opacity);
    var multiSize = Lib.isArrayOrTypedArray(optsIn.size);
    var multiLineWidth = Lib.isArrayOrTypedArray(optsIn.line.width);

    var isOpen;
    if(!multiSymbol) isOpen = constants.OPEN_RE.test(optsIn.symbol);

    // prepare colors
    if(multiSymbol || multiColor || multiLineColor || multiOpacity) {
        optsOut.colors = new Array(count);
        optsOut.borderColors = new Array(count);

        var colors = formatColor(optsIn, optsIn.opacity, count);
        var borderColors = formatColor(optsIn.line, optsIn.opacity, count);

        if(!Array.isArray(borderColors[0])) {
            var borderColor = borderColors;
            borderColors = Array(count);
            for(i = 0; i < count; i++) {
                borderColors[i] = borderColor;
            }
        }
        if(!Array.isArray(colors[0])) {
            var color = colors;
            colors = Array(count);
            for(i = 0; i < count; i++) {
                colors[i] = color;
            }
        }

        optsOut.colors = colors;
        optsOut.borderColors = borderColors;

        for(i = 0; i < count; i++) {
            if(multiSymbol) {
                var symbol = optsIn.symbol[i];
                isOpen = constants.OPEN_RE.test(symbol);
            }
            if(isOpen) {
                borderColors[i] = colors[i].slice();
                colors[i] = colors[i].slice();
                colors[i][3] = 0;
            }
        }

        optsOut.opacity = trace.opacity;
    } else {
        if(isOpen) {
            optsOut.color = rgba(optsIn.color, 'uint8');
            optsOut.color[3] = 0;
            optsOut.borderColor = rgba(optsIn.color, 'uint8');
        } else {
            optsOut.color = rgba(optsIn.color, 'uint8');
            optsOut.borderColor = rgba(optsIn.line.color, 'uint8');
        }

        optsOut.opacity = trace.opacity * optsIn.opacity;
    }

    // prepare symbols
    if(multiSymbol) {
        optsOut.markers = new Array(count);
        for(i = 0; i < count; i++) {
            optsOut.markers[i] = getSymbolSdf(optsIn.symbol[i]);
        }
    } else {
        optsOut.marker = getSymbolSdf(optsIn.symbol);
    }

    // prepare sizes
    var markerSizeFunc = makeBubbleSizeFn(trace);
    var s;

    if(multiSize || multiLineWidth) {
        var sizes = optsOut.sizes = new Array(count);
        var borderSizes = optsOut.borderSizes = new Array(count);
        var sizeTotal = 0;
        var sizeAvg;

        if(multiSize) {
            for(i = 0; i < count; i++) {
                sizes[i] = markerSizeFunc(optsIn.size[i]);
                sizeTotal += sizes[i];
            }
            sizeAvg = sizeTotal / count;
        } else {
            s = markerSizeFunc(optsIn.size);
            for(i = 0; i < count; i++) {
                sizes[i] = s;
            }
        }

        // See  https://github.com/plotly/plotly.js/pull/1781#discussion_r121820798
        if(multiLineWidth) {
            for(i = 0; i < count; i++) {
                borderSizes[i] = optsIn.line.width[i] / 2;
            }
        } else {
            s = optsIn.line.width / 2;
            for(i = 0; i < count; i++) {
                borderSizes[i] = s;
            }
        }

        optsOut.sizeAvg = sizeAvg;
    } else {
        optsOut.size = markerSizeFunc(optsIn && optsIn.size || 10);
        optsOut.borderSizes = markerSizeFunc(optsIn.line.width);
    }

    return optsOut;
}

function convertMarkerSelection(trace, target) {
    var optsIn = trace.marker;
    var optsOut = {};

    if(!target) return optsOut;

    if(target.marker && target.marker.symbol) {
        optsOut = convertMarkerStyle(Lib.extendFlat({}, optsIn, target.marker));
    } else if(target.marker) {
        if(target.marker.size) optsOut.size = target.marker.size / 2;
        if(target.marker.color) optsOut.colors = target.marker.color;
        if(target.marker.opacity !== undefined) optsOut.opacity = target.marker.opacity;
    }

    return optsOut;
}

function convertTextSelection(trace, target) {
    var optsOut = {};

    if(!target) return optsOut;

    if(target.textfont) {
        var optsIn = {
            opacity: 1,
            text: trace.text,
            textposition: trace.textposition,
            textfont: Lib.extendFlat({}, trace.textfont)
        };
        if(target.textfont) {
            Lib.extendFlat(optsIn.textfont, target.textfont);
        }
        optsOut = convertTextStyle(optsIn);
    }

    return optsOut;
}

function convertErrorBarStyle(trace, target) {
    var optsOut = {
        capSize: target.width * 2,
        lineWidth: target.thickness,
        color: target.color
    };

    if(target.copy_ystyle) {
        optsOut = trace.error_y;
    }

    return optsOut;
}

var SYMBOL_SDF_SIZE = constants.SYMBOL_SDF_SIZE;
var SYMBOL_SIZE = constants.SYMBOL_SIZE;
var SYMBOL_STROKE = constants.SYMBOL_STROKE;
var SYMBOL_SDF = {};
var SYMBOL_SVG_CIRCLE = Drawing.symbolFuncs[0](SYMBOL_SIZE * 0.05);

function getSymbolSdf(symbol) {
    if(symbol === 'circle') return null;

    var symbolPath, symbolSdf;
    var symbolNumber = Drawing.symbolNumber(symbol);
    var symbolFunc = Drawing.symbolFuncs[symbolNumber % 100];
    var symbolNoDot = !!Drawing.symbolNoDot[symbolNumber % 100];
    var symbolNoFill = !!Drawing.symbolNoFill[symbolNumber % 100];

    var isDot = constants.DOT_RE.test(symbol);

    // get symbol sdf from cache or generate it
    if(SYMBOL_SDF[symbol]) return SYMBOL_SDF[symbol];

    if(isDot && !symbolNoDot) {
        symbolPath = symbolFunc(SYMBOL_SIZE * 1.1) + SYMBOL_SVG_CIRCLE;
    } else {
        symbolPath = symbolFunc(SYMBOL_SIZE);
    }

    symbolSdf = svgSdf(symbolPath, {
        w: SYMBOL_SDF_SIZE,
        h: SYMBOL_SDF_SIZE,
        viewBox: [-SYMBOL_SIZE, -SYMBOL_SIZE, SYMBOL_SIZE, SYMBOL_SIZE],
        stroke: symbolNoFill ? SYMBOL_STROKE : -SYMBOL_STROKE
    });
    SYMBOL_SDF[symbol] = symbolSdf;

    return symbolSdf || null;
}

function convertLinePositions(gd, trace, positions) {
    var len = positions.length;
    var count = len / 2;
    var linePositions;
    var i;

    if(subTypes.hasLines(trace) && count) {
        if(trace.line.shape === 'hv') {
            linePositions = [];
            for(i = 0; i < count - 1; i++) {
                if(isNaN(positions[i * 2]) || isNaN(positions[i * 2 + 1])) {
                    linePositions.push(NaN, NaN, NaN, NaN);
                } else {
                    linePositions.push(positions[i * 2], positions[i * 2 + 1]);
                    if(!isNaN(positions[i * 2 + 2]) && !isNaN(positions[i * 2 + 3])) {
                        linePositions.push(positions[i * 2 + 2], positions[i * 2 + 1]);
                    } else {
                        linePositions.push(NaN, NaN);
                    }
                }
            }
            linePositions.push(positions[len - 2], positions[len - 1]);
        } else if(trace.line.shape === 'hvh') {
            linePositions = [];
            for(i = 0; i < count - 1; i++) {
                if(isNaN(positions[i * 2]) || isNaN(positions[i * 2 + 1]) || isNaN(positions[i * 2 + 2]) || isNaN(positions[i * 2 + 3])) {
                    if(!isNaN(positions[i * 2]) && !isNaN(positions[i * 2 + 1])) {
                        linePositions.push(positions[i * 2], positions[i * 2 + 1]);
                    } else {
                        linePositions.push(NaN, NaN);
                    }
                    linePositions.push(NaN, NaN);
                } else {
                    var midPtX = (positions[i * 2] + positions[i * 2 + 2]) / 2;
                    linePositions.push(
                        positions[i * 2],
                        positions[i * 2 + 1],
                        midPtX,
                        positions[i * 2 + 1],
                        midPtX,
                        positions[i * 2 + 3]
                    );
                }
            }
            linePositions.push(positions[len - 2], positions[len - 1]);
        } else if(trace.line.shape === 'vhv') {
            linePositions = [];
            for(i = 0; i < count - 1; i++) {
                if(isNaN(positions[i * 2]) || isNaN(positions[i * 2 + 1]) || isNaN(positions[i * 2 + 2]) || isNaN(positions[i * 2 + 3])) {
                    if(!isNaN(positions[i * 2]) && !isNaN(positions[i * 2 + 1])) {
                        linePositions.push(positions[i * 2], positions[i * 2 + 1]);
                    } else {
                        linePositions.push(NaN, NaN);
                    }
                    linePositions.push(NaN, NaN);
                } else {
                    var midPtY = (positions[i * 2 + 1] + positions[i * 2 + 3]) / 2;
                    linePositions.push(
                        positions[i * 2],
                        positions[i * 2 + 1],
                        positions[i * 2],
                        midPtY,
                        positions[i * 2 + 2],
                        midPtY
                    );
                }
            }
            linePositions.push(positions[len - 2], positions[len - 1]);
        } else if(trace.line.shape === 'vh') {
            linePositions = [];
            for(i = 0; i < count - 1; i++) {
                if(isNaN(positions[i * 2]) || isNaN(positions[i * 2 + 1])) {
                    linePositions.push(NaN, NaN, NaN, NaN);
                } else {
                    linePositions.push(positions[i * 2], positions[i * 2 + 1]);
                    if(!isNaN(positions[i * 2 + 2]) && !isNaN(positions[i * 2 + 3])) {
                        linePositions.push(positions[i * 2], positions[i * 2 + 3]);
                    } else {
                        linePositions.push(NaN, NaN);
                    }
                }
            }
            linePositions.push(positions[len - 2], positions[len - 1]);
        } else {
            linePositions = positions;
        }
    }

    // If we have data with gaps, we ought to use rect joins
    // FIXME: get rid of this
    var hasNaN = false;
    for(i = 0; i < linePositions.length; i++) {
        if(isNaN(linePositions[i])) {
            hasNaN = true;
            break;
        }
    }

    var join = (hasNaN || linePositions.length > constants.TOO_MANY_POINTS) ? 'rect' :
        subTypes.hasMarkers(trace) ? 'rect' : 'round';

    // fill gaps
    if(hasNaN && trace.connectgaps) {
        var lastX = linePositions[0];
        var lastY = linePositions[1];

        for(i = 0; i < linePositions.length; i += 2) {
            if(isNaN(linePositions[i]) || isNaN(linePositions[i + 1])) {
                linePositions[i] = lastX;
                linePositions[i + 1] = lastY;
            } else {
                lastX = linePositions[i];
                lastY = linePositions[i + 1];
            }
        }
    }

    return {
        join: join,
        positions: linePositions
    };
}

function convertErrorBarPositions(gd, trace, positions, x, y) {
    var makeComputeError = Registry.getComponentMethod('errorbars', 'makeComputeError');
    var xa = AxisIDs.getFromId(gd, trace.xaxis);
    var ya = AxisIDs.getFromId(gd, trace.yaxis);
    var count = positions.length / 2;
    var out = {};

    function convertOneAxis(coords, ax) {
        var axLetter = ax._id.charAt(0);
        var opts = trace['error_' + axLetter];

        if(opts && opts.visible && (ax.type === 'linear' || ax.type === 'log')) {
            var computeError = makeComputeError(opts);
            var pOffset = {x: 0, y: 1}[axLetter];
            var eOffset = {x: [0, 1, 2, 3], y: [2, 3, 0, 1]}[axLetter];
            var errors = new Float64Array(4 * count);
            var minShoe = Infinity;
            var maxHat = -Infinity;

            for(var i = 0, j = 0; i < count; i++, j += 4) {
                var dc = coords[i];

                if(isNumeric(dc)) {
                    var dl = positions[i * 2 + pOffset];
                    var vals = computeError(dc, i);
                    var lv = vals[0];
                    var hv = vals[1];

                    if(isNumeric(lv) && isNumeric(hv)) {
                        var shoe = dc - lv;
                        var hat = dc + hv;

                        errors[j + eOffset[0]] = dl - ax.c2l(shoe);
                        errors[j + eOffset[1]] = ax.c2l(hat) - dl;
                        errors[j + eOffset[2]] = 0;
                        errors[j + eOffset[3]] = 0;

                        minShoe = Math.min(minShoe, dc - lv);
                        maxHat = Math.max(maxHat, dc + hv);
                    }
                }
            }

            out[axLetter] = {
                positions: positions,
                errors: errors,
                _bnds: [minShoe, maxHat]
            };
        }
    }

    convertOneAxis(x, xa);
    convertOneAxis(y, ya);
    return out;
}

function convertTextPosition(gd, trace, textOpts, markerOpts) {
    var count = trace._length;
    var out = {};
    var i;

    // corresponds to textPointPosition from component.drawing
    if(subTypes.hasMarkers(trace)) {
        var fontOpts = textOpts.font;
        var align = textOpts.align;
        var baseline = textOpts.baseline;
        out.offset = new Array(count);

        for(i = 0; i < count; i++) {
            var ms = markerOpts.sizes ? markerOpts.sizes[i] : markerOpts.size;
            var fs = Array.isArray(fontOpts) ? fontOpts[i].size : fontOpts.size;

            var a = Array.isArray(align) ?
                (align.length > 1 ? align[i] : align[0]) :
                align;
            var b = Array.isArray(baseline) ?
                (baseline.length > 1 ? baseline[i] : baseline[0]) :
                baseline;

            var hSign = TEXTOFFSETSIGN[a];
            var vSign = TEXTOFFSETSIGN[b];
            var xPad = ms ? ms / 0.8 + 1 : 0;
            var yPad = -vSign * xPad - vSign * 0.5;
            out.offset[i] = [hSign * xPad / fs, yPad / fs];
        }
    }

    return out;
}

module.exports = {
    style: convertStyle,

    markerStyle: convertMarkerStyle,
    markerSelection: convertMarkerSelection,

    linePositions: convertLinePositions,
    errorBarPositions: convertErrorBarPositions,
    textPosition: convertTextPosition
};
