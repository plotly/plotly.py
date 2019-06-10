"use strict"

var implementations = [
  { name: "delaunay-triangulate", algo: require("../triangulate") }
  //,{ name: "delaunay-fast", algo: require("delaunay-fast").triangulate }
  //,{ name: "delaunay", algo: require("delaunay").triangulate }
]

var cases = require("./cases.js")

var WARM_UP = 10
var NUM_ITER = 40

function doBench(algo, points) {
  for(var i=0; i<WARM_UP; ++i) {
    algo(points)
  }
  var count = 0
  var start = Date.now()
  for(var i=0; i<NUM_ITER; ++i) {
    count += algo(points).length
  }
  var end = Date.now()
  return [ (end - start)/NUM_ITER, count ]
}


function startBench() {
  implementations.forEach(function(impl) {
    console.log("testing", impl.name, "...")
    cases.forEach(function(testCase) {
      console.log("running test case:", testCase.name)
      var res = doBench(impl.algo, testCase.points)
      console.log("time:", res[0], "ms - numTris:", res[1])
    })
  })
}

window.startBench = startBench
//startBench()