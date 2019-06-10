/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var c = require('./constants');
var d3 = require('d3');
var keyFun = require('../../lib/gup').keyFun;
var repeat = require('../../lib/gup').repeat;
var sortAsc = require('../../lib').sorterAsc;

var snapRatio = c.bar.snapRatio;
function snapOvershoot(v, vAdjacent) { return v * (1 - snapRatio) + vAdjacent * snapRatio; }

var snapClose = c.bar.snapClose;
function closeToCovering(v, vAdjacent) { return v * (1 - snapClose) + vAdjacent * snapClose; }

// snap for the low end of a range on an ordinal scale
// on an ordinal scale, always show some overshoot from the exact value,
// so it's clear we're covering it
// find the interval we're in, and snap to 1/4 the distance to the next
// these two could be unified at a slight loss of readability / perf
function ordinalScaleSnap(isHigh, a, v, existingRanges) {
    if(overlappingExisting(v, existingRanges)) return v;

    var dir = isHigh ? -1 : 1;

    var first = 0;
    var last = a.length - 1;
    if(dir < 0) {
        var tmp = first;
        first = last;
        last = tmp;
    }

    var aHere = a[first];
    var aPrev = aHere;
    for(var i = first; dir * i < dir * last; i += dir) {
        var nextI = i + dir;
        var aNext = a[nextI];

        // very close to the previous - snap down to it
        if(dir * v < dir * closeToCovering(aHere, aNext)) return snapOvershoot(aHere, aPrev);
        if(dir * v < dir * aNext || nextI === last) return snapOvershoot(aNext, aHere);

        aPrev = aHere;
        aHere = aNext;
    }
}

function overlappingExisting(v, existingRanges) {
    for(var i = 0; i < existingRanges.length; i++) {
        if(v >= existingRanges[i][0] && v <= existingRanges[i][1]) return true;
    }
    return false;
}

function barHorizontalSetup(selection) {
    selection
        .attr('x', -c.bar.captureWidth / 2)
        .attr('width', c.bar.captureWidth);
}

function backgroundBarHorizontalSetup(selection) {
    selection
        .attr('visibility', 'visible')
        .style('visibility', 'visible')
        .attr('fill', 'yellow')
        .attr('opacity', 0);
}

function setHighlight(d) {
    if(!d.brush.filterSpecified) {
        return '0,' + d.height;
    }
    var pixelRanges = unitToPx(d.brush.filter.getConsolidated(), d.height);
    var dashArray = [0]; // we start with a 0 length selection as filter ranges are inclusive, not exclusive
    var p, sectionHeight, iNext;
    var currentGap = pixelRanges.length ? pixelRanges[0][0] : null;
    for(var i = 0; i < pixelRanges.length; i++) {
        p = pixelRanges[i];
        sectionHeight = p[1] - p[0];
        dashArray.push(currentGap);
        dashArray.push(sectionHeight);
        iNext = i + 1;
        if(iNext < pixelRanges.length) {
            currentGap = pixelRanges[iNext][0] - p[1];
        }
    }
    dashArray.push(d.height);
    // d.height is added at the end to ensure that (1) we have an even number of dasharray points, MDN page says
    // "If an odd number of values is provided, then the list of values is repeated to yield an even number of values."
    // and (2) it's _at least_ as long as the full height (even if range is minuscule and at the bottom) though this
    // may not be necessary, maybe duplicating the last point would do too. But no harm in a longer dasharray than line.
    return dashArray;
}

function unitToPx(unitRanges, height) {
    return unitRanges.map(function(pr) {
        return pr.map(function(v) { return v * height; }).sort(sortAsc);
    });
}

// is the cursor over the north, middle, or south of a bar?
// the end handles extend over the last 10% of the bar
function getRegion(fPix, y) {
    var pad = c.bar.handleHeight;
    if(y > fPix[1] + pad || y < fPix[0] - pad) return;
    if(y >= 0.9 * fPix[1] + 0.1 * fPix[0]) return 'n';
    if(y <= 0.9 * fPix[0] + 0.1 * fPix[1]) return 's';
    return 'ns';
}

