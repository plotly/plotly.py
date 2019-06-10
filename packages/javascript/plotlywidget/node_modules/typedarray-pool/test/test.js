"use strict"

//Check upgrade works
var dup = require("dup")
global.__TYPEDARRAY_POOL = {
  UINT8   : dup([32, 0])
, UINT16  : dup([32, 0])
, UINT32  : dup([32, 0])
, INT8    : dup([32, 0])
, INT16   : dup([32, 0])
, INT32   : dup([32, 0])
, FLOAT   : dup([32, 0])
, DOUBLE  : dup([32, 0])
, DATA    : dup([32, 0])
}

var pool = require("../pool.js")

require("tape")("typedarray-pool", function(t) {

  pool.clearCache()

  for(var i=1; i<100; ++i) {
    var a
    a = pool.malloc(i, "int8")
    t.assert(a instanceof Int8Array, "int8array valid")
    t.assert(a.length >= i, "int8array length")
    pool.free(a)
    
    a = pool.malloc(i, "int16")
    t.assert(a instanceof Int16Array, "int16")
    t.assert(a.length >= i)
    pool.free(a)
    
    a = pool.malloc(i, "int32")
    t.assert(a instanceof Int32Array, "int32")
    t.assert(a.length >= i)
    pool.free(a)
    
    a = pool.malloc(i, "uint8")
    t.assert(a instanceof Uint8Array, "uint8")
    t.assert(!Buffer.isBuffer(a), "not buffer")
    t.assert(a.length >= i)
    pool.free(a)
    
    a = pool.malloc(i, "uint16")
    t.assert(a instanceof Uint16Array, "uint16")
    t.assert(a.length >= i)
    pool.free(a)
    
    a = pool.malloc(i, "uint32")
    t.assert(a instanceof Uint32Array, "uint32")
    t.assert(a.length >= i)
    pool.free(a)
    
    a = pool.malloc(i, "float")
    t.assert(a instanceof Float32Array, "float")
    t.assert(a.length >= i)
    pool.free(a)
    
    a = pool.malloc(i, "double")
    t.assert(a instanceof Float64Array, "double")
    t.assert(a.length >= i)
    pool.free(a)

    a = pool.malloc(i, "uint8_clamped")
    if((typeof Uint8ClampedArray) !== "undefined") {
        t.assert(a instanceof Uint8ClampedArray, "uint8_clamped")
    } else {
        t.assert(a instanceof Uint8Array, "unit8_clamped clamped default to uint8")
    }
    t.assert(a.length >= i)
    pool.free(a)

    a = pool.malloc(i, "buffer")
    t.assert(Buffer.isBuffer(a), "buffer")
    t.assert(a.length >= i)
    pool.free(a)
    
    a = pool.malloc(i)
    t.assert(a instanceof ArrayBuffer, "array buffer")
    t.assert(a.byteLength >= i)
    pool.free(a)

    a = pool.malloc(i, "arraybuffer")
    t.assert(a instanceof ArrayBuffer, "array buffer")
    t.assert(a.byteLength >= i)
    pool.free(a)

    a = pool.malloc(i, "dataview")
    t.assert(a instanceof DataView, "dataview")
    t.assert(a.byteLength >= i)
    pool.free(a)
  }
  
  for(var i=1; i<100; ++i) {
    var a
    a = pool.mallocInt8(i)
    t.assert(a instanceof Int8Array, "int8")
    t.assert(a.length >= i)
    pool.freeInt8(a)
    
    a = pool.mallocInt16(i)
    t.assert(a instanceof Int16Array, "int16")
    t.assert(a.length >= i)
    pool.freeInt16(a)
    
    a = pool.mallocInt32(i)
    t.assert(a instanceof Int32Array, "int32")
    t.assert(a.length >= i)
    pool.freeInt32(a)
    
    a = pool.mallocUint8(i)
    t.assert(a instanceof Uint8Array, "uint8")
    t.assert(!Buffer.isBuffer(a), "not buffer")
    t.assert(a.length >= i)
    pool.freeUint8(a)
    
    a = pool.mallocUint16(i)
    t.assert(a instanceof Uint16Array, "uint16")
    t.assert(a.length >= i)
    pool.freeUint16(a)
    
    a = pool.mallocUint32(i)
    t.assert(a instanceof Uint32Array, "uint32")
    t.assert(a.length >= i)
    pool.freeUint32(a)
    
    a = pool.mallocFloat(i)
    t.assert(a instanceof Float32Array, "float32")
    t.assert(a.length >= i)
    pool.freeFloat(a)
    
    a = pool.mallocDouble(i)
    t.assert(a instanceof Float64Array, "float64")
    t.assert(a.length >= i)
    pool.freeDouble(a)
    
    a = pool.mallocUint8Clamped(i)
    if((typeof Uint8ClampedArray) !== "undefined") {
        t.assert(a instanceof Uint8ClampedArray, "uint8 clamped")
    } else {
        t.assert(a instanceof Uint8Array, "uint8 clamped defaults to unt8")
    }
    t.assert(a.length >= i)
    pool.freeUint8Clamped(a)

    a = pool.mallocBuffer(i)
    t.assert(Buffer.isBuffer(a), "buffer")
    t.assert(a.length >= i)
    pool.freeBuffer(a)
    
    a = pool.mallocArrayBuffer(i)
    t.assert(a instanceof ArrayBuffer, "array buffer")
    t.assert(a.byteLength >= i)
    pool.freeArrayBuffer(a)

    a = pool.mallocDataView(i)
    t.assert(a instanceof DataView, "data view")
    t.assert(a.byteLength >= i)
    pool.freeDataView(a)
  }
  
  pool.clearCache()

  t.end()
})