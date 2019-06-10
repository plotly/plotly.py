"use strict"

var parse = require("cwise-parser")
var beautify = require("js-beautify")

var empty_func = JSON.stringify(parse(function(){}))

var proc = [
  "module.exports=require('cwise-compiler')({",
    "args:['array',{offset:[1],array:0},'scalar','scalar','index']",
    ",pre:", empty_func,
    ",post:", empty_func,
    ",body:",
      JSON.stringify(parse(function zeroCrossings(a, b, out, level, idx) {
        var da = a - level
        var db = b - level
        if((da >= 0) !== (db >= 0)) {
          out.push(idx[0] + 0.5 + 0.5 * (da + db) / (da - db))
        }
      })),
      ",funcName:'zeroCrossings'",
  "})"
]

console.log(beautify(proc.join("")))