var test = require("tape")
  , rank = require("../index.js").rank
  , unrank = require("../index.js").unrank

var ranks = [
  [1,2,3,0],
  [2,1,3,0],
  [2,3,1,0],
  [3,2,1,0],
  [1,3,2,0],
  [3,1,2,0],
  [3,2,0,1],
  [2,3,0,1],
  [2,0,3,1],
  [0,2,3,1],
  [3,0,2,1],
  [0,3,2,1],
  [1,3,0,2],
  [3,1,0,2],
  [3,0,1,2],
  [0,3,1,2],
  [1,0,3,2],
  [0,1,3,2],
  [1,2,0,3],
  [2,1,0,3],
  [2,0,1,3],
  [0,2,1,3],
  [1,0,2,3],
  [0,1,2,3]
]

test("rank", function(t) {
  t.equals(rank([]), 0)
  t.equals(rank([0]), 0)
  for(var i=0; i<ranks.length; ++i) {
    t.equals(rank(ranks[i]), i, "rank " + i + ":" + ranks[i])
  }
  
  t.end()
})



test("unrank", function(t) {

  function check(r, b) {
    var a = unrank(b.length, r)
    t.equals(a.join(","), b.join(","), "unrank " + r + ":" + b)
  }
  
  check(0, [])
  check(0, [0])
  check(0, [1,0])
  check(1, [0,1])
  
  for(var i=0; i<ranks.length; ++i) {
    check(i, ranks[i])
  }
  
  t.end()
})