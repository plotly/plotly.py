/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/


'use strict';

var d3 = require('d3');
var tinycolor = require('tinycolor2');

var Registry = require('../../registry');
var Lib = require('../../lib');
var makeColorScaleFuncFromTrace = require('../../components/colorscale').makeColorScaleFuncFromTrace;
var xmlnsNamespaces = require('../../constants/xmlns_namespaces');

module.exports = function(gd, plotinfo, cdheatmaps, heatmapLayer) {
    var xa = plotinfo.xaxis;
    var ya = plotinfo.yaxis;

    Lib.makeTraceGroups(heatmapLayer, cdheatmaps, 'hm').each(function(cd) {
        var plotGroup = d3.select(this);
        var cd0 = cd[0];
        var trace = cd0.trace;

        var z = cd0.z;
        var x = cd0.x;
        var y = cd0.y;
        var xc = cd0.xCenter;
        var yc = cd0.yCenter;
        var isContour = Registry.traceIs(trace, 'contour');
        var zsmooth = isContour ? 'best' : trace.zsmooth;

        // get z dims
        var m = z.length;
        var n = Lib.maxRowLength(z);
        var xrev = false;
        var yrev = false;

        var left, right, temp, top, bottom, i;

        // TODO: if there are multiple overlapping categorical heatmaps,
        // or if we allow category sorting, then the categories may not be
        // sequential... may need to reorder and/or expand z

        // Get edges of png in pixels (xa.c2p() maps axes coordinates to pixel coordinates)
        // figure out if either axis is reversed (y is usually reversed, in pixel coords)
        // also clip the image to maximum 50% outside the visible plot area
        // bigger image lets you pan more naturally, but slows performance.
        // TODO: use low-resolution images outside the visible plot for panning
        // these while loops find the first and last brick bounds that are defined
        // (in case of log of a negative)
        i = 0;
        while(left === undefined && i < x.length - 1) {
            left = xa.c2p(x[i]);
            i++;
        }
        i = x.length - 1;
        while(right === undefined && i > 0) {
            right = xa.c2p(x[i]);
            i--;
        }

        if(right < left) {
            temp = right;
            right = left;
            left = temp;
            xrev = true;
        }

        i = 0;
        while(top === undefined && i < y.length - 1) {
            top = ya.c2p(y[i]);
            i++;
        }
        i = y.length - 1;
        while(bottom === undefined && i > 0) {
            bottom = ya.c2p(y[i]);
            i--;
        }

        if(bottom < top) {
            temp = top;
            top = bottom;
            bottom = temp;
            yrev = true;
        }

        // for contours with heatmap fill, we generate the boundaries based on
        // brick centers but then use the brick edges for drawing the bricks
        if(isContour) {
            xc = x;
            yc = y;
            x = cd0.xfill;
            y = cd0.yfill;
        }

        // make an image that goes at most half a screen off either side, to keep
        // time reasonable when you zoom in. if zsmooth is true/fast, don't worry
        // about this, because zooming doesn't increase number of pixels
        // if zsmooth is best, don't include anything off screen because it takes too long
        if(zsmooth !== 'fast') {
            var extra = zsmooth === 'best' ? 0 : 0.5;
            left = Math.max(-extra * xa._length, left);
            right = Math.min((1 + extra) * xa._length, right);
            top = Math.max(-extra * ya._length, top);
            bottom = Math.min((1 + extra) * ya._length, bottom);
        }

        var imageWidth = Math.round(right - left);
        var imageHeight = Math.round(bottom - top);

        // setup image nodes

        // if image is entirely off-screen, don't even draw it
        var isOffScreen = (imageWidth <= 0 || imageHeight <= 0);

        if(isOffScreen) {
            var noImage = plotGroup.selectAll('image').data([]);
            noImage.exit().remove();
            return;
        }

        // generate image data

        var canvasW, canvasH;
        if(zsmooth === 'fast') {
            canvasW = n;
            canvasH = m;
        } else {
            canvasW = imageWidth;
            canvasH = imageHeight;
        }

        var canvas = document.createElement('canvas');
        canvas.width = canvasW;
        canvas.height = canvasH;
        var context = canvas.getContext('2d');

        var sclFunc = makeColorScaleFuncFromTrace(trace, {noNumericCheck: true, returnArray: true});

        // map brick boundaries to image pixels
        var xpx,
            ypx;
        if(zsmooth === 'fast') {
            xpx = xrev ?
                function(index) { return n - 1 - index; } :
                Lib.identity;
            ypx = yrev ?
                function(index) { return m - 1 - index; } :
                Lib.identity;
        } else {
            xpx = function(index) {
                return Lib.constrain(Math.round(xa.c2p(x[index]) - left),
                    0, imageWidth);
            };
            ypx = function(index) {
                return Lib.constrain(Math.round(ya.c2p(y[index]) - top),
                    0, imageHeight);
            };
        }

        // build the pixel map brick-by-brick
        // cruise through z-matrix row-by-row
        // build a brick at each z-matrix value
        var yi = ypx(0);
        var yb = [yi, yi];
        var xbi = xrev ? 0 : 1;
        var ybi = yrev ? 0 : 1;
        // for collecting an average luminosity of the heatmap
        var pixcount = 0;
        var rcount = 0;
        var gcount = 0;
        var bcount = 0;

        var xb, j, xi, v, row, c;

        function setColor(v, pixsize) {
            if(v !== undefined) {
                var c = sclFunc(v);
                c[0] = Math.round(c[0]);
                c[1] = Math.round(c[1]);
                c[2] = Math.round(c[2]);

                pixcount += pixsize;
                rcount += c[0] * pixsize;
                gcount += c[1] * pixsize;
                bcount += c[2] * pixsize;
                return c;
            }
            return [0, 0, 0, 0];
        }

        function interpColor(r0, r1, xinterp, yinterp) {
            var z00 = r0[xinterp.bin0];
            if(z00 === undefined) return setColor(undefined, 1);

            var z01 = r0[xinterp.bin1];
            var z10 = r1[xinterp.bin0];
            var z11 = r1[xinterp.bin1];
            var dx = (z01 - z00) || 0;
            var dy = (z10 - z00) || 0;
            var dxy;

            // the bilinear interpolation term needs different calculations
            // for all the different permutations of missing data
            // among the neighbors of the main point, to ensure
            // continuity across brick boundaries.
            if(z01 === undefined) {
                if(z11 === undefined) dxy = 0;
                else if(z10 === undefined) dxy = 2 * (z11 - z00);
                else dxy = (2 * z11 - z10 - z00) * 2 / 3;
            } else if(z11 === undefined) {
                if(z10 === undefined) dxy = 0;
                else dxy = (2 * z00 - z01 - z10) * 2 / 3;
            } else if(z10 === undefined) dxy = (2 * z11 - z01 - z00) * 2 / 3;
            else dxy = (z11 + z00 - z01 - z10);

            return setColor(z00 + xinterp.frac * dx + yinterp.frac * (dy + xinterp.frac * dxy));
        }

        if(zsmooth) { // best or fast, works fastest with imageData
            var pxIndex = 0;
            var pixels;

            try {
                pixels = new Uint8Array(imageWidth * imageHeight * 4);
            } catch(e) {
                pixels = new Array(imageWidth * imageHeight * 4);
            }

            if(zsmooth === 'best') {
                var xForPx = xc || x;
                var yForPx = yc || y;
                var xPixArray = new Array(xForPx.length);
                var yPixArray = new Array(yForPx.length);
                var xinterpArray = new Array(imageWidth);
                var findInterpX = xc ? findInterpFromCenters : findInterp;
                var findInterpY = yc ? findInterpFromCenters : findInterp;
                var yinterp, r0, r1;

                // first make arrays of x and y pixel locations of brick boundaries
                for(i = 0; i < xForPx.length; i++) xPixArray[i] = Math.round(xa.c2p(xForPx[i]) - left);
                for(i = 0; i < yForPx.length; i++) yPixArray[i] = Math.round(ya.c2p(yForPx[i]) - top);

                // then make arrays of interpolations
                // (bin0=closest, bin1=next, frac=fractional dist.)
                for(i = 0; i < imageWidth; i++) xinterpArray[i] = findInterpX(i, xPixArray);

                // now do the interpolations and fill the png
                for(j = 0; j < imageHeight; j++) {
                    yinterp = findInterpY(j, yPixArray);
                    r0 = z[yinterp.bin0];
                    r1 = z[yinterp.bin1];
                    for(i = 0; i < imageWidth; i++, pxIndex += 4) {
                        c = interpColor(r0, r1, xinterpArray[i], yinterp);
                        putColor(pixels, pxIndex, c);
                    }
                }
            } else { // zsmooth = fast
                for(j = 0; j < m; j++) {
                    row = z[j];
                    yb = ypx(j);
                    for(i = 0; i < imageWidth; i++) {
                        c = setColor(row[i], 1);
                        pxIndex = (yb * imageWidth + xpx(i)) * 4;
                        putColor(pixels, pxIndex, c);
                    }
                }
            }

            var imageData = context.createImageData(imageWidth, imageHeight);
            try {
                imageData.data.set(pixels);
            } catch(e) {
                var pxArray = imageData.data;
                var dlen = pxArray.length;
                for(j = 0; j < dlen; j ++) {
                    pxArray[j] = pixels[j];
                }
            }

            context.putImageData(imageData, 0, 0);
        } else { // zsmooth = false -> filling potentially large bricks works fastest with fillRect
            // gaps do not need to be exact integers, but if they *are* we will get
            // cleaner edges by rounding at least one edge
            var xGap = trace.xgap;
            var yGap = trace.ygap;
            var xGapLeft = Math.floor(xGap / 2);
            var yGapTop = Math.floor(yGap / 2);

            for(j = 0; j < m; j++) {
                row = z[j];
                yb.reverse();
                yb[ybi] = ypx(j + 1);
                if(yb[0] === yb[1] || yb[0] === undefined || yb[1] === undefined) {
                    continue;
                }
                xi = xpx(0);
                xb = [xi, xi];
                for(i = 0; i < n; i++) {
                    // build one color brick!
                    xb.reverse();
                    xb[xbi] = xpx(i + 1);
                    if(xb[0] === xb[1] || xb[0] === undefined || xb[1] === undefined) {
                        continue;
                    }
                    v = row[i];
                    c = setColor(v, (xb[1] - xb[0]) * (yb[1] - yb[0]));
                    context.fillStyle = 'rgba(' + c.join(',') + ')';

                    context.fillRect(xb[0] + xGapLeft, yb[0] + yGapTop,
                        xb[1] - xb[0] - xGap, yb[1] - yb[0] - yGap);
                }
            }
        }

        rcount = Math.round(rcount / pixcount);
        gcount = Math.round(gcount / pixcount);
        bcount = Math.round(bcount / pixcount);
        var avgColor = tinycolor('rgb(' + rcount + ',' + gcount + ',' + bcount + ')');

        gd._hmpixcount = (gd._hmpixcount||0) + pixcount;
        gd._hmlumcount = (gd._hmlumcount||0) + pixcount * avgColor.getLuminance();

        var image3 = plotGroup.selectAll('image')
            .data(cd);

        image3.enter().append('svg:image').attr({
            xmlns: xmlnsNamespaces.svg,
            preserveAspectRatio: 'none'
        });

        image3.attr({
            height: imageHeight,
            width: imageWidth,
            x: left,
            y: top,
            'xlink:href': canvas.toDataURL('image/png')
        });
    });
};

