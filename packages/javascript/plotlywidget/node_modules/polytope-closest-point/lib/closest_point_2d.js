//Optimized version for triangle closest point
// Based on Eberly's WildMagick codes
// http://www.geometrictools.com/LibMathematics/Distance/Distance.html
"use strict";

var diff = new Float64Array(4);
var edge0 = new Float64Array(4);
var edge1 = new Float64Array(4);

function closestPoint2d(V0, V1, V2, point, result) {
  //Reallocate buffers if necessary
  if(diff.length < point.length) {
    diff = new Float64Array(point.length);
    edge0 = new Float64Array(point.length);
    edge1 = new Float64Array(point.length);
  }
  //Compute edges
  for(var i=0; i<point.length; ++i) {
    diff[i]  = V0[i] - point[i];
    edge0[i] = V1[i] - V0[i];
    edge1[i] = V2[i] - V0[i];
  }
  //Compute coefficients for quadratic func
  var a00 = 0.0
    , a01 = 0.0
    , a11 = 0.0
    , b0  = 0.0
    , b1  = 0.0
    , c   = 0.0;
  for(var i=0; i<point.length; ++i) {
    var e0 = edge0[i]
      , e1 = edge1[i]
      , d  = diff[i];
    a00 += e0 * e0;
    a01 += e0 * e1;
    a11 += e1 * e1;
    b0  += d * e0;
    b1  += d * e1;
    c   += d * d;
  }
  //Compute determinant/coeffs
  var det = Math.abs(a00*a11 - a01*a01);
  var s   = a01*b1 - a11*b0;
  var t   = a01*b0 - a00*b1;
  var sqrDistance;
  //Hardcoded Voronoi diagram classification
  if (s + t <= det) {
    if (s < 0) {
      if (t < 0) { // region 4
        if (b0 < 0) {
          t = 0;
          if (-b0 >= a00) {
            s = 1.0;
            sqrDistance = a00 + 2.0*b0 + c;
          } else {
            s = -b0/a00;
            sqrDistance = b0*s + c;
          }
        } else {
          s = 0;
          if (b1 >= 0) {
            t = 0;
            sqrDistance = c;
          } else if (-b1 >= a11) {
            t = 1;
            sqrDistance = a11 + 2.0*b1 + c;
          } else {
            t = -b1/a11;
            sqrDistance = b1*t + c;
          }
        }
      } else {  // region 3
        s = 0;
        if (b1 >= 0) {
          t = 0;
          sqrDistance = c;
        } else if (-b1 >= a11) {
          t = 1;
          sqrDistance = a11 + 2.0*b1 + c;
        } else {
          t = -b1/a11;
          sqrDistance = b1*t + c;
        }
      }
    } else if (t < 0) { // region 5
      t = 0;
      if (b0 >= 0) {
        s = 0;
        sqrDistance = c;
      } else if (-b0 >= a00) {
        s = 1;
        sqrDistance = a00 + 2.0*b0 + c;
      } else {
        s = -b0/a00;
        sqrDistance = b0*s + c;
      }
    } else {  // region 0
      // minimum at interior point
      var invDet = 1.0 / det;
      s *= invDet;
      t *= invDet;
      sqrDistance = s*(a00*s + a01*t + 2.0*b0) + t*(a01*s + a11*t + 2.0*b1) + c;
    }
  } else {
    var tmp0, tmp1, numer, denom;
    
    if (s < 0) {  // region 2
      tmp0 = a01 + b0;
      tmp1 = a11 + b1;
      if (tmp1 > tmp0) {
        numer = tmp1 - tmp0;
        denom = a00 - 2.0*a01 + a11;
        if (numer >= denom) {
          s = 1;
          t = 0;
          sqrDistance = a00 + 2.0*b0 + c;
        } else {
          s = numer/denom;
          t = 1 - s;
          sqrDistance = s*(a00*s + a01*t + 2.0*b0) +
          t*(a01*s + a11*t + 2.0*b1) + c;
        }
      } else {
        s = 0;
        if (tmp1 <= 0) {
          t = 1;
          sqrDistance = a11 + 2.0*b1 + c;
        } else if (b1 >= 0) {
          t = 0;
          sqrDistance = c;
        } else {
          t = -b1/a11;
          sqrDistance = b1*t + c;
        }
      }
    } else if (t < 0) {  // region 6
      tmp0 = a01 + b1;
      tmp1 = a00 + b0;
      if (tmp1 > tmp0) {
        numer = tmp1 - tmp0;
        denom = a00 - 2.0*a01 + a11;
        if (numer >= denom) {
          t = 1;
          s = 0;
          sqrDistance = a11 + 2.0*b1 + c;
        } else {
          t = numer/denom;
          s = 1 - t;
          sqrDistance = s*(a00*s + a01*t + 2.0*b0) +
          t*(a01*s + a11*t + 2.0*b1) + c;
        }
      } else {
        t = 0;
        if (tmp1 <= 0) {
          s = 1;
          sqrDistance = a00 + 2.0*b0 + c;
        } else if (b0 >= 0) {
          s = 0;
          sqrDistance = c;
        } else {
          s = -b0/a00;
          sqrDistance = b0*s + c;
        }
      }
    } else {  // region 1
      numer = a11 + b1 - a01 - b0;
      if (numer <= 0) {
        s = 0;
        t = 1;
        sqrDistance = a11 + 2.0*b1 + c;
      } else {
        denom = a00 - 2.0*a01 + a11;
        if (numer >= denom) {
          s = 1;
          t = 0;
          sqrDistance = a00 + 2.0*b0 + c;
        } else {
          s = numer/denom;
          t = 1 - s;
          sqrDistance = s*(a00*s + a01*t + 2.0*b0) +
          t*(a01*s + a11*t + 2.0*b1) + c;
        }
      }
    }
  }
  var u = 1.0 - s - t;
  for(var i=0; i<point.length; ++i) {
    result[i] = u * V0[i] + s * V1[i] + t * V2[i];
  }
  if(sqrDistance < 0) {
    return 0;
  }
  return sqrDistance;
}

module.exports = closestPoint2d;
