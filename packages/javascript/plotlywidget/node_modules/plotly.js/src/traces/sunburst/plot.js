/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var d3 = require('d3');
var d3Hierarchy = require('d3-hierarchy');

var Registry = require('../../registry');
var Fx = require('../../components/fx');
var Color = require('../../components/color');
var Drawing = require('../../components/drawing');
var Lib = require('../../lib');
var Events = require('../../lib/events');
var svgTextUtils = require('../../lib/svg_text_utils');
var setCursor = require('../../lib/setcursor');
var appendArrayPointValue = require('../../components/fx/helpers').appendArrayPointValue;

var transformInsideText = require('../pie/plot').transformInsideText;
var formatPieValue = require('../pie/helpers').formatPieValue;
var styleOne = require('./style').styleOne;

var constants = require('./constants');

module.exports = function(gd, cdmodule, transitionOpts, makeOnCompleteCallback) {
    var fullLayout = gd._fullLayout;
    var layer = fullLayout._sunburstlayer;
    var join, onComplete;

    // If transition config is provided, then it is only a partial replot and traces not
    // updated are removed.
    var isFullReplot = !transitionOpts;
    var hasTransition = transitionOpts && transitionOpts.duration > 0;

    join = layer.selectAll('g.trace.sunburst')
        .data(cdmodule, function(cd) { return cd[0].trace.uid; });

    // using same 'stroke-linejoin' as pie traces
    join.enter().append('g')
        .classed('trace', true)
        .classed('sunburst', true)
        .attr('stroke-linejoin', 'round');

    join.order();

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
            .each('end', function() { onComplete && onComplete(); })
            .each('interrupt', function() { onComplete && onComplete(); });

        transition.each(function() {
            // Must run the selection again since otherwise enters/updates get grouped together
            // and these get executed out of order. Except we need them in order!
            layer.selectAll('g.trace').each(function(cd) {
                plotOne(gd, cd, this, transitionOpts);
            });
        });
    } else {
        join.each(function(cd) {
            plotOne(gd, cd, this, transitionOpts);
        });
    }

    if(isFullReplot) {
        join.exit().remove();
    }
};