function clearCursor() {
    d3.select(document.body)
        .style('cursor', null);
}

function styleHighlight(selection) {
    // stroke-dasharray is used to minimize the number of created DOM nodes, because the requirement calls for up to
    // 1000 individual selections on an axis, and there can be 60 axes per parcoords, and multiple parcoords per
    // dashboard. The technique is similar to https://codepen.io/monfera/pen/rLYqWR and using a `polyline` with
    // multiple sections, or a `path` element via its `d` attribute would also be DOM-sparing alternatives.
    selection.attr('stroke-dasharray', setHighlight);
}

function renderHighlight(root, tweenCallback) {
    var bar = d3.select(root).selectAll('.highlight, .highlight-shadow');
    var barToStyle = tweenCallback ? bar.transition().duration(c.bar.snapDuration).each('end', tweenCallback) : bar;
    styleHighlight(barToStyle);
}

function getInterval(d, y) {
    var b = d.brush;
    var active = b.filterSpecified;
    var closestInterval = NaN;
    var out = {};
    var i;

    if(active) {
        var height = d.height;
        var intervals = b.filter.getConsolidated();
        var pixIntervals = unitToPx(intervals, height);
        var hoveredInterval = NaN;
        var previousInterval = NaN;
        var nextInterval = NaN;
        for(i = 0; i <= pixIntervals.length; i++) {
            var p = pixIntervals[i];
            if(p && p[0] <= y && y <= p[1]) {
                // over a bar
                hoveredInterval = i;
                break;
            } else {
                // between bars, or before/after the first/last bar
                previousInterval = i ? i - 1 : NaN;
                if(p && p[0] > y) {
                    nextInterval = i;
                    break; // no point continuing as intervals are non-overlapping and sorted; could use log search
                }
            }
        }

        closestInterval = hoveredInterval;
        if(isNaN(closestInterval)) {
            if(isNaN(previousInterval) || isNaN(nextInterval)) {
                closestInterval = isNaN(previousInterval) ? nextInterval : previousInterval;
            } else {
                closestInterval = (y - pixIntervals[previousInterval][1] < pixIntervals[nextInterval][0] - y) ?
                    previousInterval : nextInterval;
            }
        }

        if(!isNaN(closestInterval)) {
            var fPix = pixIntervals[closestInterval];
            var region = getRegion(fPix, y);

            if(region) {
                out.interval = intervals[closestInterval];
                out.intervalPix = fPix;
                out.region = region;
            }
        }
    }

    if(d.ordinal && !out.region) {
        var a = d.unitTickvals;
        var unitLocation = d.unitToPaddedPx.invert(y);
        for(i = 0; i < a.length; i++) {
            var rangei = [
                a[Math.max(i - 1, 0)] * 0.25 + a[i] * 0.75,
                a[Math.min(i + 1, a.length - 1)] * 0.25 + a[i] * 0.75
            ];
            if(unitLocation >= rangei[0] && unitLocation <= rangei[1]) {
                out.clickableOrdinalRange = rangei;
                break;
            }
        }
    }

    return out;
}

