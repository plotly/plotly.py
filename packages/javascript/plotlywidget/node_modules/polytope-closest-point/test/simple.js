var test = require("tap").test;
var closestPoint = require("../index.js");

test("closest point", function(t) {

  var p0 = [1,0,0];
  var p1 = [0,1,0];
  var p2 = [0,0,1];
  var p3 = [0,0,0];
  var x  = [1,1,1];
  var r  = [0,0,0];
  
  var points = [p0, p1, p2, p3];
  
  var d = closestPoint([], points, x, r);
  console.log(r, d);
  t.assert(isNaN(d));
  
  d = closestPoint([0], points, x, r);
  t.assert(Math.abs(d - 2.0) < 1e-6);
  console.log(r, d);
  
  d = closestPoint([0,1], points, x, r);
  t.assert(Math.abs(d - 1.5) < 1e-6);
  console.log(r, d);
  
  d = closestPoint([0,1,2], points, x, r);
  t.assert(Math.abs(d - 4.0/3.0) < 1e-6);
  console.log(r, d);
  
  d = closestPoint([0,1,2,3], points, x, r);
  console.log(r, d);

  t.end();
});