function plotOne(gd, cd, element, transitionOpts) {
    var fullLayout = gd._fullLayout;
    // We could optimize hasTransition per trace,
    // as sunburst has no cross-trace logic!
    var hasTransition = transitionOpts && transitionOpts.duration > 0;

    var gTrace = d3.select(element);
    var slices = gTrace.selectAll('g.slice');

    var cd0 = cd[0];
    var trace = cd0.trace;
    var hierarchy = cd0.hierarchy;
    var entry = findEntryWithLevel(hierarchy, trace.level);
    var maxDepth = trace.maxdepth >= 0 ? trace.maxdepth : Infinity;

    var gs = fullLayout._size;
    var domain = trace.domain;
    var vpw = gs.w * (domain.x[1] - domain.x[0]);
    var vph = gs.h * (domain.y[1] - domain.y[0]);
    var rMax = 0.5 * Math.min(vpw, vph);
    var cx = cd0.cx = gs.l + gs.w * (domain.x[1] + domain.x[0]) / 2;
    var cy = cd0.cy = gs.t + gs.h * (1 - domain.y[0]) - vph / 2;

    if(!entry) {
        return slices.remove();
    }

    // previous root 'pt' (can be empty)
    var prevEntry = null;
    // stash of 'previous' position data used by tweening functions
    var prevLookup = {};

    if(hasTransition) {
        // Important: do this before binding new sliceData!
        slices.each(function(pt) {
            prevLookup[getPtId(pt)] = {
                rpx0: pt.rpx0,
                rpx1: pt.rpx1,
                x0: pt.x0,
                x1: pt.x1,
                transform: pt.transform
            };

            if(!prevEntry && isEntry(pt)) {
                prevEntry = pt;
            }
        });
    }

    // N.B. slice data isn't the calcdata,
    // grab corresponding calcdata item in sliceData[i].data.data
    var sliceData = partition(entry).descendants();
    var maxHeight = entry.height + 1;
    var yOffset = 0;
    var cutoff = maxDepth;

    // N.B. handle multiple-root special case
    if(cd0.hasMultipleRoots && isHierachyRoot(entry)) {
        sliceData = sliceData.slice(1);
        maxHeight -= 1;
        yOffset = 1;
        cutoff += 1;
    }

    // filter out slices that won't show up on graph
    sliceData = sliceData.filter(function(pt) { return pt.y1 <= cutoff; });

    // partition span ('y') to sector radial px value
    var maxY = Math.min(maxHeight, maxDepth);
    var y2rpx = function(y) { return (y - yOffset) / maxY * rMax; };
    // (radial px value, partition angle ('x'))  to px [x,y]
    var rx2px = function(r, x) { return [r * Math.cos(x), -r * Math.sin(x)]; };
    // slice path generation fn
    var pathSlice = function(d) { return Lib.pathAnnulus(d.rpx0, d.rpx1, d.x0, d.x1, cx, cy); };
    // slice text translate x/y
    var transTextX = function(d) { return cx + d.pxmid[0] * d.transform.rCenter + (d.transform.x || 0); };
    var transTextY = function(d) { return cy + d.pxmid[1] * d.transform.rCenter + (d.transform.y || 0); };

    slices = slices.data(sliceData, function(pt) { return getPtId(pt); });

    slices.enter().append('g')
        .classed('slice', true);

    if(hasTransition) {
        slices.exit().transition()
            .each(function() {
                var sliceTop = d3.select(this);

                var slicePath = sliceTop.select('path.surface');
                slicePath.transition().attrTween('d', function(pt2) {
                    var interp = makeExitSliceInterpolator(pt2);
                    return function(t) { return pathSlice(interp(t)); };
                });

                var sliceTextGroup = sliceTop.select('g.slicetext');
                sliceTextGroup.attr('opacity', 0);
            })
            .remove();
    } else {
        slices.exit().remove();
    }

    slices.order();

    // next x1 (i.e. sector end angle) of previous entry
    var nextX1ofPrevEntry = null;
    if(hasTransition && prevEntry) {
        var prevEntryId = getPtId(prevEntry);
        slices.each(function(pt) {
            if(nextX1ofPrevEntry === null && (getPtId(pt) === prevEntryId)) {
                nextX1ofPrevEntry = pt.x1;
            }
        });
    }

    var updateSlices = slices;
    if(hasTransition) {
        updateSlices = updateSlices.transition().each('end', function() {
            // N.B. gd._transitioning is (still) *true* by the time
            // transition updates get hare
            var sliceTop = d3.select(this);
            setSliceCursor(sliceTop, gd, {isTransitioning: false});
        });
    }

    updateSlices.each(function(pt) {
        var sliceTop = d3.select(this);

        var slicePath = Lib.ensureSingle(sliceTop, 'path', 'surface', function(s) {
            s.style('pointer-events', 'all');
        });

        pt.rpx0 = y2rpx(pt.y0);
        pt.rpx1 = y2rpx(pt.y1);
        pt.xmid = (pt.x0 + pt.x1) / 2;
        pt.pxmid = rx2px(pt.rpx1, pt.xmid);
        pt.midangle = -(pt.xmid - Math.PI / 2);
        pt.halfangle = 0.5 * Math.min(Lib.angleDelta(pt.x0, pt.x1) || Math.PI, Math.PI);
        pt.ring = 1 - (pt.rpx0 / pt.rpx1);
        pt.rInscribed = getInscribedRadiusFraction(pt, trace);

        if(hasTransition) {
            slicePath.transition().attrTween('d', function(pt2) {
                var interp = makeUpdateSliceIntepolator(pt2);
                return function(t) { return pathSlice(interp(t)); };
            });
        } else {
            slicePath.attr('d', pathSlice);
        }

        sliceTop
            .call(attachFxHandlers, gd, cd)
            .call(setSliceCursor, gd, {isTransitioning: gd._transitioning});

        slicePath.call(styleOne, pt, trace);

        var sliceTextGroup = Lib.ensureSingle(sliceTop, 'g', 'slicetext');
        var sliceText = Lib.ensureSingle(sliceTextGroup, 'text', '', function(s) {
            // prohibit tex interpretation until we can handle
            // tex and regular text together
            s.attr('data-notex', 1);
        });

        sliceText.text(formatSliceLabel(pt, trace, fullLayout))
            .classed('slicetext', true)
            .attr('text-anchor', 'middle')
            .call(Drawing.font, isHierachyRoot(pt) ?
              determineOutsideTextFont(trace, pt, fullLayout.font) :
              determineInsideTextFont(trace, pt, fullLayout.font))
            .call(svgTextUtils.convertToTspans, gd);

        // position the text relative to the slice
        var textBB = Drawing.bBox(sliceText.node());
        pt.transform = transformInsideText(textBB, pt, cd0);
        pt.translateX = transTextX(pt);
        pt.translateY = transTextY(pt);

        var strTransform = function(d, textBB) {
            return 'translate(' + d.translateX + ',' + d.translateY + ')' +
                (d.transform.scale < 1 ? ('scale(' + d.transform.scale + ')') : '') +
                (d.transform.rotate ? ('rotate(' + d.transform.rotate + ')') : '') +
                'translate(' +
                    (-(textBB.left + textBB.right) / 2) + ',' +
                    (-(textBB.top + textBB.bottom) / 2) +
                ')';
        };

        if(hasTransition) {
            sliceText.transition().attrTween('transform', function(pt2) {
                var interp = makeUpdateTextInterpolar(pt2);
                return function(t) { return strTransform(interp(t), textBB); };
            });
        } else {
            sliceText.attr('transform', strTransform(pt, textBB));
        }
    });

    function makeExitSliceInterpolator(pt) {
        var id = getPtId(pt);
        var prev = prevLookup[id];
        var entryPrev = prevLookup[getPtId(entry)];
        var next;

        if(entryPrev) {
            var a = pt.x1 > entryPrev.x1 ? 2 * Math.PI : 0;
            // if pt to remove:
            // - if 'below' where the root-node used to be: shrink it radially inward
            // - otherwise, collapse it clockwise or counterclockwise which ever is shortest to theta=0
            next = pt.rpx1 < entryPrev.rpx1 ? {rpx0: 0, rpx1: 0} : {x0: a, x1: a};
        } else {
            // this happens when maxdepth is set, when leaves must
            // be removed and the rootPt is new (i.e. does not have a 'prev' object)
            var parent;
            var parentId = getPtId(pt.parent);
            slices.each(function(pt2) {
                if(getPtId(pt2) === parentId) {
                    return parent = pt2;
                }
            });
            var parentChildren = parent.children;
            var ci;
            parentChildren.forEach(function(pt2, i) {
                if(getPtId(pt2) === id) {
                    return ci = i;
                }
            });
            var n = parentChildren.length;
            var interp = d3.interpolate(parent.x0, parent.x1);
            next = {
                rpx0: rMax, rpx1: rMax,
                x0: interp(ci / n), x1: interp((ci + 1) / n)
            };
        }

        return d3.interpolate(prev, next);
    }

    function makeUpdateSliceIntepolator(pt) {
        var prev0 = prevLookup[getPtId(pt)];
        var prev;
        var next = {x0: pt.x0, x1: pt.x1, rpx0: pt.rpx0, rpx1: pt.rpx1};

        if(prev0) {
            // if pt already on graph, this is easy
            prev = prev0;
        } else {
            // for new pts:
            if(prevEntry) {
                // if trace was visible before
                if(pt.parent) {
                    if(nextX1ofPrevEntry) {
                        // if new branch, twist it in clockwise or
                        // counterclockwise which ever is shorter to
                        // its final angle
                        var a = pt.x1 > nextX1ofPrevEntry ? 2 * Math.PI : 0;
                        prev = {x0: a, x1: a};
                    } else {
                        // if new leaf (when maxdepth is set),
                        // grow it radially and angularly from
                        // its parent node
                        prev = {rpx0: rMax, rpx1: rMax};
                        Lib.extendFlat(prev, interpX0X1FromParent(pt));
                    }
                } else {
                    // if new root-node, grow it radially
                    prev = {rpx0: 0, rpx1: 0};
                }
            } else {
                // start sector of new traces from theta=0
                prev = {x0: 0, x1: 0};
            }
        }

        return d3.interpolate(prev, next);
    }

    function makeUpdateTextInterpolar(pt) {
        var prev0 = prevLookup[getPtId(pt)];
        var prev;
        var transform = pt.transform;

        if(prev0) {
            prev = prev0;
        } else {
            prev = {
                rpx1: pt.rpx1,
                transform: {
                    scale: 0,
                    rotate: transform.rotate,
                    rCenter: transform.rCenter,
                    x: transform.x,
                    y: transform.y
                }
            };

            // for new pts:
            if(prevEntry) {
                // if trace was visible before
                if(pt.parent) {
                    if(nextX1ofPrevEntry) {
                        // if new branch, twist it in clockwise or
                        // counterclockwise which ever is shorter to
                        // its final angle
                        var a = pt.x1 > nextX1ofPrevEntry ? 2 * Math.PI : 0;
                        prev.x0 = prev.x1 = a;
                    } else {
                        // if leaf
                        Lib.extendFlat(prev, interpX0X1FromParent(pt));
                    }
                } else {
                    // if new root-node
                    prev.x0 = prev.x1 = 0;
                }
            } else {
                // on new traces
                prev.x0 = prev.x1 = 0;
            }
        }

        var rpx1Fn = d3.interpolate(prev.rpx1, pt.rpx1);
        var x0Fn = d3.interpolate(prev.x0, pt.x0);
        var x1Fn = d3.interpolate(prev.x1, pt.x1);
        var scaleFn = d3.interpolate(prev.transform.scale, transform.scale);
        var rotateFn = d3.interpolate(prev.transform.rotate, transform.rotate);

        // smooth out start/end from entry, to try to keep text inside sector
        // while keeping transition smooth
        var pow = transform.rCenter === 0 ? 3 :
            prev.transform.rCenter === 0 ? 1 / 3 :
            1;
        var _rCenterFn = d3.interpolate(prev.transform.rCenter, transform.rCenter);
        var rCenterFn = function(t) { return _rCenterFn(Math.pow(t, pow)); };

        return function(t) {
            var rpx1 = rpx1Fn(t);
            var x0 = x0Fn(t);
            var x1 = x1Fn(t);
            var rCenter = rCenterFn(t);

            var d = {
                pxmid: rx2px(rpx1, (x0 + x1) / 2),
                transform: {
                    rCenter: rCenter,
                    x: transform.x,
                    y: transform.y
                }
            };

            var out = {
                rpx1: rpx1Fn(t),
                translateX: transTextX(d),
                translateY: transTextY(d),
                transform: {
                    scale: scaleFn(t),
                    rotate: rotateFn(t),
                    rCenter: rCenter
                }
            };

            return out;
        };
    }

    function interpX0X1FromParent(pt) {
        var parent = pt.parent;
        var parentPrev = prevLookup[getPtId(parent)];
        var out = {};

        if(parentPrev) {
            // if parent is visible
            var parentChildren = parent.children;
            var ci = parentChildren.indexOf(pt);
            var n = parentChildren.length;
            var interp = d3.interpolate(parentPrev.x0, parentPrev.x1);
            out.x0 = interp(ci / n);
            out.x1 = interp(ci / n);
        } else {
            // w/o visible parent
            // TODO !!! HOW ???
            out.x0 = out.x1 = 0;
        }

        return out;
    }
}

