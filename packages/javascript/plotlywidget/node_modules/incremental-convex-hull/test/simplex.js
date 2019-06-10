"use strict"

var tape = require("tape")
var sc = require("simplicial-complex")
var ch = require("../ich")
var compare = require("./util/normalize").compare

for(var d=2; d<=7; ++d) {
  ;(function(d){
    tape("simplex " + d + "d", function(t) {

      var x = new Array(d)
      for(var i=0; i<d; ++i) {
        x[i] = 0.0
      }

      var points = [x]
      var cell = [0]
      for(var i=0; i<d; ++i) {
        var y = x.slice()
        y[i] = 1
        points.push(y)
        cell.push(i+1)
      }

      var expected = sc.boundary([cell])
      
      compare(t, ch(points), expected, "test base simplex boundary ok")

      var z = new Array(d)
      for(var i=0; i<d; ++i) {
        z[i] = 1.0 / (d+1)
      }
      points.unshift(z)

      cell.shift()
      cell.push(d+1)

      compare(t, ch(points), sc.boundary([cell]), "test simplex with point in center")

      t.end()
    })
  })(d)
}