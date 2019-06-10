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
var Lib = require('../../lib');
var ensureSingle = Lib.ensureSingle;
var identity = Lib.identity;
var Drawing = require('../../components/drawing');

var subTypes = require('./subtypes');
var linePoints = require('./line_points');
var linkTraces = require('./link_traces');
var polygonTester = require('../../lib/polygon').tester;

module.exports = function plot(gd, plotinfo, cdscatter, scatterLayer, transitionOpts, makeOnCompleteCallback) {
    var join, onComplete;

    // If transition config is provided, then it is only a partial replot and traces not
    // updated are removed.
    var isFullReplot = !transitionOpts;
    var hasTransition = !!transitionOpts && transitionOpts.duration > 0;

    // Link traces so the z-order of fill layers is correct
    var cdscatterSorted = linkTraces(gd, plotinfo, cdscatter);

    join = scatterLayer.selectAll('g.trace')
        .data(cdscatterSorted, function(d) { return d[0].trace.uid; });

    // Append new traces:
    join.enter().append('g')
        .attr('class', function(d) {
            return 'trace scatter trace' + d[0].trace.uid;
        })
        .style('stroke-miterlimit', 2);
    join.order();

    createFills(gd, join, plotinfo);

    if(hasTransition) {
        if(makeOnCompleteCallback) {
            // If it was passed a callback to register completion, make a callback. If
            // this is created, then it must be executed on completion, otherwise the
            // pos-transition redraw will not execute:
            onComplete = makeOnCompleteCallback();
        }

        var transition = d3.transition()
            .duration(transitionOpts.duration)
            .ease(transitionOpts.easing)
            .each('end', function() {
                onComplete && onComplete();
            })
            .each('interrupt', function() {
                onComplete && onComplete();
            });

        transition.each(function() {
            // Must run the selection again since otherwise enters/updates get grouped together
            // and these get executed out of order. Except we need them in order!
            scatterLayer.selectAll('g.trace').each(function(d, i) {
                plotOne(gd, i, plotinfo, d, cdscatterSorted, this, transitionOpts);
            });
        });
    } else {
        join.each(function(d, i) {
            plotOne(gd, i, plotinfo, d, cdscatterSorted, this, transitionOpts);
        });
    }

    if(isFullReplot) {
        join.exit().remove();
    }

    // remove paths that didn't get used
    scatterLayer.selectAll('path:not([d])').remove();
};

function createFills(gd, traceJoin, plotinfo) {
    traceJoin.each(function(d) {
        var fills = ensureSingle(d3.select(this), 'g', 'fills');
        Drawing.setClipUrl(fills, plotinfo.layerClipId, gd);

        var trace = d[0].trace;

        var fillData = [];
        if(trace._ownfill) fillData.push('_ownFill');
        if(trace._nexttrace) fillData.push('_nextFill');

        var fillJoin = fills.selectAll('g').data(fillData, identity);

        fillJoin.enter().append('g');

        fillJoin.exit()
            .each(function(d) { trace[d] = null; })
            .remove();

        fillJoin.order().each(function(d) {
            // make a path element inside the fill group, just so
            // we can give it its own data later on and the group can
            // keep its simple '_*Fill' data
            trace[d] = ensureSingle(d3.select(this), 'path', 'js-fill');
        });
    });
}