function attachDragBehavior(selection) {
    // There's some fiddling with pointer cursor styling so that the cursor preserves its shape while dragging a brush
    // even if the cursor strays from the interacting bar, which is bound to happen as bars are thin and the user
    // will inevitably leave the hotspot strip. In this regard, it does something similar to what the D3 brush would do.
    selection
        .on('mousemove', function(d) {
            d3.event.preventDefault();
            if(!d.parent.inBrushDrag) {
                var y = d.height - d3.mouse(this)[1] - 2 * c.verticalPadding;
                var interval = getInterval(d, y);

                var cursor = 'crosshair';
                if(interval.clickableOrdinalRange) cursor = 'pointer';
                else if(interval.region) cursor = interval.region + '-resize';
                d3.select(document.body)
                    .style('cursor', cursor);
            }
        })
        .on('mouseleave', function(d) {
            if(!d.parent.inBrushDrag) clearCursor();
        })
        .call(d3.behavior.drag()
            .on('dragstart', function(d) {
                d3.event.sourceEvent.stopPropagation();
                var y = d.height - d3.mouse(this)[1] - 2 * c.verticalPadding;
                var unitLocation = d.unitToPaddedPx.invert(y);
                var b = d.brush;
                var interval = getInterval(d, y);
                var unitRange = interval.interval;
                var s = b.svgBrush;
                s.wasDragged = false; // we start assuming there won't be a drag - useful for reset
                s.grabbingBar = interval.region === 'ns';
                if(s.grabbingBar) {
                    var pixelRange = unitRange.map(d.unitToPaddedPx);
                    s.grabPoint = y - pixelRange[0] - c.verticalPadding;
                    s.barLength = pixelRange[1] - pixelRange[0];
                }
                s.clickableOrdinalRange = interval.clickableOrdinalRange;
                s.stayingIntervals = (d.multiselect && b.filterSpecified) ? b.filter.getConsolidated() : [];
                if(unitRange) {
                    s.stayingIntervals = s.stayingIntervals.filter(function(int2) {
                        return int2[0] !== unitRange[0] && int2[1] !== unitRange[1];
                    });
                }
                s.startExtent = interval.region ? unitRange[interval.region === 's' ? 1 : 0] : unitLocation;
                d.parent.inBrushDrag = true;
                s.brushStartCallback();
            })
            .on('drag', function(d) {
                d3.event.sourceEvent.stopPropagation();
                var y = d.height - d3.mouse(this)[1] - 2 * c.verticalPadding;
                var s = d.brush.svgBrush;
                s.wasDragged = true;

                if(s.grabbingBar) { // moving the bar
                    s.newExtent = [y - s.grabPoint, y + s.barLength - s.grabPoint].map(d.unitToPaddedPx.invert);
                } else { // south/north drag or new bar creation
                    s.newExtent = [s.startExtent, d.unitToPaddedPx.invert(y)].sort(sortAsc);
                }

                // take care of the parcoords axis height constraint: bar can't breach it
                var bottomViolation = Math.max(0, -s.newExtent[0]);
                var topViolation = Math.max(0, s.newExtent[1] - 1);
                s.newExtent[0] += bottomViolation;
                s.newExtent[1] -= topViolation;
                if(s.grabbingBar) {
                    // in case of bar dragging (non-resizing interaction, unlike north/south resize or new bar creation)
                    // the constraint adjustment must apply to the other end of the bar as well, otherwise it'd
                    // shorten or lengthen
                    s.newExtent[1] += bottomViolation;
                    s.newExtent[0] -= topViolation;
                }

                d.brush.filterSpecified = true;
                s.extent = s.stayingIntervals.concat([s.newExtent]);
                s.brushCallback(d);
                renderHighlight(this.parentNode);
            })
            .on('dragend', function(d) {
                var e = d3.event;
                e.sourceEvent.stopPropagation();
                var brush = d.brush;
                var filter = brush.filter;
                var s = brush.svgBrush;
                var grabbingBar = s.grabbingBar;
                s.grabbingBar = false;
                s.grabLocation = undefined;
                d.parent.inBrushDrag = false;
                clearCursor(); // instead of clearing, a nicer thing would be to set it according to current location
                if(!s.wasDragged) { // a click+release on the same spot (ie. w/o dragging) means a bar or full reset
                    s.wasDragged = undefined; // logic-wise unneeded, just shows `wasDragged` has no longer a meaning
                    if(s.clickableOrdinalRange) {
                        if(brush.filterSpecified && d.multiselect) {
                            s.extent.push(s.clickableOrdinalRange);
                        } else {
                            s.extent = [s.clickableOrdinalRange];
                            brush.filterSpecified = true;
                        }
                    } else if(grabbingBar) {
                        s.extent = s.stayingIntervals;
                        if(s.extent.length === 0) {
                            brushClear(brush);
                        }
                    } else {
                        brushClear(brush);
                    }
                    s.brushCallback(d);
                    renderHighlight(this.parentNode);
                    s.brushEndCallback(brush.filterSpecified ? filter.getConsolidated() : []);
                    return; // no need to fuse intervals or snap to ordinals, so we can bail early
                }

                var mergeIntervals = function() {
                    // Key piece of logic: once the button is released, possibly overlapping intervals will be fused:
                    // Here it's done immediately on click release while on ordinal snap transition it's done at the end
                    filter.set(filter.getConsolidated());
                };

                if(d.ordinal) {
                    var a = d.unitTickvals;
                    if(a[a.length - 1] < a[0]) a.reverse();
                    s.newExtent = [
                        ordinalScaleSnap(0, a, s.newExtent[0], s.stayingIntervals),
                        ordinalScaleSnap(1, a, s.newExtent[1], s.stayingIntervals)
                    ];
                    var hasNewExtent = s.newExtent[1] > s.newExtent[0];
                    s.extent = s.stayingIntervals.concat(hasNewExtent ? [s.newExtent] : []);
                    if(!s.extent.length) {
                        brushClear(brush);
                    }
                    s.brushCallback(d);
                    if(hasNewExtent) {
                        // merging intervals post the snap tween
                        renderHighlight(this.parentNode, mergeIntervals);
                    } else {
                        // if no new interval, don't animate, just redraw the highlight immediately
                        mergeIntervals();
                        renderHighlight(this.parentNode);
                    }
                } else {
                    mergeIntervals(); // merging intervals immediately
                }
                s.brushEndCallback(brush.filterSpecified ? filter.getConsolidated() : []);
            })
        );
}

