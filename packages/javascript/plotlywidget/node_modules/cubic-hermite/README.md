cubic-hermite
=============
[Cubic hermite spline](http://en.wikipedia.org/wiki/Cubic_Hermite_spline) for interpolating position/velocity pairs.  Simplest quick and dirty way to get a smooth path between points

## Install

    npm install cubic-hermite
    
## Example

```javascript
var hermite = require("cubic-hermite")

//Compute intial position and velocity
var initial_position = [0, 1]
  , initial_velocity = [1, 0]
  , final_positions  = [1, 0]
  , final_velocity   = [0, 1]
  
//Plot curve
for(var t=0.0; t<1.0; t+=0.1) {
  console.log(hermite(initial_position, initial_velocity, final_position, final_velocity, t))
}
```

## API

### `require("cubic-hermite")(p0, v0, p1, v1, t[, result])`
Computes an interpolated position between initial and final configurations at time t.  Arguments can be either scalars or arrays

* `p0` is the initial position
* `v0` is the initial velocity
* `p1` is the final position
* `v1` is the final velocity
* `t` is the point on the curve to interpolate to in the range [0,1]
* `result` is a vector that gets the result of the interpolation (if not specified, a new vector is created)

**Returns** The interpolated point on the curve

### `require("cubic-hermite").derivative(p0, v0, p1, v1, t[, result])`
Returns the velocity along the curve at a point t

* `p0` is the initial position
* `v0` initial velocity
* `p1` final position
* `v1` final velocity
* `t` point on the curve to interpolate to, in the range [0,1]
* `result` stores the result of the interpolation.  (if not specified, is reallocated)

**Returns** The interpolated velocity at the time `t`

## Credits
(c) 2013 Mikola Lysenko. MIT License