function plotOne(gd, idx, plotinfo, cdscatter, cdscatterAll, element, transitionOpts) {
    var i;

    // Since this has been reorganized and we're executing this on individual traces,
    // we need to pass it the full list of cdscatter as well as this trace's index (idx)
    // since it does an internal n^2 loop over comparisons with other traces:
    selectMarkers(gd, idx, plotinfo, cdscatter, cdscatterAll);

    var hasTransition = !!transitionOpts && transitionOpts.duration > 0;

    function transition(selection) {
        return hasTransition ? selection.transition() : selection;
    }

    var xa = plotinfo.xaxis;
    var ya = plotinfo.yaxis;

    var trace = cdscatter[0].trace;
    var line = trace.line;
    var tr = d3.select(element);

    var errorBarGroup = ensureSingle(tr, 'g', 'errorbars');
    var lines = ensureSingle(tr, 'g', 'lines');
    var points = ensureSingle(tr, 'g', 'points');
    var text = ensureSingle(tr, 'g', 'text');

    // error bars are at the bottom
    Registry.getComponentMethod('errorbars', 'plot')(gd, errorBarGroup, plotinfo, transitionOpts);

    if(trace.visible !== true) return;

    transition(tr).style('opacity', trace.opacity);

    // BUILD LINES AND FILLS
    var ownFillEl3, tonext;
    var ownFillDir = trace.fill.charAt(trace.fill.length - 1);
    if(ownFillDir !== 'x' && ownFillDir !== 'y') ownFillDir = '';

    // store node for tweaking by selectPoints
    if(!plotinfo.isRangePlot) cdscatter[0].node3 = tr;

    var prevRevpath = '';
    var prevPolygons = [];
    var prevtrace = trace._prevtrace;

    if(prevtrace) {
        prevRevpath = prevtrace._prevRevpath || '';
        tonext = prevtrace._nextFill;
        prevPolygons = prevtrace._polygons;
    }

    var thispath;
    var thisrevpath;
    // fullpath is all paths for this curve, joined together straight
    // across gaps, for filling
    var fullpath = '';
    // revpath is fullpath reversed, for fill-to-next
    var revpath = '';
    // functions for converting a point array to a path
    var pathfn, revpathbase, revpathfn;
    // variables used before and after the data join
    var pt0, lastSegment, pt1, thisPolygons;

    // initialize line join data / method
    var segments = [];
    var makeUpdate = Lib.noop;

    ownFillEl3 = trace._ownFill;

    if(subTypes.hasLines(trace) || trace.fill !== 'none') {
        if(tonext) {
            // This tells .style which trace to use for fill information:
            tonext.datum(cdscatter);
        }

        if(['hv', 'vh', 'hvh', 'vhv'].indexOf(line.shape) !== -1) {
            pathfn = Drawing.steps(line.shape);
            revpathbase = Drawing.steps(
                line.shape.split('').reverse().join('')
            );
        } else if(line.shape === 'spline') {
            pathfn = revpathbase = function(pts) {
                var pLast = pts[pts.length - 1];
                if(pts.length > 1 && pts[0][0] === pLast[0] && pts[0][1] === pLast[1]) {
                    // identical start and end points: treat it as a
                    // closed curve so we don't get a kink
                    return Drawing.smoothclosed(pts.slice(1), line.smoothing);
                } else {
                    return Drawing.smoothopen(pts, line.smoothing);
                }
            };
        } else {
            pathfn = revpathbase = function(pts) {
                return 'M' + pts.join('L');
            };
        }

        revpathfn = function(pts) {
            // note: this is destructive (reverses pts in place) so can't use pts after this
            return revpathbase(pts.reverse());
        };

        segments = linePoints(cdscatter, {
            xaxis: xa,
            yaxis: ya,
            connectGaps: trace.connectgaps,
            baseTolerance: Math.max(line.width || 1, 3) / 4,
            shape: line.shape,
            simplify: line.simplify,
            fill: trace.fill
        });

        // since we already have the pixel segments here, use them to make
        // polygons for hover on fill
        // TODO: can we skip this if hoveron!=fills? That would mean we
        // need to redraw when you change hoveron...
        thisPolygons = trace._polygons = new Array(segments.length);
        for(i = 0; i < segments.length; i++) {
            trace._polygons[i] = polygonTester(segments[i]);
        }

        if(segments.length) {
            pt0 = segments[0][0];
            lastSegment = segments[segments.length - 1];
            pt1 = lastSegment[lastSegment.length - 1];
        }

        makeUpdate = function(isEnter) {
            return function(pts) {
                thispath = pathfn(pts);
                thisrevpath = revpathfn(pts);
                if(!fullpath) {
                    fullpath = thispath;
                    revpath = thisrevpath;
                } else if(ownFillDir) {
                    fullpath += 'L' + thispath.substr(1);
                    revpath = thisrevpath + ('L' + revpath.substr(1));
                } else {
                    fullpath += 'Z' + thispath;
                    revpath = thisrevpath + 'Z' + revpath;
                }

                if(subTypes.hasLines(trace) && pts.length > 1) {
                    var el = d3.select(this);

                    // This makes the coloring work correctly:
                    el.datum(cdscatter);

                    if(isEnter) {
                        transition(el.style('opacity', 0)
                            .attr('d', thispath)
                            .call(Drawing.lineGroupStyle))
                                .style('opacity', 1);
                    } else {
                        var sel = transition(el);
                        sel.attr('d', thispath);
                        Drawing.singleLineStyle(cdscatter, sel);
                    }
                }
            };
        };
    }

    var lineJoin = lines.selectAll('.js-line').data(segments);

    transition(lineJoin.exit())
        .style('opacity', 0)
        .remove();

    lineJoin.each(makeUpdate(false));

    lineJoin.enter().append('path')
        .classed('js-line', true)
        .style('vector-effect', 'non-scaling-stroke')
        .call(Drawing.lineGroupStyle)
        .each(makeUpdate(true));

    Drawing.setClipUrl(lineJoin, plotinfo.layerClipId, gd);

    function clearFill(selection) {
        transition(selection).attr('d', 'M0,0Z');
    }

    if(segments.length) {
        if(ownFillEl3) {
            ownFillEl3.datum(cdscatter);
            if(pt0 && pt1) {
                if(ownFillDir) {
                    if(ownFillDir === 'y') {
                        pt0[1] = pt1[1] = ya.c2p(0, true);
                    } else if(ownFillDir === 'x') {
                        pt0[0] = pt1[0] = xa.c2p(0, true);
                    }

                    // fill to zero: full trace path, plus extension of
                    // the endpoints to the appropriate axis
                    // For the sake of animations, wrap the points around so that
                    // the points on the axes are the first two points. Otherwise
                    // animations get a little crazy if the number of points changes.
                    transition(ownFillEl3).attr('d', 'M' + pt1 + 'L' + pt0 + 'L' + fullpath.substr(1))
                        .call(Drawing.singleFillStyle);
                } else {
                    // fill to self: just join the path to itself
                    transition(ownFillEl3).attr('d', fullpath + 'Z')
                        .call(Drawing.singleFillStyle);
                }
            }
        } else if(tonext) {
            if(trace.fill.substr(0, 6) === 'tonext' && fullpath && prevRevpath) {
                // fill to next: full trace path, plus the previous path reversed
                if(trace.fill === 'tonext') {
                    // tonext: for use by concentric shapes, like manually constructed
                    // contours, we just add the two paths closed on themselves.
                    // This makes strange results if one path is *not* entirely
                    // inside the other, but then that is a strange usage.
                    transition(tonext).attr('d', fullpath + 'Z' + prevRevpath + 'Z')
                        .call(Drawing.singleFillStyle);
                } else {
                    // tonextx/y: for now just connect endpoints with lines. This is
                    // the correct behavior if the endpoints are at the same value of
                    // y/x, but if they *aren't*, we should ideally do more complicated
                    // things depending on whether the new endpoint projects onto the
                    // existing curve or off the end of it
                    transition(tonext).attr('d', fullpath + 'L' + prevRevpath.substr(1) + 'Z')
                        .call(Drawing.singleFillStyle);
                }
                trace._polygons = trace._polygons.concat(prevPolygons);
            } else {
                clearFill(tonext);
                trace._polygons = null;
            }
        }
        trace._prevRevpath = revpath;
        trace._prevPolygons = thisPolygons;
    } else {
        if(ownFillEl3) clearFill(ownFillEl3);
        else if(tonext) clearFill(tonext);
        trace._polygons = trace._prevRevpath = trace._prevPolygons = null;
    }


    function visFilter(d) {
        return d.filter(function(v) { return !v.gap && v.vis; });
    }

    function visFilterWithGaps(d) {
        return d.filter(function(v) { return v.vis; });
    }

    function gapFilter(d) {
        return d.filter(function(v) { return !v.gap; });
    }

    function keyFunc(d) {
        return d.id;
    }

    // Returns a function if the trace is keyed, otherwise returns undefined
    function getKeyFunc(trace) {
        if(trace.ids) {
            return keyFunc;
        }
    }

    function hideFilter() {
        return false;
    }

    function makePoints(points, text, cdscatter) {
        var join, selection, hasNode;

        var trace = cdscatter[0].trace;
        var showMarkers = subTypes.hasMarkers(trace);
        var showText = subTypes.hasText(trace);

        var keyFunc = getKeyFunc(trace);
        var markerFilter = hideFilter;
        var textFilter = hideFilter;

        if(showMarkers || showText) {
            var showFilter = identity;
            // if we're stacking, "infer zero" gap mode gets markers in the
            // gap points - because we've inferred a zero there - but other
            // modes (currently "interpolate", later "interrupt" hopefully)
            // we don't draw generated markers
            var stackGroup = trace.stackgroup;
            var isInferZero = stackGroup && (
                gd._fullLayout._scatterStackOpts[xa._id + ya._id][stackGroup].stackgaps === 'infer zero');
            if(trace.marker.maxdisplayed || trace._needsCull) {
                showFilter = isInferZero ? visFilterWithGaps : visFilter;
            } else if(stackGroup && !isInferZero) {
                showFilter = gapFilter;
            }

            if(showMarkers) markerFilter = showFilter;
            if(showText) textFilter = showFilter;
        }

        // marker points

        selection = points.selectAll('path.point');

        join = selection.data(markerFilter, keyFunc);

        var enter = join.enter().append('path')
            .classed('point', true);

        if(hasTransition) {
            enter
                .call(Drawing.pointStyle, trace, gd)
                .call(Drawing.translatePoints, xa, ya)
                .style('opacity', 0)
                .transition()
                .style('opacity', 1);
        }

        join.order();

        var styleFns;
        if(showMarkers) {
            styleFns = Drawing.makePointStyleFns(trace);
        }

        join.each(function(d) {
            var el = d3.select(this);
            var sel = transition(el);
            hasNode = Drawing.translatePoint(d, sel, xa, ya);

            if(hasNode) {
                Drawing.singlePointStyle(d, sel, trace, styleFns, gd);

                if(plotinfo.layerClipId) {
                    Drawing.hideOutsideRangePoint(d, sel, xa, ya, trace.xcalendar, trace.ycalendar);
                }

                if(trace.customdata) {
                    el.classed('plotly-customdata', d.data !== null && d.data !== undefined);
                }
            } else {
                sel.remove();
            }
        });

        if(hasTransition) {
            join.exit().transition()
                .style('opacity', 0)
                .remove();
        } else {
            join.exit().remove();
        }

        // text points
        selection = text.selectAll('g');
        join = selection.data(textFilter, keyFunc);

        // each text needs to go in its own 'g' in case
        // it gets converted to mathjax
        join.enter().append('g').classed('textpoint', true).append('text');

        join.order();

        join.each(function(d) {
            var g = d3.select(this);
            var sel = transition(g.select('text'));
            hasNode = Drawing.translatePoint(d, sel, xa, ya);

            if(hasNode) {
                if(plotinfo.layerClipId) {
                    Drawing.hideOutsideRangePoint(d, g, xa, ya, trace.xcalendar, trace.ycalendar);
                }
            } else {
                g.remove();
            }
        });

        join.selectAll('text')
            .call(Drawing.textPointStyle, trace, gd)
            .each(function(d) {
                // This just *has* to be totally custom becuase of SVG text positioning :(
                // It's obviously copied from translatePoint; we just can't use that
                var x = xa.c2p(d.x);
                var y = ya.c2p(d.y);

                d3.select(this).selectAll('tspan.line').each(function() {
                    transition(d3.select(this)).attr({x: x, y: y});
                });
            });

        join.exit().remove();
    }

    points.datum(cdscatter);
    text.datum(cdscatter);
    makePoints(points, text, cdscatter);

    // lastly, clip points groups of `cliponaxis !== false` traces
    // on `plotinfo._hasClipOnAxisFalse === true` subplots
    var hasClipOnAxisFalse = trace.cliponaxis === false;
    var clipUrl = hasClipOnAxisFalse ? null : plotinfo.layerClipId;
    Drawing.setClipUrl(points, clipUrl, gd);
    Drawing.setClipUrl(text, clipUrl, gd);
}

