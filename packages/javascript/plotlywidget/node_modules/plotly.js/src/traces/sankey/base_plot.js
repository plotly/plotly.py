/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var overrideAll = require('../../plot_api/edit_types').overrideAll;
var getModuleCalcData = require('../../plots/get_data').getModuleCalcData;
var plot = require('./plot');
var fxAttrs = require('../../components/fx/layout_attributes');

var setCursor = require('../../lib/setcursor');
var dragElement = require('../../components/dragelement');
var prepSelect = require('../../plots/cartesian/select').prepSelect;
var Lib = require('../../lib');
var Registry = require('../../registry');

var SANKEY = 'sankey';

exports.name = SANKEY;

exports.baseLayoutAttrOverrides = overrideAll({
    hoverlabel: fxAttrs.hoverlabel
}, 'plot', 'nested');

exports.plot = function(gd) {
    var calcData = getModuleCalcData(gd.calcdata, SANKEY)[0];
    plot(gd, calcData);
    exports.updateFx(gd);
};

exports.clean = function(newFullData, newFullLayout, oldFullData, oldFullLayout) {
    var hadPlot = (oldFullLayout._has && oldFullLayout._has(SANKEY));
    var hasPlot = (newFullLayout._has && newFullLayout._has(SANKEY));

    if(hadPlot && !hasPlot) {
        oldFullLayout._paperdiv.selectAll('.sankey').remove();
        oldFullLayout._paperdiv.selectAll('.bgsankey').remove();
    }
};

exports.updateFx = function(gd) {
    for(var i = 0; i < gd._fullData.length; i++) {
        subplotUpdateFx(gd, i);
    }
};

function subplotUpdateFx(gd, index) {
    var trace = gd._fullData[index];
    var fullLayout = gd._fullLayout;

    var dragMode = fullLayout.dragmode;
    var cursor = fullLayout.dragmode === 'pan' ? 'move' : 'crosshair';
    var bgRect = trace._bgRect;

    if(dragMode === 'pan' || dragMode === 'zoom') return;

    setCursor(bgRect, cursor);

    var xaxis = {
        _id: 'x',
        c2p: Lib.identity,
        _offset: trace._sankey.translateX,
        _length: trace._sankey.width
    };
    var yaxis = {
        _id: 'y',
        c2p: Lib.identity,
        _offset: trace._sankey.translateY,
        _length: trace._sankey.height
    };

    // Note: dragOptions is needed to be declared for all dragmodes because
    // it's the object that holds persistent selection state.
    var dragOptions = {
        gd: gd,
        element: bgRect.node(),
        plotinfo: {
            id: index,
            xaxis: xaxis,
            yaxis: yaxis,
            fillRangeItems: Lib.noop
        },
        subplot: index,
        // create mock x/y axes for hover routine
        xaxes: [xaxis],
        yaxes: [yaxis],
        doneFnCompleted: function(selection) {
            var traceNow = gd._fullData[index];
            var newGroups;
            var oldGroups = traceNow.node.groups.slice();
            var newGroup = [];

            function findNode(pt) {
                var nodes = traceNow._sankey.graph.nodes;
                for(var i = 0; i < nodes.length; i++) {
                    if(nodes[i].pointNumber === pt) return nodes[i];
                }
            }

            for(var j = 0; j < selection.length; j++) {
                var node = findNode(selection[j].pointNumber);
                if(!node) continue;

                // If the node represents a group
                if(node.group) {
                    // Add all its children to the current selection
                    for(var k = 0; k < node.childrenNodes.length; k++) {
                        newGroup.push(node.childrenNodes[k].pointNumber);
                    }
                    // Flag group for removal from existing list of groups
                    oldGroups[node.pointNumber - traceNow.node._count] = false;
                } else {
                    newGroup.push(node.pointNumber);
                }
            }

            newGroups = oldGroups
                .filter(Boolean)
                .concat([newGroup]);

            Registry.call('_guiRestyle', gd, {
                'node.groups': [ newGroups ]
            }, index);
        }
    };

    dragOptions.prepFn = function(e, startX, startY) {
        prepSelect(e, startX, startY, dragOptions, dragMode);
    };

    dragElement.init(dragOptions);
}
