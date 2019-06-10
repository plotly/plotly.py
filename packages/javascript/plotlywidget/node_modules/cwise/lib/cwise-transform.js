"use strict"

module.exports = cwiseTransform

var staticModule = require("static-module")
var parse = require("cwise-parser")
var uglify = require("uglify-js")

var REQUIRED_FIELDS = [ "args", "body" ]
var OPTIONAL_FIELDS = [ "pre", "post", "printCode", "funcName", "blockSize" ]

function processFunc(func) {
  var codeStr = "var X=" + func
  var minified = uglify.minify(codeStr, {fromString: true, compress: { unused: "keep_assign" }}).code
  var code = minified.substr(6, minified.length-7)
  return parse(code)
}

function cwiseTransform(file, opts) {
  var sm = staticModule({
    cwise: function(user_args) {
      for(var id in user_args) {
        if(REQUIRED_FIELDS.indexOf(id) < 0 &&
           OPTIONAL_FIELDS.indexOf(id) < 0) {
          console.warn("cwise: Unknown argument '"+id+"' passed to expression compiler")
        }
      }
      for(var i=0; i<REQUIRED_FIELDS.length; ++i) {
        if(!user_args[REQUIRED_FIELDS[i]]) {
          throw new Error("cwise: Missing argument: " + REQUIRED_FIELDS[i])
        }
      }
      var compileBlock = {
        args:       user_args.args,
        pre:        processFunc(user_args.pre || function(){}),
        body:       processFunc(user_args.body),
        post:       processFunc(user_args.post || function(){}),
        debug:      !!user_args.printCode,
        funcName:   user_args.funcName || user_args.body.name || "cwise",
        blockSize:  user_args.blockSize || 64
      }
      var codeStr = "require('cwise/lib/wrapper')(" + JSON.stringify(compileBlock) + ")"
      return codeStr
    }
  })
  return sm
}
