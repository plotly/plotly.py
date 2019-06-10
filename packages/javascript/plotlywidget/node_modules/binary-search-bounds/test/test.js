"use strict"

var tape = require("tape")
var bounds = require("../search-bounds.js")
var guard = require("guarded-array")

tape("greaterThanEquals", function(t) {

  var lb = bounds.ge

  function checkArray(arr, values) {
    var garr = guard(arr)
    for(var l=0; l<arr.length; ++l) {
      for(var h=l; h<arr.length; ++h) {
        for(var i=0; i<values.length; ++i) {
          for(var j=l; j<=h; ++j) {
            if(arr[j] >= values[i]) {
              break
            }
          }
          t.equals(lb(garr, values[i], l, h), j, 'search in ['+l+','+h+']')
        }
      }
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
    var garr = guard(arr)
    for(var l=0; l<arr.length; ++l) {
      for(var h=l; h<arr.length; ++h) {
        for(var i=0; i<values.length; ++i) {
          for(var j=h; j>=l; --j) {
            if(values[i] > arr[j]) {
              break
            }
          }
          t.equals(lu(garr, values[i], l, h), j,
            i + " - indexOf(" + values[i] + ")="+j + " [" + l + "," + h + "]")
        }
      }
    }
  }

  checkArray([0,1,1,1,2], [-1, 0, 1, 2, 0.5, 1.5, 5])

  t.end()
})


tape("greaterThan", function(t) {

  var lb = bounds.gt

  function checkArray(arr, values) {
    var garr = guard(arr)
    for(var l=0; l<arr.length; ++l) {
      for(var h=l; h<arr.length; ++h) {
        for(var i=0; i<values.length; ++i) {
          for(var j=l; j<=h; ++j) {
            if(arr[j] > values[i]) {
              break
            }
          }
          t.equals(lb(garr, values[i], l, h), j)
        }
      }
    }
  }

  checkArray([0,1,1,1,2], [-1, 0, 1, 2, 0.5, 1.5, 5])

  t.end()
})


tape("lessThanEquals", function(t) {

  var lu = bounds.le

  function checkArray(arr, values) {
    var garr = guard(arr)
    for(var i=0; i<values.length; ++i) {
      for(var j=arr.length-1; j>=0; --j) {
        if(values[i] >= arr[j]) {
          break
        }
      }
      t.equals(lu(garr, values[i]), j, i + " - indexOf(" + values[i] + ")="+j )
    }
  }

  checkArray([0,1,1,1,2], [-1, 0, 1, 2, 0.5, 1.5, 5])

  t.end()
})



tape("equals", function(t) {

  var lu = bounds.eq

  function checkArray(arr, values) {
    var garr = guard(arr)
    for(var i=0; i<values.length; ++i) {
      if(arr.indexOf(values[i]) < 0) {
        t.equals(lu(garr, values[i]), -1)
      } else {
        t.equals(arr[lu(garr, values[i])], values[i])
      }
    }
  }

  checkArray([0,1,1,1,2], [-1, 0, 1, 2, 0.5, 1.5, 5])

  t.end()
})
