"use strict"

var vectorizeText = require("../index.js")

var polygons = vectorizeText("Hello world! 你好", {
  polygons: true,
  width: 500,
  textBaseline: "top"
})

var svg = []
svg.push('<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"  width="500"  height="80" >')
polygons.forEach(function(loops) {
  svg.push('<path d="')
  loops.forEach(function(loop) {
    var start = loop[0]
    svg.push('M ' + start[0] + ' ' + start[1])
    for(var i=1; i<loop.length; ++i) {
      var p = loop[i]
      svg.push('L ' + p[0] + ' ' + p[1])
    }
    svg.push('L ' + start[0] + ' ' + start[1])
  })
  svg.push('" fill-rule="even-odd" stroke-width="1" fill="red"></path>')
})
svg.push('</svg>')

if(typeof window !== "undefined") {
  document.body.innerHTML = svg.join("")
} else {
  console.log(svg.join(""))
}
