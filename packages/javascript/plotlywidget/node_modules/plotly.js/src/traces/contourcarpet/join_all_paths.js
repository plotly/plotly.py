/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var Drawing = require('../../components/drawing');
var axisAlignedLine = require('../carpet/axis_aligned_line');
var Lib = require('../../lib');

module.exports = function joinAllPaths(trace, pi, perimeter, ab2p, carpet, carpetcd, xa, ya) {
    var i;
    var fullpath = '';

    var startsleft = pi.edgepaths.map(function(v, i) { return i; });
    var newloop = true;
    var endpt, newendpt, cnt, nexti, possiblei, addpath;

    var atol = Math.abs(perimeter[0][0] - perimeter[2][0]) * 1e-4;
    var btol = Math.abs(perimeter[0][1] - perimeter[2][1]) * 1e-4;

    function istop(pt) { return Math.abs(pt[1] - perimeter[0][1]) < btol; }
    function isbottom(pt) { return Math.abs(pt[1] - perimeter[2][1]) < btol; }
    function isleft(pt) { return Math.abs(pt[0] - perimeter[0][0]) < atol; }
    function isright(pt) { return Math.abs(pt[0] - perimeter[2][0]) < atol; }

    function pathto(pt0, pt1) {
        var i, j, segments, axis;
        var path = '';

        if((istop(pt0) && !isright(pt0)) || (isbottom(pt0) && !isleft(pt0))) {
            axis = carpet.aaxis;
            segments = axisAlignedLine(carpet, carpetcd, [pt0[0], pt1[0]], 0.5 * (pt0[1] + pt1[1]));
        } else {
            axis = carpet.baxis;
            segments = axisAlignedLine(carpet, carpetcd, 0.5 * (pt0[0] + pt1[0]), [pt0[1], pt1[1]]);
        }

        for(i = 1; i < segments.length; i++) {
            path += axis.smoothing ? 'C' : 'L';
            for(j = 0; j < segments[i].length; j++) {
                var pt = segments[i][j];
                path += [xa.c2p(pt[0]), ya.c2p(pt[1])] + ' ';
            }
        }

        return path;
    }

    i = 0;
    endpt = null;
    while(startsleft.length) {
        var startpt = pi.edgepaths[i][0];

        if(endpt) {
            fullpath += pathto(endpt, startpt);
        }

        addpath = Drawing.smoothopen(pi.edgepaths[i].map(ab2p), pi.smoothing);
        fullpath += newloop ? addpath : addpath.replace(/^M/, 'L');
        startsleft.splice(startsleft.indexOf(i), 1);
        endpt = pi.edgepaths[i][pi.edgepaths[i].length - 1];
        nexti = -1;

        // now loop through sides, moving our endpoint until we find a new start
        for(cnt = 0; cnt < 4; cnt++) { // just to prevent infinite loops
            if(!endpt) {
                Lib.log('Missing end?', i, pi);
                break;
            }

            if(istop(endpt) && !isright(endpt)) {
                newendpt = perimeter[1]; // left top ---> right top
            } else if(isleft(endpt)) {
                newendpt = perimeter[0]; // left bottom ---> left top
            } else if(isbottom(endpt)) {
                newendpt = perimeter[3]; // right bottom
            } else if(isright(endpt)) {
                newendpt = perimeter[2]; // left bottom
            }

            for(possiblei = 0; possiblei < pi.edgepaths.length; possiblei++) {
                var ptNew = pi.edgepaths[possiblei][0];
                // is ptNew on the (horz. or vert.) segment from endpt to newendpt?
                if(Math.abs(endpt[0] - newendpt[0]) < atol) {
                    if(Math.abs(endpt[0] - ptNew[0]) < atol && (ptNew[1] - endpt[1]) * (newendpt[1] - ptNew[1]) >= 0) {
                        newendpt = ptNew;
                        nexti = possiblei;
                    }
                } else if(Math.abs(endpt[1] - newendpt[1]) < btol) {
                    if(Math.abs(endpt[1] - ptNew[1]) < btol && (ptNew[0] - endpt[0]) * (newendpt[0] - ptNew[0]) >= 0) {
                        newendpt = ptNew;
                        nexti = possiblei;
                    }
                } else {
                    Lib.log('endpt to newendpt is not vert. or horz.', endpt, newendpt, ptNew);
                }
            }

            if(nexti >= 0) break;
            fullpath += pathto(endpt, newendpt);
            endpt = newendpt;
        }

        if(nexti === pi.edgepaths.length) {
            Lib.log('unclosed perimeter path');
            break;
        }

        i = nexti;

        // if we closed back on a loop we already included,
        // close it and start a new loop
        newloop = (startsleft.indexOf(i) === -1);
        if(newloop) {
            i = startsleft[0];
            fullpath += pathto(endpt, newendpt) + 'Z';
            endpt = null;
        }
    }

    // finally add the interior paths
    for(i = 0; i < pi.paths.length; i++) {
        fullpath += Drawing.smoothclosed(pi.paths[i].map(ab2p), pi.smoothing);
    }

    return fullpath;
};
