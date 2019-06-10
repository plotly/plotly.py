/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

var d3 = require('d3');
var Lib = require('../../../lib');
var extendDeepAll = Lib.extendDeepAll;
var MID_SHIFT = require('../../../constants/alignment').MID_SHIFT;

var µ = module.exports = { version: '0.2.2' };

µ.Axis = function module() {
    var config = {
        data: [],
        layout: {}
    }, inputConfig = {}, liveConfig = {};
    var svg, container, dispatch = d3.dispatch('hover'), radialScale, angularScale;
    var exports = {};
    function render(_container) {
        container = _container || container;
        var data = config.data;
        var axisConfig = config.layout;
        if (typeof container == 'string' || container.nodeName) container = d3.select(container);
        container.datum(data).each(function(_data, _index) {
            var dataOriginal = _data.slice();
            liveConfig = {
                data: µ.util.cloneJson(dataOriginal),
                layout: µ.util.cloneJson(axisConfig)
            };
            var colorIndex = 0;
            dataOriginal.forEach(function(d, i) {
                if (!d.color) {
                    d.color = axisConfig.defaultColorRange[colorIndex];
                    colorIndex = (colorIndex + 1) % axisConfig.defaultColorRange.length;
                }
                if (!d.strokeColor) {
                    d.strokeColor = d.geometry === 'LinePlot' ? d.color : d3.rgb(d.color).darker().toString();
                }
                liveConfig.data[i].color = d.color;
                liveConfig.data[i].strokeColor = d.strokeColor;
                liveConfig.data[i].strokeDash = d.strokeDash;
                liveConfig.data[i].strokeSize = d.strokeSize;
            });
            var data = dataOriginal.filter(function(d, i) {
                var visible = d.visible;
                return typeof visible === 'undefined' || visible === true;
            });
            var isStacked = false;
            var dataWithGroupId = data.map(function(d, i) {
                isStacked = isStacked || typeof d.groupId !== 'undefined';
                return d;
            });
            if (isStacked) {
                var grouped = d3.nest().key(function(d, i) {
                    return typeof d.groupId != 'undefined' ? d.groupId : 'unstacked';
                }).entries(dataWithGroupId);
                var dataYStack = [];
                var stacked = grouped.map(function(d, i) {
                    if (d.key === 'unstacked') return d.values; else {
                        var prevArray = d.values[0].r.map(function(d, i) {
                            return 0;
                        });
                        d.values.forEach(function(d, i, a) {
                            d.yStack = [ prevArray ];
                            dataYStack.push(prevArray);
                            prevArray = µ.util.sumArrays(d.r, prevArray);
                        });
                        return d.values;
                    }
                });
                data = d3.merge(stacked);
            }
            data.forEach(function(d, i) {
                d.t = Array.isArray(d.t[0]) ? d.t : [ d.t ];
                d.r = Array.isArray(d.r[0]) ? d.r : [ d.r ];
            });
            var radius = Math.min(axisConfig.width - axisConfig.margin.left - axisConfig.margin.right, axisConfig.height - axisConfig.margin.top - axisConfig.margin.bottom) / 2;
            radius = Math.max(10, radius);
            var chartCenter = [ axisConfig.margin.left + radius, axisConfig.margin.top + radius ];
            var extent;
            if (isStacked) {
                var highestStackedValue = d3.max(µ.util.sumArrays(µ.util.arrayLast(data).r[0], µ.util.arrayLast(dataYStack)));
                extent = [ 0, highestStackedValue ];
            } else extent = d3.extent(µ.util.flattenArray(data.map(function(d, i) {
                return d.r;
            })));
            if (axisConfig.radialAxis.domain != µ.DATAEXTENT) extent[0] = 0;
            radialScale = d3.scale.linear().domain(axisConfig.radialAxis.domain != µ.DATAEXTENT && axisConfig.radialAxis.domain ? axisConfig.radialAxis.domain : extent).range([ 0, radius ]);
            liveConfig.layout.radialAxis.domain = radialScale.domain();
            var angularDataMerged = µ.util.flattenArray(data.map(function(d, i) {
                return d.t;
            }));
            var isOrdinal = typeof angularDataMerged[0] === 'string';
            var ticks;
            if (isOrdinal) {
                angularDataMerged = µ.util.deduplicate(angularDataMerged);
                ticks = angularDataMerged.slice();
                angularDataMerged = d3.range(angularDataMerged.length);
                data = data.map(function(d, i) {
                    var result = d;
                    d.t = [ angularDataMerged ];
                    if (isStacked) result.yStack = d.yStack;
                    return result;
                });
            }
            var hasOnlyLineOrDotPlot = data.filter(function(d, i) {
                return d.geometry === 'LinePlot' || d.geometry === 'DotPlot';
            }).length === data.length;
            var needsEndSpacing = axisConfig.needsEndSpacing === null ? isOrdinal || !hasOnlyLineOrDotPlot : axisConfig.needsEndSpacing;
            var useProvidedDomain = axisConfig.angularAxis.domain && axisConfig.angularAxis.domain != µ.DATAEXTENT && !isOrdinal && axisConfig.angularAxis.domain[0] >= 0;
            var angularDomain = useProvidedDomain ? axisConfig.angularAxis.domain : d3.extent(angularDataMerged);
            var angularDomainStep = Math.abs(angularDataMerged[1] - angularDataMerged[0]);
            if (hasOnlyLineOrDotPlot && !isOrdinal) angularDomainStep = 0;
            var angularDomainWithPadding = angularDomain.slice();
            if (needsEndSpacing && isOrdinal) angularDomainWithPadding[1] += angularDomainStep;
            var tickCount = axisConfig.angularAxis.ticksCount || 4;
            if (tickCount > 8) tickCount = tickCount / (tickCount / 8) + tickCount % 8;
            if (axisConfig.angularAxis.ticksStep) {
                tickCount = (angularDomainWithPadding[1] - angularDomainWithPadding[0]) / tickCount;
            }
            var angularTicksStep = axisConfig.angularAxis.ticksStep || (angularDomainWithPadding[1] - angularDomainWithPadding[0]) / (tickCount * (axisConfig.minorTicks + 1));
            if (ticks) angularTicksStep = Math.max(Math.round(angularTicksStep), 1);
            if (!angularDomainWithPadding[2]) angularDomainWithPadding[2] = angularTicksStep;
            var angularAxisRange = d3.range.apply(this, angularDomainWithPadding);
            angularAxisRange = angularAxisRange.map(function(d, i) {
                return parseFloat(d.toPrecision(12));
            });
            angularScale = d3.scale.linear().domain(angularDomainWithPadding.slice(0, 2)).range(axisConfig.direction === 'clockwise' ? [ 0, 360 ] : [ 360, 0 ]);
            liveConfig.layout.angularAxis.domain = angularScale.domain();
            liveConfig.layout.angularAxis.endPadding = needsEndSpacing ? angularDomainStep : 0;
            svg = d3.select(this).select('svg.chart-root');
            if (typeof svg === 'undefined' || svg.empty()) {
                var skeleton = "<svg xmlns='http://www.w3.org/2000/svg' class='chart-root'>' + '<g class='outer-group'>' + '<g class='chart-group'>' + '<circle class='background-circle'></circle>' + '<g class='geometry-group'></g>' + '<g class='radial axis-group'>' + '<circle class='outside-circle'></circle>' + '</g>' + '<g class='angular axis-group'></g>' + '<g class='guides-group'><line></line><circle r='0'></circle></g>' + '</g>' + '<g class='legend-group'></g>' + '<g class='tooltips-group'></g>' + '<g class='title-group'><text></text></g>' + '</g>' + '</svg>";
                var doc = new DOMParser().parseFromString(skeleton, 'application/xml');
                var newSvg = this.appendChild(this.ownerDocument.importNode(doc.documentElement, true));
                svg = d3.select(newSvg);
            }
            svg.select('.guides-group').style({
                'pointer-events': 'none'
            });
            svg.select('.angular.axis-group').style({
                'pointer-events': 'none'
            });
            svg.select('.radial.axis-group').style({
                'pointer-events': 'none'
            });
            var chartGroup = svg.select('.chart-group');
            var lineStyle = {
                fill: 'none',
                stroke: axisConfig.tickColor
            };
            var fontStyle = {
                'font-size': axisConfig.font.size,
                'font-family': axisConfig.font.family,
                fill: axisConfig.font.color,
                'text-shadow': [ '-1px 0px', '1px -1px', '-1px 1px', '1px 1px' ].map(function(d, i) {
                    return ' ' + d + ' 0 ' + axisConfig.font.outlineColor;
                }).join(',')
            };
            var legendContainer;
            if (axisConfig.showLegend) {
                legendContainer = svg.select('.legend-group').attr({
                    transform: 'translate(' + [ radius, axisConfig.margin.top ] + ')'
                }).style({
                    display: 'block'
                });
                var elements = data.map(function(d, i) {
                    var datumClone = µ.util.cloneJson(d);
                    datumClone.symbol = d.geometry === 'DotPlot' ? d.dotType || 'circle' : d.geometry != 'LinePlot' ? 'square' : 'line';
                    datumClone.visibleInLegend = typeof d.visibleInLegend === 'undefined' || d.visibleInLegend;
                    datumClone.color = d.geometry === 'LinePlot' ? d.strokeColor : d.color;
                    return datumClone;
                });

                µ.Legend().config({
                    data: data.map(function(d, i) {
                        return d.name || 'Element' + i;
                    }),
                    legendConfig: extendDeepAll({},
                        µ.Legend.defaultConfig().legendConfig,
                        {
                            container: legendContainer,
                            elements: elements,
                            reverseOrder: axisConfig.legend.reverseOrder
                        }
                    )
                })();

                var legendBBox = legendContainer.node().getBBox();
                radius = Math.min(axisConfig.width - legendBBox.width - axisConfig.margin.left - axisConfig.margin.right, axisConfig.height - axisConfig.margin.top - axisConfig.margin.bottom) / 2;
                radius = Math.max(10, radius);
                chartCenter = [ axisConfig.margin.left + radius, axisConfig.margin.top + radius ];
                radialScale.range([ 0, radius ]);
                liveConfig.layout.radialAxis.domain = radialScale.domain();
                legendContainer.attr('transform', 'translate(' + [ chartCenter[0] + radius, chartCenter[1] - radius ] + ')');
            } else {
                legendContainer = svg.select('.legend-group').style({
                    display: 'none'
                });
            }
            svg.attr({
                width: axisConfig.width,
                height: axisConfig.height
            }).style({
                opacity: axisConfig.opacity
            });
            chartGroup.attr('transform', 'translate(' + chartCenter + ')').style({
                cursor: 'crosshair'
            });
            var centeringOffset = [ (axisConfig.width - (axisConfig.margin.left + axisConfig.margin.right + radius * 2 + (legendBBox ? legendBBox.width : 0))) / 2, (axisConfig.height - (axisConfig.margin.top + axisConfig.margin.bottom + radius * 2)) / 2 ];
            centeringOffset[0] = Math.max(0, centeringOffset[0]);
            centeringOffset[1] = Math.max(0, centeringOffset[1]);
            svg.select('.outer-group').attr('transform', 'translate(' + centeringOffset + ')');
            if (axisConfig.title && axisConfig.title.text) {
                var title = svg.select('g.title-group text').style(fontStyle).text(axisConfig.title.text);
                var titleBBox = title.node().getBBox();
                title.attr({
                    x: chartCenter[0] - titleBBox.width / 2,
                    y: chartCenter[1] - radius - 20
                });
            }
            var radialAxis = svg.select('.radial.axis-group');
            if (axisConfig.radialAxis.gridLinesVisible) {
                var gridCircles = radialAxis.selectAll('circle.grid-circle').data(radialScale.ticks(5));
                gridCircles.enter().append('circle').attr({
                    'class': 'grid-circle'
                }).style(lineStyle);
                gridCircles.attr('r', radialScale);
                gridCircles.exit().remove();
            }
            radialAxis.select('circle.outside-circle').attr({
                r: radius
            }).style(lineStyle);
            var backgroundCircle = svg.select('circle.background-circle').attr({
                r: radius
            }).style({
                fill: axisConfig.backgroundColor,
                stroke: axisConfig.stroke
            });
            function currentAngle(d, i) {
                return angularScale(d) % 360 + axisConfig.orientation;
            }
            if (axisConfig.radialAxis.visible) {
                var axis = d3.svg.axis().scale(radialScale).ticks(5).tickSize(5);
                radialAxis.call(axis).attr({
                    transform: 'rotate(' + axisConfig.radialAxis.orientation + ')'
                });
                radialAxis.selectAll('.domain').style(lineStyle);
                radialAxis.selectAll('g>text').text(function(d, i) {
                    return this.textContent + axisConfig.radialAxis.ticksSuffix;
                }).style(fontStyle).style({
                    'text-anchor': 'start'
                }).attr({
                    x: 0,
                    y: 0,
                    dx: 0,
                    dy: 0,
                    transform: function(d, i) {
                        if (axisConfig.radialAxis.tickOrientation === 'horizontal') {
                            return 'rotate(' + -axisConfig.radialAxis.orientation + ') translate(' + [ 0, fontStyle['font-size'] ] + ')';
                        } else return 'translate(' + [ 0, fontStyle['font-size'] ] + ')';
                    }
                });
                radialAxis.selectAll('g>line').style({
                    stroke: 'black'
                });
            }
            var angularAxis = svg.select('.angular.axis-group').selectAll('g.angular-tick').data(angularAxisRange);
            var angularAxisEnter = angularAxis.enter().append('g').classed('angular-tick', true);
            angularAxis.attr({
                transform: function(d, i) {
                    return 'rotate(' + currentAngle(d, i) + ')';
                }
            }).style({
                display: axisConfig.angularAxis.visible ? 'block' : 'none'
            });
            angularAxis.exit().remove();
            angularAxisEnter.append('line').classed('grid-line', true).classed('major', function(d, i) {
                return i % (axisConfig.minorTicks + 1) == 0;
            }).classed('minor', function(d, i) {
                return !(i % (axisConfig.minorTicks + 1) == 0);
            }).style(lineStyle);
            angularAxisEnter.selectAll('.minor').style({
                stroke: axisConfig.minorTickColor
            });
            angularAxis.select('line.grid-line').attr({
                x1: axisConfig.tickLength ? radius - axisConfig.tickLength : 0,
                x2: radius
            }).style({
                display: axisConfig.angularAxis.gridLinesVisible ? 'block' : 'none'
            });
            angularAxisEnter.append('text').classed('axis-text', true).style(fontStyle);
            var ticksText = angularAxis.select('text.axis-text').attr({
                x: radius + axisConfig.labelOffset,
                dy: MID_SHIFT + 'em',
                transform: function(d, i) {
                    var angle = currentAngle(d, i);
                    var rad = radius + axisConfig.labelOffset;
                    var orient = axisConfig.angularAxis.tickOrientation;
                    if (orient == 'horizontal') return 'rotate(' + -angle + ' ' + rad + ' 0)'; else if (orient == 'radial') return angle < 270 && angle > 90 ? 'rotate(180 ' + rad + ' 0)' : null; else return 'rotate(' + (angle <= 180 && angle > 0 ? -90 : 90) + ' ' + rad + ' 0)';
                }
            }).style({
                'text-anchor': 'middle',
                display: axisConfig.angularAxis.labelsVisible ? 'block' : 'none'
            }).text(function(d, i) {
                if (i % (axisConfig.minorTicks + 1) != 0) return '';
                if (ticks) {
                    return ticks[d] + axisConfig.angularAxis.ticksSuffix;
                } else return d + axisConfig.angularAxis.ticksSuffix;
            }).style(fontStyle);
            if (axisConfig.angularAxis.rewriteTicks) ticksText.text(function(d, i) {
                if (i % (axisConfig.minorTicks + 1) != 0) return '';
                return axisConfig.angularAxis.rewriteTicks(this.textContent, i);
            });
            var rightmostTickEndX = d3.max(chartGroup.selectAll('.angular-tick text')[0].map(function(d, i) {
                return d.getCTM().e + d.getBBox().width;
            }));
            legendContainer.attr({
                transform: 'translate(' + [ radius + rightmostTickEndX, axisConfig.margin.top ] + ')'
            });
            var hasGeometry = svg.select('g.geometry-group').selectAll('g').size() > 0;
            var geometryContainer = svg.select('g.geometry-group').selectAll('g.geometry').data(data);
            geometryContainer.enter().append('g').attr({
                'class': function(d, i) {
                    return 'geometry geometry' + i;
                }
            });
            geometryContainer.exit().remove();
            if (data[0] || hasGeometry) {
                var geometryConfigs = [];
                data.forEach(function(d, i) {
                    var geometryConfig = {};
                    geometryConfig.radialScale = radialScale;
                    geometryConfig.angularScale = angularScale;
                    geometryConfig.container = geometryContainer.filter(function(dB, iB) {
                        return iB == i;
                    });
                    geometryConfig.geometry = d.geometry;
                    geometryConfig.orientation = axisConfig.orientation;
                    geometryConfig.direction = axisConfig.direction;
                    geometryConfig.index = i;
                    geometryConfigs.push({
                        data: d,
                        geometryConfig: geometryConfig
                    });
                });
                var geometryConfigsGrouped = d3.nest().key(function(d, i) {
                    return typeof d.data.groupId != 'undefined' || 'unstacked';
                }).entries(geometryConfigs);
                var geometryConfigsGrouped2 = [];
                geometryConfigsGrouped.forEach(function(d, i) {
                    if (d.key === 'unstacked') geometryConfigsGrouped2 = geometryConfigsGrouped2.concat(d.values.map(function(d, i) {
                        return [ d ];
                    })); else geometryConfigsGrouped2.push(d.values);
                });
                geometryConfigsGrouped2.forEach(function(d, i) {
                    var geometry;
                    if (Array.isArray(d)) geometry = d[0].geometryConfig.geometry; else geometry = d.geometryConfig.geometry;
                    var finalGeometryConfig = d.map(function(dB, iB) {
                        return extendDeepAll(µ[geometry].defaultConfig(), dB);
                    });
                    µ[geometry]().config(finalGeometryConfig)();
                });
            }
            var guides = svg.select('.guides-group');
            var tooltipContainer = svg.select('.tooltips-group');
            var angularTooltip = µ.tooltipPanel().config({
                container: tooltipContainer,
                fontSize: 8
            })();
            var radialTooltip = µ.tooltipPanel().config({
                container: tooltipContainer,
                fontSize: 8
            })();
            var geometryTooltip = µ.tooltipPanel().config({
                container: tooltipContainer,
                hasTick: true
            })();
            var angularValue, radialValue;
            if (!isOrdinal) {
                var angularGuideLine = guides.select('line').attr({
                    x1: 0,
                    y1: 0,
                    y2: 0
                }).style({
                    stroke: 'grey',
                    'pointer-events': 'none'
                });
                chartGroup.on('mousemove.angular-guide', function(d, i) {
                    var mouseAngle = µ.util.getMousePos(backgroundCircle).angle;
                    angularGuideLine.attr({
                        x2: -radius,
                        transform: 'rotate(' + mouseAngle + ')'
                    }).style({
                        opacity: .5
                    });
                    var angleWithOriginOffset = (mouseAngle + 180 + 360 - axisConfig.orientation) % 360;
                    angularValue = angularScale.invert(angleWithOriginOffset);
                    var pos = µ.util.convertToCartesian(radius + 12, mouseAngle + 180);
                    angularTooltip.text(µ.util.round(angularValue)).move([ pos[0] + chartCenter[0], pos[1] + chartCenter[1] ]);
                }).on('mouseout.angular-guide', function(d, i) {
                    guides.select('line').style({
                        opacity: 0
                    });
                });
            }
            var angularGuideCircle = guides.select('circle').style({
                stroke: 'grey',
                fill: 'none'
            });
            chartGroup.on('mousemove.radial-guide', function(d, i) {
                var r = µ.util.getMousePos(backgroundCircle).radius;
                angularGuideCircle.attr({
                    r: r
                }).style({
                    opacity: .5
                });
                radialValue = radialScale.invert(µ.util.getMousePos(backgroundCircle).radius);
                var pos = µ.util.convertToCartesian(r, axisConfig.radialAxis.orientation);
                radialTooltip.text(µ.util.round(radialValue)).move([ pos[0] + chartCenter[0], pos[1] + chartCenter[1] ]);
            }).on('mouseout.radial-guide', function(d, i) {
                angularGuideCircle.style({
                    opacity: 0
                });
                geometryTooltip.hide();
                angularTooltip.hide();
                radialTooltip.hide();
            });
            svg.selectAll('.geometry-group .mark').on('mouseover.tooltip', function(d, i) {
                var el = d3.select(this);
                var color = this.style.fill;
                var newColor = 'black';
                var opacity = this.style.opacity || 1;
                el.attr({
                    'data-opacity': opacity
                });
                if (color && color !== 'none') {
                    el.attr({
                        'data-fill': color
                    });
                    newColor = d3.hsl(color).darker().toString();
                    el.style({
                        fill: newColor,
                        opacity: 1
                    });
                    var textData = {
                        t: µ.util.round(d[0]),
                        r: µ.util.round(d[1])
                    };
                    if (isOrdinal) textData.t = ticks[d[0]];
                    var text = 't: ' + textData.t + ', r: ' + textData.r;
                    var bbox = this.getBoundingClientRect();
                    var svgBBox = svg.node().getBoundingClientRect();
                    var pos = [ bbox.left + bbox.width / 2 - centeringOffset[0] - svgBBox.left, bbox.top + bbox.height / 2 - centeringOffset[1] - svgBBox.top ];
                    geometryTooltip.config({
                        color: newColor
                    }).text(text);
                    geometryTooltip.move(pos);
                } else {
                    color = this.style.stroke || 'black';
                    el.attr({
                        'data-stroke': color
                    });
                    newColor = d3.hsl(color).darker().toString();
                    el.style({
                        stroke: newColor,
                        opacity: 1
                    });
                }
            }).on('mousemove.tooltip', function(d, i) {
                if (d3.event.which != 0) return false;
                if (d3.select(this).attr('data-fill')) geometryTooltip.show();
            }).on('mouseout.tooltip', function(d, i) {
                geometryTooltip.hide();
                var el = d3.select(this);
                var fillColor = el.attr('data-fill');
                if (fillColor) el.style({
                    fill: fillColor,
                    opacity: el.attr('data-opacity')
                }); else el.style({
                    stroke: el.attr('data-stroke'),
                    opacity: el.attr('data-opacity')
                });
            });
        });
        return exports;
    }
    exports.render = function(_container) {
        render(_container);
        return this;
    };
    exports.config = function(_x) {
        if (!arguments.length) return config;
        var xClone = µ.util.cloneJson(_x);
        xClone.data.forEach(function(d, i) {
            if (!config.data[i]) config.data[i] = {};
            extendDeepAll(config.data[i], µ.Axis.defaultConfig().data[0]);
            extendDeepAll(config.data[i], d);
        });
        extendDeepAll(config.layout, µ.Axis.defaultConfig().layout);
        extendDeepAll(config.layout, xClone.layout);
        return this;
    };
    exports.getLiveConfig = function() {
        return liveConfig;
    };
    exports.getinputConfig = function() {
        return inputConfig;
    };
    exports.radialScale = function(_x) {
        return radialScale;
    };
    exports.angularScale = function(_x) {
        return angularScale;
    };
    exports.svg = function() {
        return svg;
    };
    d3.rebind(exports, dispatch, 'on');
    return exports;
};

