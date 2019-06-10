"use strict"

var tape = require("tape")
var bounds = require("../search-bounds.js")
var ndarray = require("ndarray")

tape("greaterThanEquals", function(t) {

  var lb = bounds.ge

  function checkArray(arr, values) {
    for(var i=0; i<values.length; ++i) {
      for(var j=0; j<arr.length; ++j) {
        if(arr[j] >= values[i]) {
          break
        }
      }
      t.equals(lb(arr, values[i]), j)
    }
  }
  
  checkArray([0,1,1,1,2], [-1, 0, 1, 2, 0.5, 1.5, 5])

  t.equals(lb([0,2,5,6], 0), 0)
  t.equals(lb([0,2,5,6], 1), 1)
  t.equals(lb([0,2,5,6], 2), 1)
  t.equals(lb([0,2,5,6], 3), 2)
  t.equals(lb([0,2,5,6], 4), 2)
  t.equals(lb([0,2,5,6], 5), 2)
  t.equals(lb([0,2,5,6], 6), 3)

  function cmp(a,b) {
    return a - b
  }
  
  t.equals(lb([0,1,1,1,2], -1, cmp), 0)
  t.equals(lb([0,1,1,1,2], 0, cmp), 0)
  t.equals(lb([0,1,1,1,2], 1, cmp), 1)
  t.equals(lb([0,1,1,1,2], 2, cmp), 4)
  t.equals(lb([0,1,1,1,2], 0.5, cmp), 1)
  t.equals(lb([0,1,1,1,2], 1.5, cmp), 4)
  t.equals(lb([0,1,1,1,2], 5, cmp), 5)

  t.equals(lb([0,2,5,6], 0, cmp), 0)
  t.equals(lb([0,2,5,6], 1, cmp), 1)
  t.equals(lb([0,2,5,6], 2, cmp), 1)
  t.equals(lb([0,2,5,6], 3, cmp), 2)
  t.equals(lb([0,2,5,6], 4, cmp), 2)
  t.equals(lb([0,2,5,6], 5, cmp), 2)
  t.equals(lb([0,2,5,6], 6, cmp), 3)

  t.end()
})

tape("lessThan", function(t) {

  var lu = bounds.lt

  function checkArray(arr, values) {
    for(var i=0; i<values.length; ++i) {
      for(var j=arr.length-1; j>=0; --j) {
        if(values[i] > arr[j]) {
          break
        }
      }
      t.equals(lu(arr, values[i]), j, i + " - indexOf(" + values[i] + ")="+j )
    }
  }

  checkArray([0,1,1,1,2], [-1, 0, 1, 2, 0.5, 1.5, 5])

  t.end()
})


tape("greaterThan", function(t) {

  var lb = bounds.gt

  function checkArray(arr, values) {
    for(var i=0; i<values.length; ++i) {
      for(var j=0; j<arr.length; ++j) {
        if(arr[j] > values[i]) {
          break
        }
      }
      t.equals(lb(arr, values[i]), j)
    }
  }

  checkArray([0,1,1,1,2], [-1, 0, 1, 2, 0.5, 1.5, 5])

  t.end()
})


tape("lessThanEquals", function(t) {

  var lu = bounds.le

  function checkArray(arr, values) {
    for(var i=0; i<values.length; ++i) {
      for(var j=arr.length-1; j>=0; --j) {
        if(values[i] >= arr[j]) {
          break
        }
      }
      t.equals(lu(arr, values[i]), j, i + " - indexOf(" + values[i] + ")="+j )
    }
  }

  checkArray([0,1,1,1,2], [-1, 0, 1, 2, 0.5, 1.5, 5])

  t.end()
})



tape("equals", function(t) {

  var lu = bounds.eq

  function checkArray(arr, values) {
    for(var i=0; i<values.length; ++i) {
      if(arr.indexOf(values[i]) < 0) {
        t.equals(lu(arr, values[i]), -1)
      } else {
        t.equals(arr[lu(arr, values[i])], values[i])
      }
    }
  }

  checkArray([0,1,1,1,2], [-1, 0, 1, 2, 0.5, 1.5, 5])

  t.end()
})