function selectMarkers(gd, idx, plotinfo, cdscatter, cdscatterAll) {
    var xa = plotinfo.xaxis;
    var ya = plotinfo.yaxis;
    var xr = d3.extent(Lib.simpleMap(xa.range, xa.r2c));
    var yr = d3.extent(Lib.simpleMap(ya.range, ya.r2c));

    var trace = cdscatter[0].trace;
    if(!subTypes.hasMarkers(trace)) return;
    // if marker.maxdisplayed is used, select a maximum of
    // mnum markers to show, from the set that are in the viewport
    var mnum = trace.marker.maxdisplayed;

    // TODO: remove some as we get away from the viewport?
    if(mnum === 0) return;

    var cd = cdscatter.filter(function(v) {
        return v.x >= xr[0] && v.x <= xr[1] && v.y >= yr[0] && v.y <= yr[1];
    });
    var inc = Math.ceil(cd.length / mnum);
    var tnum = 0;
    cdscatterAll.forEach(function(cdj, j) {
        var tracei = cdj[0].trace;
        if(subTypes.hasMarkers(tracei) &&
                tracei.marker.maxdisplayed > 0 && j < idx) {
            tnum++;
        }
    });

    // if multiple traces use maxdisplayed, stagger which markers we
    // display this formula offsets successive traces by 1/3 of the
    // increment, adding an extra small amount after each triplet so
    // it's not quite periodic
    var i0 = Math.round(tnum * inc / 3 + Math.floor(tnum / 3) * inc / 7.1);

    // for error bars: save in cd which markers to show
    // so we don't have to repeat this
    cdscatter.forEach(function(v) { delete v.vis; });
    cd.forEach(function(v, i) {
        if(Math.round((i + i0) % inc) === 0) v.vis = true;
    });
}
