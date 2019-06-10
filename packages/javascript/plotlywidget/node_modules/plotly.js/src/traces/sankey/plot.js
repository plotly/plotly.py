/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var d3 = require('d3');
var render = require('./render');
var Fx = require('../../components/fx');
var Color = require('../../components/color');
var Lib = require('../../lib');
var cn = require('./constants').cn;

var _ = Lib._;

function renderableValuePresent(d) {return d !== '';}

function ownTrace(selection, d) {
    return selection.filter(function(s) {return s.key === d.traceId;});
}

function makeTranslucent(element, alpha) {
    d3.select(element)
        .select('path')
        .style('fill-opacity', alpha);
    d3.select(element)
        .select('rect')
        .style('fill-opacity', alpha);
}

function makeTextContrasty(element) {
    d3.select(element)
        .select('text.name')
        .style('fill', 'black');
}

function relatedLinks(d) {
    return function(l) {
        return d.node.sourceLinks.indexOf(l.link) !== -1 || d.node.targetLinks.indexOf(l.link) !== -1;
    };
}

function relatedNodes(l) {
    return function(d) {
        return d.node.sourceLinks.indexOf(l.link) !== -1 || d.node.targetLinks.indexOf(l.link) !== -1;
    };
}

function nodeHoveredStyle(sankeyNode, d, sankey) {
    if(d && sankey) {
        ownTrace(sankey, d)
            .selectAll('.' + cn.sankeyLink)
            .filter(relatedLinks(d))
            .call(linkHoveredStyle.bind(0, d, sankey, false));
    }
}

function nodeNonHoveredStyle(sankeyNode, d, sankey) {
    if(d && sankey) {
        ownTrace(sankey, d)
            .selectAll('.' + cn.sankeyLink)
            .filter(relatedLinks(d))
            .call(linkNonHoveredStyle.bind(0, d, sankey, false));
    }
}

function linkHoveredStyle(d, sankey, visitNodes, sankeyLink) {
    var label = sankeyLink.datum().link.label;

    sankeyLink.style('fill-opacity', function(l) {
        if(!l.link.concentrationscale) {
            return 0.4;
        }
    });

    if(label) {
        ownTrace(sankey, d)
            .selectAll('.' + cn.sankeyLink)
            .filter(function(l) {return l.link.label === label;})
            .style('fill-opacity', function(l) {
                if(!l.link.concentrationscale) {
                    return 0.4;
                }
            });
    }

    if(visitNodes) {
        ownTrace(sankey, d)
            .selectAll('.' + cn.sankeyNode)
            .filter(relatedNodes(d))
            .call(nodeHoveredStyle);
    }
}

function linkNonHoveredStyle(d, sankey, visitNodes, sankeyLink) {
    var label = sankeyLink.datum().link.label;

    sankeyLink.style('fill-opacity', function(d) {return d.tinyColorAlpha;});
    if(label) {
        ownTrace(sankey, d)
            .selectAll('.' + cn.sankeyLink)
            .filter(function(l) {return l.link.label === label;})
            .style('fill-opacity', function(d) {return d.tinyColorAlpha;});
    }

    if(visitNodes) {
        ownTrace(sankey, d)
            .selectAll(cn.sankeyNode)
            .filter(relatedNodes(d))
            .call(nodeNonHoveredStyle);
    }
}

// does not support array values for now
function castHoverOption(trace, attr) {
    var labelOpts = trace.hoverlabel || {};
    var val = Lib.nestedProperty(labelOpts, attr).get();
    return Array.isArray(val) ? false : val;
}

