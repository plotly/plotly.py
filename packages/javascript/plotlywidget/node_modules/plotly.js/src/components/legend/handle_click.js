/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var Lib = require('../../lib');
var Registry = require('../../registry');

var SHOWISOLATETIP = true;

module.exports = function handleClick(g, gd, numClicks) {
    var fullLayout = gd._fullLayout;

    if(gd._dragged || gd._editing) return;

    var itemClick = fullLayout.legend.itemclick;
    var itemDoubleClick = fullLayout.legend.itemdoubleclick;

    if(numClicks === 1 && itemClick === 'toggle' && itemDoubleClick === 'toggleothers' &&
        SHOWISOLATETIP && gd.data && gd._context.showTips
    ) {
        Lib.notifier(Lib._(gd, 'Double-click on legend to isolate one trace'), 'long');
        SHOWISOLATETIP = false;
    } else {
        SHOWISOLATETIP = false;
    }

    var mode;
    if(numClicks === 1) mode = itemClick;
    else if(numClicks === 2) mode = itemDoubleClick;
    if(!mode) return;

    var hiddenSlices = fullLayout.hiddenlabels ?
        fullLayout.hiddenlabels.slice() :
        [];

    var legendItem = g.data()[0][0];
    var fullData = gd._fullData;
    var fullTrace = legendItem.trace;
    var legendgroup = fullTrace.legendgroup;

    var i, j, kcont, key, keys, val;
    var attrUpdate = {};
    var attrIndices = [];
    var carrs = [];
    var carrIdx = [];

    function insertUpdate(traceIndex, key, value) {
        var attrIndex = attrIndices.indexOf(traceIndex);
        var valueArray = attrUpdate[key];
        if(!valueArray) {
            valueArray = attrUpdate[key] = [];
        }

        if(attrIndices.indexOf(traceIndex) === -1) {
            attrIndices.push(traceIndex);
            attrIndex = attrIndices.length - 1;
        }

        valueArray[attrIndex] = value;

        return attrIndex;
    }

    function setVisibility(fullTrace, visibility) {
        var fullInput = fullTrace._fullInput;
        if(Registry.hasTransform(fullInput, 'groupby')) {
            var kcont = carrs[fullInput.index];
            if(!kcont) {
                var groupbyIndices = Registry.getTransformIndices(fullInput, 'groupby');
                var lastGroupbyIndex = groupbyIndices[groupbyIndices.length - 1];
                kcont = Lib.keyedContainer(fullInput, 'transforms[' + lastGroupbyIndex + '].styles', 'target', 'value.visible');
                carrs[fullInput.index] = kcont;
            }

            var curState = kcont.get(fullTrace._group);

            // If not specified, assume visible. This happens if there are other style
            // properties set for a group but not the visibility. There are many similar
            // ways to do this (e.g. why not just `curState = fullTrace.visible`??? The
            // answer is: because it breaks other things like groupby trace names in
            // subtle ways.)
            if(curState === undefined) {
                curState = true;
            }

            if(curState !== false) {
                // true -> legendonly. All others toggle to true:
                kcont.set(fullTrace._group, visibility);
            }
            carrIdx[fullInput.index] = insertUpdate(fullInput.index, 'visible', fullInput.visible === false ? false : true);
        } else {
            // false -> false (not possible since will not be visible in legend)
            // true -> legendonly
            // legendonly -> true
            var nextVisibility = fullInput.visible === false ? false : visibility;

            insertUpdate(fullInput.index, 'visible', nextVisibility);
        }
    }

    if(Registry.traceIs(fullTrace, 'pie-like')) {
        var thisLabel = legendItem.label;
        var thisLabelIndex = hiddenSlices.indexOf(thisLabel);

        if(mode === 'toggle') {
            if(thisLabelIndex === -1) hiddenSlices.push(thisLabel);
            else hiddenSlices.splice(thisLabelIndex, 1);
        } else if(mode === 'toggleothers') {
            hiddenSlices = [];
            gd.calcdata[0].forEach(function(d) {
                if(thisLabel !== d.label) {
                    hiddenSlices.push(d.label);
                }
            });
            if(gd._fullLayout.hiddenlabels && gd._fullLayout.hiddenlabels.length === hiddenSlices.length && thisLabelIndex === -1) {
                hiddenSlices = [];
            }
        }

        Registry.call('_guiRelayout', gd, 'hiddenlabels', hiddenSlices);
    } else {
        var hasLegendgroup = legendgroup && legendgroup.length;
        var traceIndicesInGroup = [];
        var tracei;
        if(hasLegendgroup) {
            for(i = 0; i < fullData.length; i++) {
                tracei = fullData[i];
                if(!tracei.visible) continue;
                if(tracei.legendgroup === legendgroup) {
                    traceIndicesInGroup.push(i);
                }
            }
        }

        if(mode === 'toggle') {
            var nextVisibility;

            switch(fullTrace.visible) {
                case true:
                    nextVisibility = 'legendonly';
                    break;
                case false:
                    nextVisibility = false;
                    break;
                case 'legendonly':
                    nextVisibility = true;
                    break;
            }

            if(hasLegendgroup) {
                for(i = 0; i < fullData.length; i++) {
                    if(fullData[i].visible !== false && fullData[i].legendgroup === legendgroup) {
                        setVisibility(fullData[i], nextVisibility);
                    }
                }
            } else {
                setVisibility(fullTrace, nextVisibility);
            }
        } else if(mode === 'toggleothers') {
            // Compute the clicked index. expandedIndex does what we want for expanded traces
            // but also culls hidden traces. That means we have some work to do.
            var isClicked, isInGroup, otherState;
            var isIsolated = true;
            for(i = 0; i < fullData.length; i++) {
                isClicked = fullData[i] === fullTrace;
                if(isClicked) continue;

                isInGroup = (hasLegendgroup && fullData[i].legendgroup === legendgroup);

                if(!isInGroup && fullData[i].visible === true && !Registry.traceIs(fullData[i], 'notLegendIsolatable')) {
                    isIsolated = false;
                    break;
                }
            }

            for(i = 0; i < fullData.length; i++) {
                // False is sticky; we don't change it.
                if(fullData[i].visible === false) continue;

                if(Registry.traceIs(fullData[i], 'notLegendIsolatable')) {
                    continue;
                }

                switch(fullTrace.visible) {
                    case 'legendonly':
                        setVisibility(fullData[i], true);
                        break;
                    case true:
                        otherState = isIsolated ? true : 'legendonly';
                        isClicked = fullData[i] === fullTrace;
                        isInGroup = isClicked || (hasLegendgroup && fullData[i].legendgroup === legendgroup);
                        setVisibility(fullData[i], isInGroup ? true : otherState);
                        break;
                }
            }
        }

        for(i = 0; i < carrs.length; i++) {
            kcont = carrs[i];
            if(!kcont) continue;
            var update = kcont.constructUpdate();

            var updateKeys = Object.keys(update);
            for(j = 0; j < updateKeys.length; j++) {
                key = updateKeys[j];
                val = attrUpdate[key] = attrUpdate[key] || [];
                val[carrIdx[i]] = update[key];
            }
        }

        // The length of the value arrays should be equal and any unspecified
        // values should be explicitly undefined for them to get properly culled
        // as updates and not accidentally reset to the default value. This fills
        // out sparse arrays with the required number of undefined values:
        keys = Object.keys(attrUpdate);
        for(i = 0; i < keys.length; i++) {
            key = keys[i];
            for(j = 0; j < attrIndices.length; j++) {
                // Use hasOwnPropety to protect against falsey values:
                if(!attrUpdate[key].hasOwnProperty(j)) {
                    attrUpdate[key][j] = undefined;
                }
            }
        }

        Registry.call('_guiRestyle', gd, attrUpdate, attrIndices);
    }
};
