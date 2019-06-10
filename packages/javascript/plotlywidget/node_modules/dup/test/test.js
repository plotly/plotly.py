var dup = require("../dup.js")

require("tap").test("dup", function(t) {

  t.equals(dup().length, 0)
  
  var a = dup(5)
  t.equals(a.length, 5)
  for(var i=0; i<5; ++i) {
    t.equals(a[i], 0)
  }

  var b = dup([3,2], 1)
  t.equals(b.length, 3)
  for(var i=0; i<3; ++i) {
    var c = b[i]
    t.equals(c.length, 2)
    t.equals(c[0], 1)
    t.equals(c[1], 1)
    if(i > 0) {
      t.assert(b[i] !== b[i-1])
    }
  }
  
  var c = dup([], 100)
  t.equals(c.length, 0)
  
  t.end()
})