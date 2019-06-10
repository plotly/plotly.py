'use strict'

require('enable-mobile')
document.body.style.fontFamily = 'sans-serif'
document.body.style.padding = '2rem'

var calcSDF = require('./')

var canvas = document.body.appendChild(document.createElement('canvas'))
canvas.style.margin = '1rem 1rem 1rem 0'

canvas.width = 165
canvas.height = 150

var ctx = canvas.getContext('2d')
ctx.fillStyle = 'black'
ctx.fillRect(0,0,canvas.width, canvas.height)
ctx.fillStyle = 'white'
ctx.font = 'bold 100px sans-serif'
ctx.fillText('X', 50, 100)


var out = document.body.appendChild(document.createElement('canvas'))
out.style.margin = '1rem 1rem 1rem 0'

out.width = 165
out.height = 150
var outCtx = out.getContext('2d')

outCtx.drawImage(canvas, 0, 0);


var cutoff = 0, radius = 10

update()

function update () {
	var idata = ctx.getImageData(0,0,canvas.width, canvas.height).data
	var data = Array(canvas.width*canvas.height)
	for (var i = 0; i < data.length; i++) {
		data[i] = idata[i*4]/255
	}

	console.time('sdf')
	var arr = calcSDF(data, {
		cutoff: cutoff,
		radius: radius,
		width: canvas.width,
		height:  canvas.height
	})
	console.timeEnd('sdf')

	let imgArr
	if (global.Uint8ClampedArray) {
		imgArr = new Uint8ClampedArray(165*150*4)
	} else {
		imgArr = Array(165*150*4)
	}
	for (let i = 0; i < 165; i++) {
		for (let j = 0; j < 150; j++) {
			imgArr[j*165*4 + i*4 + 0] = arr[j*165+i]*255
			imgArr[j*165*4 + i*4 + 1] = arr[j*165+i]*255
			imgArr[j*165*4 + i*4 + 2] = arr[j*165+i]*255
			imgArr[j*165*4 + i*4 + 3] = 255
		}
	}

	// IE way
	var c = document.createElement('canvas');
	var data = c.getContext('2d').createImageData(165, 150);

	if (data.data.set) {
		data.data.set(imgArr);
	}
	else {
		for (var i = 0; i < imgArr.length; i++) {
			data.data[i] = imgArr[i]
		}
	}

	// var data = new ImageData(imgArr, 165, 150)
	outCtx.putImageData(data, 0, 0)
}


var cutoffTitle = document.body.appendChild(document.createElement('label'))
cutoffTitle.innerHTML = 'Cutoff'
cutoffTitle.style.display = 'block'

var cutoffEl = document.body.appendChild(document.createElement('input'))
cutoffEl.type = 'range'
cutoffEl.min = 0
cutoffEl.max = 1
cutoffEl.step = 0.001
cutoffEl.value = cutoff
cutoffEl.oninput = e => {
	cutoff = parseFloat(cutoffEl.value)
	update()
}


var radTitle = document.body.appendChild(document.createElement('label'))
radTitle.innerHTML = 'Radius'
radTitle.style.display = 'block'

var radEl = document.body.appendChild(document.createElement('input'))
radEl.type = 'range'
radEl.min = 0
radEl.max = 100
radEl.step = 0.2
radEl.value = radius
radEl.oninput = e => {
	radius = parseFloat(radEl.value)
	update()
}
