var test = require("tap").test;
var closestPoint2d = require("../lib/closest_point_2d.js");
var closestPointnd = require("../lib/closest_point_nd.js");

test("2d closest point", function(t) {
  for(var d=1; d<6; ++d) {
    var p0 = new Array(d);
    var p1 = new Array(d);
    var p2 = new Array(d);
    var x  = new Array(d);
    var r0 = new Array(d);
    var r1 = new Array(d);
    for(var n=0; n<100; ++n) {
      for(var i=0; i<d; ++i) {
        p0[i] = Math.random() * 10.0 - 5.0;
        p1[i] = Math.random() * 10.0 - 5.0;
        p2[i] = Math.random() * 10.0 - 5.0;
        x[i]  = Math.random() * 10.0 - 5.0;
      }
      var d0 = closestPoint2d(p0, p1, p2, x, r0);
      var d1 = closestPointnd([0,1,2], [p0, p1, p2], x, r1);
      if(isNaN(d1)) {
        console.warn("closest_point_nd failed: ", p0, p1, x, d0, r0);
        continue;
      }
      t.assert(Math.abs(d0 - d1) < 1e-4, "check d:" + d0 + " ~ " + d1 + "; p0:"+p0 + ", p1:" + p1 + ", x:" + x);
      for(var i=0; i<d; ++i) {
        t.assert(Math.abs(r0[i] - r1[i]) < 1e-4, "check r:" + r0 + " ~ " + r1);
      }
    }
  }
  t.end();
});