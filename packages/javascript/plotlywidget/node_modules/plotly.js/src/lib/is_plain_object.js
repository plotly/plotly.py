/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/


'use strict';

// more info: http://stackoverflow.com/questions/18531624/isplainobject-thing
module.exports = function isPlainObject(obj) {
    // We need to be a little less strict in the `imagetest` container because
    // of how async image requests are handled.
    //
    // N.B. isPlainObject(new Constructor()) will return true in `imagetest`
    if(window && window.process && window.process.versions) {
        return Object.prototype.toString.call(obj) === '[object Object]';
    }

    return (
        Object.prototype.toString.call(obj) === '[object Object]' &&
        Object.getPrototypeOf(obj) === Object.prototype
    );
};
