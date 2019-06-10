/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var Lib = require('../../lib');
var hasColorscale = require('./helpers').hasColorscale;
var extractOpts = require('./helpers').extractOpts;

module.exports = function crossTraceDefaults(fullData, fullLayout) {
    function replace(cont, k) {
        var val = cont['_' + k];
        if(val !== undefined) {
            cont[k] = val;
        }
    }

    function relinkColorAtts(outerCont, cbOpt) {
        var cont = cbOpt.container ?
            Lib.nestedProperty(outerCont, cbOpt.container).get() :
            outerCont;

        if(cont) {
            if(cont.coloraxis) {
                // stash ref to color axis
                cont._colorAx = fullLayout[cont.coloraxis];
            } else {
                var cOpts = extractOpts(cont);
                var isAuto = cOpts.auto;

                if(isAuto || cOpts.min === undefined) {
                    replace(cont, cbOpt.min);
                }
                if(isAuto || cOpts.max === undefined) {
                    replace(cont, cbOpt.max);
                }
                if(cOpts.autocolorscale) {
                    replace(cont, 'colorscale');
                }
            }
        }
    }

    for(var i = 0; i < fullData.length; i++) {
        var trace = fullData[i];
        var cbOpts = trace._module.colorbar;

        if(cbOpts) {
            if(Array.isArray(cbOpts)) {
                for(var j = 0; j < cbOpts.length; j++) {
                    relinkColorAtts(trace, cbOpts[j]);
                }
            } else {
                relinkColorAtts(trace, cbOpts);
            }
        }

        if(hasColorscale(trace, 'marker.line')) {
            relinkColorAtts(trace, {
                container: 'marker.line',
                min: 'cmin',
                max: 'cmax'
            });
        }
    }

    for(var k in fullLayout._colorAxes) {
        relinkColorAtts(fullLayout[k], {min: 'cmin', max: 'cmax'});
    }
};