module.exports = function plot(gd, calcData) {
    var fullLayout = gd._fullLayout;
    var svg = fullLayout._paper;
    var size = fullLayout._size;

    // stash initial view
    for(var i = 0; i < gd._fullData.length; i++) {
        if(gd._fullData[i].type !== cn.sankey) continue;
        if(!gd._fullData[i]._viewInitial) {
            var node = gd._fullData[i].node;
            gd._fullData[i]._viewInitial = {
                node: {
                    groups: node.groups.slice(),
                    x: node.x.slice(),
                    y: node.y.slice()
                }
            };
        }
    }

    var linkSelect = function(element, d) {
        var evt = d.link;
        evt.originalEvent = d3.event;
        gd._hoverdata = [evt];
        Fx.click(gd, { target: true });
    };

    var linkHover = function(element, d, sankey) {
        if(gd._fullLayout.hovermode === false) return;
        d3.select(element).call(linkHoveredStyle.bind(0, d, sankey, true));
        if(d.link.trace.link.hoverinfo !== 'skip') {
            d.link.fullData = d.link.trace;
            gd.emit('plotly_hover', {
                event: d3.event,
                points: [d.link]
            });
        }
    };

    var sourceLabel = _(gd, 'source:') + ' ';
    var targetLabel = _(gd, 'target:') + ' ';
    var concentrationLabel = _(gd, 'concentration:') + ' ';
    var incomingLabel = _(gd, 'incoming flow count:') + ' ';
    var outgoingLabel = _(gd, 'outgoing flow count:') + ' ';

    var linkHoverFollow = function(element, d) {
        if(gd._fullLayout.hovermode === false) return;
        var obj = d.link.trace.link;
        if(obj.hoverinfo === 'none' || obj.hoverinfo === 'skip') return;

        var hoverItems = [];

        function hoverCenterPosition(link) {
            var hoverCenterX, hoverCenterY;
            if(link.circular) {
                hoverCenterX = (link.circularPathData.leftInnerExtent + link.circularPathData.rightInnerExtent) / 2 + d.parent.translateX;
                hoverCenterY = link.circularPathData.verticalFullExtent + d.parent.translateY;
            } else {
                hoverCenterX = (link.source.x1 + link.target.x0) / 2 + d.parent.translateX;
                hoverCenterY = (link.y0 + link.y1) / 2 + d.parent.translateY;
            }
            return [hoverCenterX, hoverCenterY];
        }

        // For each related links, create a hoverItem
        var anchorIndex = 0;
        for(var i = 0; i < d.flow.links.length; i++) {
            var link = d.flow.links[i];
            if(gd._fullLayout.hovermode === 'closest' && d.link.pointNumber !== link.pointNumber) continue;
            if(d.link.pointNumber === link.pointNumber) anchorIndex = i;
            link.fullData = link.trace;
            obj = d.link.trace.link;
            var hoverCenter = hoverCenterPosition(link);
            var hovertemplateLabels = {valueLabel: d3.format(d.valueFormat)(link.value) + d.valueSuffix};

            hoverItems.push({
                x: hoverCenter[0],
                y: hoverCenter[1],
                name: hovertemplateLabels.valueLabel,
                text: [
                    link.label || '',
                    sourceLabel + link.source.label,
                    targetLabel + link.target.label,
                    link.concentrationscale ? concentrationLabel + d3.format('%0.2f')(link.flow.labelConcentration) : ''
                ].filter(renderableValuePresent).join('<br>'),
                color: castHoverOption(obj, 'bgcolor') || Color.addOpacity(link.color, 1),
                borderColor: castHoverOption(obj, 'bordercolor'),
                fontFamily: castHoverOption(obj, 'font.family'),
                fontSize: castHoverOption(obj, 'font.size'),
                fontColor: castHoverOption(obj, 'font.color'),
                nameLength: castHoverOption(obj, 'namelength'),
                textAlign: castHoverOption(obj, 'align'),
                idealAlign: d3.event.x < hoverCenter[0] ? 'right' : 'left',

                hovertemplate: obj.hovertemplate,
                hovertemplateLabels: hovertemplateLabels,
                eventData: [link]
            });
        }

        var tooltips = Fx.loneHover(hoverItems, {
            container: fullLayout._hoverlayer.node(),
            outerContainer: fullLayout._paper.node(),
            gd: gd,
            anchorIndex: anchorIndex
        });

        tooltips.each(function() {
            var tooltip = this;
            if(!d.link.concentrationscale) {
                makeTranslucent(tooltip, 0.65);
            }
            makeTextContrasty(tooltip);
        });
    };

    var linkUnhover = function(element, d, sankey) {
        if(gd._fullLayout.hovermode === false) return;
        d3.select(element).call(linkNonHoveredStyle.bind(0, d, sankey, true));
        if(d.link.trace.link.hoverinfo !== 'skip') {
            d.link.fullData = d.link.trace;
            gd.emit('plotly_unhover', {
                event: d3.event,
                points: [d.link]
            });
        }

        Fx.loneUnhover(fullLayout._hoverlayer.node());
    };

    var nodeSelect = function(element, d, sankey) {
        var evt = d.node;
        evt.originalEvent = d3.event;
        gd._hoverdata = [evt];
        d3.select(element).call(nodeNonHoveredStyle, d, sankey);
        Fx.click(gd, { target: true });
    };

    var nodeHover = function(element, d, sankey) {
        if(gd._fullLayout.hovermode === false) return;
        d3.select(element).call(nodeHoveredStyle, d, sankey);
        if(d.node.trace.node.hoverinfo !== 'skip') {
            d.node.fullData = d.node.trace;
            gd.emit('plotly_hover', {
                event: d3.event,
                points: [d.node]
            });
        }
    };

    var nodeHoverFollow = function(element, d) {
        if(gd._fullLayout.hovermode === false) return;

        var obj = d.node.trace.node;
        if(obj.hoverinfo === 'none' || obj.hoverinfo === 'skip') return;
        var nodeRect = d3.select(element).select('.' + cn.nodeRect);
        var rootBBox = gd._fullLayout._paperdiv.node().getBoundingClientRect();
        var boundingBox = nodeRect.node().getBoundingClientRect();
        var hoverCenterX0 = boundingBox.left - 2 - rootBBox.left;
        var hoverCenterX1 = boundingBox.right + 2 - rootBBox.left;
        var hoverCenterY = boundingBox.top + boundingBox.height / 4 - rootBBox.top;

        var hovertemplateLabels = {valueLabel: d3.format(d.valueFormat)(d.node.value) + d.valueSuffix};
        d.node.fullData = d.node.trace;

        var tooltip = Fx.loneHover({
            x0: hoverCenterX0,
            x1: hoverCenterX1,
            y: hoverCenterY,
            name: d3.format(d.valueFormat)(d.node.value) + d.valueSuffix,
            text: [
                d.node.label,
                incomingLabel + d.node.targetLinks.length,
                outgoingLabel + d.node.sourceLinks.length
            ].filter(renderableValuePresent).join('<br>'),
            color: castHoverOption(obj, 'bgcolor') || d.tinyColorHue,
            borderColor: castHoverOption(obj, 'bordercolor'),
            fontFamily: castHoverOption(obj, 'font.family'),
            fontSize: castHoverOption(obj, 'font.size'),
            fontColor: castHoverOption(obj, 'font.color'),
            nameLength: castHoverOption(obj, 'namelength'),
            textAlign: castHoverOption(obj, 'align'),
            idealAlign: 'left',

            hovertemplate: obj.hovertemplate,
            hovertemplateLabels: hovertemplateLabels,
            eventData: [d.node]
        }, {
            container: fullLayout._hoverlayer.node(),
            outerContainer: fullLayout._paper.node(),
            gd: gd
        });

        makeTranslucent(tooltip, 0.85);
        makeTextContrasty(tooltip);
    };

    var nodeUnhover = function(element, d, sankey) {
        if(gd._fullLayout.hovermode === false) return;
        d3.select(element).call(nodeNonHoveredStyle, d, sankey);
        if(d.node.trace.node.hoverinfo !== 'skip') {
            d.node.fullData = d.node.trace;
            gd.emit('plotly_unhover', {
                event: d3.event,
                points: [d.node]
            });
        }

        Fx.loneUnhover(fullLayout._hoverlayer.node());
    };

    render(
        gd,
        svg,
        calcData,
        {
            width: size.w,
            height: size.h,
            margin: {
                t: size.t,
                r: size.r,
                b: size.b,
                l: size.l
            }
        },
        {
            linkEvents: {
                hover: linkHover,
                follow: linkHoverFollow,
                unhover: linkUnhover,
                select: linkSelect
            },
            nodeEvents: {
                hover: nodeHover,
                follow: nodeHoverFollow,
                unhover: nodeUnhover,
                select: nodeSelect
            }
        }
    );
};
