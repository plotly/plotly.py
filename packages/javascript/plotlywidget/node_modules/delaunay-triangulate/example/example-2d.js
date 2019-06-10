"use strict"

var shell = require("game-shell")()
var dt = require("../triangulate")

//Initialize triangulation
var points = new Array(1000)
  for(var i=0; i<1000; ++i) {
    points[i] = [Math.random(), Math.random()]
  }
var cells = dt(points)

var canvas, context

shell.on("init", function() {
  canvas = document.createElement("canvas")
  canvas.width = shell.width
  canvas.height = shell.height
  context = canvas.getContext("2d")
  shell.element.appendChild(canvas)
})

shell.on("resize", function(w, h) {
  canvas.width = w
  canvas.height = h
})

shell.on("render", function() {
  var w = canvas.width
  var h = canvas.height
  var mouse = [shell.mouseX/w, shell.mouseY/h]
  context.setTransform(
    w, 0, 
    0, h,
    0, 0)
  context.fillStyle = "#fff"
  context.fillRect(0,0,w,h)

  context.strokeStyle = "#000"
  context.lineWidth = Math.min(1.0/w, 1.0/h)
  for(var i=0; i<cells.length; ++i) {
    var cell = cells[i]
    context.beginPath()
    context.moveTo(points[cell[0]][0], points[cell[0]][1])
    for(var j=1; j<cell.length; ++j) {
      context.lineTo(points[cell[j]][0], points[cell[j]][1])
    }
    context.closePath()
    context.stroke()
  }

  context.fillStyle = "#000"
  for(var i=0; i<points.length; ++i) {
    context.beginPath()
    context.arc(points[i][0], points[i][1], 5.0/w, 0, 2*Math.PI)
    context.closePath()
    context.fill()
  }
})