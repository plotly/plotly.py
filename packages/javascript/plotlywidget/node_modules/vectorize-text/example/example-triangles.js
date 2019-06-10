"use strict"

var vectorizeText = require("../index.js")

var complex = vectorizeText("Hello world! 你好", {
  triangles: true,
  width: 500,
  textBaseline: "top"
})

var svg = ['<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"  width="500"  height="80" >']
complex.cells.forEach(function(c) {
  for(var j=0; j<3; ++j) {
    var p0 = complex.positions[c[j]]
    var p1 = complex.positions[c[(j+1)%3]]
    svg.push('<line x1="' + p0[0] + '" y1="' + p0[1] + 
      '" x2="' + p1[0] + '" y2="' + p1[1] + 
      '" stroke-width="1" stroke="black" />')
  }
})
svg.push("</svg>")

if(typeof window !== "undefined") {
  document.body.innerHTML = svg.join("")
} else {
  console.log(svg.join(""))
}