// x[0-1] keys are angles [radians]
// y[0-1] keys are hierarchy heights [integers]
function partition(entry) {
    return d3Hierarchy.partition()
        .size([2 * Math.PI, entry.height + 1])(entry);
}

function findEntryWithLevel(hierarchy, level) {
    var out;
    if(level) {
        hierarchy.eachAfter(function(pt) {
            if(getPtId(pt) === level) {
                return out = pt.copy();
            }
        });
    }
    return out || hierarchy;
}

function findEntryWithChild(hierarchy, childId) {
    var out;
    hierarchy.eachAfter(function(pt) {
        var children = pt.children || [];
        for(var i = 0; i < children.length; i++) {
            var child = children[i];
            if(getPtId(child) === childId) {
                return out = pt.copy();
            }
        }
    });
    return out || hierarchy;
}

function isHierachyRoot(pt) {
    var cdi = pt.data.data;
    return cdi.pid === '';
}

function isEntry(pt) {
    return !pt.parent;
}

function isLeaf(pt) {
    return !pt.children;
}

function getPtId(pt) {
    var cdi = pt.data.data;
    return cdi.id;
}

function setSliceCursor(sliceTop, gd, opts) {
    var pt = sliceTop.datum();
    var isTransitioning = (opts || {}).isTransitioning;
    setCursor(sliceTop, (isTransitioning || isLeaf(pt) || isHierachyRoot(pt)) ? null : 'pointer');
}

