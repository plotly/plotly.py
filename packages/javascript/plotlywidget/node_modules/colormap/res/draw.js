/**
 * Compare canonic/compressed colormaps.
 * Generate compressed colormap jsons.
 */

var cubehelix = require('color-space/cubehelix');


if (typeof document === 'undefined') return;

//paint original and compressed colormap for comparison
var magma = require('./res/magma');
show(toImageData(magma), 'magma original');
show(toImageData(compress(magma, 32)), 'magma compressed');

var viridis = require('./res/viridis');
show(toImageData(viridis), 'viridis original');
show(toImageData(compress(viridis, 32)), 'viridis compressed');

var inferno = require('./res/inferno');
show(toImageData(inferno), 'inferno original');
show(toImageData(compress(inferno, 32)), 'inferno compressed');

var plasma = require('./res/plasma');
show(toImageData(plasma), 'plasma original');
show(toImageData(compress(plasma, 32)), 'plasma compressed');

getColors('./test/res/warm.png')
.then(function (data) {
	show(toImageData(data), 'warm original');
	show(toImageData(createCubehelix(16, {
		rotation: .6,
		start: 0,
		hue: 3,
		gamma: 1
	})), 'warm cubehelix approx');

	show(toImageData(compress(data, 111)), 'warm compressed');
});

getColors('./test/res/cool.png')
.then(function (data) {
	show(toImageData(data), 'cool original');
	show(toImageData(compress(data, 111)), 'cool compressed');
});

getColors('./test/res/rainbow.png')
.then(function (data) {
	show(toImageData(data), 'rainbow original');
	show(toImageData(compress(data, 88)), 'rainbow compressed');
});

var bathymetry = require('./res/bathymetry');
show(toImageData(bathymetry), 'bathymetry original');
show(toImageData(compress(bathymetry, 32)), 'bathymetry compressed');

var cdom = require('./res/cdom');
show(toImageData(cdom), 'cdom original');
show(toImageData(compress(cdom, 32)), 'cdom compressed');

var chlorophyll = require('./res/chlorophyll');
show(toImageData(chlorophyll), 'chlorophyll original');
show(toImageData(compress(chlorophyll, 32)), 'chlorophyll compressed');

var density = require('./res/density');
show(toImageData(density), 'density original');
show(toImageData(compress(density, 32)), 'density compressed');

var freesurfaceBlue = require('./res/freesurface-blue');
show(toImageData(freesurfaceBlue), 'freesurfaceBlue original');
show(toImageData(compress(freesurfaceBlue, 32)), 'freesurfaceBlue compressed');

var freesurfaceRed = require('./res/freesurface-red');
show(toImageData(freesurfaceRed), 'freesurfaceRed original');
show(toImageData(compress(freesurfaceRed, 32)), 'freesurfaceRed compressed');

var oxygen = require('./res/oxygen');
show(toImageData(oxygen), 'oxygen original');
show(toImageData(compress(oxygen, 32)), 'oxygen compressed');

var par = require('./res/par');
show(toImageData(par), 'par original');
show(toImageData(compress(par, 32)), 'par compressed');

var phase = require('./res/phase');
show(toImageData(phase), 'phase original');
show(toImageData(compress(phase, 32)), 'phase compressed');

var salinity = require('./res/salinity');
show(toImageData(salinity), 'salinity original');
show(toImageData(compress(salinity, 32)), 'salinity compressed');

var temperature = require('./res/temperature');
show(toImageData(temperature), 'temperature original');
show(toImageData(compress(temperature, 32)), 'temperature compressed');

var turbidity = require('./res/turbidity');
show(toImageData(turbidity), 'turbidity original');
show(toImageData(compress(turbidity, 32)), 'turbidity compressed');

var velocityBlue = require('./res/velocity-blue');
show(toImageData(velocityBlue), 'velocity-blue original');
show(toImageData(compress(velocityBlue, 32)), 'velocity-blue compressed');

var velocityGreen = require('./res/velocity-green');
show(toImageData(velocityGreen), 'velocity-green original');
show(toImageData(compress(velocityGreen, 32)), 'velocity-green compressed');
// console.log(JSON.stringify(toColormap(compress(velocityGreen, 32))));




//Helpers here

//get image colors
function getColors (image, cb) {
	var data = [];

	var img = createImage(image);

	var promise = new Promise(function (resolve) {
		img.onload = function () {
			var canvas = document.createElement('canvas');
			canvas.width = img.width;
			canvas.height = img.height;
			canvas.getContext('2d').drawImage(img, 0, 0, img.width, img.height);

			var ctx = canvas.getContext('2d');

			var imageData = ctx.getImageData(0, 0, img.width, 1).data;

			for (var i = 0; i < img.width; i++) {
				data.push([imageData[i*4]/255, imageData[i*4+1]/255, imageData[i*4+2]/255]);
			}

			resolve(data);
		};
	});


	return promise;
}


function createImage (url) {
	if (img instanceof Image) return img;

	var img = new Image();
	img.src = url;

	return img;
}

//create colormap by rotating cubehelix
function createCubehelix (steps, opts) {
	var data = [];

	for (var i = 0; i < steps; i++ ){
		data.push(cubehelix.rgb(i/steps, opts).map((v) => v/255));
	}

	return data;
}

//return imagedata from colormap
function toImageData (colors) {
	return colors.map((color) => color.map((v) => v*255).concat(255))
	.reduce((prev, curr) => prev.concat(curr));
}

//return interpolated imagedata with only each @factor pixel left
function compress (colors, factor) {
	var data = [];

	var len = (colors.length) / factor;
	var step = (colors.length-1) / len;

	for (var i = 0; i < colors.length; i+= step) {
		data.push(colors[i|0]);
	}

	return data;
}

//convert imagedata to colormap JSON
function toColormap (data) {
	var stops = [];

	for (var i = 0; i < data.length; i++) {
		stops.push({
			index: Math.round(i * 100 / (data.length - 1)) / 100,
			rgb: data[i].map((v) => Math.round(v*255))
		});
	}

	return stops;
}

//create a canvas with the image/colordata preview
function show (pixels, title) {
	if (typeof pixels === 'string') {
		var img = createImage(pixels);
		img.style.height = '40px';
		img.style.width = '100%';

		title && img.setAttribute('title', title);

		document.body.appendChild(img);
		return;
	}

	var canvas = document.createElement('canvas');
	var w = (pixels.length/4)|0;

	canvas.width = w;
	canvas.height = 1;
	canvas.style.height = '40px';
	canvas.style.width = '100%';

	var ctx = canvas.getContext('2d');
	var imageData = ctx.createImageData(w, 1);

	imageData.data.set(pixels);

	ctx.putImageData(imageData, 0, 0);

	title && canvas.setAttribute('title', title);

	document.body.appendChild(canvas);
	document.body.appendChild(document.createElement('br'));
}