function startAsc(a, b) { return a[0] - b[0]; }

function renderAxisBrush(axisBrush) {
    var background = axisBrush.selectAll('.background').data(repeat);

    background.enter()
        .append('rect')
        .classed('background', true)
        .call(barHorizontalSetup)
        .call(backgroundBarHorizontalSetup)
        .style('pointer-events', 'auto') // parent pointer events are disabled; we must have it to register events
        .attr('transform', 'translate(0 ' + c.verticalPadding + ')');

    background
        .call(attachDragBehavior)
        .attr('height', function(d) {
            return d.height - c.verticalPadding;
        });

    var highlightShadow = axisBrush.selectAll('.highlight-shadow').data(repeat); // we have a set here, can't call it `extent`

    highlightShadow.enter()
        .append('line')
        .classed('highlight-shadow', true)
        .attr('x', -c.bar.width / 2)
        .attr('stroke-width', c.bar.width + c.bar.strokeWidth)
        .attr('stroke', c.bar.strokeColor)
        .attr('opacity', c.bar.strokeOpacity)
        .attr('stroke-linecap', 'butt');

    highlightShadow
        .attr('y1', function(d) { return d.height; })
        .call(styleHighlight);

    var highlight = axisBrush.selectAll('.highlight').data(repeat); // we have a set here, can't call it `extent`

    highlight.enter()
        .append('line')
        .classed('highlight', true)
        .attr('x', -c.bar.width / 2)
        .attr('stroke-width', c.bar.width - c.bar.strokeWidth)
        .attr('stroke', c.bar.fillColor)
        .attr('opacity', c.bar.fillOpacity)
        .attr('stroke-linecap', 'butt');

    highlight
        .attr('y1', function(d) { return d.height; })
        .call(styleHighlight);
}

