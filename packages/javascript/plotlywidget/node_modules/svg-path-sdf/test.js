'use strict'

require('enable-mobile')
require('insert-styles')(`
    canvas {
        display: block;
        float: left;
    }
`)
let sdf = require('./')

// polyfills
Number.isInteger = Number.isInteger || function(value) {
  return typeof value === 'number' &&
    isFinite(value) &&
    Math.floor(value) === value;
}
Math.sign = Math.sign || function(x) {
return ((x > 0) - (x < 0)) || +x;
}

let roundn = require('round-to')


let shapes = {
    circle: function(r) {
        var rs = roundn(r, 2);
        return 'M' + rs + ',0A' + rs + ',' + rs + ' 0 1,1 0,-' + rs +
            'A' + rs + ',' + rs + ' 0 0,1 ' + rs + ',0Z';
    },

    square: function(r) {
        var rs = roundn(r, 2);
        return 'M' + rs + ',' + rs + 'H-' + rs + 'V-' + rs + 'H' + rs + 'Z';
    },

    diamond: function(r) {
        var rd = roundn(r * 1.3, 2);
        return 'M' + rd + ',0L0,' + rd + 'L-' + rd + ',0L0,-' + rd + 'Z';
    },

    cross: function(r) {
        var rc = roundn(r * 0.4, 2),
            rc2 = roundn(r * 1.2, 2);
        return 'M' + rc2 + ',' + rc + 'H' + rc + 'V' + rc2 + 'H-' + rc +
            'V' + rc + 'H-' + rc2 + 'V-' + rc + 'H-' + rc + 'V-' + rc2 +
            'H' + rc + 'V-' + rc + 'H' + rc2 + 'Z';
    },

    x: function(r) {
        var rx = roundn(r * 0.8 / Math.sqrt(2), 2),
            ne = 'l' + rx + ',' + rx,
            se = 'l' + rx + ',-' + rx,
            sw = 'l-' + rx + ',-' + rx,
            nw = 'l-' + rx + ',' + rx;
        return 'M0,' + rx + ne + se + sw + se + sw + nw + sw + nw + ne + nw + ne + 'Z';
    },

    'triangle-up': function(r) {
        var rt = roundn(r * 2 / Math.sqrt(3), 2),
            r2 = roundn(r / 2, 2),
            rs = roundn(r, 2);
        return 'M-' + rt + ',' + r2 + 'H' + rt + 'L0,-' + rs + 'Z';
    },

    'triangle-down': function(r) {
        var rt = roundn(r * 2 / Math.sqrt(3), 2),
            r2 = roundn(r / 2, 2),
            rs = roundn(r, 2);
        return 'M-' + rt + ',-' + r2 + 'H' + rt + 'L0,' + rs + 'Z';
    },

    'triangle-left': function(r) {
        var rt = roundn(r * 2 / Math.sqrt(3), 2),
            r2 = roundn(r / 2, 2),
            rs = roundn(r, 2);
        return 'M' + r2 + ',-' + rt + 'V' + rt + 'L-' + rs + ',0Z';
    },

    'triangle-right': function(r) {
        var rt = roundn(r * 2 / Math.sqrt(3), 2),
            r2 = roundn(r / 2, 2),
            rs = roundn(r, 2);
        return 'M-' + r2 + ',-' + rt + 'V' + rt + 'L' + rs + ',0Z';
    },

    'triangle-ne': function(r) {
        var r1 = roundn(r * 0.6, 2),
            r2 = roundn(r * 1.2, 2);
        return 'M-' + r2 + ',-' + r1 + 'H' + r1 + 'V' + r2 + 'Z';
    },

    'triangle-se': function(r) {
        var r1 = roundn(r * 0.6, 2),
            r2 = roundn(r * 1.2, 2);
        return 'M' + r1 + ',-' + r2 + 'V' + r1 + 'H-' + r2 + 'Z';
    },

    'triangle-sw': function(r) {
        var r1 = roundn(r * 0.6, 2),
            r2 = roundn(r * 1.2, 2);
        return 'M' + r2 + ',' + r1 + 'H-' + r1 + 'V-' + r2 + 'Z';
    },

    'triangle-nw': function(r) {
        var r1 = roundn(r * 0.6, 2),
            r2 = roundn(r * 1.2, 2);
        return 'M-' + r1 + ',' + r2 + 'V-' + r1 + 'H' + r2 + 'Z';
    },

	pentagon: function(r) {
        var x1 = roundn(r * 0.951, 2),
            x2 = roundn(r * 0.588, 2),
            y0 = roundn(-r, 2),
            y1 = roundn(r * -0.309, 2),
            y2 = roundn(r * 0.809, 2);
        return 'M' + x1 + ',' + y1 + 'L' + x2 + ',' + y2 + 'H-' + x2 +
            'L-' + x1 + ',' + y1 + 'L0,' + y0 + 'Z';
    },

	hexagon: function(r) {
        var y0 = roundn(r, 2),
            y1 = roundn(r / 2, 2),
            x = roundn(r * Math.sqrt(3) / 2, 2);
        return 'M' + x + ',-' + y1 + 'V' + y1 + 'L0,' + y0 +
            'L-' + x + ',' + y1 + 'V-' + y1 + 'L0,-' + y0 + 'Z';
    },

    hexagon2: function(r) {
        var x0 = roundn(r, 2),
            x1 = roundn(r / 2, 2),
            y = roundn(r * Math.sqrt(3) / 2, 2);
        return 'M-' + x1 + ',' + y + 'H' + x1 + 'L' + x0 +
            ',0L' + x1 + ',-' + y + 'H-' + x1 + 'L-' + x0 + ',0Z';
    },

	octagon: function(r) {
        var a = roundn(r * 0.924, 2),
            b = roundn(r * 0.383, 2);
        return 'M-' + b + ',-' + a + 'H' + b + 'L' + a + ',-' + b + 'V' + b +
            'L' + b + ',' + a + 'H-' + b + 'L-' + a + ',' + b + 'V-' + b + 'Z';
    },

    star: function(r) {
        var rs = r * 1.4,
            x1 = roundn(rs * 0.225, 2),
            x2 = roundn(rs * 0.951, 2),
            x3 = roundn(rs * 0.363, 2),
            x4 = roundn(rs * 0.588, 2),
            y0 = roundn(-rs, 2),
            y1 = roundn(rs * -0.309, 2),
            y3 = roundn(rs * 0.118, 2),
            y4 = roundn(rs * 0.809, 2),
            y5 = roundn(rs * 0.382, 2);
        return 'M' + x1 + ',' + y1 + 'H' + x2 + 'L' + x3 + ',' + y3 +
            'L' + x4 + ',' + y4 + 'L0,' + y5 + 'L-' + x4 + ',' + y4 +
            'L-' + x3 + ',' + y3 + 'L-' + x2 + ',' + y1 + 'H-' + x1 +
            'L0,' + y0 + 'Z';
    },

    hexagram: function(r) {
        var y = roundn(r * 0.66, 2),
            x1 = roundn(r * 0.38, 2),
            x2 = roundn(r * 0.76, 2);
        return 'M-' + x2 + ',0l-' + x1 + ',-' + y + 'h' + x2 +
            'l' + x1 + ',-' + y + 'l' + x1 + ',' + y + 'h' + x2 +
            'l-' + x1 + ',' + y + 'l' + x1 + ',' + y + 'h-' + x2 +
            'l-' + x1 + ',' + y + 'l-' + x1 + ',-' + y + 'h-' + x2 + 'Z';
    },

    'star-triangle-up': function(r) {
        var x = roundn(r * Math.sqrt(3) * 0.8, 2),
            y1 = roundn(r * 0.8, 2),
            y2 = roundn(r * 1.6, 2),
            rc = roundn(r * 4, 2),
            aPart = 'A ' + rc + ',' + rc + ' 0 0 1 ';
        return 'M-' + x + ',' + y1 + aPart + x + ',' + y1 +
            aPart + '0,-' + y2 + aPart + '-' + x + ',' + y1 + 'Z';
    },

    'star-triangle-down': function(r) {
        var x = roundn(r * Math.sqrt(3) * 0.8, 2),
            y1 = roundn(r * 0.8, 2),
            y2 = roundn(r * 1.6, 2),
            rc = roundn(r * 4, 2),
            aPart = 'A ' + rc + ',' + rc + ' 0 0 1 ';
        return 'M' + x + ',-' + y1 + aPart + '-' + x + ',-' + y1 +
            aPart + '0,' + y2 + aPart + x + ',-' + y1 + 'Z';
    },

    'star-square': function(r) {
        var rp = roundn(r * 1.1, 2),
            rc = roundn(r * 2, 2),
            aPart = 'A ' + rc + ',' + rc + ' 0 0 1 ';
        return 'M-' + rp + ',-' + rp + aPart + '-' + rp + ',' + rp +
            aPart + rp + ',' + rp + aPart + rp + ',-' + rp +
            aPart + '-' + rp + ',-' + rp + 'Z';
    },

    'star-diamond': function(r) {
        var rp = roundn(r * 1.4, 2),
            rc = roundn(r * 1.9, 2),
            aPart = 'A ' + rc + ',' + rc + ' 0 0 1 ';
        return 'M-' + rp + ',0' + aPart + '0,' + rp +
            aPart + rp + ',0' + aPart + '0,-' + rp +
            aPart + '-' + rp + ',0' + 'Z';
    },

    'diamond-tall': function(r) {
        var x = roundn(r * 0.7, 2),
            y = roundn(r * 1.4, 2);
        return 'M0,' + y + 'L' + x + ',0L0,-' + y + 'L-' + x + ',0Z';
    },

    'diamond-wide': function(r) {
        var x = roundn(r * 1.4, 2),
            y = roundn(r * 0.7, 2);
        return 'M0,' + y + 'L' + x + ',0L0,-' + y + 'L-' + x + ',0Z';
    },

    hourglass: function(r) {
        var rs = roundn(r, 2);
        return 'M' + rs + ',' + rs + 'H-' + rs + 'L' + rs + ',-' + rs + 'H-' + rs + 'Z';
    },

    bowtie: function(r) {
        var rs = roundn(r, 2);
        return 'M' + rs + ',' + rs + 'V-' + rs + 'L-' + rs + ',' + rs + 'V-' + rs + 'Z';
    },

    'circle-cross': function(r) {
        var rs = roundn(r, 2);
        return 'M0,' + rs + 'V-' + rs + 'M' + rs + ',0H-' + rs +
            'M' + rs + ',0A' + rs + ',' + rs + ' 0 1,1 0,-' + rs +
            'A' + rs + ',' + rs + ' 0 0,1 ' + rs + ',0Z';
    },

    'circle-x': function(r) {
        var rs = roundn(r, 2),
            rc = roundn(r / Math.sqrt(2), 2);
        return 'M' + rc + ',' + rc + 'L-' + rc + ',-' + rc +
            'M' + rc + ',-' + rc + 'L-' + rc + ',' + rc +
            'M' + rs + ',0A' + rs + ',' + rs + ' 0 1,1 0,-' + rs +
            'A' + rs + ',' + rs + ' 0 0,1 ' + rs + ',0Z';
    },

    'square-cross': function(r) {
        var rs = roundn(r, 2);
        return 'M0,' + rs + 'V-' + rs + 'M' + rs + ',0H-' + rs +
            'M' + rs + ',' + rs + 'H-' + rs + 'V-' + rs + 'H' + rs + 'Z';
    },

    'square-x': function(r) {
        var rs = roundn(r, 2);
        return 'M' + rs + ',' + rs + 'L-' + rs + ',-' + rs +
            'M' + rs + ',-' + rs + 'L-' + rs + ',' + rs +
            'M' + rs + ',' + rs + 'H-' + rs + 'V-' + rs + 'H' + rs + 'Z';
    },

    'diamond-cross': function(r) {
        var rd = roundn(r * 1.3, 2);
        return 'M' + rd + ',0L0,' + rd + 'L-' + rd + ',0L0,-' + rd + 'Z' +
            'M0,-' + rd + 'V' + rd + 'M-' + rd + ',0H' + rd;
    },

    'diamond-x': function(r) {
        var rd = roundn(r * 1.3, 2),
            r2 = roundn(r * 0.65, 2);
        return 'M' + rd + ',0L0,' + rd + 'L-' + rd + ',0L0,-' + rd + 'Z' +
            'M-' + r2 + ',-' + r2 + 'L' + r2 + ',' + r2 +
            'M-' + r2 + ',' + r2 + 'L' + r2 + ',-' + r2;
    },

    'cross-thin': function(r) {
        var rc = roundn(r * 1.4, 2);
        return 'M0,' + rc + 'V-' + rc + 'M' + rc + ',0H-' + rc;
    },

    'x-thin': function(r) {
        var rx = roundn(r, 2);
        return 'M' + rx + ',' + rx + 'L-' + rx + ',-' + rx +
            'M' + rx + ',-' + rx + 'L-' + rx + ',' + rx;
    },

    asterisk: function(r) {
        var rc = roundn(r * 1.2, 2);
        var rs = roundn(r * 0.85, 2);
        return 'M0,' + rc + 'V-' + rc + 'M' + rc + ',0H-' + rc +
            'M' + rs + ',' + rs + 'L-' + rs + ',-' + rs +
            'M' + rs + ',-' + rs + 'L-' + rs + ',' + rs;
    },

    hash: function(r) {
        var r1 = roundn(r / 2, 2),
            r2 = roundn(r, 2);
        return 'M' + r1 + ',' + r2 + 'V-' + r2 +
            'm-' + r2 + ',0V' + r2 +
            'M' + r2 + ',' + r1 + 'H-' + r2 +
            'm0,-' + r2 + 'H' + r2;
    },

    'y-up': function(r) {
        var x = roundn(r * 1.2, 2),
            y0 = roundn(r * 1.6, 2),
            y1 = roundn(r * 0.8, 2);
        return 'M-' + x + ',' + y1 + 'L0,0M' + x + ',' + y1 + 'L0,0M0,-' + y0 + 'L0,0';
    },

    'y-down': function(r) {
        var x = roundn(r * 1.2, 2),
            y0 = roundn(r * 1.6, 2),
            y1 = roundn(r * 0.8, 2);
        return 'M-' + x + ',-' + y1 + 'L0,0M' + x + ',-' + y1 + 'L0,0M0,' + y0 + 'L0,0';
    },

    'y-left': function(r) {
        var y = roundn(r * 1.2, 2),
            x0 = roundn(r * 1.6, 2),
            x1 = roundn(r * 0.8, 2);
        return 'M' + x1 + ',' + y + 'L0,0M' + x1 + ',-' + y + 'L0,0M-' + x0 + ',0L0,0';
    },

    'y-right': function(r) {
        var y = roundn(r * 1.2, 2),
            x0 = roundn(r * 1.6, 2),
            x1 = roundn(r * 0.8, 2);
        return 'M-' + x1 + ',' + y + 'L0,0M-' + x1 + ',-' + y + 'L0,0M' + x0 + ',0L0,0';
    },

    'line-ew': function(r) {
        var rc = roundn(r * 1.4, 2);
        return 'M' + rc + ',0H-' + rc;
    },

    'line-ns': function(r) {
        var rc = roundn(r * 1.4, 2);
        return 'M0,' + rc + 'V-' + rc;
    },

    'line-ne': function(r) {
        var rx = roundn(r, 2);
        return 'M' + rx + ',-' + rx + 'L-' + rx + ',' + rx;
    },

    'line-nw': function(r) {
        var rx = roundn(r, 2);
        return 'M' + rx + ',' + rx + 'L-' + rx + ',-' + rx;
    },
};


