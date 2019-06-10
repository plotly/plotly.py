"use strict"

function interp1d(arr, x) {
  var ix = Math.floor(x)
    , fx = x - ix
    , s0 = 0 <= ix   && ix   < arr.shape[0]
    , s1 = 0 <= ix+1 && ix+1 < arr.shape[0]
    , w0 = s0 ? +arr.get(ix)   : 0.0
    , w1 = s1 ? +arr.get(ix+1) : 0.0
  return (1.0-fx)*w0 + fx*w1
}

function interp2d(arr, x, y) {
  var ix = Math.floor(x)
    , fx = x - ix
    , s0 = 0 <= ix   && ix   < arr.shape[0]
    , s1 = 0 <= ix+1 && ix+1 < arr.shape[0]
    , iy = Math.floor(y)
    , fy = y - iy
    , t0 = 0 <= iy   && iy   < arr.shape[1]
    , t1 = 0 <= iy+1 && iy+1 < arr.shape[1]
    , w00 = s0&&t0 ? arr.get(ix  ,iy  ) : 0.0
    , w01 = s0&&t1 ? arr.get(ix  ,iy+1) : 0.0
    , w10 = s1&&t0 ? arr.get(ix+1,iy  ) : 0.0
    , w11 = s1&&t1 ? arr.get(ix+1,iy+1) : 0.0
  return (1.0-fy) * ((1.0-fx)*w00 + fx*w10) + fy * ((1.0-fx)*w01 + fx*w11)
}

function interp3d(arr, x, y, z) {
  var ix = Math.floor(x)
    , fx = x - ix
    , s0 = 0 <= ix   && ix   < arr.shape[0]
    , s1 = 0 <= ix+1 && ix+1 < arr.shape[0]
    , iy = Math.floor(y)
    , fy = y - iy
    , t0 = 0 <= iy   && iy   < arr.shape[1]
    , t1 = 0 <= iy+1 && iy+1 < arr.shape[1]
    , iz = Math.floor(z)
    , fz = z - iz
    , u0 = 0 <= iz   && iz   < arr.shape[2]
    , u1 = 0 <= iz+1 && iz+1 < arr.shape[2]
    , w000 = s0&&t0&&u0 ? arr.get(ix,iy,iz)       : 0.0
    , w010 = s0&&t1&&u0 ? arr.get(ix,iy+1,iz)     : 0.0
    , w100 = s1&&t0&&u0 ? arr.get(ix+1,iy,iz)     : 0.0
    , w110 = s1&&t1&&u0 ? arr.get(ix+1,iy+1,iz)   : 0.0
    , w001 = s0&&t0&&u1 ? arr.get(ix,iy,iz+1)     : 0.0
    , w011 = s0&&t1&&u1 ? arr.get(ix,iy+1,iz+1)   : 0.0
    , w101 = s1&&t0&&u1 ? arr.get(ix+1,iy,iz+1)   : 0.0
    , w111 = s1&&t1&&u1 ? arr.get(ix+1,iy+1,iz+1) : 0.0
  return (1.0-fz) * ((1.0-fy) * ((1.0-fx)*w000 + fx*w100) + fy * ((1.0-fx)*w010 + fx*w110)) + fz * ((1.0-fy) * ((1.0-fx)*w001 + fx*w101) + fy * ((1.0-fx)*w011 + fx*w111))
}

function interpNd(arr) {
  var d = arr.shape.length|0
    , ix = new Array(d)
    , fx = new Array(d)
    , s0 = new Array(d)
    , s1 = new Array(d)
    , i, t
  for(i=0; i<d; ++i) {
    t = +arguments[i+1]
    ix[i] = Math.floor(t)
    fx[i] = t - ix[i]
    s0[i] = (0 <= ix[i]   && ix[i]   < arr.shape[i])
    s1[i] = (0 <= ix[i]+1 && ix[i]+1 < arr.shape[i])
  }
  var r = 0.0, j, w, idx
i_loop:
  for(i=0; i<(1<<d); ++i) {
    w = 1.0
    idx = arr.offset
    for(j=0; j<d; ++j) {
      if(i & (1<<j)) {
        if(!s1[j]) {
          continue i_loop
        }
        w *= fx[j]
        idx += arr.stride[j] * (ix[j] + 1)
      } else {
        if(!s0[j]) {
          continue i_loop
        }
        w *= 1.0 - fx[j]
        idx += arr.stride[j] * ix[j]
      }
    }
    r += w * arr.data[idx]
  }
  return r
}

function interpolate(arr, x, y, z) {
  switch(arr.shape.length) {
    case 0:
      return 0.0
    case 1:
      return interp1d(arr, x)
    case 2:
      return interp2d(arr, x, y)
    case 3:
      return interp3d(arr, x, y, z)
    default:
      return interpNd.apply(undefined, arguments)
  }
}
module.exports = interpolate
module.exports.d1 = interp1d
module.exports.d2 = interp2d
module.exports.d3 = interp3d
