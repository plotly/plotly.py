extract-frustum-planes
======================
Returns a list of frustum planes from a given WebGL matrix (assuming the matrix is stored in the same format as used by [gl-matrix](https://github.com/toji/gl-matrix)).


## Install

    npm install extract-frustum-planes

## Example

```javascript
var getPlanes = require("extract-frustum-planes")

var glm = require("gl-matrix")
var m = glm.mat4.perspective()
```

## API

### `require("extract-frustum-planes")(worldToClip[, zNear, zFar])`
Extracts the frustum planes of the combined world to clip coordinate matrix for WebGL

* `worldToClip` is the concatenated model-view-projection matrix in the same format as expected by WebGL (ie compatible with gl-matrix)
* `zNear` is the near clip plane distance as set by `gl.depthRange` (default 0.0)
* `zFar` is the far clip plane distance as set by `gl.depthRange`

**Returns** An array of 6 planes encoding the view frustum stored in the order:

* `left`
* `right`
* `top`
* `bottom`
* `near`
* `far`

## Credits
(c) 2013 Mikola Lysenko. MIT License