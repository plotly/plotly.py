var sgn = require("../permutation-sign")
var unrank = require("permutation-rank").unrank


var start = Date.now()
for(var n=0; n<1; ++n) {
  for(var i=0; i<3628800; ++i) {
    var p = unrank(10, i)
    var s = sgn(p)
  }
}
console.log(Date.now()-start)