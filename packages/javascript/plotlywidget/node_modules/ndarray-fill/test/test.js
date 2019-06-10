var zeros = require("zeros")
var fill = require("../index.js")

if(typeof test === "undefined") {
  test = require("tape")
}

test('fill zeros', function(t) {

  var x = zeros([10,10])
  
  fill(x, function(a, b) {
    return a * 10 + b
  })
  
  for(var i=0; i<10; ++i) {
    for(var j=0; j<10; ++j) {
      t.equals(x.get(i,j), 10*i+j)
    }
  }
  
  t.end()
})
