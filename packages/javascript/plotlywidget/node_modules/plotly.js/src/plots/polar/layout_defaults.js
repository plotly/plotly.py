/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var Lib = require('../../lib');
var Color = require('../../components/color');
var Template = require('../../plot_api/plot_template');

var handleSubplotDefaults = require('../subplot_defaults');
var getSubplotData = require('../get_data').getSubplotData;

var handleTickValueDefaults = require('../cartesian/tick_value_defaults');
var handleTickMarkDefaults = require('../cartesian/tick_mark_defaults');
var handleTickLabelDefaults = require('../cartesian/tick_label_defaults');
var handleCategoryOrderDefaults = require('../cartesian/category_order_defaults');
var handleLineGridDefaults = require('../cartesian/line_grid_defaults');
var autoType = require('../cartesian/axis_autotype');

var layoutAttributes = require('./layout_attributes');
var setConvert = require('./set_convert');
var constants = require('./constants');
var axisNames = constants.axisNames;

function handleDefaults(contIn, contOut, coerce, opts) {
    var bgColor = coerce('bgcolor');
    opts.bgColor = Color.combine(bgColor, opts.paper_bgcolor);

    var sector = coerce('sector');
    coerce('hole');

    // could optimize, subplotData is not always needed!
    var subplotData = getSubplotData(opts.fullData, constants.name, opts.id);
    var layoutOut = opts.layoutOut;
    var axName;

    function coerceAxis(attr, dflt) {
        return coerce(axName + '.' + attr, dflt);
    }

    for(var i = 0; i < axisNames.length; i++) {
        axName = axisNames[i];

        if(!Lib.isPlainObject(contIn[axName])) {
            contIn[axName] = {};
        }

        var axIn = contIn[axName];
        var axOut = Template.newContainer(contOut, axName);
        axOut._id = axOut._name = axName;
        axOut._attr = opts.id + '.' + axName;
        axOut._traceIndices = subplotData.map(function(t) { return t._expandedIndex; });

        var dataAttr = constants.axisName2dataArray[axName];
        var axType = handleAxisTypeDefaults(axIn, axOut, coerceAxis, subplotData, dataAttr);

        handleCategoryOrderDefaults(axIn, axOut, coerceAxis, {
            axData: subplotData,
            dataAttr: dataAttr
        });

        var visible = coerceAxis('visible');
        setConvert(axOut, contOut, layoutOut);

        coerceAxis('uirevision', contOut.uirevision);

        var dfltColor;
        var dfltFontColor;

        if(visible) {
            dfltColor = coerceAxis('color');
            dfltFontColor = (dfltColor === axIn.color) ? dfltColor : opts.font.color;
        }

        // We don't want to make downstream code call ax.setScale,
        // as both radial and angular axes don't have a set domain.
        // Furthermore, angular axes don't have a set range.
        //
        // Mocked domains and ranges are set by the polar subplot instances,
        // but Axes.findExtremes uses the sign of _m to determine which padding value
        // to use.
        //
        // By setting, _m to 1 here, we make Axes.findExtremes think that
        // range[1] > range[0], and vice-versa for `autorange: 'reversed'` below.
        axOut._m = 1;

        switch(axName) {
            case 'radialaxis':
                var autoRange = coerceAxis('autorange', !axOut.isValidRange(axIn.range));
                axIn.autorange = autoRange;
                if(autoRange && (axType === 'linear' || axType === '-')) coerceAxis('rangemode');
                if(autoRange === 'reversed') axOut._m = -1;

                coerceAxis('range');
                axOut.cleanRange('range', {dfltRange: [0, 1]});

                if(visible) {
                    coerceAxis('side');
                    coerceAxis('angle', sector[0]);

                    coerceAxis('title.text');
                    Lib.coerceFont(coerceAxis, 'title.font', {
                        family: opts.font.family,
                        size: Math.round(opts.font.size * 1.2),
                        color: dfltFontColor
                    });
                }
                break;

            case 'angularaxis':
                // We do not support 'true' date angular axes yet,
                // users can still plot dates on angular axes by setting
                // `angularaxis.type: 'category'`.
                //
                // Here, if a date angular axes is detected, we make
                // all its corresponding traces invisible, so that
                // when we do add support for data angular axes, the new
                // behavior won't conflict with existing behavior
                if(axType === 'date') {
                    Lib.log('Polar plots do not support date angular axes yet.');

                    for(var j = 0; j < subplotData.length; j++) {
                        subplotData[j].visible = false;
                    }

                    // turn this into a 'dummy' linear axis so that
                    // the subplot still renders ok
                    axType = axIn.type = axOut.type = 'linear';
                }

                if(axType === 'linear') {
                    coerceAxis('thetaunit');
                } else {
                    coerceAxis('period');
                }

                var direction = coerceAxis('direction');
                coerceAxis('rotation', {counterclockwise: 0, clockwise: 90}[direction]);
                break;
        }

        if(visible) {
            handleTickValueDefaults(axIn, axOut, coerceAxis, axOut.type);
            handleTickLabelDefaults(axIn, axOut, coerceAxis, axOut.type, {
                tickSuffixDflt: axOut.thetaunit === 'degrees' ? '°' : undefined
            });
            handleTickMarkDefaults(axIn, axOut, coerceAxis, {outerTicks: true});

            var showTickLabels = coerceAxis('showticklabels');
            if(showTickLabels) {
                Lib.coerceFont(coerceAxis, 'tickfont', {
                    family: opts.font.family,
                    size: opts.font.size,
                    color: dfltFontColor
                });
                coerceAxis('tickangle');
                coerceAxis('tickformat');
            }

            handleLineGridDefaults(axIn, axOut, coerceAxis, {
                dfltColor: dfltColor,
                bgColor: opts.bgColor,
                // default grid color is darker here (60%, vs cartesian default ~91%)
                // because the grid is not square so the eye needs heavier cues to follow
                blend: 60,
                showLine: true,
                showGrid: true,
                noZeroLine: true,
                attributes: layoutAttributes[axName]
            });

            coerceAxis('layer');
        }

        if(axType !== 'category') coerceAxis('hoverformat');

        axOut._input = axIn;
    }

    if(contOut.angularaxis.type === 'category') {
        coerce('gridshape');
    }
}

function handleAxisTypeDefaults(axIn, axOut, coerce, subplotData, dataAttr) {
    var axType = coerce('type');

    if(axType === '-') {
        var trace;

        for(var i = 0; i < subplotData.length; i++) {
            if(subplotData[i].visible) {
                trace = subplotData[i];
                break;
            }
        }

        if(trace && trace[dataAttr]) {
            axOut.type = autoType(trace[dataAttr], 'gregorian');
        }

        if(axOut.type === '-') {
            axOut.type = 'linear';
        } else {
            // copy autoType back to input axis
            // note that if this object didn't exist
            // in the input layout, we have to put it in
            // this happens in the main supplyDefaults function
            axIn.type = axOut.type;
        }
    }

    return axOut.type;
}

module.exports = function supplyLayoutDefaults(layoutIn, layoutOut, fullData) {
    handleSubplotDefaults(layoutIn, layoutOut, fullData, {
        type: constants.name,
        attributes: layoutAttributes,
        handleDefaults: handleDefaults,
        font: layoutOut.font,
        paper_bgcolor: layoutOut.paper_bgcolor,
        fullData: fullData,
        layoutOut: layoutOut
    });
};