µ.Axis.defaultConfig = function(d, i) {
    var config = {
        data: [ {
            t: [ 1, 2, 3, 4 ],
            r: [ 10, 11, 12, 13 ],
            name: 'Line1',
            geometry: 'LinePlot',
            color: null,
            strokeDash: 'solid',
            strokeColor: null,
            strokeSize: '1',
            visibleInLegend: true,
            opacity: 1
        } ],
        layout: {
            defaultColorRange: d3.scale.category10().range(),
            title: null,
            height: 450,
            width: 500,
            margin: {
                top: 40,
                right: 40,
                bottom: 40,
                left: 40
            },
            font: {
                size: 12,
                color: 'gray',
                outlineColor: 'white',
                family: 'Tahoma, sans-serif'
            },
            direction: 'clockwise',
            orientation: 0,
            labelOffset: 10,
            radialAxis: {
                domain: null,
                orientation: -45,
                ticksSuffix: '',
                visible: true,
                gridLinesVisible: true,
                tickOrientation: 'horizontal',
                rewriteTicks: null
            },
            angularAxis: {
                domain: [ 0, 360 ],
                ticksSuffix: '',
                visible: true,
                gridLinesVisible: true,
                labelsVisible: true,
                tickOrientation: 'horizontal',
                rewriteTicks: null,
                ticksCount: null,
                ticksStep: null
            },
            minorTicks: 0,
            tickLength: null,
            tickColor: 'silver',
            minorTickColor: '#eee',
            backgroundColor: 'none',
            needsEndSpacing: null,
            showLegend: true,
            legend: {
                reverseOrder: false
            },
            opacity: 1
        }
    };
    return config;
};

