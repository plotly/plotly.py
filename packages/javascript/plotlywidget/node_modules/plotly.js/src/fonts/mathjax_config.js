/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

/* global MathJax:false */

module.exports = function() {
    if(typeof MathJax !== 'undefined') {
        var globalConfig = (window.PlotlyConfig || {}).MathJaxConfig !== 'local';

        if(globalConfig) {
            MathJax.Hub.Config({
                messageStyle: 'none',
                skipStartupTypeset: true,
                displayAlign: 'left',
                tex2jax: {
                    inlineMath: [['$', '$'], ['\\(', '\\)']]
                }
            });
            MathJax.Hub.Configured();
        }
    }
};
