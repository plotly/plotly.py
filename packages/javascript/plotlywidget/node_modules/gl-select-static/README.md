gl-select-static
================
A variation of gl-select which is designed for non-animated scenes

## Install

```
npm install gl-select-static
```

## API

```javascript
var createSelectBuffer = require("gl-select-static")
```

### Constructor

#### `var select = createSelectBuffer(gl, shape)`

Creates a select buffer with the given shape

### Methods

#### `select.begin()`

Begins a selection rendering pass.

#### `select.end()`

Finishes the selection pass.

#### `select.query(x,y,radius)`

Queries the selection buffer for all points within radius.

* `x` is the x coordinate of the query point
* `y` is the y coordinate of the query point
* `radius` is the radius of the selection

**Returns** A SelectResult with the same contents as in gl-select

#### `select.dispose()`

Destroys the selection buffer and releases all associated resources

### Properties

#### `select.shape`

Updates or retrieves the shape of the selection buffer.

## Legal

(c) 2014 Mikola Lysenko. MIT License