µ.util = {};

µ.DATAEXTENT = 'dataExtent';

µ.AREA = 'AreaChart';

µ.LINE = 'LinePlot';

µ.DOT = 'DotPlot';

µ.BAR = 'BarChart';

µ.util._override = function(_objA, _objB) {
    for (var x in _objA) if (x in _objB) _objB[x] = _objA[x];
};

µ.util._extend = function(_objA, _objB) {
    for (var x in _objA) _objB[x] = _objA[x];
};

µ.util._rndSnd = function() {
    return Math.random() * 2 - 1 + (Math.random() * 2 - 1) + (Math.random() * 2 - 1);
};

µ.util.dataFromEquation2 = function(_equation, _step) {
    var step = _step || 6;
    var data = d3.range(0, 360 + step, step).map(function(deg, index) {
        var theta = deg * Math.PI / 180;
        var radius = _equation(theta);
        return [ deg, radius ];
    });
    return data;
};

µ.util.dataFromEquation = function(_equation, _step, _name) {
    var step = _step || 6;
    var t = [], r = [];
    d3.range(0, 360 + step, step).forEach(function(deg, index) {
        var theta = deg * Math.PI / 180;
        var radius = _equation(theta);
        t.push(deg);
        r.push(radius);
    });
    var result = {
        t: t,
        r: r
    };
    if (_name) result.name = _name;
    return result;
};

