/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/


'use strict';

var createSurface = require('gl-surface3d');

var ndarray = require('ndarray');
var homography = require('ndarray-homography');
var fill = require('ndarray-fill');

var isArrayOrTypedArray = require('../../lib').isArrayOrTypedArray;
var parseColorScale = require('../../lib/gl_format_color').parseColorScale;
var str2RgbaArray = require('../../lib/str2rgbarray');
var extractOpts = require('../../components/colorscale').extractOpts;

var interp2d = require('../heatmap/interp2d');
var findEmpties = require('../heatmap/find_empties');

function SurfaceTrace(scene, surface, uid) {
    this.scene = scene;
    this.uid = uid;
    this.surface = surface;
    this.data = null;
    this.showContour = [false, false, false];
    this.contourStart = [null, null, null];
    this.contourEnd = [null, null, null];
    this.contourSize = [0, 0, 0];
    this.minValues = [Infinity, Infinity, Infinity];
    this.maxValues = [-Infinity, -Infinity, -Infinity];
    this.dataScaleX = 1.0;
    this.dataScaleY = 1.0;
    this.refineData = true;
    this.objectOffset = [0, 0, 0];
}

var proto = SurfaceTrace.prototype;

proto.getXat = function(a, b, calendar, axis) {
    var v = (
       (!isArrayOrTypedArray(this.data.x)) ?
            a :
       (isArrayOrTypedArray(this.data.x[0])) ?
            this.data.x[b][a] :
            this.data.x[a]
    );

    return (calendar === undefined) ? v : axis.d2l(v, 0, calendar);
};

proto.getYat = function(a, b, calendar, axis) {
    var v = (
       (!isArrayOrTypedArray(this.data.y)) ?
            b :
       (isArrayOrTypedArray(this.data.y[0])) ?
            this.data.y[b][a] :
            this.data.y[b]
    );

    return (calendar === undefined) ? v : axis.d2l(v, 0, calendar);
};

proto.getZat = function(a, b, calendar, axis) {
    var v = this.data.z[b][a];

    if(v === null && this.data.connectgaps && this.data._interpolatedZ) {
        v = this.data._interpolatedZ[b][a];
    }

    return (calendar === undefined) ? v : axis.d2l(v, 0, calendar);
};

proto.handlePick = function(selection) {
    if(selection.object === this.surface) {
        var xRatio = (selection.data.index[0] - 1) / this.dataScaleX - 1;
        var yRatio = (selection.data.index[1] - 1) / this.dataScaleY - 1;

        var j = Math.max(Math.min(Math.round(xRatio), this.data.z[0].length - 1), 0);
        var k = Math.max(Math.min(Math.round(yRatio), this.data._ylength - 1), 0);

        selection.index = [j, k];

        selection.traceCoordinate = [
            this.getXat(j, k),
            this.getYat(j, k),
            this.getZat(j, k)
        ];

        selection.dataCoordinate = [
            this.getXat(j, k, this.data.xcalendar, this.scene.fullSceneLayout.xaxis),
            this.getYat(j, k, this.data.ycalendar, this.scene.fullSceneLayout.yaxis),
            this.getZat(j, k, this.data.zcalendar, this.scene.fullSceneLayout.zaxis)
        ];

        for(var i = 0; i < 3; i++) {
            var v = selection.dataCoordinate[i];
            if(v !== null && v !== undefined) {
                selection.dataCoordinate[i] *= this.scene.dataScale[i];
            }
        }

        var text = this.data.hovertext || this.data.text;
        if(Array.isArray(text) && text[k] && text[k][j] !== undefined) {
            selection.textLabel = text[k][j];
        } else if(text) {
            selection.textLabel = text;
        } else {
            selection.textLabel = '';
        }

        selection.data.dataCoordinate = selection.dataCoordinate.slice();

        this.surface.highlight(selection.data);

        // Snap spikes to data coordinate
        this.scene.glplot.spikes.position = selection.dataCoordinate;

        return true;
    }
};

function isColormapCircular(colormap) {
    var first = colormap[0].rgb;
    var last = colormap[colormap.length - 1].rgb;

    return (
        first[0] === last[0] &&
        first[1] === last[1] &&
        first[2] === last[2] &&
        first[3] === last[3]
    );
}

