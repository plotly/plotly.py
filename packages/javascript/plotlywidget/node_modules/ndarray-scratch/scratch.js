"use strict"

var ndarray = require("ndarray")
var ops = require("ndarray-ops")
var pool = require("typedarray-pool")

function clone(array) {
  var dtype = array.dtype
  if(dtype === "generic" || dtype === "array") {
    dtype = "double"
  }
  var data = pool.malloc(array.size, dtype)
  var result = ndarray(data, array.shape)
  ops.assign(result, array)
  return result
}
exports.clone = clone

function malloc(shape, dtype) {
  if(!dtype) {
    dtype = "double"
  }
  var sz = 1
  var stride = new Array(shape.length)
  for(var i=shape.length-1; i>=0; --i) {
    stride[i] = sz
    sz *= shape[i]
  }
  return ndarray(pool.malloc(sz, dtype), shape, stride, 0)
}
exports.malloc = malloc

function free(array) {
  if(array.dtype === "generic" || array.dtype === "array") {
    return
  }
  pool.free(array.data)
}
exports.free = free

function zeros(shape, dtype) {
  if(!dtype) {
    dtype = "double"
  }

  var sz = 1
  var stride = new Array(shape.length)
  for(var i=shape.length-1; i>=0; --i) {
    stride[i] = sz
    sz *= shape[i]
  }
  var buf = pool.malloc(sz, dtype)
  for(var i=0; i<sz; ++i) {
    buf[i] = 0
  }
  return ndarray(buf, shape, stride, 0)
}
exports.zeros = zeros

function ones(shape, dtype) {
  if(!dtype) {
    dtype = "double"
  }

  var sz = 1
  var stride = new Array(shape.length)
  for(var i=shape.length-1; i>=0; --i) {
    stride[i] = sz
    sz *= shape[i]
  }
  var buf = pool.malloc(sz, dtype)
  for(var i=0; i<sz; ++i) {
    buf[i] = 1
  }
  return ndarray(buf, shape, stride, 0)
}
exports.ones = ones

function eye(shape, dtype) {
  var i, offset
  if(!dtype) {
    dtype = "double"
  }

  var sz = 1
  var stride = new Array(shape.length)
  for(i=shape.length-1; i>=0; --i) {
    stride[i] = sz
    sz *= shape[i]
  }
  var buf = pool.malloc(sz, dtype)
  for(i=0; i<sz; ++i) {
    buf[i] = 0
  }
  var mindim = Infinity
  var offsum = 0
  for( i=shape.length-1; i>=0; i--) {
    offsum += stride[i]
    mindim = Math.min(mindim,shape[i])
  }
  for(i=0,offset=0; i<mindim; i++,offset+=offsum) {
    buf[offset] = 1
  }
  return ndarray(buf, shape, stride, 0)
}
exports.eye = eye
