/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var identity = require('./identity');

function wrap(d) {return [d];}

module.exports = {

    // The D3 data binding concept and the General Update Pattern promotes the idea of
    // traversing into the scenegraph by using the `.data(fun, keyFun)` call.
    // The `fun` is most often a `repeat`, ie. the elements beneath a `<g>` element need
    // access to the same data, or a `descend`, which fans a scenegraph node into a bunch of
    // of elements, e.g. points, lines, rows, requiring an array as input.
    // The role of the `keyFun` is to identify what elements are being entered/exited/updated,
    // otherwise D3 reverts to using a plain index which would screw up `transition`s.
    keyFun: function(d) {return d.key;},
    repeat: wrap,
    descend: identity,

    // Plotly.js uses a convention of storing the actual contents of the `calcData` as the
    // element zero of a container array. These helpers are just used for clarity as a
    // newcomer to the codebase may not know what the `[0]` is, and whether there can be further
    // elements (not atm).
    wrap: wrap,
    unwrap: function(d) {return d[0];}
};