µ.util.ensureArray = function(_val, _count) {
    if (typeof _val === 'undefined') return null;
    var arr = [].concat(_val);
    return d3.range(_count).map(function(d, i) {
        return arr[i] || arr[0];
    });
};

µ.util.fillArrays = function(_obj, _valueNames, _count) {
    _valueNames.forEach(function(d, i) {
        _obj[d] = µ.util.ensureArray(_obj[d], _count);
    });
    return _obj;
};

µ.util.cloneJson = function(json) {
    return JSON.parse(JSON.stringify(json));
};

µ.util.validateKeys = function(obj, keys) {
    if (typeof keys === 'string') keys = keys.split('.');
    var next = keys.shift();
    return obj[next] && (!keys.length || objHasKeys(obj[next], keys));
};

µ.util.sumArrays = function(a, b) {
    return d3.zip(a, b).map(function(d, i) {
        return d3.sum(d);
    });
};

µ.util.arrayLast = function(a) {
    return a[a.length - 1];
};

µ.util.arrayEqual = function(a, b) {
    var i = Math.max(a.length, b.length, 1);
    while (i-- >= 0 && a[i] === b[i]) ;
    return i === -2;
};

µ.util.flattenArray = function(arr) {
    var r = [];
    while (!µ.util.arrayEqual(r, arr)) {
        r = arr;
        arr = [].concat.apply([], arr);
    }
    return arr;
};