var shortPrimes = [
    2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,
    101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199,
    211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293,
    307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397,
    401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499,
    503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599,
    601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691,
    701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797,
    809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887,
    907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997,
    1009, 1013, 1019, 1021, 1031, 1033, 1039, 1049, 1051, 1061, 1063, 1069, 1087, 1091, 1093, 1097,
    1103, 1109, 1117, 1123, 1129, 1151, 1153, 1163, 1171, 1181, 1187, 1193,
    1201, 1213, 1217, 1223, 1229, 1231, 1237, 1249, 1259, 1277, 1279, 1283, 1289, 1291, 1297,
    1301, 1303, 1307, 1319, 1321, 1327, 1361, 1367, 1373, 1381, 1399,
    1409, 1423, 1427, 1429, 1433, 1439, 1447, 1451, 1453, 1459, 1471, 1481, 1483, 1487, 1489, 1493, 1499,
    1511, 1523, 1531, 1543, 1549, 1553, 1559, 1567, 1571, 1579, 1583, 1597,
    1601, 1607, 1609, 1613, 1619, 1621, 1627, 1637, 1657, 1663, 1667, 1669, 1693, 1697, 1699,
    1709, 1721, 1723, 1733, 1741, 1747, 1753, 1759, 1777, 1783, 1787, 1789,
    1801, 1811, 1823, 1831, 1847, 1861, 1867, 1871, 1873, 1877, 1879, 1889,
    1901, 1907, 1913, 1931, 1933, 1949, 1951, 1973, 1979, 1987, 1993, 1997, 1999,
    2003, 2011, 2017, 2027, 2029, 2039, 2053, 2063, 2069, 2081, 2083, 2087, 2089, 2099,
    2111, 2113, 2129, 2131, 2137, 2141, 2143, 2153, 2161, 2179,
    2203, 2207, 2213, 2221, 2237, 2239, 2243, 2251, 2267, 2269, 2273, 2281, 2287, 2293, 2297,
    2309, 2311, 2333, 2339, 2341, 2347, 2351, 2357, 2371, 2377, 2381, 2383, 2389, 2393, 2399,
    2411, 2417, 2423, 2437, 2441, 2447, 2459, 2467, 2473, 2477,
    2503, 2521, 2531, 2539, 2543, 2549, 2551, 2557, 2579, 2591, 2593,
    2609, 2617, 2621, 2633, 2647, 2657, 2659, 2663, 2671, 2677, 2683, 2687, 2689, 2693, 2699,
    2707, 2711, 2713, 2719, 2729, 2731, 2741, 2749, 2753, 2767, 2777, 2789, 2791, 2797,
    2801, 2803, 2819, 2833, 2837, 2843, 2851, 2857, 2861, 2879, 2887, 2897,
    2903, 2909, 2917, 2927, 2939, 2953, 2957, 2963, 2969, 2971, 2999
];

function getPow(a, b) {
    if(a < b) return 0;
    var n = 0;
    while(Math.floor(a % b) === 0) {
        a /= b;
        n++;
    }
    return n;
}

function getFactors(a) {
    var powers = [];
    for(var i = 0; i < shortPrimes.length; i++) {
        var b = shortPrimes[i];
        powers.push(
            getPow(a, b)
        );
    }
    return powers;
}

function smallestDivisor(a) {
    var A = getFactors(a);
    var result = a;
    for(var i = 0; i < shortPrimes.length; i++) {
        if(A[i] > 0) {
            result = shortPrimes[i];
            break;
        }
    }
    return result;
}

function leastCommonMultiple(a, b) {
    if(a < 1 || b < 1) return undefined;
    var A = getFactors(a);
    var B = getFactors(b);
    var n = 1;
    for(var i = 0; i < shortPrimes.length; i++) {
        n *= Math.pow(
            shortPrimes[i], Math.max(A[i], B[i])
        );
    }
    return n;
}

function arrayLCM(A) {
    if(A.length === 0) return undefined;
    var n = 1;
    for(var i = 0; i < A.length; i++) {
        n = leastCommonMultiple(n, A[i]);
    }
    return n;
}