// get interpolated bin value. Returns {bin0:closest bin, frac:fractional dist to next, bin1:next bin}
function findInterp(pixel, pixArray) {
    var maxBin = pixArray.length - 2;
    var bin = Lib.constrain(Lib.findBin(pixel, pixArray), 0, maxBin);
    var pix0 = pixArray[bin];
    var pix1 = pixArray[bin + 1];
    var interp = Lib.constrain(bin + (pixel - pix0) / (pix1 - pix0) - 0.5, 0, maxBin);
    var bin0 = Math.round(interp);
    var frac = Math.abs(interp - bin0);

    if(!interp || interp === maxBin || !frac) {
        return {
            bin0: bin0,
            bin1: bin0,
            frac: 0
        };
    }
    return {
        bin0: bin0,
        frac: frac,
        bin1: Math.round(bin0 + frac / (interp - bin0))
    };
}

function findInterpFromCenters(pixel, centerPixArray) {
    var maxBin = centerPixArray.length - 1;
    var bin = Lib.constrain(Lib.findBin(pixel, centerPixArray), 0, maxBin);
    var pix0 = centerPixArray[bin];
    var pix1 = centerPixArray[bin + 1];
    var frac = ((pixel - pix0) / (pix1 - pix0)) || 0;
    if(frac <= 0) {
        return {
            bin0: bin,
            bin1: bin,
            frac: 0
        };
    }
    if(frac < 0.5) {
        return {
            bin0: bin,
            bin1: bin + 1,
            frac: frac
        };
    }
    return {
        bin0: bin + 1,
        bin1: bin,
        frac: 1 - frac
    };
}

function putColor(pixels, pxIndex, c) {
    pixels[pxIndex] = c[0];
    pixels[pxIndex + 1] = c[1];
    pixels[pxIndex + 2] = c[2];
    pixels[pxIndex + 3] = Math.round(c[3] * 255);
}
