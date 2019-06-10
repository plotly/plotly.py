# mouse-event
Provides a normalized, cross-browser, garbage-collection-free API for reading out the state of a mouse event.

### Why is this needed?
Because it is 2015 and somehow every major browser still disagrees on even the most basic details of MouseEvents.  Seriously guys.

# Example

```javascript
var mouse = require('mouse-event')

window.addEventListener('mousemove', function(ev) {
  document.body.innerHTML =
    '<p>Buttons: ' + mouse.buttons(ev) + 
    ' x:' + mouse.x(ev) + 
    ' y:' + mouse.y(ev) + '</p>'
})
```

[Try this in your browser](https://mikolalysenko.github.io/mouse-event)

# Install

```
npm i mouse-event
```

# API

```javascript
var mouse = require('mouse-event')
```

#### `mouse.buttons(event)`
Returns a bit vector, similar to `event.which` in WebKit encoding the state of the mouse buttons.

* `event` is a mouse event

**Returns** A bit vector with the following interpretation for the flags:
* `1` - left mouse
* `2` - right mouse
* `4` - middle mouse
* `8` - button 4
* `16` - button 5
* ...
* `1<<k`  - button k+1

#### `mouse.x(event)`
Returns the relative x-coordinate of the mouse event

* `event` is a mouse event

**Returns** The relative x-coordinate of `event`, similar to `event.x` in WebKit

#### `mouse.y(event)`
Returns the relative y-coordinate of the mouse  event

* `event` is a mouse event

**Returns** The relative y-coordinate of `event`, similar to `event.y` in WebKit

#### `mouse.element(event)`
Get the element which triggered the event.

* `event` is a mouse event

**Returns** The `target` or `srcElement` or whatever it was that triggered the event

# License
(c) 2015 Mikola Lysenko. MIT License