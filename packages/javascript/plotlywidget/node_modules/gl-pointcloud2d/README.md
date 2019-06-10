gl-pointcloud2d
============
WebGL 2D point cloud for lots of points

## Example
... to be created

## Install
Using [npm](https://docs.npmjs.com/), you can install this module as follows:

```
npm i gl-pointcloud2d
```

## API

### Constructor

#### `var pointcloud = require('gl-pointcloud2d')(plot, options)`
Creates a new 2D point cloud.

* `plot` is a reference to a `gl-plot2d` object
* `options` is a JSON object containing the parameters which are passed to the object when it is updated.

`options` has the following properties:

* `data` is a packed 2*n length array of the unrolled xy coordinates of the points (required) - buffering is significantly faster if it's of type Float32Array
* `idToIndex` is an optional array of length n where `idToIndex[i] = i` - buffering is significantly faster if it's supplied and of type Int32Array
* `color` is the color of a marker as a length 4 RGBA array (default `[1,0,0,1]`)
* `borderSize` is the ratio of the border around each point (default `0`)
* `borderColor` is the color of the border of each point (default `[0,0,0,1]`)
* `blend` determines if `gl` blending is enabled for a translucency effect on overlaps; enabling it lowers draw speed somewhat (default `false`)

**Returns** A new point cloud plot object, which is also registered to `plot`

### Methods

#### `pointcloud.update(options)`
Updates the point cloud plot.

* `options` is an object with the same properties as in the point cloud plot constructor

#### `pointcloud.dispose()`
Destroys the point cloud plot and all associated resources.

## License
(c) 2015 Mikola Lysenko. MIT License

Development supported by plot.ly