function attachFxHandlers(sliceTop, gd, cd) {
    var cd0 = cd[0];
    var trace = cd0.trace;

    // hover state vars
    // have we drawn a hover label, so it should be cleared later
    if(!('_hasHoverLabel' in trace)) trace._hasHoverLabel = false;
    // have we emitted a hover event, so later an unhover event should be emitted
    // note that click events do not depend on this - you can still get them
    // with hovermode: false or if you were earlier dragging, then clicked
    // in the same slice that you moused up in
    if(!('_hasHoverEvent' in trace)) trace._hasHoverEvent = false;

    sliceTop.on('mouseover', function(pt) {
        var fullLayoutNow = gd._fullLayout;

        if(gd._dragging || fullLayoutNow.hovermode === false) return;

        var traceNow = gd._fullData[trace.index];
        var cdi = pt.data.data;
        var ptNumber = cdi.i;

        var _cast = function(astr) {
            return Lib.castOption(traceNow, ptNumber, astr);
        };

        var hovertemplate = _cast('hovertemplate');
        var hoverinfo = Fx.castHoverinfo(traceNow, fullLayoutNow, ptNumber);
        var separators = fullLayoutNow.separators;

        if(hovertemplate || (hoverinfo && hoverinfo !== 'none' && hoverinfo !== 'skip')) {
            var rInscribed = pt.rInscribed;
            var hoverCenterX = cd0.cx + pt.pxmid[0] * (1 - rInscribed);
            var hoverCenterY = cd0.cy + pt.pxmid[1] * (1 - rInscribed);
            var hoverPt = {};
            var parts = [];
            var thisText = [];
            var hasFlag = function(flag) { return parts.indexOf(flag) !== -1; };

            if(hoverinfo) {
                parts = hoverinfo === 'all' ?
                    traceNow._module.attributes.hoverinfo.flags :
                    hoverinfo.split('+');
            }

            hoverPt.label = cdi.label;
            if(hasFlag('label') && hoverPt.label) thisText.push(hoverPt.label);

            if(cdi.hasOwnProperty('v')) {
                hoverPt.value = cdi.v;
                hoverPt.valueLabel = formatPieValue(hoverPt.value, separators);
                if(hasFlag('value')) thisText.push(hoverPt.valueLabel);
            }

            hoverPt.text = _cast('hovertext') || _cast('text');
            if(hasFlag('text')) {
                var tx = hoverPt.text;
                if(Lib.isValidTextValue(tx)) thisText.push(tx);
            }

            Fx.loneHover({
                trace: traceNow,
                x0: hoverCenterX - rInscribed * pt.rpx1,
                x1: hoverCenterX + rInscribed * pt.rpx1,
                y: hoverCenterY,
                idealAlign: pt.pxmid[0] < 0 ? 'left' : 'right',
                text: thisText.join('<br>'),
                name: (hovertemplate || hasFlag('name')) ? traceNow.name : undefined,
                color: _cast('hoverlabel.bgcolor') || cdi.color,
                borderColor: _cast('hoverlabel.bordercolor'),
                fontFamily: _cast('hoverlabel.font.family'),
                fontSize: _cast('hoverlabel.font.size'),
                fontColor: _cast('hoverlabel.font.color'),
                nameLength: _cast('hoverlabel.namelength'),
                textAlign: _cast('hoverlabel.align'),
                hovertemplate: hovertemplate,
                hovertemplateLabels: hoverPt,
                eventData: [makeEventData(pt, traceNow)]
            }, {
                container: fullLayoutNow._hoverlayer.node(),
                outerContainer: fullLayoutNow._paper.node(),
                gd: gd
            });

            trace._hasHoverLabel = true;
        }

        trace._hasHoverEvent = true;
        gd.emit('plotly_hover', {
            points: [makeEventData(pt, traceNow)],
            event: d3.event
        });
    });

    sliceTop.on('mouseout', function(evt) {
        var fullLayoutNow = gd._fullLayout;
        var traceNow = gd._fullData[trace.index];
        var pt = d3.select(this).datum();

        if(trace._hasHoverEvent) {
            evt.originalEvent = d3.event;
            gd.emit('plotly_unhover', {
                points: [makeEventData(pt, traceNow)],
                event: d3.event
            });
            trace._hasHoverEvent = false;
        }

        if(trace._hasHoverLabel) {
            Fx.loneUnhover(fullLayoutNow._hoverlayer.node());
            trace._hasHoverLabel = false;
        }
    });

    sliceTop.on('click', function(pt) {
        // TODO: this does not support right-click. If we want to support it, we
        // would likely need to change pie to use dragElement instead of straight
        // mapbox event binding. Or perhaps better, make a simple wrapper with the
        // right mousedown, mousemove, and mouseup handlers just for a left/right click
        // mapbox would use this too.
        var fullLayoutNow = gd._fullLayout;
        var traceNow = gd._fullData[trace.index];

        var clickVal = Events.triggerHandler(gd, 'plotly_sunburstclick', {
            points: [makeEventData(pt, traceNow)],
            event: d3.event
        });

        // 'regular' click event when sunburstclick is disabled or when
        // clikcin on leaves or the hierarchy root
        if(clickVal === false || isLeaf(pt) || isHierachyRoot(pt)) {
            if(fullLayoutNow.hovermode) {
                gd._hoverdata = [makeEventData(pt, traceNow)];
                Fx.click(gd, d3.event);
            }
            return;
        }

        // skip if triggered from dragging a nearby cartesian subplot
        if(gd._dragging) return;

        // skip during transitions, to avoid potential bugs
        // we could remove this check later
        if(gd._transitioning) return;

        // store 'old' level in guiEdit stash, so that subsequent Plotly.react
        // calls with the same uirevision can start from the same entry
        Registry.call('_storeDirectGUIEdit', traceNow, fullLayoutNow._tracePreGUI[traceNow.uid], {level: traceNow.level});

        var hierarchy = cd0.hierarchy;
        var id = getPtId(pt);
        var nextEntry = isEntry(pt) ?
            findEntryWithChild(hierarchy, id) :
            findEntryWithLevel(hierarchy, id);

        var frame = {
            data: [{level: getPtId(nextEntry)}],
            traces: [trace.index]
        };

        var animOpts = {
            frame: {
                redraw: false,
                duration: constants.CLICK_TRANSITION_TIME
            },
            transition: {
                duration: constants.CLICK_TRANSITION_TIME,
                easing: constants.CLICK_TRANSITION_EASING
            },
            mode: 'immediate',
            fromcurrent: true
        };

        Fx.loneUnhover(fullLayoutNow._hoverlayer.node());
        Registry.call('animate', gd, frame, animOpts);
    });
}