function ensureAxisBrush(axisOverlays) {
    var axisBrush = axisOverlays.selectAll('.' + c.cn.axisBrush)
        .data(repeat, keyFun);

    axisBrush.enter()
        .append('g')
        .classed(c.cn.axisBrush, true);

    renderAxisBrush(axisBrush);
}

function getBrushExtent(brush) {
    return brush.svgBrush.extent.map(function(e) {return e.slice();});
}

function brushClear(brush) {
    brush.filterSpecified = false;
    brush.svgBrush.extent = [[0, 1]];
}

function axisBrushMoved(callback) {
    return function axisBrushMoved(dimension) {
        var brush = dimension.brush;
        var extent = getBrushExtent(brush);
        var newExtent = extent.slice();
        brush.filter.set(newExtent);
        callback();
    };
}

function dedupeRealRanges(intervals) {
    // Fuses elements of intervals if they overlap, yielding discontiguous intervals, results.length <= intervals.length
    // Currently uses closed intervals, ie. dedupeRealRanges([[400, 800], [300, 400]]) -> [300, 800]
    var queue = intervals.slice();
    var result = [];
    var currentInterval;
    var current = queue.shift();
    while(current) { // [].shift === undefined, so we don't descend into an empty array
        currentInterval = current.slice();
        while((current = queue.shift()) && current[0] <= /* right-open interval would need `<` */ currentInterval[1]) {
            currentInterval[1] = Math.max(currentInterval[1], current[1]);
        }
        result.push(currentInterval);
    }
    return result;
}

function makeFilter() {
    var filter = [];
    var consolidated;
    var bounds;
    return {
        set: function(a) {
            filter = a
                .map(function(d) { return d.slice().sort(sortAsc); })
                .sort(startAsc);
            consolidated = dedupeRealRanges(filter);
            bounds = filter.reduce(function(p, n) {
                return [Math.min(p[0], n[0]), Math.max(p[1], n[1])];
            }, [Infinity, -Infinity]);
        },
        get: function() { return filter.slice(); },
        getConsolidated: function() { return consolidated; },
        getBounds: function() { return bounds; }
    };
}

function makeBrush(state, rangeSpecified, initialRange, brushStartCallback, brushCallback, brushEndCallback) {
    var filter = makeFilter();
    filter.set(initialRange);
    return {
        filter: filter,
        filterSpecified: rangeSpecified, // there's a difference between not filtering and filtering a non-proper subset
        svgBrush: {
            extent: [], // this is where the svgBrush writes contents into
            brushStartCallback: brushStartCallback,
            brushCallback: axisBrushMoved(brushCallback),
            brushEndCallback: brushEndCallback
        }
    };
}

// for use by supplyDefaults, but it needed tons of pieces from here so
// seemed to make more sense just to put the whole routine here
function cleanRanges(ranges, dimension) {
    if(Array.isArray(ranges[0])) {
        ranges = ranges.map(function(ri) { return ri.sort(sortAsc); });

        if(!dimension.multiselect) ranges = [ranges[0]];
        else ranges = dedupeRealRanges(ranges.sort(startAsc));
    } else ranges = [ranges.sort(sortAsc)];

    // ordinal snapping
    if(dimension.tickvals) {
        var sortedTickVals = dimension.tickvals.slice().sort(sortAsc);
        ranges = ranges.map(function(ri) {
            var rSnapped = [
                ordinalScaleSnap(0, sortedTickVals, ri[0], []),
                ordinalScaleSnap(1, sortedTickVals, ri[1], [])
            ];
            if(rSnapped[1] > rSnapped[0]) return rSnapped;
        })
        .filter(function(ri) { return ri; });

        if(!ranges.length) return;
    }
    return ranges.length > 1 ? ranges : ranges[0];
}

module.exports = {
    makeBrush: makeBrush,
    ensureAxisBrush: ensureAxisBrush,
    cleanRanges: cleanRanges
};