µ.util.deduplicate = function(arr) {
    return arr.filter(function(v, i, a) {
        return a.indexOf(v) == i;
    });
};

µ.util.convertToCartesian = function(radius, theta) {
    var thetaRadians = theta * Math.PI / 180;
    var x = radius * Math.cos(thetaRadians);
    var y = radius * Math.sin(thetaRadians);
    return [ x, y ];
};

µ.util.round = function(_value, _digits) {
    var digits = _digits || 2;
    var mult = Math.pow(10, digits);
    return Math.round(_value * mult) / mult;
};

µ.util.getMousePos = function(_referenceElement) {
    var mousePos = d3.mouse(_referenceElement.node());
    var mouseX = mousePos[0];
    var mouseY = mousePos[1];
    var mouse = {};
    mouse.x = mouseX;
    mouse.y = mouseY;
    mouse.pos = mousePos;
    mouse.angle = (Math.atan2(mouseY, mouseX) + Math.PI) * 180 / Math.PI;
    mouse.radius = Math.sqrt(mouseX * mouseX + mouseY * mouseY);
    return mouse;
};

µ.util.duplicatesCount = function(arr) {
    var uniques = {}, val;
    var dups = {};
    for (var i = 0, len = arr.length; i < len; i++) {
        val = arr[i];
        if (val in uniques) {
            uniques[val]++;
            dups[val] = uniques[val];
        } else {
            uniques[val] = 1;
        }
    }
    return dups;
};

µ.util.duplicates = function(arr) {
    return Object.keys(µ.util.duplicatesCount(arr));
};

µ.util.translator = function(obj, sourceBranch, targetBranch, reverse) {
    if (reverse) {
        var targetBranchCopy = targetBranch.slice();
        targetBranch = sourceBranch;
        sourceBranch = targetBranchCopy;
    }
    var value = sourceBranch.reduce(function(previousValue, currentValue) {
        if (typeof previousValue != 'undefined') return previousValue[currentValue];
    }, obj);
    if (typeof value === 'undefined') return;
    sourceBranch.reduce(function(previousValue, currentValue, index) {
        if (typeof previousValue == 'undefined') return;
        if (index === sourceBranch.length - 1) delete previousValue[currentValue];
        return previousValue[currentValue];
    }, obj);
    targetBranch.reduce(function(previousValue, currentValue, index) {
        if (typeof previousValue[currentValue] === 'undefined') previousValue[currentValue] = {};
        if (index === targetBranch.length - 1) previousValue[currentValue] = value;
        return previousValue[currentValue];
    }, obj);
};

µ.PolyChart = function module() {
    var config = [ µ.PolyChart.defaultConfig() ];
    var dispatch = d3.dispatch('hover');
    var dashArray = {
        solid: 'none',
        dash: [ 5, 2 ],
        dot: [ 2, 5 ]
    };
    var colorScale;
    function exports() {
        var geometryConfig = config[0].geometryConfig;
        var container = geometryConfig.container;
        if (typeof container == 'string') container = d3.select(container);
        container.datum(config).each(function(_config, _index) {
            var isStack = !!_config[0].data.yStack;
            var data = _config.map(function(d, i) {
                if (isStack) return d3.zip(d.data.t[0], d.data.r[0], d.data.yStack[0]); else return d3.zip(d.data.t[0], d.data.r[0]);
            });
            var angularScale = geometryConfig.angularScale;
            var domainMin = geometryConfig.radialScale.domain()[0];
            var generator = {};
            generator.bar = function(d, i, pI) {
                var dataConfig = _config[pI].data;
                var h = geometryConfig.radialScale(d[1]) - geometryConfig.radialScale(0);
                var stackTop = geometryConfig.radialScale(d[2] || 0);
                var w = dataConfig.barWidth;
                d3.select(this).attr({
                    'class': 'mark bar',
                    d: 'M' + [ [ h + stackTop, -w / 2 ], [ h + stackTop, w / 2 ], [ stackTop, w / 2 ], [ stackTop, -w / 2 ] ].join('L') + 'Z',
                    transform: function(d, i) {
                        return 'rotate(' + (geometryConfig.orientation + angularScale(d[0])) + ')';
                    }
                });
            };
            generator.dot = function(d, i, pI) {
                var stackedData = d[2] ? [ d[0], d[1] + d[2] ] : d;
                var symbol = d3.svg.symbol().size(_config[pI].data.dotSize).type(_config[pI].data.dotType)(d, i);
                d3.select(this).attr({
                    'class': 'mark dot',
                    d: symbol,
                    transform: function(d, i) {
                        var coord = convertToCartesian(getPolarCoordinates(stackedData));
                        return 'translate(' + [ coord.x, coord.y ] + ')';
                    }
                });
            };
            var line = d3.svg.line.radial().interpolate(_config[0].data.lineInterpolation).radius(function(d) {
                return geometryConfig.radialScale(d[1]);
            }).angle(function(d) {
                return geometryConfig.angularScale(d[0]) * Math.PI / 180;
            });
            generator.line = function(d, i, pI) {
                var lineData = d[2] ? data[pI].map(function(d, i) {
                    return [ d[0], d[1] + d[2] ];
                }) : data[pI];
                d3.select(this).each(generator['dot']).style({
                    opacity: function(dB, iB) {
                        return +_config[pI].data.dotVisible;
                    },
                    fill: markStyle.stroke(d, i, pI)
                }).attr({
                    'class': 'mark dot'
                });
                if (i > 0) return;
                var lineSelection = d3.select(this.parentNode).selectAll('path.line').data([ 0 ]);
                lineSelection.enter().insert('path');
                lineSelection.attr({
                    'class': 'line',
                    d: line(lineData),
                    transform: function(dB, iB) {
                        return 'rotate(' + (geometryConfig.orientation + 90) + ')';
                    },
                    'pointer-events': 'none'
                }).style({
                    fill: function(dB, iB) {
                        return markStyle.fill(d, i, pI);
                    },
                    'fill-opacity': 0,
                    stroke: function(dB, iB) {
                        return markStyle.stroke(d, i, pI);
                    },
                    'stroke-width': function(dB, iB) {
                        return markStyle['stroke-width'](d, i, pI);
                    },
                    'stroke-dasharray': function(dB, iB) {
                        return markStyle['stroke-dasharray'](d, i, pI);
                    },
                    opacity: function(dB, iB) {
                        return markStyle.opacity(d, i, pI);
                    },
                    display: function(dB, iB) {
                        return markStyle.display(d, i, pI);
                    }
                });
            };
            var angularRange = geometryConfig.angularScale.range();
            var triangleAngle = Math.abs(angularRange[1] - angularRange[0]) / data[0].length * Math.PI / 180;
            var arc = d3.svg.arc().startAngle(function(d) {
                return -triangleAngle / 2;
            }).endAngle(function(d) {
                return triangleAngle / 2;
            }).innerRadius(function(d) {
                return geometryConfig.radialScale(domainMin + (d[2] || 0));
            }).outerRadius(function(d) {
                return geometryConfig.radialScale(domainMin + (d[2] || 0)) + geometryConfig.radialScale(d[1]);
            });
            generator.arc = function(d, i, pI) {
                d3.select(this).attr({
                    'class': 'mark arc',
                    d: arc,
                    transform: function(d, i) {
                        return 'rotate(' + (geometryConfig.orientation + angularScale(d[0]) + 90) + ')';
                    }
                });
            };
            var markStyle = {
                fill: function(d, i, pI) {
                    return _config[pI].data.color;
                },
                stroke: function(d, i, pI) {
                    return _config[pI].data.strokeColor;
                },
                'stroke-width': function(d, i, pI) {
                    return _config[pI].data.strokeSize + 'px';
                },
                'stroke-dasharray': function(d, i, pI) {
                    return dashArray[_config[pI].data.strokeDash];
                },
                opacity: function(d, i, pI) {
                    return _config[pI].data.opacity;
                },
                display: function(d, i, pI) {
                    return typeof _config[pI].data.visible === 'undefined' || _config[pI].data.visible ? 'block' : 'none';
                }
            };
            var geometryLayer = d3.select(this).selectAll('g.layer').data(data);
            geometryLayer.enter().append('g').attr({
                'class': 'layer'
            });
            var geometry = geometryLayer.selectAll('path.mark').data(function(d, i) {
                return d;
            });
            geometry.enter().append('path').attr({
                'class': 'mark'
            });
            geometry.style(markStyle).each(generator[geometryConfig.geometryType]);
            geometry.exit().remove();
            geometryLayer.exit().remove();
            function getPolarCoordinates(d, i) {
                var r = geometryConfig.radialScale(d[1]);
                var t = (geometryConfig.angularScale(d[0]) + geometryConfig.orientation) * Math.PI / 180;
                return {
                    r: r,
                    t: t
                };
            }
            function convertToCartesian(polarCoordinates) {
                var x = polarCoordinates.r * Math.cos(polarCoordinates.t);
                var y = polarCoordinates.r * Math.sin(polarCoordinates.t);
                return {
                    x: x,
                    y: y
                };
            }
        });
    }
    exports.config = function(_x) {
        if (!arguments.length) return config;
        _x.forEach(function(d, i) {
            if (!config[i]) config[i] = {};
            extendDeepAll(config[i], µ.PolyChart.defaultConfig());
            extendDeepAll(config[i], d);
        });
        return this;
    };
    exports.getColorScale = function() {
        return colorScale;
    };
    d3.rebind(exports, dispatch, 'on');
    return exports;
};

