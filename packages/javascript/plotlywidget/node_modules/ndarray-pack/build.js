"use strict"

var bake = require("cwise-bake")

console.log("module.exports=require('cwise-compiler')(" + JSON.stringify(
  bake({
    args: ["array", "scalar", "index"],
    body: function(o, a, x) {
var v=a,i
for(i=0;i<x.length-1;++i) {
v=v[x[i]]
}
o=v[x[x.length-1]]
},
    funcName: "convert"
  })) + ")")