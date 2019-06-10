ndarray-homography
==================
Applies a homography to an ndarray.

# Example

```javascript
var imshow = require('ndarray-imshow')
var baboon = require('baboon-image')
var luminance = require('luminance')
var applyHomography = require('ndarray-homography')
var scratch = require('ndarray-scratch')

var baboonGrey = luminance(
  scratch.zeros([baboon.shape[0], baboon.shape[1]]),
  baboon)

imshow(applyHomography(
  scratch.zeros(baboonGrey.shape),
  baboonGrey,
  [1, 0, 0,
   0, 1, 0,
   0, 0, 1]
))
```

# Install

```
npm install ndarray-homography
```

# API

### `require('ndarray-homography')(dest, src, M)`
Applies a [homography](http://en.wikipedia.org/Homography) to an ndarray.

* `dest` is a destination image, which has the same size as the input image
* `src` is the input image
* `M` is a homography encoded as a flattened matrix in column major order (consistent with OpenGL's format)

**Returns** `dest`

# Credits
(c) 2014 Mikola Lysenko. MIT License