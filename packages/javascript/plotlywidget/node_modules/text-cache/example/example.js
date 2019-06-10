'use strict'

var getText = require('../textcache')
var complex = getText('arial', '123 hello world a5d5   7 0.123')

//"Hello world! 你好"

var scale = 500 / complex.shape
var data = complex.data

var svg = ['<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"  width="500"  height="500" >']
for(var i=0; i<data.length; i+=6) {
  for(var j=0; j<6; j+=2) {
    var x0 = scale * data[i+j]
    var y0 = scale * data[i+j+1]
    var x1 = scale * data[i+((j+2)%6)]
    var y1 = scale * data[i+((j+3)%6)]
    svg.push('<line x1="' + x0 + '" y1="' + y0 +
      '" x2="' + x1 + '" y2="' + y1 +
      '" stroke-width="1" stroke="black" />')
  }
}
svg.push("</svg>")

document.body.innerHTML = svg.join("")
