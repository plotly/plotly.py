var orient = require("robust-orientation")
var orderSegments = require("../lib/order-segments")

module.exports = checkInvariants

function sgn(x) {
  if(x < 0) {
    return -1
  }
  if(x > 0) {
    return 1
  }
  return 0
}

function checkInvariants(t, slabs) {
  var numSlabs = slabs.slabs.length
  t.equals(slabs.coordinates.length, numSlabs, "checking numSlabs")
  t.equals(slabs.horizontal.length, numSlabs, "checking horizontal")
  if(numSlabs > 0) {
    t.equals(slabs.slabs[numSlabs-1], null, "check last slab null")
  }
  for(var i=0; i<numSlabs; ++i) {
    var x = slabs.coordinates[i]
    var y = Infinity
    if(i<numSlabs-1) {
      y = slabs.coordinates[i+1]
    }
    t.ok(x < y, "check coordinate order increasing")
    var h = slabs.horizontal[i]
    for(var j=0; j<h.length; ++j) {
      if(j < h.length-1) {
        t.ok(h[j].y <= h[j+1].y, "checking horizontal ordering")
        t.ok(h[j].start != h[j+1].start, "checking alternating")
        if(h[j].start) {
          t.notEquals(h[j].closed, h[j+1].closed, "check halfopen")
        }
      }
    }
    var s = slabs.slabs[i]
    if(s) {
      var list = []
      function visit(node) {
        var k = node.key
        var lo = Math.min(node.key[0][0], node.key[1][0])
        var hi = Math.max(node.key[0][0], node.key[1][0])
        t.ok(lo <= x, "check segment in range of slab lo")
        t.ok(y <= hi, "check segment in range of slab hi")
        if(node.left) {
          visit(node.left)
        }
        list.push(node)
        if(node.right) {
          visit(node.right)
        }
      }
      visit(s)

      //Verify segments are in ascending y
      for(var j=0; j<list.length-1; ++j) {
        var a = list[j].key
        var b = list[j+1].key
        t.equals(sgn(orderSegments(a, b)), -1, "check segment order")
        t.notEqual(a[0][0], a[1][0], "check not horizontal a")
        t.notEqual(b[0][0], b[1][0], "check not horizontal b")
        if(b[0][0] < b[1][0]) {
          t.ok(orient(b[0], b[1], a[0]) <= 0, "check a[0] below b")
          t.ok(orient(b[0], b[1], a[1]) <= 0, "check a[1] below b")
        } else {
          t.ok(orient(b[1], b[0], a[0]) <= 0, "check a[0] below b")
          t.ok(orient(b[1], b[0], a[1]) <= 0, "check a[1] below b")
        }
        if(a[0][0] < a[1][0]) {
          t.ok(orient(a[0], a[1], b[0]) >= 0, "check b[0] above a")
          t.ok(orient(a[0], a[1], b[1]) >= 0, "check b[1] above a")
        } else {
          t.ok(orient(a[1], a[0], b[0]) >= 0, "check b[0] above a")
          t.ok(orient(a[1], a[0], b[1]) >= 0, "check b[1] above a")
        }
      }
    }
  }
}