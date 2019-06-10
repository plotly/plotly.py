mouse-change
============
Listens for any mouse state changes.

# Example

```javascript
require('mouse-change')(function(buttons, x, y) {
  document.body.innerHTML =
    '<p>Buttons: 0b' + buttons.toString(2) +
    ', x:' + x +
    ', y:' + y + '</p>'
})
```

[Try it out in your browser](https://mikolalysenko.github.io/mouse-change)

# Install

```
npm i mouse-change
```

# API

#### `var l = require('mouse-change')([element, onchange(buttons,x,y,mods)])`
Listens for any mouse state changes on the given element.

* `element` is an optional element
* `onchange(buttons,x,y,mods)` is an optional callback which gets called every time that the mouse state changes inside `element`
    + `buttons` is the state of the mouse buttons
    + `x` is the x coordinate of the mouse
    + `y` is the y coordinate of the mouse
    + `mods` is an object storing the state of any key modifiers
        * `mods.shift` is the state of the shift key
        * `mods.alt` is the state of then alt key
        * `mods.control` is the state of the control key
        * `mods.meta` is the state of the meta key

**Returns** A new listener object which can be used to configure the listener.

#### `l.enabled`
Toggles whether or not

#### `l.x`
The x coordinate of the mouse

#### `l.y`
The y coordinate of the mouse

#### `l.buttons`
The button state of the mouse

#### `l.mods`
The current state of the keyboard modifiers

# License
(c) 2015 Mikola Lysenko. MIT License
