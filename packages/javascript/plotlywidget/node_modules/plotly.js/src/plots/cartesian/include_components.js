/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/


'use strict';

var Registry = require('../../registry');
var Lib = require('../../lib');

/**
 * Factory function for checking component arrays for subplot references.
 *
 * @param {string} containerArrayName: the top-level array in gd.layout to check
 *   If an item in this container is found that references a cartesian x and/or y axis,
 *   ensure cartesian is marked as a base plot module and record the axes (and subplot
 *   if both refs are axes) in gd._fullLayout
 *
 * @return {function}: with args layoutIn (gd.layout) and layoutOut (gd._fullLayout)
 * as expected of a component includeBasePlot method
 */
module.exports = function makeIncludeComponents(containerArrayName) {
    return function includeComponents(layoutIn, layoutOut) {
        var array = layoutIn[containerArrayName];
        if(!Array.isArray(array)) return;

        var Cartesian = Registry.subplotsRegistry.cartesian;
        var idRegex = Cartesian.idRegex;
        var subplots = layoutOut._subplots;
        var xaList = subplots.xaxis;
        var yaList = subplots.yaxis;
        var cartesianList = subplots.cartesian;
        var hasCartesianOrGL2D = layoutOut._has('cartesian') || layoutOut._has('gl2d');

        for(var i = 0; i < array.length; i++) {
            var itemi = array[i];
            if(!Lib.isPlainObject(itemi)) continue;

            var xref = itemi.xref;
            var yref = itemi.yref;

            var hasXref = idRegex.x.test(xref);
            var hasYref = idRegex.y.test(yref);
            if(hasXref || hasYref) {
                if(!hasCartesianOrGL2D) Lib.pushUnique(layoutOut._basePlotModules, Cartesian);

                var newAxis = false;
                if(hasXref && xaList.indexOf(xref) === -1) {
                    xaList.push(xref);
                    newAxis = true;
                }
                if(hasYref && yaList.indexOf(yref) === -1) {
                    yaList.push(yref);
                    newAxis = true;
                }

                /*
                 * Notice the logic here: only add a subplot for a component if
                 * it's referencing both x and y axes AND it's creating a new axis
                 * so for example if your plot already has xy and x2y2, an annotation
                 * on x2y or xy2 will not create a new subplot.
                 */
                if(newAxis && hasXref && hasYref) {
                    cartesianList.push(xref + yref);
                }
            }
        }
    };
};