proto.calcXnums = function(xlen) {
    var i;
    var nums = [];
    for(i = 1; i < xlen; i++) {
        var a = this.getXat(i - 1, 0);
        var b = this.getXat(i, 0);

        if(b !== a &&
            a !== undefined && a !== null &&
            b !== undefined && b !== null) {
            nums[i - 1] = Math.abs(b - a);
        } else {
            nums[i - 1] = 0;
        }
    }

    var totalDist = 0;
    for(i = 1; i < xlen; i++) {
        totalDist += nums[i - 1];
    }

    for(i = 1; i < xlen; i++) {
        if(nums[i - 1] === 0) {
            nums[i - 1] = 1;
        } else {
            nums[i - 1] = Math.round(totalDist / nums[i - 1]);
        }
    }

    return nums;
};

proto.calcYnums = function(ylen) {
    var i;
    var nums = [];
    for(i = 1; i < ylen; i++) {
        var a = this.getYat(0, i - 1);
        var b = this.getYat(0, i);

        if(b !== a &&
            a !== undefined && a !== null &&
            b !== undefined && b !== null) {
            nums[i - 1] = Math.abs(b - a);
        } else {
            nums[i - 1] = 0;
        }
    }

    var totalDist = 0;
    for(i = 1; i < ylen; i++) {
        totalDist += nums[i - 1];
    }

    for(i = 1; i < ylen; i++) {
        if(nums[i - 1] === 0) {
            nums[i - 1] = 1;
        } else {
            nums[i - 1] = Math.round(totalDist / nums[i - 1]);
        }
    }

    return nums;
};

var highlyComposites = [1, 2, 4, 6, 12, 24, 36, 48, 60, 120, 180, 240, 360, 720, 840, 1260];

var MIN_RESOLUTION = highlyComposites[9];
var MAX_RESOLUTION = highlyComposites[13];

proto.estimateScale = function(resSrc, axis) {
    var nums = (axis === 0) ?
        this.calcXnums(resSrc) :
        this.calcYnums(resSrc);

    var resDst = 1 + arrayLCM(nums);

    while(resDst < MIN_RESOLUTION) {
        resDst *= 2;
    }

    while(resDst > MAX_RESOLUTION) {
        resDst--;
        resDst /= smallestDivisor(resDst);
        resDst++;

        if(resDst < MIN_RESOLUTION) {
         // resDst = MIN_RESOLUTION; // option 1: use min resolution
            resDst = MAX_RESOLUTION; // option 2: use max resolution
        }
    }

    var scale = Math.round(resDst / resSrc);
    return (scale > 1) ? scale : 1;
};

proto.refineCoords = function(coords) {
    var scaleW = this.dataScaleX;
    var scaleH = this.dataScaleY;

    var width = coords[0].shape[0];
    var height = coords[0].shape[1];

    var newWidth = Math.floor(coords[0].shape[0] * scaleW + 1) | 0;
    var newHeight = Math.floor(coords[0].shape[1] * scaleH + 1) | 0;

    // Pad coords by +1
    var padWidth = 1 + width + 1;
    var padHeight = 1 + height + 1;
    var padImg = ndarray(new Float32Array(padWidth * padHeight), [padWidth, padHeight]);

    for(var i = 0; i < coords.length; ++i) {
        this.surface.padField(padImg, coords[i]);

        var scaledImg = ndarray(new Float32Array(newWidth * newHeight), [newWidth, newHeight]);
        homography(scaledImg, padImg,
            [
                scaleW, 0, 0,
                0, scaleH, 0,
                0, 0, 1
            ]
        );
        coords[i] = scaledImg;
    }
};

function insertIfNewLevel(arr, newValue) {
    var found = false;
    for(var k = 0; k < arr.length; k++) {
        if(newValue === arr[k]) {
            found = true;
            break;
        }
    }
    if(found === false) arr.push(newValue);
}

proto.setContourLevels = function() {
    var newLevels = [[], [], []];
    var useNewLevels = [false, false, false];
    var needsUpdate = false;

    var i, j, value;

    for(i = 0; i < 3; ++i) {
        if(this.showContour[i]) {
            needsUpdate = true;

            if(
                this.contourSize[i] > 0 &&
                this.contourStart[i] !== null &&
                this.contourEnd[i] !== null &&
                this.contourEnd[i] > this.contourStart[i]
            ) {
                useNewLevels[i] = true;

                for(j = this.contourStart[i]; j < this.contourEnd[i]; j += this.contourSize[i]) {
                    value = j * this.scene.dataScale[i];

                    insertIfNewLevel(newLevels[i], value);
                }
            }
        }
    }

    if(needsUpdate) {
        var allLevels = [[], [], []];
        for(i = 0; i < 3; ++i) {
            if(this.showContour[i]) {
                allLevels[i] = useNewLevels[i] ? newLevels[i] : this.scene.contourLevels[i];
            }
        }
        this.surface.update({ levels: allLevels });
    }
};

