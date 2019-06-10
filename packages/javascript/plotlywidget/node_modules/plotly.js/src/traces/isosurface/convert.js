/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var createMesh = require('gl-mesh3d');

var Lib = require('../../lib');

var parseColorScale = require('../../lib/gl_format_color').parseColorScale;
var str2RgbaArray = require('../../lib/str2rgbarray');
var extractOpts = require('../../components/colorscale').extractOpts;
var zip3 = require('../../plots/gl3d/zip3');

function distinctVals(col) {
    return Lib.distinctVals(col).vals;
}

var findNearestOnAxis = function(w, arr) {
    for(var q = arr.length - 1; q > 0; q--) {
        var min = Math.min(arr[q], arr[q - 1]);
        var max = Math.max(arr[q], arr[q - 1]);
        if(max > min && min < w && w <= max) {
            return {
                id: q,
                distRatio: (max - w) / (max - min)
            };
        }
    }
    return {
        id: 0,
        distRatio: 0
    };
};

function IsosurfaceTrace(scene, mesh, uid) {
    this.scene = scene;
    this.uid = uid;
    this.mesh = mesh;
    this.name = '';
    this.data = null;
    this.showContour = false;
}

var proto = IsosurfaceTrace.prototype;

proto.handlePick = function(selection) {
    if(selection.object === this.mesh) {
        var rawId = selection.data.index;

        var x = this.data._x[rawId];
        var y = this.data._y[rawId];
        var z = this.data._z[rawId];

        var height = this.data._Ys.length;
        var depth = this.data._Zs.length;

        var i = findNearestOnAxis(x, this.data._Xs).id;
        var j = findNearestOnAxis(y, this.data._Ys).id;
        var k = findNearestOnAxis(z, this.data._Zs).id;

        var selectIndex = selection.index = k + depth * j + depth * height * i;

        selection.traceCoordinate = [
            this.data._x[selectIndex],
            this.data._y[selectIndex],
            this.data._z[selectIndex],
            this.data.value[selectIndex]
        ];

        var text = this.data.hovertext || this.data.text;
        if(Array.isArray(text) && text[selectIndex] !== undefined) {
            selection.textLabel = text[selectIndex];
        } else if(text) {
            selection.textLabel = text;
        }

        return true;
    }
};

proto.update = function(data) {
    var scene = this.scene;
    var layout = scene.fullSceneLayout;

    this.data = generateIsoMeshes(data);

    // Unpack position data
    function toDataCoords(axis, coord, scale, calendar) {
        return coord.map(function(x) {
            return axis.d2l(x, 0, calendar) * scale;
        });
    }

    var positions = zip3(
        toDataCoords(layout.xaxis, data._x, scene.dataScale[0], data.xcalendar),
        toDataCoords(layout.yaxis, data._y, scene.dataScale[1], data.ycalendar),
        toDataCoords(layout.zaxis, data._z, scene.dataScale[2], data.zcalendar));

    var cells = zip3(data._i, data._j, data._k);

    var config = {
        positions: positions,
        cells: cells,
        lightPosition: [data.lightposition.x, data.lightposition.y, data.lightposition.z],
        ambient: data.lighting.ambient,
        diffuse: data.lighting.diffuse,
        specular: data.lighting.specular,
        roughness: data.lighting.roughness,
        fresnel: data.lighting.fresnel,
        vertexNormalsEpsilon: data.lighting.vertexnormalsepsilon,
        faceNormalsEpsilon: data.lighting.facenormalsepsilon,
        opacity: data.opacity,
        contourEnable: data.contour.show,
        contourColor: str2RgbaArray(data.contour.color).slice(0, 3),
        contourWidth: data.contour.width,
        useFacetNormals: data.flatshading
    };

    var cOpts = extractOpts(data);
    config.vertexIntensity = data._intensity;
    config.vertexIntensityBounds = [cOpts.min, cOpts.max];
    config.colormap = parseColorScale(data);

    // Update mesh
    this.mesh.update(config);
};

proto.dispose = function() {
    this.scene.glplot.remove(this.mesh);
    this.mesh.dispose();
};

