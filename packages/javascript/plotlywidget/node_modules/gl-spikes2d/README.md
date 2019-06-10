gl-spikes2d
===========
Draws axis spikes for 2D plots

## Example

Check back later

## Install

```
npm i gl-spikes2d
```

## API

### Constructor

#### `var spikes = require('gl-spikes2d')(plot, options)`
Creates a new spike overlay for the given 2d plot

* `plot` is a `gl-plot2d` instance
* `options` is an object with a set of properties for the spike object

The properties of the options object are as follows:

* `enable` Enables rendering of the spikes for each axis
* `width` The width of each spike
* `color` Color of each spike
* `center` Center of spikes

### Methods

#### `spikes.update(options)`
Updates the spike object in place.  Similar behavior to constructor.

#### `spikes.dispose()`
Destroys the spikes object

## License
(c) 2015 Mikola Lysenko. MIT License
