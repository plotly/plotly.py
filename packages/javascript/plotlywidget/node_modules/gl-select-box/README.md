# gl-select-box
An overlay which draws select boxes for 2d webgl plots

## Example

Check back later

## Install

```
npm i gl-select-box
```

## API

### Constructor

#### `var selectBox = require('gl-select-box')(plot, options)`
Creates a select box primitive

* `plot` is a `gl-plot2d` instance
* `options` is a set of configuration parameters for the select box

The parameters for `options` are as follows:

* `selectBox` The bounding box for the selection region
* `innerFill` If set, fill in the inner box
* `innerColor` Color of the inner box
* `outerFill` If set, fill region outside box
* `outerColor` Color of outer fill
* `borderWidth` Border of box in pixels
* `borderColor` Border color

### Methods

#### `selectBox.update(options)`
Updates select box in place

#### `selectBox.dispose()`
Destroys the select box

## License
(c) 2015 Mikola Lysenko. MIT License