µ.PolyChart.defaultConfig = function() {
    var config = {
        data: {
            name: 'geom1',
            t: [ [ 1, 2, 3, 4 ] ],
            r: [ [ 1, 2, 3, 4 ] ],
            dotType: 'circle',
            dotSize: 64,
            dotVisible: false,
            barWidth: 20,
            color: '#ffa500',
            strokeSize: 1,
            strokeColor: 'silver',
            strokeDash: 'solid',
            opacity: 1,
            index: 0,
            visible: true,
            visibleInLegend: true
        },
        geometryConfig: {
            geometry: 'LinePlot',
            geometryType: 'arc',
            direction: 'clockwise',
            orientation: 0,
            container: 'body',
            radialScale: null,
            angularScale: null,
            colorScale: d3.scale.category20()
        }
    };
    return config;
};

µ.BarChart = function module() {
    return µ.PolyChart();
};

µ.BarChart.defaultConfig = function() {
    var config = {
        geometryConfig: {
            geometryType: 'bar'
        }
    };
    return config;
};

µ.AreaChart = function module() {
    return µ.PolyChart();
};

µ.AreaChart.defaultConfig = function() {
    var config = {
        geometryConfig: {
            geometryType: 'arc'
        }
    };
    return config;
};

µ.DotPlot = function module() {
    return µ.PolyChart();
};

µ.DotPlot.defaultConfig = function() {
    var config = {
        geometryConfig: {
            geometryType: 'dot',
            dotType: 'circle'
        }
    };
    return config;
};

µ.LinePlot = function module() {
    return µ.PolyChart();
};

µ.LinePlot.defaultConfig = function() {
    var config = {
        geometryConfig: {
            geometryType: 'line'
        }
    };
    return config;
};