function makeEventData(pt, trace) {
    var cdi = pt.data.data;

    var out = {
        curveNumber: trace.index,
        pointNumber: cdi.i,
        data: trace._input,
        fullData: trace,

        // TODO more things like 'children', 'siblings', 'hierarchy?
    };

    appendArrayPointValue(out, trace, cdi.i);

    return out;
}

function formatSliceLabel(pt, trace, fullLayout) {
    var textinfo = trace.textinfo;

    if(!textinfo || textinfo === 'none') {
        return '';
    }

    var cdi = pt.data.data;
    var separators = fullLayout.separators;
    var parts = textinfo.split('+');
    var hasFlag = function(flag) { return parts.indexOf(flag) !== -1; };
    var thisText = [];

    if(hasFlag('label') && cdi.label) thisText.push(cdi.label);

    if(cdi.hasOwnProperty('v') && hasFlag('value')) {
        thisText.push(formatPieValue(cdi.v, separators));
    }

    if(hasFlag('text')) {
        var tx = Lib.castOption(trace, cdi.i, 'text');
        if(Lib.isValidTextValue(tx)) thisText.push(tx);
    }

    return thisText.join('<br>');
}

function determineOutsideTextFont(trace, pt, layoutFont) {
    var cdi = pt.data.data;
    var ptNumber = cdi.i;

    var color = Lib.castOption(trace, ptNumber, 'outsidetextfont.color') ||
        Lib.castOption(trace, ptNumber, 'textfont.color') ||
        layoutFont.color;

    var family = Lib.castOption(trace, ptNumber, 'outsidetextfont.family') ||
        Lib.castOption(trace, ptNumber, 'textfont.family') ||
        layoutFont.family;

    var size = Lib.castOption(trace, ptNumber, 'outsidetextfont.size') ||
        Lib.castOption(trace, ptNumber, 'textfont.size') ||
        layoutFont.size;

    return {
        color: color,
        family: family,
        size: size
    };
}

