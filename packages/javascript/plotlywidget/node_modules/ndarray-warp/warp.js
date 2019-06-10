'use strict'

var interp  = require('ndarray-linear-interpolate')
var cwise   = require('cwise')

var do_warp = cwise({
  args: ['index', 'array', 'scalar', 'scalar', 'scalar'],
  pre: function(idx, dest, func, interp, n) {
    this.warped = new Array(n)
  },
  body: function warpND(idx, dest, func, interp, n) {
    func(this.warped, idx)
    dest = interp.apply(undefined, this.warped)
  }
})

var do_warp_1 = cwise({
  args: ['index', 'array', 'scalar', 'scalar', 'scalar'],
  pre: function() {
    this.warped = [0]
  },
  body: function warp1D(idx, dest, func, interp, src) {
    func(this.warped, idx)
    dest = interp(src, this.warped[0])
  }
})

var do_warp_2 = cwise({
  args: ['index', 'array', 'scalar', 'scalar', 'scalar'],
  pre: function() {
    this.warped = [0, 0]
  },
  body: function warp2D(idx, dest, func, interp, src) {
    func(this.warped, idx)
    dest = interp(src, this.warped[0], this.warped[1])
  }
})

var do_warp_3 = cwise({
  args: ['index', 'array', 'scalar', 'scalar', 'scalar'],
  pre: function() {
    this.warped = [0, 0, 0]
  },
  body: function warp3D(idx, dest, func, interp, src) {
    func(this.warped, idx)
    dest = interp(src, this.warped[0], this.warped[1], this.warped[2])
  }
})

module.exports = function warp(dest, src, func) {
  switch(src.shape.length) {
    case 1:
      do_warp_1(dest, func, interp.d1, src)
      break
    case 2:
      do_warp_2(dest, func, interp.d2, src)
      break
    case 3:
      do_warp_3(dest, func, interp.d3, src)
      break
    default:
      do_warp(dest, func, interp.bind(undefined, src), src.shape.length)
      break
  }
  return dest
}
