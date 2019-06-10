filtered-vector
===============
Applies cubic smoothing to a vector valued curve.  This is useful for smoothing out inputs from the mouse or other input devices.

# Example

```javascript
var now = require('right-now')
var filterVector = require('filtered-vector')
var smoothPosition = filterVector([256, 256])

var canvas = document.createElement('canvas')
canvas.width = 512
canvas.height = 512
document.body.appendChild(canvas)
var context = canvas.getContext('2d')

canvas.addEventListener('mousemove', function(ev) {
  smoothPosition.push(now(), ev.x, ev.y)
})

function paint() {
  requestAnimationFrame(paint)
  var t = now()
  context.fillStyle = 'rgba(0,0,0,1)'
  context.fillRect(0,0,512,512)
  
  context.strokeStyle = '#0f0'
  context.lineWidth = 1
  context.beginPath()
  var x = smoothPosition.curve(t)
  context.moveTo(x[0], x[1])
  for(var i=0; i<2000; ++i) {
    var y = smoothPosition.curve(Math.floor(t - i))
    context.lineTo(y[0], y[1])
  }
  context.stroke()
}
paint()
```

[Try out the demo in your browser.](https://mikolalysenko.github.io/filtered-vector)

# Install

```
npm i filtered-vector
```

# API

## Constructor

#### `var vec = require('filtered-vector')(initState[, initVelocity, initTime])`
Creates a new smoothed vector with the given initial state, velocity and time.

* `initState` is the initial state of the vector
* `initVelocity` is the initial velocity of the vector
* `initTime` is the initial time of the vector

**Returns** A new smoothed vector valued curve

## Methods

#### `vec.curve(t)`
Computes the value of the curve at time `t`

* `t` is the time parameter to sample the curve

**Returns** The value of the curve at time `t`

#### `vec.dcurve(t)`
Computes the derivative of the curve at time `t`

* `t` is the time parameter

**Returns** The derivative of the curve at time `t`

#### `vec.bounds`
A pair of arrays giving the upper and lower bounds on the constraints of the vector.  Default is `[-Infinity,-Infinity, ...]` and `[Infinity,Infinity,...]`

#### `vec.push(t, ...)`
Adds a new data point onto the end of the curve

* `t` is the time the new data point was sampled
* `...` are the components of the curve vector

#### `vec.move(t, ...)`
Incrementally moves the curve from the last sampled position by an offset.  This is useful with input devices that emit relative motion (for example scrolling, key press events, pointer lock)

* `t` is the time at which the move event occured
* `...` are the components of the relative motion

#### `vec.set(t, ...)`
Sets the state of the curve at time `t`

* `t` is the time parameter to sample
* `...` are the components of the state

#### `vec.jump(t, ...)`
Sets the state of the vector at time `t` with no smoothing.

* `t` is the time parameter to sample
* `...` are the components of the vector

#### `vec.idle(t)`
Adds a stationary data point to the curve (ie notify the curve that no input state has changed)

* `t` is the time at which the curve was idle

#### `vec.flush(t)`
Removes all samples in the buffer before time `t`

* `t` is the cutoff time

#### `vec.lastT()`

**Returns** The time of the last sample in the curve

#### `vec.stable()`

**Returns** `true` is the vector is stationary as of the last event.

# License
(c) 2015 Mikola Lysenko.  MIT License