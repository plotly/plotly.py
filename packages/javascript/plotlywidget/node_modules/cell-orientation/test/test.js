'use strict'

var tape = require('tape')
var orientation = require('../orientation')

tape('cell-orientation', function(t) {

  t.equals(orientation([0, 1, 2]), 1)
  t.equals(orientation([1, 0, 2]), -1)
  t.equals(orientation([0, 2, 1]), -1)
  t.equals(orientation([1, 1, 2]), 0)

  t.end()
})
