ndarray-warp
============
Inverse [image warping](http://www.cs.princeton.edu/courses/archive/fall00/cs426/lectures/warp/warp.pdf) operations for [ndarrays](https://github.com/mikolalysenko/ndarray).


Example
=======

```javascript
//Load input image
var lena = require("luminance")(require("lena"))

//Allocate storage for result
var result = require("zeros")([512, 512])

//Apply warp
require("ndarray-warp")(result, lena, function(out, inp) {
  var dx = inp[0] - 256
  var dy = inp[1] - 256
  var r  = Math.sqrt(dx * dx + dy * dy)
  var theta = Math.atan2(dy, dx)
  
  out[0] = 0.9 * r * Math.cos(theta + 0.01 * r) + 256
  out[1] = 0.7 * r * Math.sin(theta + 0.01 * r) + 256
})

//Save the result to stdout
require("save-pixels")(result, "png").pipe(process.stdout)
```

Which produces the following image:

<img src="https://raw.github.com/mikolalysenko/ndarray-warp/master/example/warp.png">

Install
=======

    npm install ndarray-warp
    
### `require("ndarray-warp")(output, input, map(out_coord, in_coord))`
Applies an inverse warp to an image

* `output` is an ndarray image that gets the result of applying the warp
* `input` is an ndarray iamge that is warped
* `map(result, coord)` is a mapping from the coordinates of out image to input image.

  + `result` gets the resulting coordinate in `input`
  + `coord` is the coordinate in `output`

# Credits
(c) 2013 Mikola Lysenko. MIT License
