/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/


'use strict';

// works with our CSS cursor classes (see css/_cursor.scss)
// to apply cursors to d3 single-element selections.
// omit cursor to revert to the default.
module.exports = function setCursor(el3, csr) {
    (el3.attr('class') || '').split(' ').forEach(function(cls) {
        if(cls.indexOf('cursor-') === 0) el3.classed(cls, false);
    });

    if(csr) el3.classed('cursor-' + csr, true);
};
