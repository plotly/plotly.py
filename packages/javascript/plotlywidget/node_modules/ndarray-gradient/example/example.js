var pack = require('ndarray-pack')
var pool = require('ndarray-scratch')
var grad = require('../fdg')
var show = require('ndarray-show')

var X = pack([[0, 0, 0],
              [0, 1, 1],
              [0, 0, 0]])

//Compute gradient of X
var dX = grad(pool.zeros([3,3,2]), X, 'wrap')

console.log('X = \n', show(X))

console.log('grad(X) = \n', show(dX))