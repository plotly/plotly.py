var test = require("tap").test;
var closestPoint0d = require("../lib/closest_point_0d.js");
var closestPointnd = require("../lib/closest_point_nd.js");

test("0d closest point", function(t) {
  for(var d=1; d<6; ++d) {
    var p0 = new Array(d);
    var x  = new Array(d);
    var r0 = new Array(d);
    var r1 = new Array(d);
    for(var n=0; n<100; ++n) {
      for(var i=0; i<d; ++i) {
        p0[i] = Math.random() * 10.0 - 5.0;
        x[i]  = Math.random() * 10.0 - 5.0;
      }
      var d0 = closestPoint0d(p0, x, r0);
      var d1 = closestPointnd([0], [p0], x, r1);
      t.assert(Math.abs(d0 - d1) < 1e-4, "check:" + d0 + " ~ " + d1);
     
      for(var i=0; i<d; ++i) {
        t.assert(Math.abs(r0[i] - r1[i]) < 1e-4, "check:" + r0 + " ~ " + r1);
      }
    }
  }
  t.end();
});