µ.Legend = function module() {
    var config = µ.Legend.defaultConfig();
    var dispatch = d3.dispatch('hover');
    function exports() {
        var legendConfig = config.legendConfig;
        var flattenData = config.data.map(function(d, i) {
            return [].concat(d).map(function(dB, iB) {
                var element = extendDeepAll({}, legendConfig.elements[i]);
                element.name = dB;
                element.color = [].concat(legendConfig.elements[i].color)[iB];
                return element;
            });
        });
        var data = d3.merge(flattenData);
        data = data.filter(function(d, i) {
            return legendConfig.elements[i] && (legendConfig.elements[i].visibleInLegend || typeof legendConfig.elements[i].visibleInLegend === 'undefined');
        });
        if (legendConfig.reverseOrder) data = data.reverse();
        var container = legendConfig.container;
        if (typeof container == 'string' || container.nodeName) container = d3.select(container);
        var colors = data.map(function(d, i) {
            return d.color;
        });
        var lineHeight = legendConfig.fontSize;
        var isContinuous = legendConfig.isContinuous == null ? typeof data[0] === 'number' : legendConfig.isContinuous;
        var height = isContinuous ? legendConfig.height : lineHeight * data.length;
        var legendContainerGroup = container.classed('legend-group', true);
        var svg = legendContainerGroup.selectAll('svg').data([ 0 ]);
        var svgEnter = svg.enter().append('svg').attr({
            width: 300,
            height: height + lineHeight,
            xmlns: 'http://www.w3.org/2000/svg',
            'xmlns:xlink': 'http://www.w3.org/1999/xlink',
            version: '1.1'
        });
        svgEnter.append('g').classed('legend-axis', true);
        svgEnter.append('g').classed('legend-marks', true);
        var dataNumbered = d3.range(data.length);
        var colorScale = d3.scale[isContinuous ? 'linear' : 'ordinal']().domain(dataNumbered).range(colors);
        var dataScale = d3.scale[isContinuous ? 'linear' : 'ordinal']().domain(dataNumbered)[isContinuous ? 'range' : 'rangePoints']([ 0, height ]);
        var shapeGenerator = function(_type, _size) {
            var squareSize = _size * 3;
            if (_type === 'line') {
                return 'M' + [ [ -_size / 2, -_size / 12 ], [ _size / 2, -_size / 12 ], [ _size / 2, _size / 12 ], [ -_size / 2, _size / 12 ] ] + 'Z';
            } else if (d3.svg.symbolTypes.indexOf(_type) != -1) return d3.svg.symbol().type(_type).size(squareSize)(); else return d3.svg.symbol().type('square').size(squareSize)();
        };
        if (isContinuous) {
            var gradient = svg.select('.legend-marks').append('defs').append('linearGradient').attr({
                id: 'grad1',
                x1: '0%',
                y1: '0%',
                x2: '0%',
                y2: '100%'
            }).selectAll('stop').data(colors);
            gradient.enter().append('stop');
            gradient.attr({
                offset: function(d, i) {
                    return i / (colors.length - 1) * 100 + '%';
                }
            }).style({
                'stop-color': function(d, i) {
                    return d;
                }
            });
            svg.append('rect').classed('legend-mark', true).attr({
                height: legendConfig.height,
                width: legendConfig.colorBandWidth,
                fill: 'url(#grad1)'
            });
        } else {
            var legendElement = svg.select('.legend-marks').selectAll('path.legend-mark').data(data);
            legendElement.enter().append('path').classed('legend-mark', true);
            legendElement.attr({
                transform: function(d, i) {
                    return 'translate(' + [ lineHeight / 2, dataScale(i) + lineHeight / 2 ] + ')';
                },
                d: function(d, i) {
                    var symbolType = d.symbol;
                    return shapeGenerator(symbolType, lineHeight);
                },
                fill: function(d, i) {
                    return colorScale(i);
                }
            });
            legendElement.exit().remove();
        }
        var legendAxis = d3.svg.axis().scale(dataScale).orient('right');
        var axis = svg.select('g.legend-axis').attr({
            transform: 'translate(' + [ isContinuous ? legendConfig.colorBandWidth : lineHeight, lineHeight / 2 ] + ')'
        }).call(legendAxis);
        axis.selectAll('.domain').style({
            fill: 'none',
            stroke: 'none'
        });
        axis.selectAll('line').style({
            fill: 'none',
            stroke: isContinuous ? legendConfig.textColor : 'none'
        });
        axis.selectAll('text').style({
            fill: legendConfig.textColor,
            'font-size': legendConfig.fontSize
        }).text(function(d, i) {
            return data[i].name;
        });
        return exports;
    }
    exports.config = function(_x) {
        if (!arguments.length) return config;
        extendDeepAll(config, _x);
        return this;
    };
    d3.rebind(exports, dispatch, 'on');
    return exports;
};

µ.Legend.defaultConfig = function(d, i) {
    var config = {
        data: [ 'a', 'b', 'c' ],
        legendConfig: {
            elements: [ {
                symbol: 'line',
                color: 'red'
            }, {
                symbol: 'square',
                color: 'yellow'
            }, {
                symbol: 'diamond',
                color: 'limegreen'
            } ],
            height: 150,
            colorBandWidth: 30,
            fontSize: 12,
            container: 'body',
            isContinuous: null,
            textColor: 'grey',
            reverseOrder: false
        }
    };
    return config;
};

µ.tooltipPanel = function() {
    var tooltipEl, tooltipTextEl, backgroundEl;
    var config = {
        container: null,
        hasTick: false,
        fontSize: 12,
        color: 'white',
        padding: 5
    };
    var id = 'tooltip-' + µ.tooltipPanel.uid++;
    var tickSize = 10;
    var exports = function() {
        tooltipEl = config.container.selectAll('g.' + id).data([ 0 ]);
        var tooltipEnter = tooltipEl.enter().append('g').classed(id, true).style({
            'pointer-events': 'none',
            display: 'none'
        });
        backgroundEl = tooltipEnter.append('path').style({
            fill: 'white',
            'fill-opacity': .9
        }).attr({
            d: 'M0 0'
        });
        tooltipTextEl = tooltipEnter.append('text').attr({
            dx: config.padding + tickSize,
            dy: +config.fontSize * .3
        });
        return exports;
    };
    exports.text = function(_text) {
        var l = d3.hsl(config.color).l;
        var strokeColor = l >= .5 ? '#aaa' : 'white';
        var fillColor = l >= .5 ? 'black' : 'white';
        var text = _text || '';
        tooltipTextEl.style({
            fill: fillColor,
            'font-size': config.fontSize + 'px'
        }).text(text);
        var padding = config.padding;
        var bbox = tooltipTextEl.node().getBBox();
        var boxStyle = {
            fill: config.color,
            stroke: strokeColor,
            'stroke-width': '2px'
        };
        var backGroundW = bbox.width + padding * 2 + tickSize;
        var backGroundH = bbox.height + padding * 2;
        backgroundEl.attr({
            d: 'M' + [ [ tickSize, -backGroundH / 2 ], [ tickSize, -backGroundH / 4 ], [ config.hasTick ? 0 : tickSize, 0 ], [ tickSize, backGroundH / 4 ], [ tickSize, backGroundH / 2 ], [ backGroundW, backGroundH / 2 ], [ backGroundW, -backGroundH / 2 ] ].join('L') + 'Z'
        }).style(boxStyle);
        tooltipEl.attr({
            transform: 'translate(' + [ tickSize, -backGroundH / 2 + padding * 2 ] + ')'
        });
        tooltipEl.style({
            display: 'block'
        });
        return exports;
    };
    exports.move = function(_pos) {
        if (!tooltipEl) return;
        tooltipEl.attr({
            transform: 'translate(' + [ _pos[0], _pos[1] ] + ')'
        }).style({
            display: 'block'
        });
        return exports;
    };
    exports.hide = function() {
        if (!tooltipEl) return;
        tooltipEl.style({
            display: 'none'
        });
        return exports;
    };
    exports.show = function() {
        if (!tooltipEl) return;
        tooltipEl.style({
            display: 'block'
        });
        return exports;
    };
    exports.config = function(_x) {
        extendDeepAll(config, _x);
        return exports;
    };
    return exports;
};

µ.tooltipPanel.uid = 1;

µ.adapter = {};

