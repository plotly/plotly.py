/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var Lib = require('../../lib');
var polygonTester = require('../../lib/polygon').tester;

var findIndexOfMin = Lib.findIndexOfMin;
var isAngleInsideSector = Lib.isAngleInsideSector;
var angleDelta = Lib.angleDelta;
var angleDist = Lib.angleDist;

/**
 * is pt (r,a) inside polygon made up vertices at angles 'vangles'
 * inside a given polar sector
 *
 * @param {number} r : pt's radial coordinate
 * @param {number} a : pt's angular coordinate in *radians*
 * @param {2-item array} rBnds : sector's radial bounds
 * @param {2-item array} aBnds : sector's angular bounds *radians*
 * @param {array} vangles : angles of polygon vertices in *radians*
 * @return {boolean}
 */
function isPtInsidePolygon(r, a, rBnds, aBnds, vangles) {
    if(!isAngleInsideSector(a, aBnds)) return false;

    var r0, r1;

    if(rBnds[0] < rBnds[1]) {
        r0 = rBnds[0];
        r1 = rBnds[1];
    } else {
        r0 = rBnds[1];
        r1 = rBnds[0];
    }

    var polygonIn = polygonTester(makePolygon(r0, aBnds[0], aBnds[1], vangles));
    var polygonOut = polygonTester(makePolygon(r1, aBnds[0], aBnds[1], vangles));
    var xy = [r * Math.cos(a), r * Math.sin(a)];
    return polygonOut.contains(xy) && !polygonIn.contains(xy);
}

// find intersection of 'v0' <-> 'v1' edge with a ray at angle 'a'
// (i.e. a line that starts from the origin at angle 'a')
// given an (xp,yp) pair on the 'v0' <-> 'v1' line
// (N.B. 'v0' and 'v1' are angles in radians)
function findIntersectionXY(v0, v1, a, xpyp) {
    var xstar, ystar;

    var xp = xpyp[0];
    var yp = xpyp[1];
    var dsin = clampTiny(Math.sin(v1) - Math.sin(v0));
    var dcos = clampTiny(Math.cos(v1) - Math.cos(v0));
    var tanA = Math.tan(a);
    var cotanA = clampTiny(1 / tanA);
    var m = dsin / dcos;
    var b = yp - m * xp;

    if(cotanA) {
        if(dsin && dcos) {
            // given
            //  g(x) := v0 -> v1 line = m*x + b
            //  h(x) := ray at angle 'a' = m*x = tanA*x
            // solve g(xstar) = h(xstar)
            xstar = b / (tanA - m);
            ystar = tanA * xstar;
        } else if(dcos) {
            // horizontal v0 -> v1
            xstar = yp * cotanA;
            ystar = yp;
        } else {
            // vertical v0 -> v1
            xstar = xp;
            ystar = xp * tanA;
        }
    } else {
        // vertical ray
        if(dsin && dcos) {
            xstar = 0;
            ystar = b;
        } else if(dcos) {
            xstar = 0;
            ystar = yp;
        } else {
            // does this case exists?
            xstar = ystar = NaN;
        }
    }

    return [xstar, ystar];
}

// solves l^2 = (f(x)^2 - yp)^2 + (x - xp)^2
// rearranged into 0 = a*x^2 + b * x + c
//
// where f(x) = m*x + t + yp
// and   (x0, x1) = (-b +/- del) / (2*a)
function findXYatLength(l, m, xp, yp) {
    var t = -m * xp;
    var a = m * m + 1;
    var b = 2 * (m * t - xp);
    var c = t * t + xp * xp - l * l;
    var del = Math.sqrt(b * b - 4 * a * c);
    var x0 = (-b + del) / (2 * a);
    var x1 = (-b - del) / (2 * a);
    return [
        [x0, m * x0 + t + yp],
        [x1, m * x1 + t + yp]
    ];
}

function makeRegularPolygon(r, vangles) {
    var len = vangles.length;
    var vertices = new Array(len + 1);
    var i;
    for(i = 0; i < len; i++) {
        var va = vangles[i];
        vertices[i] = [r * Math.cos(va), r * Math.sin(va)];
    }
    vertices[i] = vertices[0].slice();
    return vertices;
}

