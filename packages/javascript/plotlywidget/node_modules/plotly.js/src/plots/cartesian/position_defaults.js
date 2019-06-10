/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/


'use strict';

var isNumeric = require('fast-isnumeric');

var Lib = require('../../lib');


module.exports = function handlePositionDefaults(containerIn, containerOut, coerce, options) {
    var counterAxes = options.counterAxes || [];
    var overlayableAxes = options.overlayableAxes || [];
    var letter = options.letter;
    var grid = options.grid;

    var dfltAnchor, dfltDomain, dfltSide, dfltPosition;

    if(grid) {
        dfltDomain = grid._domains[letter][grid._axisMap[containerOut._id]];
        dfltAnchor = grid._anchors[containerOut._id];
        if(dfltDomain) {
            dfltSide = grid[letter + 'side'].split(' ')[0];
            dfltPosition = grid.domain[letter][dfltSide === 'right' || dfltSide === 'top' ? 1 : 0];
        }
    }

    // Even if there's a grid, this axis may not be in it - fall back on non-grid defaults
    dfltDomain = dfltDomain || [0, 1];
    dfltAnchor = dfltAnchor || (isNumeric(containerIn.position) ? 'free' : (counterAxes[0] || 'free'));
    dfltSide = dfltSide || (letter === 'x' ? 'bottom' : 'left');
    dfltPosition = dfltPosition || 0;

    var anchor = Lib.coerce(containerIn, containerOut, {
        anchor: {
            valType: 'enumerated',
            values: ['free'].concat(counterAxes),
            dflt: dfltAnchor
        }
    }, 'anchor');

    if(anchor === 'free') coerce('position', dfltPosition);

    Lib.coerce(containerIn, containerOut, {
        side: {
            valType: 'enumerated',
            values: letter === 'x' ? ['bottom', 'top'] : ['left', 'right'],
            dflt: dfltSide
        }
    }, 'side');

    var overlaying = false;
    if(overlayableAxes.length) {
        overlaying = Lib.coerce(containerIn, containerOut, {
            overlaying: {
                valType: 'enumerated',
                values: [false].concat(overlayableAxes),
                dflt: false
            }
        }, 'overlaying');
    }

    if(!overlaying) {
        // TODO: right now I'm copying this domain over to overlaying axes
        // in ax.setscale()... but this means we still need (imperfect) logic
        // in the axes popover to hide domain for the overlaying axis.
        // perhaps I should make a private version _domain that all axes get???
        var domain = coerce('domain', dfltDomain);

        // according to https://www.npmjs.com/package/canvas-size
        // the minimum value of max canvas width across browsers and devices is 4096
        // which applied in the calculation below:
        if(domain[0] > domain[1] - 1 / 4096) containerOut.domain = dfltDomain;
        Lib.noneOrAll(containerIn.domain, containerOut.domain, dfltDomain);
    }

    coerce('layer');

    return containerOut;
};