µ.adapter.plotly = function module() {
    var exports = {};
    exports.convert = function(_inputConfig, reverse) {
        var outputConfig = {};
        if (_inputConfig.data) {
            outputConfig.data = _inputConfig.data.map(function(d, i) {
                var r = extendDeepAll({}, d);
                var toTranslate = [
                    [ r, [ 'marker', 'color' ], [ 'color' ] ],
                    [ r, [ 'marker', 'opacity' ], [ 'opacity' ] ],
                    [ r, [ 'marker', 'line', 'color' ], [ 'strokeColor' ] ],
                    [ r, [ 'marker', 'line', 'dash' ], [ 'strokeDash' ] ],
                    [ r, [ 'marker', 'line', 'width' ], [ 'strokeSize' ] ],
                    [ r, [ 'marker', 'symbol' ], [ 'dotType' ] ],
                    [ r, [ 'marker', 'size' ], [ 'dotSize' ] ],
                    [ r, [ 'marker', 'barWidth' ], [ 'barWidth' ] ],
                    [ r, [ 'line', 'interpolation' ], [ 'lineInterpolation' ] ],
                    [ r, [ 'showlegend' ], [ 'visibleInLegend' ] ]
                ];
                toTranslate.forEach(function(d, i) {
                    µ.util.translator.apply(null, d.concat(reverse));
                });

                if (!reverse) delete r.marker;
                if (reverse) delete r.groupId;
                if (!reverse) {
                    if (r.type === 'scatter') {
                        if (r.mode === 'lines') r.geometry = 'LinePlot'; else if (r.mode === 'markers') r.geometry = 'DotPlot'; else if (r.mode === 'lines+markers') {
                            r.geometry = 'LinePlot';
                            r.dotVisible = true;
                        }
                    } else if (r.type === 'area') r.geometry = 'AreaChart'; else if (r.type === 'bar') r.geometry = 'BarChart';
                    delete r.mode;
                    delete r.type;
                } else {
                    if (r.geometry === 'LinePlot') {
                        r.type = 'scatter';
                        if (r.dotVisible === true) {
                            delete r.dotVisible;
                            r.mode = 'lines+markers';
                        } else r.mode = 'lines';
                    } else if (r.geometry === 'DotPlot') {
                        r.type = 'scatter';
                        r.mode = 'markers';
                    } else if (r.geometry === 'AreaChart') r.type = 'area'; else if (r.geometry === 'BarChart') r.type = 'bar';
                    delete r.geometry;
                }
                return r;
            });
            if (!reverse && _inputConfig.layout && _inputConfig.layout.barmode === 'stack') {
                var duplicates = µ.util.duplicates(outputConfig.data.map(function(d, i) {
                    return d.geometry;
                }));
                outputConfig.data.forEach(function(d, i) {
                    var idx = duplicates.indexOf(d.geometry);
                    if (idx != -1) outputConfig.data[i].groupId = idx;
                });
            }
        }
        if (_inputConfig.layout) {
            var r = extendDeepAll({}, _inputConfig.layout);
            var toTranslate = [
                [ r, [ 'plot_bgcolor' ], [ 'backgroundColor' ] ],
                [ r, [ 'showlegend' ], [ 'showLegend' ] ],
                [ r, [ 'radialaxis' ], [ 'radialAxis' ] ],
                [ r, [ 'angularaxis' ], [ 'angularAxis' ] ],
                [ r.angularaxis, [ 'showline' ], [ 'gridLinesVisible' ] ],
                [ r.angularaxis, [ 'showticklabels' ], [ 'labelsVisible' ] ],
                [ r.angularaxis, [ 'nticks' ], [ 'ticksCount' ] ],
                [ r.angularaxis, [ 'tickorientation' ], [ 'tickOrientation' ] ],
                [ r.angularaxis, [ 'ticksuffix' ], [ 'ticksSuffix' ] ],
                [ r.angularaxis, [ 'range' ], [ 'domain' ] ],
                [ r.angularaxis, [ 'endpadding' ], [ 'endPadding' ] ],
                [ r.radialaxis, [ 'showline' ], [ 'gridLinesVisible' ] ],
                [ r.radialaxis, [ 'tickorientation' ], [ 'tickOrientation' ] ],
                [ r.radialaxis, [ 'ticksuffix' ], [ 'ticksSuffix' ] ],
                [ r.radialaxis, [ 'range' ], [ 'domain' ] ],
                [ r.angularAxis, [ 'showline' ], [ 'gridLinesVisible' ] ],
                [ r.angularAxis, [ 'showticklabels' ], [ 'labelsVisible' ] ],
                [ r.angularAxis, [ 'nticks' ], [ 'ticksCount' ] ],
                [ r.angularAxis, [ 'tickorientation' ], [ 'tickOrientation' ] ],
                [ r.angularAxis, [ 'ticksuffix' ], [ 'ticksSuffix' ] ],
                [ r.angularAxis, [ 'range' ], [ 'domain' ] ],
                [ r.angularAxis, [ 'endpadding' ], [ 'endPadding' ] ],
                [ r.radialAxis, [ 'showline' ], [ 'gridLinesVisible' ] ],
                [ r.radialAxis, [ 'tickorientation' ], [ 'tickOrientation' ] ],
                [ r.radialAxis, [ 'ticksuffix' ], [ 'ticksSuffix' ] ],
                [ r.radialAxis, [ 'range' ], [ 'domain' ] ],
                [ r.font, [ 'outlinecolor' ], [ 'outlineColor' ] ],
                [ r.legend, [ 'traceorder' ], [ 'reverseOrder' ] ],
                [ r, [ 'labeloffset' ], [ 'labelOffset' ] ],
                [ r, [ 'defaultcolorrange' ], [ 'defaultColorRange' ] ]
            ];
            toTranslate.forEach(function(d, i) {
                µ.util.translator.apply(null, d.concat(reverse));
            });

            if (!reverse) {
                if (r.angularAxis && typeof r.angularAxis.ticklen !== 'undefined') r.tickLength = r.angularAxis.ticklen;
                if (r.angularAxis && typeof r.angularAxis.tickcolor !== 'undefined') r.tickColor = r.angularAxis.tickcolor;
            } else {
                if (typeof r.tickLength !== 'undefined') {
                    r.angularaxis.ticklen = r.tickLength;
                    delete r.tickLength;
                }
                if (r.tickColor) {
                    r.angularaxis.tickcolor = r.tickColor;
                    delete r.tickColor;
                }
            }
            if (r.legend && typeof r.legend.reverseOrder != 'boolean') {
                r.legend.reverseOrder = r.legend.reverseOrder != 'normal';
            }
            if (r.legend && typeof r.legend.traceorder == 'boolean') {
                r.legend.traceorder = r.legend.traceorder ? 'reversed' : 'normal';
                delete r.legend.reverseOrder;
            }
            if (r.margin && typeof r.margin.t != 'undefined') {
                var source = [ 't', 'r', 'b', 'l', 'pad' ];
                var target = [ 'top', 'right', 'bottom', 'left', 'pad' ];
                var margin = {};
                d3.entries(r.margin).forEach(function(dB, iB) {
                    margin[target[source.indexOf(dB.key)]] = dB.value;
                });
                r.margin = margin;
            }
            if (reverse) {
                delete r.needsEndSpacing;
                delete r.minorTickColor;
                delete r.minorTicks;
                delete r.angularaxis.ticksCount;
                delete r.angularaxis.ticksCount;
                delete r.angularaxis.ticksStep;
                delete r.angularaxis.rewriteTicks;
                delete r.angularaxis.nticks;
                delete r.radialaxis.ticksCount;
                delete r.radialaxis.ticksCount;
                delete r.radialaxis.ticksStep;
                delete r.radialaxis.rewriteTicks;
                delete r.radialaxis.nticks;
            }
            outputConfig.layout = r;
        }
        return outputConfig;
    };
    return exports;
};
