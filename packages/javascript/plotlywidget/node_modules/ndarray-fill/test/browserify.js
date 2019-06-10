"use strict"

var browserify = require("browserify")
var tape = require("tape")
var vm = require("vm")

var cases = [ "test" ]

bundleCasesFrom(0)

function bundleCasesFrom(i) {
  if (i>=cases.length) return
  var b = browserify()
  b.ignore("tape")
  b.add(__dirname + "/" + cases[i] + ".js")
  tape(cases[i], function(t) { // Without nested tests, the asynchronous nature of bundle causes issues with tape...
    b.bundle(function(err, src) {
      if(err) {
        throw new Error("failed to bundle!")
      }
      vm.runInNewContext(src, {
        test: t.test.bind(t),
        Buffer: Buffer,
        Int8Array: Int8Array,
        Int16Array: Int16Array,
        Int32Array: Int32Array,
        Float32Array: Float32Array,
        Float64Array: Float64Array,
        Uint8Array: Uint8Array,
        Uint16Array: Uint16Array,
        Uint32Array: Uint32Array,
        Uint8ClampedArray: Uint8ClampedArray,
        console: { log: console.log.bind(console) }
      })
      t.end()
    })
  })
  bundleCasesFrom(i+1)
}
