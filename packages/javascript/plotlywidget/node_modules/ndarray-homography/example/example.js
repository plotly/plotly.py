'use strict'

var imshow = require('ndarray-imshow')
var baboon = require('baboon-image')
var luminance = require('luminance')
var applyHomography = require('../xform')
var scratch = require('ndarray-scratch')

var baboonGrey = luminance(
  scratch.zeros([baboon.shape[0], baboon.shape[1]]),
  baboon)

imshow(applyHomography(
  scratch.zeros(baboonGrey.shape),
  baboonGrey,
  [1, 0, 0,
   0, 1, 0,
   1, 100, 1]
))