function makeClippedPolygon(r, a0, a1, vangles) {
    var len = vangles.length;
    var vertices = [];
    var i, j;

    function a2xy(a) {
        return [r * Math.cos(a), r * Math.sin(a)];
    }

    function findXY(va0, va1, s) {
        return findIntersectionXY(va0, va1, s, a2xy(va0));
    }

    function cycleIndex(ind) {
        return Lib.mod(ind, len);
    }

    function isInside(v) {
        return isAngleInsideSector(v, [a0, a1]);
    }

    // find index in sector closest to a0
    // use it to find intersection of v[i0] <-> v[i0-1] edge with sector radius
    var i0 = findIndexOfMin(vangles, function(v) {
        return isInside(v) ? angleDist(v, a0) : Infinity;
    });
    var xy0 = findXY(vangles[i0], vangles[cycleIndex(i0 - 1)], a0);
    vertices.push(xy0);

    // fill in in-sector vertices
    for(i = i0, j = 0; j < len; i++, j++) {
        var va = vangles[cycleIndex(i)];
        if(!isInside(va)) break;
        vertices.push(a2xy(va));
    }

    // find index in sector closest to a1,
    // use it to find intersection of v[iN] <-> v[iN+1] edge with sector radius
    var iN = findIndexOfMin(vangles, function(v) {
        return isInside(v) ? angleDist(v, a1) : Infinity;
    });
    var xyN = findXY(vangles[iN], vangles[cycleIndex(iN + 1)], a1);
    vertices.push(xyN);

    vertices.push([0, 0]);
    vertices.push(vertices[0].slice());

    return vertices;
}

function makePolygon(r, a0, a1, vangles) {
    return Lib.isFullCircle([a0, a1]) ?
        makeRegularPolygon(r, vangles) :
        makeClippedPolygon(r, a0, a1, vangles);
}

function findPolygonOffset(r, a0, a1, vangles) {
    var minX = Infinity;
    var minY = Infinity;
    var vertices = makePolygon(r, a0, a1, vangles);

    for(var i = 0; i < vertices.length; i++) {
        var v = vertices[i];
        minX = Math.min(minX, v[0]);
        minY = Math.min(minY, -v[1]);
    }
    return [minX, minY];
}

/**
 * find vertex angles (in 'vangles') the enclose angle 'a'
 *
 * @param {number} a : angle in *radians*
 * @param {array} vangles : angles of polygon vertices in *radians*
 * @return {2-item array}
 */
function findEnclosingVertexAngles(a, vangles) {
    var minFn = function(v) {
        var adelta = angleDelta(v, a);
        return adelta > 0 ? adelta : Infinity;
    };
    var i0 = findIndexOfMin(vangles, minFn);
    var i1 = Lib.mod(i0 + 1, vangles.length);
    return [vangles[i0], vangles[i1]];
}

// to more easily catch 'almost zero' numbers in if-else blocks
function clampTiny(v) {
    return Math.abs(v) > 1e-10 ? v : 0;
}

function transformForSVG(pts0, cx, cy) {
    cx = cx || 0;
    cy = cy || 0;

    var len = pts0.length;
    var pts1 = new Array(len);

    for(var i = 0; i < len; i++) {
        var pt = pts0[i];
        pts1[i] = [cx + pt[0], cy - pt[1]];
    }
    return pts1;
}

/**
 * path polygon
 *
 * @param {number} r : polygon 'radius'
 * @param {number} a0 : first angular coordinate in *radians*
 * @param {number} a1 : second angular coordinate in *radians*
 * @param {array} vangles : angles of polygon vertices in *radians*
 * @param {number (optional)} cx : x coordinate of center
 * @param {number (optional)} cy : y coordinate of center
 * @return {string} svg path
 *
 */
function pathPolygon(r, a0, a1, vangles, cx, cy) {
    var poly = makePolygon(r, a0, a1, vangles);
    return 'M' + transformForSVG(poly, cx, cy).join('L');
}

/**
 * path a polygon 'annulus'
 * i.e. a polygon with a concentric hole
 *
 * N.B. this routine uses the evenodd SVG rule
 *
 * @param {number} r0 : first radial coordinate
 * @param {number} r1 : second radial coordinate
 * @param {number} a0 : first angular coordinate in *radians*
 * @param {number} a1 : second angular coordinate in *radians*
 * @param {array} vangles : angles of polygon vertices in *radians*
 * @param {number (optional)} cx : x coordinate of center
 * @param {number (optional)} cy : y coordinate of center
 * @return {string} svg path
 *
 */
function pathPolygonAnnulus(r0, r1, a0, a1, vangles, cx, cy) {
    var rStart, rEnd;

    if(r0 < r1) {
        rStart = r0;
        rEnd = r1;
    } else {
        rStart = r1;
        rEnd = r0;
    }

    var inner = transformForSVG(makePolygon(rStart, a0, a1, vangles), cx, cy);
    var outer = transformForSVG(makePolygon(rEnd, a0, a1, vangles), cx, cy);
    return 'M' + outer.reverse().join('L') + 'M' + inner.join('L');
}

module.exports = {
    isPtInsidePolygon: isPtInsidePolygon,
    findPolygonOffset: findPolygonOffset,
    findEnclosingVertexAngles: findEnclosingVertexAngles,
    findIntersectionXY: findIntersectionXY,
    findXYatLength: findXYatLength,
    clampTiny: clampTiny,
    pathPolygon: pathPolygon,
    pathPolygonAnnulus: pathPolygonAnnulus
};
