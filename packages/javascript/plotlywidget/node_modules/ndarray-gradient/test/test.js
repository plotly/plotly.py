'use strict'

var tape = require('tape')
var pack = require('ndarray-pack')
var unpack = require('ndarray-unpack')
var zeros = require('ndarray-scratch').zeros
var grad = require('../fdg')

function g(X, bc) {
  var Y = pack(X)
  var dX = grad(zeros(Y.shape.slice().concat([Y.dimension])), Y, bc)
  var perm = [Y.dimension]
  for(var i=0; i<Y.dimension; ++i) {
    perm[i+1] = i
  }
  return unpack(dX.transpose.apply(dX, perm))
}

tape('ndarray-gradient', function(t) {

  t.same(g([1,2,3], 'wrap'), [[0.5, -1, 0.5]])
  t.same(g([1,2,3], 'clamp'), [[-0.5,-1, -0.5]])
  t.same(g([1,2,3], 'mirror'), [[0, -1, 0]])

  t.same(g([1,2], 'wrap'), [[0,0]])
  t.same(g([1,2], 'clamp'), [[-0.5, -0.5]])
  t.same(g([1,2], 'mirror'), [[0,0]])

  t.same(g([[1,2,3]], 'wrap'), [[[0,0,0]],[[0.5, -1, 0.5]]])
  t.same(g([[1,2,3]], 'clamp'), [[[0,0,0]],[[-0.5,-1, -0.5]]])
  t.same(g([[1,2,3]], 'mirror'), [[[0,0,0]],[[0, -1, 0]]])

  t.end()
})