proto.update = function(data) {
    var scene = this.scene;
    var sceneLayout = scene.fullSceneLayout;
    var surface = this.surface;
    var alpha = data.opacity;
    var colormap = parseColorScale(data, alpha);
    var scaleFactor = scene.dataScale;
    var xlen = data.z[0].length;
    var ylen = data._ylength;
    var contourLevels = scene.contourLevels;

    // Save data
    this.data = data;

    /*
     * Fill and transpose zdata.
     * Consistent with 'heatmap' and 'contour', plotly 'surface'
     * 'z' are such that sub-arrays correspond to y-coords
     * and that the sub-array entries correspond to a x-coords,
     * which is the transpose of 'gl-surface-plot'.
     */

    var i, j, k, v;
    var rawCoords = [];
    for(i = 0; i < 3; i++) {
        rawCoords[i] = [];
        for(j = 0; j < xlen; j++) {
            rawCoords[i][j] = [];
            /*
            for(k = 0; k < ylen; k++) {
                rawCoords[i][j][k] = undefined;
            }
            */
        }
    }

    // coords x, y & z
    for(j = 0; j < xlen; j++) {
        for(k = 0; k < ylen; k++) {
            rawCoords[0][j][k] = this.getXat(j, k, data.xcalendar, sceneLayout.xaxis);
            rawCoords[1][j][k] = this.getYat(j, k, data.ycalendar, sceneLayout.yaxis);
            rawCoords[2][j][k] = this.getZat(j, k, data.zcalendar, sceneLayout.zaxis);
        }
    }

    if(data.connectgaps) {
        data._emptypoints = findEmpties(rawCoords[2]);
        interp2d(rawCoords[2], data._emptypoints);

        data._interpolatedZ = [];
        for(j = 0; j < xlen; j++) {
            data._interpolatedZ[j] = [];
            for(k = 0; k < ylen; k++) {
                data._interpolatedZ[j][k] = rawCoords[2][j][k];
            }
        }
    }

    // Note: log axes are not defined in surfaces yet.
    // but they could be defined here...

    for(i = 0; i < 3; i++) {
        for(j = 0; j < xlen; j++) {
            for(k = 0; k < ylen; k++) {
                v = rawCoords[i][j][k];
                if(v === null || v === undefined) {
                    rawCoords[i][j][k] = NaN;
                } else {
                    v = rawCoords[i][j][k] *= scaleFactor[i];
                }
            }
        }
    }

    for(i = 0; i < 3; i++) {
        for(j = 0; j < xlen; j++) {
            for(k = 0; k < ylen; k++) {
                v = rawCoords[i][j][k];
                if(v !== null && v !== undefined) {
                    if(this.minValues[i] > v) {
                        this.minValues[i] = v;
                    }
                    if(this.maxValues[i] < v) {
                        this.maxValues[i] = v;
                    }
                }
            }
        }
    }

    for(i = 0; i < 3; i++) {
        this.objectOffset[i] = 0.5 * (this.minValues[i] + this.maxValues[i]);
    }

    for(i = 0; i < 3; i++) {
        for(j = 0; j < xlen; j++) {
            for(k = 0; k < ylen; k++) {
                v = rawCoords[i][j][k];
                if(v !== null && v !== undefined) {
                    rawCoords[i][j][k] -= this.objectOffset[i];
                }
            }
        }
    }

    // convert processed raw data to Float32 matrices
    var coords = [
        ndarray(new Float32Array(xlen * ylen), [xlen, ylen]),
        ndarray(new Float32Array(xlen * ylen), [xlen, ylen]),
        ndarray(new Float32Array(xlen * ylen), [xlen, ylen])
    ];
    fill(coords[0], function(row, col) { return rawCoords[0][row][col]; });
    fill(coords[1], function(row, col) { return rawCoords[1][row][col]; });
    fill(coords[2], function(row, col) { return rawCoords[2][row][col]; });
    rawCoords = []; // free memory

    var params = {
        colormap: colormap,
        levels: [[], [], []],
        showContour: [true, true, true],
        showSurface: !data.hidesurface,
        contourProject: [
            [false, false, false],
            [false, false, false],
            [false, false, false]
        ],
        contourWidth: [1, 1, 1],
        contourColor: [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]],
        contourTint: [1, 1, 1],
        dynamicColor: [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]],
        dynamicWidth: [1, 1, 1],
        dynamicTint: [1, 1, 1],
        opacity: data.opacity
    };

    var cOpts = extractOpts(data);
    params.intensityBounds = [cOpts.min, cOpts.max];

    // Refine surface color if necessary
    if(data.surfacecolor) {
        var intensity = ndarray(new Float32Array(xlen * ylen), [xlen, ylen]);

        fill(intensity, function(row, col) {
            return data.surfacecolor[col][row];
        });

        coords.push(intensity);
    } else {
        // when 'z' is used as 'intensity',
        // we must scale its value
        params.intensityBounds[0] *= scaleFactor[2];
        params.intensityBounds[1] *= scaleFactor[2];
    }

    if(MAX_RESOLUTION < coords[0].shape[0] ||
        MAX_RESOLUTION < coords[0].shape[1]) {
        this.refineData = false;
    }

    if(this.refineData === true) {
        this.dataScaleX = this.estimateScale(coords[0].shape[0], 0);
        this.dataScaleY = this.estimateScale(coords[0].shape[1], 1);
        if(this.dataScaleX !== 1 || this.dataScaleY !== 1) {
            this.refineCoords(coords);
        }
    }

    if(data.surfacecolor) {
        params.intensity = coords.pop();
    }

    var highlightEnable = [true, true, true];
    var axis = ['x', 'y', 'z'];

    for(i = 0; i < 3; ++i) {
        var contourParams = data.contours[axis[i]];
        highlightEnable[i] = contourParams.highlight;

        params.showContour[i] = contourParams.show || contourParams.highlight;
        if(!params.showContour[i]) continue;

        params.contourProject[i] = [
            contourParams.project.x,
            contourParams.project.y,
            contourParams.project.z
        ];

        if(contourParams.show) {
            this.showContour[i] = true;
            params.levels[i] = contourLevels[i];
            surface.highlightColor[i] = params.contourColor[i] = str2RgbaArray(contourParams.color);

            if(contourParams.usecolormap) {
                surface.highlightTint[i] = params.contourTint[i] = 0;
            } else {
                surface.highlightTint[i] = params.contourTint[i] = 1;
            }
            params.contourWidth[i] = contourParams.width;

            this.contourStart[i] = contourParams.start;
            this.contourEnd[i] = contourParams.end;
            this.contourSize[i] = contourParams.size;
        } else {
            this.showContour[i] = false;

            this.contourStart[i] = null;
            this.contourEnd[i] = null;
            this.contourSize[i] = 0;
        }

        if(contourParams.highlight) {
            params.dynamicColor[i] = str2RgbaArray(contourParams.highlightcolor);
            params.dynamicWidth[i] = contourParams.highlightwidth;
        }
    }

    // see https://github.com/plotly/plotly.js/issues/940
    if(isColormapCircular(colormap)) {
        params.vertexColor = true;
    }

    params.objectOffset = this.objectOffset;

    params.coords = coords;
    surface.update(params);

    surface.visible = data.visible;
    surface.enableDynamic = highlightEnable;
    surface.enableHighlight = highlightEnable;

    surface.snapToData = true;

    if('lighting' in data) {
        surface.ambientLight = data.lighting.ambient;
        surface.diffuseLight = data.lighting.diffuse;
        surface.specularLight = data.lighting.specular;
        surface.roughness = data.lighting.roughness;
        surface.fresnel = data.lighting.fresnel;
    }

    if('lightposition' in data) {
        surface.lightPosition = [data.lightposition.x, data.lightposition.y, data.lightposition.z];
    }

    if(alpha && alpha < 1) {
        surface.supportsTransparency = true;
    }
};

proto.dispose = function() {
    this.scene.glplot.remove(this.surface);
    this.surface.dispose();
};

function createSurfaceTrace(scene, data) {
    var gl = scene.glplot.gl;
    var surface = createSurface({ gl: gl });
    var result = new SurfaceTrace(scene, surface, data.uid);
    surface._trace = result;
    result.update(data);
    scene.glplot.add(surface);
    return result;
}

module.exports = createSurfaceTrace;
