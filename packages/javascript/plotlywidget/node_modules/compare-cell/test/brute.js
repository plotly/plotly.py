'use strict'

var tape = require('tape')
var compare = require('../compare')

tape('brute force check', function(t) {
  function seq(d, n, cb) {
    var comb = new Array(d)
    function rec(i) {
      if(i === d) {
        cb(comb)
      } else for(var j=0; j<n; ++j) {
        comb[i] = j
        rec(i+1)
      }
    }
    rec(0)
  }

  for(var i=1; i<=4; ++i) {
    seq(i, 5, function(a) {
      seq(i, 5, function(b) {
        var d = compare(a, b)
        var x = a.slice().sort().join()
        var y = b.slice().sort().join()
        if(x === y) {
          t.ok(d === 0, x + ' == ' + y)
        } else {
          t.ok(d !== 0, x + ' != ' + y)
        }
      })
    })
  }

  t.end()
})
