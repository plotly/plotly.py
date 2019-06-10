# gl-plot2d

A rendering engine for drawing huge 2D plots using WebGL.

## Install

With [npm](http://github.com/gl-vis/gl-plot2d),

```
npm i gl-plot2d
```

## API

### Constructor

#### `var plot = require('gl-plot2d')(options)`
Constructs a new `gl-plot2d` object.

* `options` is an object containing parameters for constructing the plot

Options can contain the following parameters,

##### Required properties

| Property | Description |
|----------|-------------|
| `gl` | A `WebGLRenderingContext` object, into which the plot is drawn |
| `pixelRatio` | A scale factor which is applied to pixel coordinates |
| `screenBox` | Bounds on the plot within the WebGL context |
| `viewBox` | Pixel coordinates where the plot is drawn |
| `dataBox` | Data coordinates for the view of the plot |

*Note:*  Coordinates for `screenBox, viewBox, dataBox,` etc. are given by 4-tuples of bounding box coordinates in the form `[xmin, ymin, xmax, ymax]`.

##### Border and background colors

| Property | Description | Default |
|----------|-------------|---------|
| `borderColor` | Border color as a normalized RGBA tuple | `[0,0,0,0]` |
| `backgroundColor` | Background color | `[0,0,0,0]` |
| `borderLineEnable` | Toggle drawing lines for left,bottom,right,top of border | `[true,true,true,true]` |
| `borderLineWidth` | Width of border lines | `[2,2,2,2]` |
| `borderLineColor` | Color of border lines | `[[0,0,0,1], [0,0,0,1], [0,0,0,1], [0,0,0,1]]` |

*Note:* For properties which are specified per-screen direction like `borderLineEnable` etc., the components are always arranged in the order `left,bottom,right,top`.

##### Ticks

| Property | Description | Default |
|----------|-------------|---------|
| `ticks` | See note below | `[[], []]` |
| `tickEnable` | Turn on display of ticks for a given axis | `[true, true, true, true]` |
| `tickPad` | Distance between tick text and tick marks |  `[15,15,15,15]` |
| `tickAngle` | Angle to draw ticks at | `[0,0,0,0]` |
| `tickColor` | Color of tick labels | `[[0,0,0,1], [0,0,0,1], [0,0,0,1], [0,0,0,1]]`
| `tickMarkWidth` | Tick marks | `[0,0,0,0]` |
| `tickMarkLength` |    | `[0,0,0,0]` |
| `tickMarkColor` |    | `[[0,0,0,1],[0,0,0,1],[0,0,0,1],[0,0,0,1]]` |

*Note:* Ticks are encoded as an array of objects, each with the following properties:

* `x` The data coordinate of the tick
* `text` The text associated to the tict mark
* `font` The font for the text
* `size` The font size for the tick

##### Labels

| Property | Description | Default |
|----------|-------------|---------|
| `labels` | The label text for each axis  | `['x', 'y']` |
| `labelEnable` | Turns on/off rendering for the labels on the left,bottom,top,right | `[true, true, true, true]` |
| `labelAngle` | Angle to draw label text | `[0,Math.PI/2,0,3.0*Math.PI/2]` |
| `labelPad` | Padding for labels in pixel coordinates | `[15,15,15,15]` |
| `labelSize` | Size of labels in pixels | `[12, 12]` |
| `labelFont` | Font for labels | `['sans-serif', 'sans-serif']` |
| `labelColor` | Color of labels | `[[0,0,0,1],[0,0,0,1],[0,0,0,1],[0,0,0,1]]` |

##### Title

| Property | Description | Default |
|----------|-------------|---------|
| `title` | Title text | `''` |
| `titleEnable` | Toggles title rendering | `true` |
| `titleCenter` | Pixel coordinates for center of title | `[0.5*(viewBox[0]+viewBox[2]), viewBox[3] - 40]` |
| `titleAngle` | Angle to draw title text | `0` |
| `titleColor` | Color of title | `[0,0,0,1]` |
| `titleFont` | Title font | `'sans-serif'` |
| `titleSize` | Title font size | `18` |

##### Grid lines

| Property | Description | Default |
|----------|-------------|---------|
| `gridLineEnable` | Turns on grid lines per axis | `[true, true]` |
| `gridLineColor` | Grid line color | `[[0,0,0,0.5], [0,0,0,0.5]]` |
| `gridLineWidth` | Width of grid lines | `[1, 1]` |
| `zeroLineEnable` | Toggle rendering of zero line | `[true, true]` |
| `zeroLineWidth` | Width of zero line in pixels | `[2, 2]` |
| `zeroLineColor` | Color of zero line | `[[0,0,0,1], [0,0,0,1]]` |

### Methods

#### `plot.update(options)`
Updates the properties of the plot.

* `options` is an option structure, as described in the constructor

#### `plot.draw()`
Redraws the plot.  Call this once per `requestAnimationFrame()`

#### `plot.pick(x, y)`
Finds the current data point highlighted by the user.  

* `x,y` are the coordinates of the mouse in pixel coordinates

**Returns** If the user is selecting a data point, then returns the current data point selected by the user.  Otherwise, returns `null`

#### `plot.dispose()`
Destroy plot and release all associated resources

# License
(c) Mikola Lysenko.  MIT License

Supported by [plot.ly](http://plot.ly)