for (let name in shapes) {
	let path = shapes[name](10) + shapes.circle(1)
    // if (name != 'triangle-left') continue

	showPath(path)
	showSdf(sdf(path, {w: 77, h: 77, viewBox: [-10, -10, 10, 10], stroke: -2}))
}


function showPath (path) {
    let cnv = document.body.appendChild(document.createElement('canvas'))
    let ctx = cnv.getContext('2d')
    let w = cnv.width = 77
    let h = cnv.height = 77

    ctx.fillStyle = 'black'
    ctx.fillRect(0,0,w,h)

    ctx.fillStyle = 'rgb(0,100,100)'
    ctx.strokeStyle = 'white'
    ctx.lineWidth = 2

    ctx.translate(77/2, 77/2)

    // IE fix
    if (!window.Path2D) return;

    let path2d = new Path2D(path)
    // ctx.fill(path2d)
    ctx.stroke(path2d)

    ctx.setTransform(1, 0, 0, 1, 0, 0);
}



function showSdf (arr) {
	let dim = Math.sqrt(arr.length)
	let cnv = document.body.appendChild(document.createElement('canvas'))
	let ctx = cnv.getContext('2d')
	let w = cnv.width = dim
	let h = cnv.height = dim
	let iData = ctx.createImageData(w, h) //new ImageData(w, h)
	let data = iData.data

	for (let i = 0; i < w; i++) {
		for (let j = 0; j < h; j++) {
			data[i*w*4 + j*4 + 0] = arr[i*w + j] * 255
			data[i*w*4 + j*4 + 1] = arr[i*w + j] * 255
			data[i*w*4 + j*4 + 2] = arr[i*w + j] * 255
			data[i*w*4 + j*4 + 3] = 255
		}
	}

	ctx.putImageData(iData, 0, 0)
}
