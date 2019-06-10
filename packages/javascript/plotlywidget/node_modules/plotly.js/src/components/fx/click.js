/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var Registry = require('../../registry');
var hover = require('./hover').hover;

module.exports = function click(gd, evt, subplot) {
    var annotationsDone = Registry.getComponentMethod('annotations', 'onClick')(gd, gd._hoverdata);

    // fallback to fail-safe in case the plot type's hover method doesn't pass the subplot.
    // Ternary, for example, didn't, but it was caught because tested.
    if(subplot !== undefined) {
        // The true flag at the end causes it to re-run the hover computation to figure out *which*
        // point is being clicked. Without this, clicking is somewhat unreliable.
        hover(gd, evt, subplot, true);
    }

    function emitClick() { gd.emit('plotly_click', {points: gd._hoverdata, event: evt}); }

    if(gd._hoverdata && evt && evt.target) {
        if(annotationsDone && annotationsDone.then) {
            annotationsDone.then(emitClick);
        } else emitClick();

        // why do we get a double event without this???
        if(evt.stopImmediatePropagation) evt.stopImmediatePropagation();
    }
};