function determineInsideTextFont(trace, pt, layoutFont) {
    var cdi = pt.data.data;
    var ptNumber = cdi.i;

    var customColor = Lib.castOption(trace, ptNumber, 'insidetextfont.color');
    if(!customColor && trace._input.textfont) {
        // Why not simply using trace.textfont? Because if not set, it
        // defaults to layout.font which has a default color. But if
        // textfont.color and insidetextfont.color don't supply a value,
        // a contrasting color shall be used.
        customColor = Lib.castOption(trace._input, ptNumber, 'textfont.color');
    }

    var family = Lib.castOption(trace, ptNumber, 'insidetextfont.family') ||
        Lib.castOption(trace, ptNumber, 'textfont.family') ||
        layoutFont.family;

    var size = Lib.castOption(trace, ptNumber, 'insidetextfont.size') ||
        Lib.castOption(trace, ptNumber, 'textfont.size') ||
        layoutFont.size;

    return {
        color: customColor || Color.contrast(cdi.color),
        family: family,
        size: size
    };
}

function getInscribedRadiusFraction(pt) {
    if(pt.rpx0 === 0 && Lib.isFullCircle([pt.x0, pt.x1])) {
        // special case of 100% with no hole
        return 1;
    } else {
        return Math.max(0, Math.min(
            1 / (1 + 1 / Math.sin(pt.halfangle)),
            pt.ring / 2
        ));
    }
}
