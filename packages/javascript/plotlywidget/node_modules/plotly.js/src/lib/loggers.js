/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

/* eslint-disable no-console */

var dfltConfig = require('../plot_api/plot_config').dfltConfig;

var loggers = module.exports = {};

/**
 * ------------------------------------------
 * debugging tools
 * ------------------------------------------
 */

loggers.log = function() {
    if(dfltConfig.logging > 1) {
        var messages = ['LOG:'];

        for(var i = 0; i < arguments.length; i++) {
            messages.push(arguments[i]);
        }

        apply(console.trace || console.log, messages);
    }
};

loggers.warn = function() {
    if(dfltConfig.logging > 0) {
        var messages = ['WARN:'];

        for(var i = 0; i < arguments.length; i++) {
            messages.push(arguments[i]);
        }

        apply(console.trace || console.log, messages);
    }
};

loggers.error = function() {
    if(dfltConfig.logging > 0) {
        var messages = ['ERROR:'];

        for(var i = 0; i < arguments.length; i++) {
            messages.push(arguments[i]);
        }

        apply(console.error, messages);
    }
};

/*
 * Robust apply, for IE9 where console.log doesn't support
 * apply like other functions do
 */
function apply(f, args) {
    if(f && f.apply) {
        try {
            // `this` should always be console, since here we're always
            // applying a method of the console object.
            f.apply(console, args);
            return;
        } catch(e) { /* in case apply failed, fall back on the code below */ }
    }

    // no apply - just try calling the function on each arg independently
    for(var i = 0; i < args.length; i++) {
        try {
            f(args[i]);
        } catch(e) {
            // still fails - last resort simple console.log
            console.log(args[i]);
        }
    }
}
