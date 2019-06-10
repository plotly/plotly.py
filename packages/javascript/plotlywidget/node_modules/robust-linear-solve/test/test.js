"use strict"

var robustScale = require("robust-scale")
var robustSum = require("robust-sum")
var robustCompre = require("robust-compare")
var validate = require("validate-robust-sequence")
var compress = require("robust-compress")
var tape = require("tape")

var robustLinSolve = require("../linsolve")

tape("robust-linear-solve", function(t) {

  function verify(A, b, unsolvable, label) {
    if(!label) {
      label = "hardcoded: "
    }
    var x = robustLinSolve(A, b)
    t.equals(x.length, A.length + 1, label + "check vector length")
    for(var i=0; i<x.length; ++i) {
      t.ok(validate(x[i]), label + "check valid sequence")
      t.ok(x[i].length <= compress(x[i]).length, label + "check compression")
    }
    if(unsolvable) {
      t.same(x[A.length], [0], "check system unsolvable")
    } else {
      for(var i=0; i<A.length; ++i) {
        var bi = robustScale(x[A.length], b[i])
        var ai = [ 0 ] 
        for(var j=0; j<A.length; ++j) {
          ai = robustSum(ai, robustScale(x[j], A[i][j]))
        }
        t.equals(robustCompre(ai, bi), 0, label + "check component " + i + " equal")
      }
    }
  }

  verify([[1]], [1])
  verify([[1,0], [0,1]], [1, 2])
  verify([[1,0], [0,0]], [1,2], true)


  //Fuzz 1D
  for(var i=0; i<10; ++i) {
    verify([[Math.random()-0.5]], [Math.random()-0.5], false, "fuzz1d: ")
  }

  //Fuzz 2D
  for(var i=0; i<10; ++i) {
    verify([[Math.random()-0.5, Math.random()-0.5],
            [Math.random()-0.5, Math.random()-0.5]], 
            [Math.random()-0.5, Math.random()-0.5], false, "fuzz2d: ")
  }

  //Fuzz 3D  
  for(var i=0; i<10; ++i) {
    verify([[Math.random()-0.5, Math.random()-0.5, Math.random()-0.5],
            [Math.random()-0.5, Math.random()-0.5, Math.random()-0.5],
            [Math.random()-0.5, Math.random()-0.5, Math.random()-0.5]], 
            [Math.random()-0.5, Math.random()-0.5, Math.random()-0.5], false, "fuzz3d: ")
  }

  t.end()
})