function generateIsoMeshes(data) {
    data._i = [];
    data._j = [];
    data._k = [];

    var showSurface = data.surface.show;
    var showSpaceframe = data.spaceframe.show;

    var surfaceFill = data.surface.fill;
    var spaceframeFill = data.spaceframe.fill;

    var drawingSurface = false;
    var drawingSpaceframe = false;

    var numFaces = 0;
    var numVertices;
    var beginVertextLength;

    var Xs = distinctVals(data.x.slice(0, data._len));
    var Ys = distinctVals(data.y.slice(0, data._len));
    var Zs = distinctVals(data.z.slice(0, data._len));

    var width = Xs.length;
    var height = Ys.length;
    var depth = Zs.length;

    function getIndex(i, j, k) {
        return k + depth * j + depth * height * i;
    }

    var minValues = data._minValues;
    var maxValues = data._maxValues;

    var vMin = data._vMin;
    var vMax = data._vMax;

    var allXs;
    var allYs;
    var allZs;
    var allVs;

    function findVertexId(x, y, z) {
        // could be used to find the vertex id of previously generated vertex within the group

        var len = allVs.length;
        for(var f = beginVertextLength; f < len; f++) {
            if(
                x === allXs[f] &&
                y === allYs[f] &&
                z === allZs[f]
            ) {
                return f;
            }
        }
        return -1;
    }

    function beginGroup() {
        beginVertextLength = numVertices;
    }

    function emptyVertices() {
        allXs = [];
        allYs = [];
        allZs = [];
        allVs = [];
        numVertices = 0;

        beginGroup();
    }

    function addVertex(x, y, z, v) {
        allXs.push(x);
        allYs.push(y);
        allZs.push(z);
        allVs.push(v);
        numVertices++;

        return numVertices - 1;
    }

    function addFace(a, b, c) {
        data._i.push(a);
        data._j.push(b);
        data._k.push(c);
        numFaces++;

        return numFaces - 1;
    }

    function getCenter(A, B, C) {
        var M = [];
        for(var i = 0; i < A.length; i++) {
            M[i] = (A[i] + B[i] + C[i]) / 3.0;
        }
        return M;
    }

    function getBetween(A, B, r) {
        var M = [];
        for(var i = 0; i < A.length; i++) {
            M[i] = A[i] * (1 - r) + r * B[i];
        }
        return M;
    }

    var activeFill;
    function setFill(fill) {
        activeFill = fill;
    }

    function createOpenTri(xyzv, abc) {
        var A = xyzv[0];
        var B = xyzv[1];
        var C = xyzv[2];
        var G = getCenter(A, B, C);

        var r = Math.sqrt(1 - activeFill);
        var p1 = getBetween(G, A, r);
        var p2 = getBetween(G, B, r);
        var p3 = getBetween(G, C, r);

        var a = abc[0];
        var b = abc[1];
        var c = abc[2];

        return {
            xyzv: [
                [A, B, p2], [p2, p1, A],
                [B, C, p3], [p3, p2, B],
                [C, A, p1], [p1, p3, C]
            ],
            abc: [
                [a, b, -1], [-1, -1, a],
                [b, c, -1], [-1, -1, b],
                [c, a, -1], [-1, -1, c]
            ]
        };
    }

    function styleIncludes(style, char) {
        if(style === 'all' || style === null) return true;
        return (style.indexOf(char) > -1);
    }

    function mapValue(style, value) {
        if(style === null) return value;
        return style;
    }

    function drawTri(style, xyzv, abc) {
        beginGroup();

        var allXYZVs = [xyzv];
        var allABCs = [abc];
        if(activeFill >= 1) {
            allXYZVs = [xyzv];
            allABCs = [abc];
        } else if(activeFill > 0) {
            var openTri = createOpenTri(xyzv, abc);
            allXYZVs = openTri.xyzv;
            allABCs = openTri.abc;
        }

        for(var f = 0; f < allXYZVs.length; f++) {
            xyzv = allXYZVs[f];
            abc = allABCs[f];

            var pnts = [];
            for(var i = 0; i < 3; i++) {
                var x = xyzv[i][0];
                var y = xyzv[i][1];
                var z = xyzv[i][2];
                var v = xyzv[i][3];

                var id = (abc[i] > -1) ? abc[i] : findVertexId(x, y, z);
                if(id > -1) {
                    pnts[i] = id;
                } else {
                    pnts[i] = addVertex(x, y, z, mapValue(style, v));
                }
            }

            addFace(pnts[0], pnts[1], pnts[2]);
        }
    }

    function drawQuad(style, xyzv, abcd) {
        var makeTri = function(i, j, k) {
            drawTri(style, [xyzv[i], xyzv[j], xyzv[k]], [abcd[i], abcd[j], abcd[k]]);
        };

        makeTri(0, 1, 2);
        makeTri(2, 3, 0);
    }

    function drawTetra(style, xyzv, abcd) {
        var makeTri = function(i, j, k) {
            drawTri(style, [xyzv[i], xyzv[j], xyzv[k]], [abcd[i], abcd[j], abcd[k]]);
        };

        makeTri(0, 1, 2);
        makeTri(3, 0, 1);
        makeTri(2, 3, 0);
        makeTri(1, 2, 3);
    }

    function calcIntersection(pointOut, pointIn, min, max) {
        var value = pointOut[3];

        if(value < min) value = min;
        if(value > max) value = max;

        var ratio = (pointOut[3] - value) / (pointOut[3] - pointIn[3] + 0.000000001); // we had to add this error to force solve the tiny caps

        var result = [];
        for(var s = 0; s < 4; s++) {
            result[s] = (1 - ratio) * pointOut[s] + ratio * pointIn[s];
        }
        return result;
    }

    function inRange(value, min, max) {
        return (
            value >= min &&
            value <= max
        );
    }

    function almostInFinalRange(value) {
        var vErr = 0.001 * (vMax - vMin);
        return (
            value >= vMin - vErr &&
            value <= vMax + vErr
        );
    }

    function getXYZV(indecies) {
        var xyzv = [];
        for(var q = 0; q < 4; q++) {
            var index = indecies[q];
            xyzv.push(
                [
                    data.x[index],
                    data.y[index],
                    data.z[index],
                    data.value[index]
                ]
            );
        }

        return xyzv;
    }

    var MAX_PASS = 3;

    function tryCreateTri(style, xyzv, abc, min, max, nPass) {
        if(!nPass) nPass = 1;

        abc = [-1, -1, -1]; // Note: for the moment we override indices
        // to run faster! But it is possible to comment this line
        // to reduce the number of vertices.

        var result = false;

        var ok = [
            inRange(xyzv[0][3], min, max),
            inRange(xyzv[1][3], min, max),
            inRange(xyzv[2][3], min, max)
        ];

        if(!ok[0] && !ok[1] && !ok[2]) {
            return false;
        }

        var tryDrawTri = function(style, xyzv, abc) {
            if( // we check here if the points are in `real` iso-min/max range
                almostInFinalRange(xyzv[0][3]) &&
                almostInFinalRange(xyzv[1][3]) &&
                almostInFinalRange(xyzv[2][3])
            ) {
                drawTri(style, xyzv, abc);
                return true;
            } else if(nPass < MAX_PASS) {
                return tryCreateTri(style, xyzv, abc, vMin, vMax, ++nPass); // i.e. second pass using actual vMin vMax bounds
            }
            return false;
        };

        if(ok[0] && ok[1] && ok[2]) {
            return tryDrawTri(style, xyzv, abc) || result;
        }

        var interpolated = false;

        [
            [0, 1, 2],
            [2, 0, 1],
            [1, 2, 0]
        ].forEach(function(e) {
            if(ok[e[0]] && ok[e[1]] && !ok[e[2]]) {
                var A = xyzv[e[0]];
                var B = xyzv[e[1]];
                var C = xyzv[e[2]];

                var p1 = calcIntersection(C, A, min, max);
                var p2 = calcIntersection(C, B, min, max);

                result = tryDrawTri(style, [p2, p1, A], [-1, -1, abc[e[0]]]) || result;
                result = tryDrawTri(style, [A, B, p2], [abc[e[0]], abc[e[1]], -1]) || result;

                interpolated = true;
            }
        });
        if(interpolated) return result;

        [
            [0, 1, 2],
            [1, 2, 0],
            [2, 0, 1]
        ].forEach(function(e) {
            if(ok[e[0]] && !ok[e[1]] && !ok[e[2]]) {
                var A = xyzv[e[0]];
                var B = xyzv[e[1]];
                var C = xyzv[e[2]];

                var p1 = calcIntersection(B, A, min, max);
                var p2 = calcIntersection(C, A, min, max);

                result = tryDrawTri(style, [p2, p1, A], [-1, -1, abc[e[0]]]) || result;

                interpolated = true;
            }
        });
        return result;
    }

    function tryCreateTetra(style, abcd, min, max) {
        var result = false;

        var xyzv = getXYZV(abcd);

        var ok = [
            inRange(xyzv[0][3], min, max),
            inRange(xyzv[1][3], min, max),
            inRange(xyzv[2][3], min, max),
            inRange(xyzv[3][3], min, max)
        ];

        if(!ok[0] && !ok[1] && !ok[2] && !ok[3]) {
            return result;
        }

        if(ok[0] && ok[1] && ok[2] && ok[3]) {
            if(drawingSpaceframe) {
                result = drawTetra(style, xyzv, abcd) || result;
            }
            return result;
        }

        var interpolated = false;

        [
            [0, 1, 2, 3],
            [3, 0, 1, 2],
            [2, 3, 0, 1],
            [1, 2, 3, 0]
        ].forEach(function(e) {
            if(ok[e[0]] && ok[e[1]] && ok[e[2]] && !ok[e[3]]) {
                var A = xyzv[e[0]];
                var B = xyzv[e[1]];
                var C = xyzv[e[2]];
                var D = xyzv[e[3]];

                if(drawingSpaceframe) {
                    result = drawTri(style, [A, B, C], [abcd[e[0]], abcd[e[1]], abcd[e[2]]]) || result;
                } else {
                    var p1 = calcIntersection(D, A, min, max);
                    var p2 = calcIntersection(D, B, min, max);
                    var p3 = calcIntersection(D, C, min, max);

                    result = drawTri(null, [p1, p2, p3], [-1, -1, -1]) || result;
                }

                interpolated = true;
            }
        });
        if(interpolated) return result;

        [
            [0, 1, 2, 3],
            [1, 2, 3, 0],
            [2, 3, 0, 1],
            [3, 0, 1, 2],
            [0, 2, 3, 1],
            [1, 3, 2, 0]
        ].forEach(function(e) {
            if(ok[e[0]] && ok[e[1]] && !ok[e[2]] && !ok[e[3]]) {
                var A = xyzv[e[0]];
                var B = xyzv[e[1]];
                var C = xyzv[e[2]];
                var D = xyzv[e[3]];

                var p1 = calcIntersection(C, A, min, max);
                var p2 = calcIntersection(C, B, min, max);
                var p3 = calcIntersection(D, B, min, max);
                var p4 = calcIntersection(D, A, min, max);

                if(drawingSpaceframe) {
                    result = drawTri(style, [A, p4, p1], [abcd[e[0]], -1, -1]) || result;
                    result = drawTri(style, [B, p2, p3], [abcd[e[1]], -1, -1]) || result;
                } else {
                    result = drawQuad(null, [p1, p2, p3, p4], [-1, -1, -1, -1]) || result;
                }

                interpolated = true;
            }
        });
        if(interpolated) return result;

        [
            [0, 1, 2, 3],
            [1, 2, 3, 0],
            [2, 3, 0, 1],
            [3, 0, 1, 2]
        ].forEach(function(e) {
            if(ok[e[0]] && !ok[e[1]] && !ok[e[2]] && !ok[e[3]]) {
                var A = xyzv[e[0]];
                var B = xyzv[e[1]];
                var C = xyzv[e[2]];
                var D = xyzv[e[3]];

                var p1 = calcIntersection(B, A, min, max);
                var p2 = calcIntersection(C, A, min, max);
                var p3 = calcIntersection(D, A, min, max);

                if(drawingSpaceframe) {
                    result = drawTri(style, [A, p1, p2], [abcd[e[0]], -1, -1]) || result;
                    result = drawTri(style, [A, p2, p3], [abcd[e[0]], -1, -1]) || result;
                    result = drawTri(style, [A, p3, p1], [abcd[e[0]], -1, -1]) || result;
                } else {
                    result = drawTri(null, [p1, p2, p3], [-1, -1, -1]) || result;
                }

                interpolated = true;
            }
        });
        return result;
    }

    function addCube(style, p000, p001, p010, p011, p100, p101, p110, p111, min, max) {
        var result = false;

        if(drawingSurface) {
            if(styleIncludes(style, 'A')) {
                result = tryCreateTetra(null, [p000, p001, p010, p100], min, max) || result;
            }
            if(styleIncludes(style, 'B')) {
                result = tryCreateTetra(null, [p001, p010, p011, p111], min, max) || result;
            }
            if(styleIncludes(style, 'C')) {
                result = tryCreateTetra(null, [p001, p100, p101, p111], min, max) || result;
            }
            if(styleIncludes(style, 'D')) {
                result = tryCreateTetra(null, [p010, p100, p110, p111], min, max) || result;
            }
            if(styleIncludes(style, 'E')) {
                result = tryCreateTetra(null, [p001, p010, p100, p111], min, max) || result;
            }
        }

        if(drawingSpaceframe) {
            result = tryCreateTetra(style, [p001, p010, p100, p111], min, max) || result;
        }

        return result;
    }

    function addRect(style, a, b, c, d, min, max, previousResult) {
        return [
            (previousResult[0] === true) ? true :
            tryCreateTri(style, getXYZV([a, b, c]), [a, b, c], min, max),
            (previousResult[1] === true) ? true :
            tryCreateTri(style, getXYZV([c, d, a]), [c, d, a], min, max)
        ];
    }

    function begin2dCell(style, p00, p01, p10, p11, min, max, isEven, previousResult) {
        // used to create caps and/or slices on exact axis points
        if(isEven) {
            return addRect(style, p00, p01, p11, p10, min, max, previousResult);
        } else {
            return addRect(style, p01, p11, p10, p00, min, max, previousResult);
        }
    }

    function beginSection(style, i, j, k, min, max, distRatios) {
        // used to create slices between axis points

        var result = false;
        var A, B, C, D;

        var makeSection = function() {
            result = tryCreateTri(style, [A, B, C], [-1, -1, -1], min, max) || result;
            result = tryCreateTri(style, [C, D, A], [-1, -1, -1], min, max) || result;
        };

        var rX = distRatios[0];
        var rY = distRatios[1];
        var rZ = distRatios[2];

        if(rX) {
            A = getBetween(getXYZV([getIndex(i, j - 0, k - 0)])[0], getXYZV([getIndex(i - 1, j - 0, k - 0)])[0], rX);
            B = getBetween(getXYZV([getIndex(i, j - 0, k - 1)])[0], getXYZV([getIndex(i - 1, j - 0, k - 1)])[0], rX);
            C = getBetween(getXYZV([getIndex(i, j - 1, k - 1)])[0], getXYZV([getIndex(i - 1, j - 1, k - 1)])[0], rX);
            D = getBetween(getXYZV([getIndex(i, j - 1, k - 0)])[0], getXYZV([getIndex(i - 1, j - 1, k - 0)])[0], rX);
            makeSection();
        }

        if(rY) {
            A = getBetween(getXYZV([getIndex(i - 0, j, k - 0)])[0], getXYZV([getIndex(i - 0, j - 1, k - 0)])[0], rY);
            B = getBetween(getXYZV([getIndex(i - 0, j, k - 1)])[0], getXYZV([getIndex(i - 0, j - 1, k - 1)])[0], rY);
            C = getBetween(getXYZV([getIndex(i - 1, j, k - 1)])[0], getXYZV([getIndex(i - 1, j - 1, k - 1)])[0], rY);
            D = getBetween(getXYZV([getIndex(i - 1, j, k - 0)])[0], getXYZV([getIndex(i - 1, j - 1, k - 0)])[0], rY);
            makeSection();
        }

        if(rZ) {
            A = getBetween(getXYZV([getIndex(i - 0, j - 0, k)])[0], getXYZV([getIndex(i - 0, j - 0, k - 1)])[0], rZ);
            B = getBetween(getXYZV([getIndex(i - 0, j - 1, k)])[0], getXYZV([getIndex(i - 0, j - 1, k - 1)])[0], rZ);
            C = getBetween(getXYZV([getIndex(i - 1, j - 1, k)])[0], getXYZV([getIndex(i - 1, j - 1, k - 1)])[0], rZ);
            D = getBetween(getXYZV([getIndex(i - 1, j - 0, k)])[0], getXYZV([getIndex(i - 1, j - 0, k - 1)])[0], rZ);
            makeSection();
        }

        return result;
    }

    function begin3dCell(style, p000, p001, p010, p011, p100, p101, p110, p111, min, max, isEven) {
        // used to create spaceframe and/or iso-surfaces

        var cellStyle = style;
        if(isEven) {
            if(drawingSurface && style === 'even') cellStyle = null;
            return addCube(cellStyle, p000, p001, p010, p011, p100, p101, p110, p111, min, max);
        } else {
            if(drawingSurface && style === 'odd') cellStyle = null;
            return addCube(cellStyle, p111, p110, p101, p100, p011, p010, p001, p000, min, max);
        }
    }

    function draw2dX(style, items, min, max, previousResult) {
        var result = [];
        var n = 0;
        for(var q = 0; q < items.length; q++) {
            var i = items[q];
            for(var k = 1; k < depth; k++) {
                for(var j = 1; j < height; j++) {
                    result.push(
                        begin2dCell(style,
                            getIndex(i, j - 1, k - 1),
                            getIndex(i, j - 1, k),
                            getIndex(i, j, k - 1),
                            getIndex(i, j, k),
                            min,
                            max,
                            (i + j + k) % 2,
                            (previousResult && previousResult[n]) ? previousResult[n] : []
                        )
                    );
                    n++;
                }
            }
        }
        return result;
    }

    function draw2dY(style, items, min, max, previousResult) {
        var result = [];
        var n = 0;
        for(var q = 0; q < items.length; q++) {
            var j = items[q];
            for(var i = 1; i < width; i++) {
                for(var k = 1; k < depth; k++) {
                    result.push(
                        begin2dCell(style,
                            getIndex(i - 1, j, k - 1),
                            getIndex(i, j, k - 1),
                            getIndex(i - 1, j, k),
                            getIndex(i, j, k),
                            min,
                            max,
                            (i + j + k) % 2,
                            (previousResult && previousResult[n]) ? previousResult[n] : []
                        )
                    );
                    n++;
                }
            }
        }
        return result;
    }

    function draw2dZ(style, items, min, max, previousResult) {
        var result = [];
        var n = 0;
        for(var q = 0; q < items.length; q++) {
            var k = items[q];
            for(var j = 1; j < height; j++) {
                for(var i = 1; i < width; i++) {
                    result.push(
                        begin2dCell(style,
                            getIndex(i - 1, j - 1, k),
                            getIndex(i - 1, j, k),
                            getIndex(i, j - 1, k),
                            getIndex(i, j, k),
                            min,
                            max,
                            (i + j + k) % 2,
                            (previousResult && previousResult[n]) ? previousResult[n] : []
                        )
                    );
                    n++;
                }
            }
        }
        return result;
    }

    function draw3d(style, min, max) {
        for(var k = 1; k < depth; k++) {
            for(var j = 1; j < height; j++) {
                for(var i = 1; i < width; i++) {
                    begin3dCell(style,
                        getIndex(i - 1, j - 1, k - 1),
                        getIndex(i - 1, j - 1, k),
                        getIndex(i - 1, j, k - 1),
                        getIndex(i - 1, j, k),
                        getIndex(i, j - 1, k - 1),
                        getIndex(i, j - 1, k),
                        getIndex(i, j, k - 1),
                        getIndex(i, j, k),
                        min,
                        max,
                        (i + j + k) % 2
                    );
                }
            }
        }
    }

    function drawSpaceframe(style, min, max) {
        drawingSpaceframe = true;
        draw3d(style, min, max);
        drawingSpaceframe = false;
    }

    function drawSurface(style, min, max) {
        drawingSurface = true;
        draw3d(style, min, max);
        drawingSurface = false;
    }

    function drawSectionX(style, items, min, max, distRatios, previousResult) {
        var result = [];
        var n = 0;
        for(var q = 0; q < items.length; q++) {
            var i = items[q];
            for(var k = 1; k < depth; k++) {
                for(var j = 1; j < height; j++) {
                    result.push(
                        beginSection(style, i, j, k, min, max, distRatios[q],
                            (previousResult && previousResult[n]) ? previousResult[n] : []
                        )
                    );
                    n++;
                }
            }
        }
        return result;
    }

    function drawSectionY(style, items, min, max, distRatios, previousResult) {
        var result = [];
        var n = 0;
        for(var q = 0; q < items.length; q++) {
            var j = items[q];
            for(var i = 1; i < width; i++) {
                for(var k = 1; k < depth; k++) {
                    result.push(
                        beginSection(style, i, j, k, min, max, distRatios[q],
                            (previousResult && previousResult[n]) ? previousResult[n] : []
                        )
                    );
                    n++;
                }
            }
        }
        return result;
    }

    function drawSectionZ(style, items, min, max, distRatios, previousResult) {
        var result = [];
        var n = 0;
        for(var q = 0; q < items.length; q++) {
            var k = items[q];
            for(var j = 1; j < height; j++) {
                for(var i = 1; i < width; i++) {
                    result.push(
                        beginSection(style, i, j, k, min, max, distRatios[q],
                            (previousResult && previousResult[n]) ? previousResult[n] : []
                        )
                    );
                    n++;
                }
            }
        }
        return result;
    }

    function createRange(a, b) {
        var range = [];
        for(var q = a; q < b; q++) {
            range.push(q);
        }
        return range;
    }

    function insertGridPoints() {
        for(var i = 0; i < width; i++) {
            for(var j = 0; j < height; j++) {
                for(var k = 0; k < depth; k++) {
                    var index = getIndex(i, j, k);
                    addVertex(
                        data.x[index],
                        data.y[index],
                        data.z[index],
                        data.value[index]
                    );
                }
            }
        }
    }

    function drawAll() {
        emptyVertices();

        // insert grid points
        insertGridPoints();

        var activeStyle = null;

        // draw spaceframes
        if(showSpaceframe && spaceframeFill) {
            setFill(spaceframeFill);

            drawSpaceframe(activeStyle, vMin, vMax);
        }

        // draw iso-surfaces
        if(showSurface && surfaceFill) {
            setFill(surfaceFill);

            var surfacePattern = data.surface.pattern;
            var surfaceCount = data.surface.count;
            for(var q = 0; q < surfaceCount; q++) {
                var ratio = (surfaceCount === 1) ? 0.5 : q / (surfaceCount - 1);
                var level = (1 - ratio) * vMin + ratio * vMax;

                var d1 = Math.abs(level - minValues);
                var d2 = Math.abs(level - maxValues);
                var ranges = (d1 > d2) ?
                    [minValues, level] :
                    [level, maxValues];

                drawSurface(surfacePattern, ranges[0], ranges[1]);
            }
        }

        var setupMinMax = [
            [ Math.min(vMin, maxValues), Math.max(vMin, maxValues) ],
            [ Math.min(minValues, vMax), Math.max(minValues, vMax) ]
        ];

        ['x', 'y', 'z'].forEach(function(e) {
            var preRes = [];
            for(var s = 0; s < setupMinMax.length; s++) {
                var count = 0;

                var activeMin = setupMinMax[s][0];
                var activeMax = setupMinMax[s][1];

                // draw slices
                var slice = data.slices[e];
                if(slice.show && slice.fill) {
                    setFill(slice.fill);

                    var exactIndices = [];
                    var ceilIndices = [];
                    var distRatios = [];
                    if(slice.locations.length) {
                        for(var q = 0; q < slice.locations.length; q++) {
                            var near = findNearestOnAxis(
                                slice.locations[q],
                                (e === 'x') ? Xs :
                                (e === 'y') ? Ys : Zs
                            );

                            if(near.distRatio === 0) {
                                exactIndices.push(near.id);
                            } else if(near.id > 0) {
                                ceilIndices.push(near.id);
                                if(e === 'x') {
                                    distRatios.push([near.distRatio, 0, 0]);
                                } else if(e === 'y') {
                                    distRatios.push([0, near.distRatio, 0]);
                                } else {
                                    distRatios.push([0, 0, near.distRatio]);
                                }
                            }
                        }
                    } else {
                        if(e === 'x') {
                            exactIndices = createRange(1, width - 1);
                        } else if(e === 'y') {
                            exactIndices = createRange(1, height - 1);
                        } else {
                            exactIndices = createRange(1, depth - 1);
                        }
                    }

                    if(ceilIndices.length > 0) {
                        if(e === 'x') {
                            preRes[count] = drawSectionX(activeStyle, ceilIndices, activeMin, activeMax, distRatios, preRes[count]);
                        } else if(e === 'y') {
                            preRes[count] = drawSectionY(activeStyle, ceilIndices, activeMin, activeMax, distRatios, preRes[count]);
                        } else {
                            preRes[count] = drawSectionZ(activeStyle, ceilIndices, activeMin, activeMax, distRatios, preRes[count]);
                        }
                        count++;
                    }

                    if(exactIndices.length > 0) {
                        if(e === 'x') {
                            preRes[count] = draw2dX(activeStyle, exactIndices, activeMin, activeMax, preRes[count]);
                        } else if(e === 'y') {
                            preRes[count] = draw2dY(activeStyle, exactIndices, activeMin, activeMax, preRes[count]);
                        } else {
                            preRes[count] = draw2dZ(activeStyle, exactIndices, activeMin, activeMax, preRes[count]);
                        }
                        count++;
                    }
                }

                // draw caps
                var cap = data.caps[e];
                if(cap.show && cap.fill) {
                    setFill(cap.fill);
                    if(e === 'x') {
                        preRes[count] = draw2dX(activeStyle, [0, width - 1], activeMin, activeMax, preRes[count]);
                    } else if(e === 'y') {
                        preRes[count] = draw2dY(activeStyle, [0, height - 1], activeMin, activeMax, preRes[count]);
                    } else {
                        preRes[count] = draw2dZ(activeStyle, [0, depth - 1], activeMin, activeMax, preRes[count]);
                    }
                    count++;
                }
            }
        });

        // remove vertices arrays (i.e. grid points) in case no face was created.
        if(numFaces === 0) {
            emptyVertices();
        }

        data._x = allXs;
        data._y = allYs;
        data._z = allZs;
        data._intensity = allVs;

        data._Xs = Xs;
        data._Ys = Ys;
        data._Zs = Zs;
    }

    drawAll();

    return data;
}

function createIsosurfaceTrace(scene, data) {
    var gl = scene.glplot.gl;
    var mesh = createMesh({gl: gl});
    var result = new IsosurfaceTrace(scene, mesh, data.uid);

    mesh._trace = result;
    result.update(data);
    scene.glplot.add(mesh);
    return result;
}

module.exports = {
    findNearestOnAxis: findNearestOnAxis,
    generateIsoMeshes: generateIsoMeshes,
    createIsosurfaceTrace: createIsosurfaceTrace,
};
