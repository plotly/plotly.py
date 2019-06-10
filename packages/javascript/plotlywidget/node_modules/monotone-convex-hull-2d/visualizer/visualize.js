// Based on code from Dan Melanz
// https://github.com/melanz/graham-scan
//
var hull = require("../index.js")

var scale = document.body.querySelector("#scale").value
var resetButton = document.body.querySelector("#reset");
var canvas = document.body.querySelector("#canvas");
var context = canvas.getContext("2d");
var points = new Array();
var boundaryPoints = new Array();

function initialize() {   
    resetButton.addEventListener("click",reset);
    canvas.addEventListener("mousedown",addPoint,false);
    reset()
}

function drawAll() {
    scale = document.body.querySelector("#scale").value
    canvas.width = scale*2;
    canvas.height = scale*2;
    
    context.fillStyle = "rgb(255, 255, 255)"
    context.fillRect(0, 0, 400*scale/200, 400*scale/200)
    
  drawBoundary()
    drawPoints()
    console.log("points")
    console.log(points)
    boundaryPoints = hull(points).map(function(idx) {
        return points[idx]
    })
    console.log("bounds")
    console.log(boundaryPoints)
  drawConvexHull()
}

function convertCartesianToPixels(point) {
    var newPoint = [0, 0]
    newPoint[0] = scale*(point[0]+1)
    newPoint[1] = scale*(1-point[1])
    
    return newPoint
}

function convertPixelsToCartesian(point) {
    var newPoint = [0, 0]
    newPoint[0] = point[0]/scale-1
    newPoint[1] = 1-point[1]/scale
    
    return newPoint
}

function drawPoint(position) {
    var pos = convertCartesianToPixels(position)
    context.strokeStyle = "rgb(0, 0, 255)"
    context.beginPath();
    context.arc(pos[0],pos[1],4,0,2*Math.PI, true)
    context.closePath()
    context.stroke();
}

function drawLine(startCart, endCart) {
    context.beginPath()
    context.strokeStyle = "rgb(255, 0, 0)"
    var start = convertCartesianToPixels(startCart)
    var end = convertCartesianToPixels(endCart)
    context.moveTo(start[0],start[1])
    context.lineTo(end[0],end[1])
    context.closePath()
    context.stroke();
}

function drawConvexHull() {
  if(boundaryPoints.length>2) {
    for (var i=0;i<boundaryPoints.length-1;i++) {
      drawLine(boundaryPoints[i],boundaryPoints[i+1])
    }
    drawLine(boundaryPoints[boundaryPoints.length-1],boundaryPoints[0])
  }
}

function drawPoints() {
    for (var i=0;i<points.length;i++) {
        drawPoint(points[i])
    }
}

function drawBoundary() {
  drawLine([-1,-1],[-1,1])
  drawLine([-1,1],[1,1])
  drawLine([1,1],[1,-1])
  drawLine([1,-1],[-1,-1])
}

function reset() {
  points = new Array();
  boundaryPoints = new Array();
    drawAll()
}

function addPoint(event) {
    //console.log("Point added at px("+event.pageX+", "+event.pageY+")")
    var point = [0,0];
    point = convertPixelsToCartesian([event.pageX-canvas.offsetLeft, event.pageY-canvas.offsetTop])
    //position.push(point)
    //console.log(position)
    //initialPosition.push(point)
    console.log("Point added at ("+point[0]+", "+point[1]+")")
    console.log(" ");
  points.push(point);
    drawAll()
}

initialize()