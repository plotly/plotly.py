quantize
========

Node.js module for color quantization, based on Leptonica.

Install
-------

	npm install quantize

Quick Overview
--------------

###Usage

`````javascript
var quantize = require('quantize');

var arrayOfPixels = [[190,197,190], [202,204,200], [207,214,210], [211,214,211], [205,207,207]];
var maximumColorCount = 4;

var colorMap = quantize(arrayOfPixels, maximumColorCount);
`````

* `arrayOfPixels` - An array of pixels (represented as [R,G,B arrays]) to quantize
* `maxiumColorCount` - The maximum number of colours allowed in the reduced palette

#####Reduced Palette

The `.palette()` method returns an array that contains the reduced color palette.

`````javascript
// Returns the reduced palette
colorMap.palette(); 
// [[204, 204, 204], [208,212,212], [188,196,188], [212,204,196]]
`````

#####Reduced pixel

The `.map(pixel)` method maps an individual pixel to the reduced color palette.

`````javascript
// Returns the reduced pixel
colorMap.map(arrayOfPixels[0]);
// [188,196,188]
`````

Author
------

* [Olivier Lesnicki](https://github.com/olivierlesnicki)

Contributors
------------

* [Nick Rabinowitz](https://github.com/nrabinowitz)
* [Mike Bostock] (https://github.com/mbostock)

License
-------

Licensed under the MIT License.