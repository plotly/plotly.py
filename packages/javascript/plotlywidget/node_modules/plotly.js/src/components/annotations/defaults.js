/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/


'use strict';

var Lib = require('../../lib');
var Axes = require('../../plots/cartesian/axes');
var handleArrayContainerDefaults = require('../../plots/array_container_defaults');

var handleAnnotationCommonDefaults = require('./common_defaults');
var attributes = require('./attributes');


module.exports = function supplyLayoutDefaults(layoutIn, layoutOut) {
    handleArrayContainerDefaults(layoutIn, layoutOut, {
        name: 'annotations',
        handleItemDefaults: handleAnnotationDefaults
    });
};

function handleAnnotationDefaults(annIn, annOut, fullLayout) {
    function coerce(attr, dflt) {
        return Lib.coerce(annIn, annOut, attributes, attr, dflt);
    }

    var visible = coerce('visible');
    var clickToShow = coerce('clicktoshow');

    if(!(visible || clickToShow)) return;

    handleAnnotationCommonDefaults(annIn, annOut, fullLayout, coerce);

    var showArrow = annOut.showarrow;

    // positioning
    var axLetters = ['x', 'y'];
    var arrowPosDflt = [-10, -30];
    var gdMock = {_fullLayout: fullLayout};

    for(var i = 0; i < 2; i++) {
        var axLetter = axLetters[i];

        // xref, yref
        var axRef = Axes.coerceRef(annIn, annOut, gdMock, axLetter, '', 'paper');

        if(axRef !== 'paper') {
            var ax = Axes.getFromId(gdMock, axRef);
            ax._annIndices.push(annOut._index);
        }

        // x, y
        Axes.coercePosition(annOut, gdMock, coerce, axRef, axLetter, 0.5);

        if(showArrow) {
            var arrowPosAttr = 'a' + axLetter;
            // axref, ayref
            var aaxRef = Axes.coerceRef(annIn, annOut, gdMock, arrowPosAttr, 'pixel');

            // for now the arrow can only be on the same axis or specified as pixels
            // TODO: sometime it might be interesting to allow it to be on *any* axis
            // but that would require updates to drawing & autorange code and maybe more
            if(aaxRef !== 'pixel' && aaxRef !== axRef) {
                aaxRef = annOut[arrowPosAttr] = 'pixel';
            }

            // ax, ay
            var aDflt = (aaxRef === 'pixel') ? arrowPosDflt[i] : 0.4;
            Axes.coercePosition(annOut, gdMock, coerce, aaxRef, arrowPosAttr, aDflt);
        }

        // xanchor, yanchor
        coerce(axLetter + 'anchor');

        // xshift, yshift
        coerce(axLetter + 'shift');
    }

    // if you have one coordinate you should have both
    Lib.noneOrAll(annIn, annOut, ['x', 'y']);

    // if you have one part of arrow length you should have both
    if(showArrow) {
        Lib.noneOrAll(annIn, annOut, ['ax', 'ay']);
    }

    if(clickToShow) {
        var xClick = coerce('xclick');
        var yClick = coerce('yclick');

        // put the actual click data to bind to into private attributes
        // so we don't have to do this little bit of logic on every hover event
        annOut._xclick = (xClick === undefined) ?
            annOut.x :
            Axes.cleanPosition(xClick, gdMock, annOut.xref);
        annOut._yclick = (yClick === undefined) ?
            annOut.y :
            Axes.cleanPosition(yClick, gdMock, annOut.yref);
    }
}
