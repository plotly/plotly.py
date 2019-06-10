"use strict"

var scc = require("../scc.js")

require("tape")(function(t) {

  var g = [
    [4], // 0
    [0,2], // 1
    [1,3], // 2
    [2], // 3
    [1], // 4
    [4,6], // 5
    [5,2], // 6
    [7,6,3], // 7
  ]
  
  // SCCs:
  // A: 0 -> 4 -> 1 -> 0, 1 -> 2 -> 1, 2 -> 3 -> 2
  // B: 5 -> 6 -> 5
  // C: 7 -> 7
  // graph on SCCs:
  // B -> A
  // C -> A, B
  
  var sccRet = scc(g)
  console.log(sccRet)
  t.equal(sccRet.components.length, 3)

  t.end()
})
