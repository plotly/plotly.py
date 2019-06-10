require('../mouse-listen')(function(buttons, x, y, mods) {
  document.body.innerHTML =
    '<p>Buttons: 0b' + buttons.toString(2) +
    ', x:' + x +
    ', y:' + y +
    ', mods:' + JSON.stringify(mods) + '</p>'
})
